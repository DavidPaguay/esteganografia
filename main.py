import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

import esteganografia_marco_agua
import esteganografia_lsb
import esteganografia_f5

ruta =''

def cargar_imagen():
    ruta_imagen = filedialog.askopenfilename()  # Abre un cuadro de diálogo para seleccionar una imagen
    if ruta_imagen:
        global ruta
        ruta=ruta_imagen
        print(ruta)
        imagen = Image.open(ruta_imagen)
        imagen.thumbnail((400, 300))  # Redimensiona la imagen para que se ajuste a la pantalla
        imagen = ImageTk.PhotoImage(imagen)
        etiqueta_imagen = tk.Label(canvas_izquierdo, image=imagen)
        etiqueta_imagen.image = imagen  # Guarda una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        etiqueta_imagen.pack()
        # Guarda una referencia a la imagen para evitar que sea eliminada por el recolector de basura

def procesar():
    opcion_seleccionada = opcion.get()
    texto_ingresado = cuadro_texto.get("1.0", "end-1c")
    if(opcion_seleccionada == 'F5'):
        esteganografia_f5.codificar(texto_ingresado,ruta).save('imagen_modificada.png')
        imagen = Image.open('/home/david/Documents/GitHub/esteganografia/imagen_f5.png')
        imagen.thumbnail((400, 300))  # Redimensiona la imagen para que se ajuste a la pantalla
        imagen = ImageTk.PhotoImage(imagen)
        etiqueta_imagen = tk.Label(canvas_derecho, image=imagen)
        etiqueta_imagen.image = imagen  # Guarda una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        etiqueta_imagen.pack()
    if(opcion_seleccionada == 'LSB'):
        esteganografia_lsb.codificar(texto_ingresado,ruta)
        imagen = Image.open('/home/david/Documents/GitHub/esteganografia/imagen_lsb.png')
        imagen.thumbnail((400, 300))  # Redimensiona la imagen para que se ajuste a la pantalla
        imagen = ImageTk.PhotoImage(imagen)
        etiqueta_imagen = tk.Label(canvas_derecho, image=imagen)
        etiqueta_imagen.image = imagen  # Guarda una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        etiqueta_imagen.pack()
    if(opcion_seleccionada == 'Maco de Agua'):
        esteganografia_marco_agua.codificar(ruta,texto_ingresado)
        imagen = Image.open('/home/david/Documents/GitHub/esteganografia/imagen_water.png')
        imagen.thumbnail((400, 300))  # Redimensiona la imagen para que se ajuste a la pantalla
        imagen = ImageTk.PhotoImage(imagen)
        etiqueta_imagen = tk.Label(canvas_derecho, image=imagen)
        etiqueta_imagen.image = imagen  # Guarda una referencia a la imagen para evitar que sea eliminada por el recolector de basura
        etiqueta_imagen.pack()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cargar imagen")
ventana.geometry("1200x900")  # Tamaño estático de la ventana

boton_cargar = tk.Button(ventana, text="Cargar imagen", command=cargar_imagen)
boton_cargar.pack(pady=10)

# Crear los botones de radio en una sola fila
opciones = ["F5", "LSB", "Maco de Agua"]
opcion = tk.StringVar()
opcion.set(opciones[0])  # Establecer la opción predeterminada
frame_botones = tk.Frame(ventana)
frame_botones.pack()

for opcion_texto in opciones:
    boton_opcion = tk.Radiobutton(frame_botones, text=opcion_texto, variable=opcion, value=opcion_texto)
    boton_opcion.pack(side=tk.LEFT, padx=5)
    

etiqueta_titulo = tk.Label(ventana, text="Ingrese un texto:")
etiqueta_titulo.pack(pady=(20, 0))

cuadro_texto = tk.Text(ventana, height=3, width=40)
cuadro_texto.pack(pady=10)

boton_procesar = tk.Button(ventana, text="Procesar", command=procesar)
boton_procesar.pack(pady=10)

linea_divisora = tk.Frame(ventana, height=2, bd=1, relief=tk.SUNKEN)
linea_divisora.pack(fill=tk.X, padx=10, pady=10)

canvas_izquierdo = tk.Canvas(ventana, bd=4, relief=tk.SOLID, width=400, height=300)
canvas_izquierdo.pack(side=tk.LEFT, padx=5, pady=5)


canvas_derecho = tk.Canvas(ventana, bd=4, relief=tk.SOLID,width=400, height=300)
canvas_derecho.pack(side=tk.LEFT, padx=5, pady=5)


def mostrar_texto():
    texto = cuadro_texto.get("1.0", "end-1c")
    opcion_seleccionada = opcion.get()
    result = ''
    if(opcion_seleccionada == 'F5'):
        result =esteganografia_f5.decodificar('/home/david/Documents/GitHub/esteganografia/imagen_f5.png')
        etiqueta_texto.config(text=result)
    if(opcion_seleccionada == 'LSB'):
        result = esteganografia_lsb.decodificar('/home/david/Documents/GitHub/esteganografia/imagen_lsb.png')
        etiqueta_texto.config(text=result)
    if(opcion_seleccionada == 'Maco de Agua'):
        result =esteganografia_marco_agua.decodificar('/home/david/Documents/GitHub/esteganografia/imagen_water.png')        
        etiqueta_texto.config(text=result)

def mostrar_texto_verificar():
    texto = cuadro_texto.get("1.0", "end-1c")
    texto_ingresado = cuadro_texto.get("1.0", "end-1c")
    result =esteganografia_marco_agua.verify_text_in_image(ruta,texto_ingresado)
    etiqueta_texto_verificar.config(text=str(result))
        
        
marco_inferior = tk.Frame(ventana)
marco_inferior.pack()

boton_mostrar_verificacion = tk.Button(marco_inferior, text="Verificar", command=mostrar_texto_verificar)
boton_mostrar_verificacion.pack(pady=10, padx=100)

etiqueta_texto_verificar = tk.Label(marco_inferior, text="")
etiqueta_texto_verificar.pack()

marco_inferior2 = tk.Frame(ventana)
marco_inferior2.pack()
boton_mostrar = tk.Button(marco_inferior2, text="Mostrar Texto", command=mostrar_texto)
boton_mostrar.pack(pady=10, padx=100)


etiqueta_texto = tk.Label(marco_inferior2, text="")
etiqueta_texto.pack()



# Iniciar el bucle de evento
ventana.mainloop()
