import gradio as gr
import replicate
import os

# Token
os.environ["REPLICATE_API_TOKEN"] = "r8_f312U5UTkUhnVDi2Kjz8rqiggIuazQq0mbiNc"

MODEL = "fofr/anything-v4.0"

def generate_anime_style(image):
    output = replicate.run(
        MODEL,
        input={
            "image": open(image, "rb"),
            "prompt": "anime style portrait, clean background, colorful, high quality",
            "num_inference_steps": 30,
            "guidance_scale": 7.5
        }
    )
    return output

with gr.Blocks() as demo:
    gr.Markdown("## 👕 AI Anime / Cartoon Tasarım Aracı")
    with gr.Row():
        with gr.Column():
            image = gr.Image(type="filepath", label="Fotoğrafını yükle")
            button = gr.Button("Karakterini Oluştur")
        with gr.Column():
            output = gr.Image(label="Oluşturulan Görsel")

    button.click(fn=generate_anime_style, inputs=[image], outputs=[output])

# Burada açık port belirtiliyor!
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=10000)
