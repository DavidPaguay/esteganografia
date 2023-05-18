from stegano import lsb
from PIL import Image

def codificar(text: str, ruta: str):
    img = Image.open(ruta)
    img_con_texto = lsb.hide(img, text)
    img_con_texto.save('imagen_lsb.png')
    return img_con_texto
    
def decodificar(ruta: str):
    img = Image.open(ruta)
    mensaje_recuperado = lsb.reveal(img)
    print(mensaje_recuperado)
    return mensaje_recuperado