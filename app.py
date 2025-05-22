import gradio as gr
import replicate
import os
from PIL import Image

# Replicate API token'ı ortam değişkeninden al
replicate_token = os.getenv("REPLICATE_API_TOKEN")
client = replicate.Client(api_token=replicate_token)

# Dönüştürme fonksiyonu
def rick_and_morty_convert(image):
    if image is None:
        return "Lütfen bir görsel yükleyin."

    # Görseli geçici dosya olarak kaydet
    image_path = "input.png"
    image.save(image_path)

    # Replicate API çağrısı
    output_url = client.run(
        "fofr/anything-to-rick-and-morty:cc8db15b6ec0fb1b8423798f35e3e62f0bb1a76a6e62edc8347c8cf5be3c77f6",
        input={"image": open(image_path, "rb")}
    )

    return output_url

# Arayüz
iface = gr.Interface(
    fn=rick_and_morty_convert,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="filepath"),
    title="Rick and Morty Avatar Generator",
    description="Fotoğrafını yükle, Rick and Morty karakterine dönüşsün!"
)

# Başlat
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=8080)
