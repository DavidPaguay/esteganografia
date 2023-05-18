from PIL import Image
import numpy as np

def codificar(text: str, ruta: str):
    img = Image.open(ruta)
    img_array = np.array(img)
    message_bits = [int(bit) for bit in ''.join([bin(ord(char))[2:].zfill(8) for char in text])]
    message_bits += [0] * (len(img_array.flat) - len(message_bits))
    img_array.flat = [(pixel & ~1) | bit for pixel, bit in zip(img_array.flat, message_bits)]
    encoded_img = Image.fromarray(img_array)
    encoded_img.save('imagen_f5.png')
    return encoded_img
    
def decodificar(ruta: str):
    img = Image.open(ruta)
    img_array = np.array(img)
    message_bits = [pixel & 1 for pixel in img_array.flat]
    message_chars = [chr(int(''.join([str(bit) for bit in message_bits[i:i+8]]), 2)) for i in range(0, len(message_bits), 8)]
    message = ''.join(message_chars).split('\x00')[0]
    return message