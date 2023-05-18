from PIL import Image
import stepic

def codificar(image_path: str, text: str) -> Image:
    with Image.open(image_path) as image:
        encoded_image = stepic.encode(image, text.encode())
        encoded_image.save('imagen_water.png')
        return encoded_image
    

def decodificar(image_path: str) -> str:
    with Image.open(image_path) as image:
        decoded_text = stepic.decode(image)
        return decoded_text

def verify_text_in_image(image_path: str, text: str) -> bool:    
    with Image.open('imagen_water.png') as image:
        decoded_text = decodificar('imagen_water.png')
        return decoded_text == text
    
def convert_jpeg_to_png(jpeg_path: str, png_path: str):
    with Image.open(jpeg_path) as jpeg_image:
        jpeg_image.save(png_path)
    return png_path