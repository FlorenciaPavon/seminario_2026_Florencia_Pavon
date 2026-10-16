
import os
from flask import Flask, request, render_template_string
from huggingface_hub import InferenceClient

app = Flask(__name__)

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["HF_TOKEN"],
)

MODELO = "nlptown/bert-base-multilingual-uncased-sentiment"

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Analizador de sentimientos</title>
</head>
<body>
    <h1>Analizador de sentimientos</h1>
    <p>Escribí una opinión sobre un producto:</p>

    <form method="POST">
        <textarea name="texto" rows="4" cols="45"
                  placeholder="Ej.: Me encantó el producto..."
                  required>{{ texto }}</textarea>
        <br>
        <button type="submit">Analizar</button>
    </form>

    {% if sentimiento %}
        <h2>Resultado</h2>
        <p>Sentimiento: <strong>{{ sentimiento }}</strong></p>
        <p>Confianza estimada: {{ "%.2f"|format(confianza * 100) }}%</p>
    {% endif %}

    {% if error %}
        <p>Error al analizar el texto: {{ error }}</p>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def inicio():
    texto = ""
    sentimiento = None
    confianza = None
    error = None

    if request.method == "POST":
        texto = request.form.get("texto", "").strip()

        if texto:
            try:
                resultado = client.text_classification(
                    texto,
                    model=MODELO,
                )

                prediccion = max(resultado, key=lambda x: x.score)
                sentimiento = prediccion.label
                confianza = prediccion.score

            except Exception as e:
                print(f"Error al consultar Hugging Face: {e}")
                error = f"Error al consultar Hugging Face: {e}"

    return render_template_string(
        HTML,
        texto=texto,
        sentimiento=sentimiento,
        confianza=confianza,
        error=error,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
