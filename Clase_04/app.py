import gradio as gr


# Función original de la Clase 02
def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)


# Nueva función de la Clase 04 para que funcione  en hugging spaces
def reverse_text(text):
    return text[::-1]


# Interfaz utilizando Blocks tarea de la clasepip show gradio
with gr.Blocks() as demo:
    gr.Markdown("# Mi aplicación Gradio")

    # Primera función: saludo
    gr.Markdown("## Generar un saludo")

    name_input = gr.Textbox(label="Nombre")
    intensity_input = gr.Slider(
        minimum=1,
        maximum=5,
        step=1,
        value=1,
        label="Intensidad"
    )

    greet_button = gr.Button("Saludar")
    greet_output = gr.Textbox(label="Resultado")

    greet_button.click(
        fn=greet,
        inputs=[name_input, intensity_input],
        outputs=greet_output
    )

    # Segunda función: invertir texto
    gr.Markdown("## Invertir texto")

    text_input = gr.Textbox(label="Texto")
    reverse_button = gr.Button("Invertir")
    reverse_output = gr.Textbox(label="Resultado")

    reverse_button.click(
        fn=reverse_text,
        inputs=text_input,
        outputs=reverse_output
    )


# Ejecutar la aplicación y generar un enlace público temporal
demo.launch(share=True)

