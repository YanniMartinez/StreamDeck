import tkinter as tk

def boton_presionado(palabra):
    print(palabra)

# Arreglo con las palabras para los botones
palabras = ["VisualStudio", "PowerPoint", "Excel", "Word"]

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Interfaz con Tkinter")
ventana.geometry("650x700")

# Ruta de las imágenes
rutas_imagenes = [
    "visualstudio.png",
    "powerpoint.png",
    "excel.png",
    "word.png"
]

# Crear botones dinámicamente
for i in range(len(palabras)):
    palabra = palabras[i]
    ruta_imagen = rutas_imagenes[i]
    
    # Cargar la imagen
    imagen = tk.PhotoImage(file=ruta_imagen)
    imagen = imagen.subsample(50,50)
    boton = tk.Button(ventana, text=palabra, image=imagen, compound=tk.TOP,
                      command=lambda p=palabra: boton_presionado(p))
    boton.image = imagen  # Guardar una referencia para evitar que la imagen sea eliminada por el recolector de basura
    boton.pack(pady=10)

ventana.mainloop()
