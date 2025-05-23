import gradio as gr
import replicate
import os

# Replicate API token
os.environ["REPLICATE_API_TOKEN"] = "r8_f312U5UTkUhnVDi2Kjz8rqiggIuazQq0mbiNc"

def generate_anime_style(image):
    output = replicate.run(
        "tstramer/anime-art-diffusion:7d702670ae67e64794c8096fd9d64892e6d82de61a37a97f5b4512e2f220f264",
        input={
            "image": image,
            "prompt": "anime style",
            "guidance_scale": 7.5,
            "num_inference_steps": 30
        }
    )
    return output

with gr.Blocks() as demo:
    gr.Markdown("## Anime Stilinde Çizim Oluştur")
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(type="filepath", label="Bir fotoğraf yükleyin")
            generate_button = gr.Button("Anime'ye Dönüştür")
        with gr.Column():
            output_image = gr.Image(label="Anime Çizimi")

    generate_button.click(fn=generate_anime_style, inputs=[input_image], outputs=[output_image])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    demo.launch(server_name="0.0.0.0", server_port=port)

