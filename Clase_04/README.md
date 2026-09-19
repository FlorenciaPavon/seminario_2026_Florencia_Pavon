# Clase 04 - Gradio Blocks

## Descripción

En esta actividad se modifica la aplicación desarrollada en la Clase 02 utilizando `gr.Blocks()` de Gradio.

Además, se agrega una nueva función y nuevos componentes a la interfaz, conectándolos mediante eventos de Gradio.

## Objetivos

* Modificar la interfaz utilizando `gr.Blocks()`.
* Incorporar nuevos componentes de Gradio.
* Crear una función propia con parámetros y retorno.
* Conectar la nueva función con su correspondiente entrada y salida.
* Ejecutar la aplicación utilizando `share=True`.

## Funcionalidades

La aplicación cuenta con dos funcionalidades principales:

### 1. Generar un saludo

Se mantiene la función original de la Clase 02:

```python
def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)
```

El usuario ingresa su nombre y selecciona la intensidad del saludo mediante un `Slider`.

### 2. Invertir texto

Se incorpora una nueva función:

```python
def reverse_text(text):
    return text[::-1]
```

El usuario ingresa un texto y, al presionar el botón **"Invertir"**, la aplicación devuelve el texto escrito al revés.

## Componentes utilizados

Entre los componentes utilizados se encuentran:

* `gr.Blocks`
* `gr.Markdown`
* `gr.Textbox`
* `gr.Slider`
* `gr.Button`

Los botones se conectan con las funciones mediante el evento `.click()`.

## Requisitos

* Python 3.x
* Gradio

Las dependencias utilizadas se encuentran en `requirements.txt`.

## Instalación

Crear y activar un entorno virtual:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

## Ejecución

Con el entorno virtual activado, ejecutar:

```powershell
python app.py
```

La aplicación se ejecuta localmente y puede accederse desde la dirección indicada por Gradio, normalmente:

```text
http://127.0.0.1:7860
```

La aplicación utiliza:

```python
demo.launch(share=True)
```

para intentar generar también un enlace público temporal.

## Estructura

```text
Clase_04/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

El entorno virtual `.venv/` también se encuentra dentro de la carpeta, pero está excluido del repositorio mediante `.gitignore`.
