# Aplicación de análisis de sentimientos

Aplicación web en Flask que recibe una opinión escrita y consulta el modelo
`nlptown/bert-base-multilingual-uncased-sentiment` mediante Hugging Face
Inference Providers. Muestra la etiqueta de sentimiento y el puntaje devuelto
por el modelo.

## Requisitos

- Python 3.9 o superior (Flask 3.1 requiere Python 3.9 como mínimo).
- Un token de Hugging Face habilitado para usar Inference Providers.

## Instalación

Desde esta carpeta, creá y activá un entorno virtual e instalá las dependencias:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

En macOS o Linux, la activación del entorno virtual es:

```sh
source .venv/bin/activate
```

## Configuración

La aplicación necesita la variable de entorno `HF_TOKEN`. Configurala antes de
iniciarla y no incluyas el valor del token en archivos del proyecto ni en el
control de versiones.

En PowerShell:

```powershell
$env:HF_TOKEN = "tu_token_de_hugging_face"
```

En macOS o Linux:

```sh
export HF_TOKEN="tu_token_de_hugging_face"
```

## Ejecución local

Con el entorno virtual activado y `HF_TOKEN` configurado:

```sh
python app.py
```

Abrí `http://localhost:5000` en el navegador. Si la variable `PORT` está
configurada, la aplicación usará ese puerto en lugar del 5000.

## Ejecución en producción

En un entorno Linux que use Gunicorn, iniciá la aplicación desde esta carpeta
con:

```sh
gunicorn --bind 0.0.0.0:${PORT:-5000} app:app
```

Configurá `HF_TOKEN` y, si la plataforma lo requiere, `PORT` como variables de
entorno o secretos del servicio de despliegue.