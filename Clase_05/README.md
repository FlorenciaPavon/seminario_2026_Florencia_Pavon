# Clase 05 - Despliegue de aplicaciones

## Descripción

En esta actividad se desarrollan dos aplicaciones web mínimas y se realizan sus respectivos despliegues utilizando **Streamlit** y **Render**.

El objetivo es comprobar que las aplicaciones pueden ejecutarse de manera independiente del entorno local y accederse mediante un enlace público.

## Aplicaciones
enlace de render https://seminario-2026-florencia-pavon.onrender.com/

enlace de streamlit  https://seminario2026florenciapavon-bmf3ac8us6h8fgd8bap56q.streamlit.app/

### 1. Aplicación con Streamlit

Se desarrolló una aplicación mínima utilizando Streamlit.

La aplicación permite ingresar un nombre mediante un campo de texto y muestra un saludo personalizado.

Archivo principal:

```text
streamlit_app/app.py
```

Para ejecutarla localmente:

```powershell
streamlit run app.py
```

La aplicación se ejecuta inicialmente en:

```text
http://localhost:8501
```

### 2. Aplicación con Flask para Render

Se desarrolló una aplicación web mínima utilizando Flask, preparada para ser desplegada en Render.

La aplicación muestra un mensaje al acceder a la ruta principal `/`.

Archivo principal:

```text
render_app/app.py
```

Para ejecutarla localmente:

```powershell
python app.py
```

La aplicación se ejecuta inicialmente en:

```text
http
```
