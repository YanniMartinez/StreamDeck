import tkinter as tk
import socket
import pickle  # Módulo para serialización
import time

class ClienteSocketApp:
    def __init__(self):
        self.palabras = ["visualstudio", "powerpoint", "excel", "word"]
        self.rutas_imagenes = [
            "visualstudio.png",
            "powerpoint.png",
            "excel.png",
            "word.png"
        ]

        self.ventana = tk.Tk()
        self.ventana.title("Interfaz con Tkinter y Socket")
        self.ventana.geometry("650x700")

        self.crear_interfaz()
        self.conectar_servidor()

        self.ventana.mainloop()

    def crear_interfaz(self):
        for i in range(len(self.palabras)):
            palabra = self.palabras[i]
            ruta_imagen = self.rutas_imagenes[i]

            imagen = tk.PhotoImage(file=ruta_imagen)
            imagen = imagen.subsample(50, 50)
            boton = tk.Button(self.ventana, text=palabra, image=imagen, compound=tk.TOP,
                              command=lambda p=palabra: self.boton_presionado(p))
            boton.image = imagen
            boton.pack(pady=10)

        palabra = "config"
        imagen = tk.PhotoImage(file="config.png")
        imagen = imagen.subsample(100, 100)
        boton = tk.Button(self.ventana, text=palabra, image=imagen, compound=tk.TOP,
                            command=lambda p=palabra: self.boton_presionado(palabra))
        boton.image = imagen
        boton.pack(pady=10)

    def conectar_servidor(self):
        self.mi_socket = socket.socket()
        self.mi_socket.connect(("localhost", 8000))

    def boton_presionado(self, palabra):
        self.mi_socket.send(palabra.encode())
        respuesta = self.mi_socket.recv(1024)

        if palabra == "config":
            #time.sleep(2)
            print("Se envio el config")
            arreglo_serializado = self.mi_socket.recv(1024)
            print("Se recibio info del socket")
            print(arreglo_serializado)
            arreglo = pickle.loads(arreglo_serializado)
            print("Actualizando datos")
            self.actualizar_palabras(arreglo)

    def __del__(self):
        self.mi_socket.close()

    def actualizar_palabras(self, nuevo_arreglo):
        self.palabras = nuevo_arreglo
        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        # Eliminar los botones existentes
        for widget in self.ventana.winfo_children():
            widget.destroy()

        # Crear nuevos botones con los valores actualizados del arreglo
        for i in range(len(self.palabras)):
            palabra = self.palabras[i]
            ruta_imagen = self.rutas_imagenes[i]

            imagen = tk.PhotoImage(file=ruta_imagen)
            imagen = imagen.subsample(50, 50)
            boton = tk.Button(self.ventana, text=palabra, image=imagen, compound=tk.TOP,
                            command=lambda p=palabra: self.boton_presionado(p))
            boton.image = imagen
            boton.pack(pady=10)



if __name__ == "__main__":
    app = ClienteSocketApp()
