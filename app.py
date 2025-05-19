
import gradio as gr
import replicate
import requests
from PIL import Image
import io
import os

# Replicate API token (replace with your actual token or use an environment variable)
replicate_token = os.environ.get("REPLICATE_API_TOKEN")

def rick_and_morty_convert(image):
    # Save input image temporarily
    image.save("input.png")

    # Upload to a temporary image host (Replicate requires URL input)
    imgur_response = requests.post(
        "https://api.imgbb.com/1/upload",
        params={"key": "r8_EeewhYnIxeBgF6NbnmbxbwZK6hWrTod1enCMT"},
        files={"image": open("input.png", "rb")}
    )
    image_url = imgur_response.json()["data"]["url"]

    # Call Replicate API
    client = replicate.Client(api_token=replicate_token)
    output = client.run(
        "fofr/face-to-rick:8d60b17d7c9f3fce0d0cb8a2d4ef10ff14e45c6cfc0ea81c9f6acb2041c9e2e7",
        input={"image": image_url}
    )

    result_image_url = output["image"]
    result_image = Image.open(requests.get(result_image_url, stream=True).raw)
    return result_image

iface = gr.Interface(
    fn=rick_and_morty_convert,
    inputs=gr.Image(type="pil"),
    outputs="image",
    title="Rick and Morty Avatar Generator (Real AI)",
    description="Yüz fotoğrafını yükle, AI ile Rick and Morty tarzında avatarına dönüş!"
)

iface.launch(server_name="0.0.0.0", server_port=8080)
