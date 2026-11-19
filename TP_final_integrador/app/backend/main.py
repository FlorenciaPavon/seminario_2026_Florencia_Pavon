
from fastapi import FastAPI
import pandas as pd
import joblib
from pathlib import Path

from schemas import DatosPaciente

# Inicialización
app = FastAPI(
    title="Framingham - Predicción de riesgo cardiovascular",
    description="API de predicción de riesgo de enfermedad coronaria a 10 años.",
    version="1.0.0"
)

# Cargar el modelo entrenado
BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_MODELO = BASE_DIR / "modelo" / "modelo_framingham.joblib"

modelo = joblib.load(RUTA_MODELO)


# Endpoints
@app.get("/")
def inicio():
    return {
        "mensaje": "API de predicción cardiovascular funcionando",
        "modelo": "Regresión Logística - Framingham"
    }


@app.post("/predict")
def predecir(datos: DatosPaciente):

    # Convertir los datos recibidos en un diccionario
    datos_paciente = datos.model_dump()

    # Crear un DataFrame
    df = pd.DataFrame([datos_paciente])

    # Depuración temporal
    print("Columnas recibidas:", df.columns.tolist())
    print("Shape:", df.shape)
    print(df)

    # Obtener la predicción
    prediccion = modelo.predict(df)[0]

    # Obtener las probabilidades
    probabilidades = modelo.predict_proba(df)[0]

    # Buscar la probabilidad correspondiente a la clase 1
    indice_clase_1 = list(modelo.classes_).index(1)
    probabilidad = probabilidades[indice_clase_1]

    return {
        "prediccion": int(prediccion),
        "resultado": "Riesgo estimado positivo" if prediccion == 1 else "Riesgo estimado negativo",
        "probabilidad": round(float(probabilidad), 4),
        "porcentaje": round(float(probabilidad) * 100, 2)
    }
