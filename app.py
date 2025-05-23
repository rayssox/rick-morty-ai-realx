import gradio as gr
import replicate
import os

# API Token – Güvenli kullanım için çevresel değişkenle çalışalım
os.environ["REPLICATE_API_TOKEN"] = "r8_f312U5UTkUhnVDi2Kjz8rqiggIuazQq0mbiNc"

def generate(image, style):
    output = replicate.run(
        "lucataco/anything-to-anything:06a6ad3cb0b70679cf85303fd26368c7d9bc65eb960e5cdbb8c55a6c3df01565",
        input={
            "image": open(image, "rb"),
            "prompt": style
        }
    )
    return output

# Arayüz
with gr.Blocks() as demo:
    gr.Markdown("## 📸 Fotoğrafını yükle, çizgi stile dönüştür!")
    with gr.Row():
        with gr.Column():
            style = gr.Textbox(label="Stil (örnek: Rick and Morty, Marvel, Naruto...)")
            image = gr.Image(type="filepath", label="Fotoğraf Yükle")
            btn = gr.Button("Dönüştür")
        with gr.Column():
            output = gr.Image(label="Çizilmiş Görsel")

    btn.click(fn=generate, inputs=[image, style], outputs=output)

if __name__ == "__main__":
    demo.launch()
