import gradio as gr


def greet(name):
    return f"Hola, {name}!"


with gr.Blocks() as demo:
    gr.Markdown("# Mi app con Gradio")
    name = gr.Textbox(label="Tu nombre")
    output = gr.Textbox(label="Salida")
    btn = gr.Button("Enviar")
    btn.click(fn=greet, inputs=name, outputs=output)


if __name__ == "__main__":
    demo.launch()
