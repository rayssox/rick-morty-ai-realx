import gradio as gr
import replicate
import os

# Replicate API token (gizli tutmalısın!)
os.environ["REPLICATE_API_TOKEN"] = "r8_f312U5UTkUhnVDi2Kjz8rqiggIuazQq0mbiNc"

# Kullanılacak model (anime tarzı, test edildi ve public)
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

if __name__ == "__main__":
    demo.launch()
