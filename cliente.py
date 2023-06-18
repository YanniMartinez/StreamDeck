import tkinter as tk
import socket

class ClienteSocketApp:
    def __init__(self):
        self.palabras = ["VisualStudio", "PowerPoint", "Excel", "Word"]
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

    def conectar_servidor(self):
        self.mi_socket = socket.socket()
        self.mi_socket.connect(("localhost", 8000))

    def boton_presionado(self, palabra):
        self.mi_socket.send(palabra.encode())
        respuesta = self.mi_socket.recv(1024)
        print(respuesta.decode())

    def __del__(self):
        self.mi_socket.close()


if __name__ == "__main__":
    app = ClienteSocketApp()
