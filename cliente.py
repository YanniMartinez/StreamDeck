import tkinter as tk
import socket
import pickle  # Módulo para serialización

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

        self.botones = []

        self.crear_interfaz()
        self.conectar_servidor()

        self.ventana.mainloop()

    def crear_interfaz(self):

        self.limpiar_ventana()
        for i in range(len(self.palabras)):
            palabra = self.palabras[i]
            imagen = tk.PhotoImage(file=palabra+".png")
            imagen = imagen.subsample(30, 30)
            boton = tk.Button(self.ventana, text=palabra, image=imagen,  compound=tk.TOP,
                              command=lambda p=palabra: self.boton_presionado(p), width=100, height=100)
            boton.image = imagen
            boton.pack(pady=10)
            self.botones.append(boton)
        
        palabra = "config"
        imagen = tk.PhotoImage(file="config.png")
        imagen = imagen.subsample(100, 100)
        boton = tk.Button(self.ventana, text=palabra, image=imagen, compound=tk.TOP,
                            command=lambda p=palabra: self.boton_presionado(palabra),width=100, height=100)
        boton.image = imagen
        boton.pack(pady=10)

    def conectar_servidor(self):
        self.mi_socket = socket.socket()
        self.mi_socket.connect(("localhost", 8000))

    def boton_presionado(self, palabra):
        self.mi_socket.send(palabra.encode())
        #respuesta = self.mi_socket.recv(1024)

        if palabra == "config":
            #time.sleep(2)
            print("Se envio el config")
            arreglo_serializado = self.mi_socket.recv(1024)
            arreglo_decod = arreglo_serializado.decode('utf-8')
            #print("Se recibio info del socket")
            #print(arreglo_serializado)
            #arreglo = pickle.loads(arreglo_serializado)
            #print("Actualizando datos")
            if(arreglo_decod):
                #print(arreglo_decod)
                arreglo = arreglo_decod.split(',')
                #print(arreglo)
                self.actualizar_palabras(arreglo)

    def actualizar_palabras(self, nuevas_palabras):
        #for i, palabra in enumerate(nuevas_palabras):
            #print(palabra)
        #    self.botones[i]["text"] = palabra
        self.palabras = nuevas_palabras
        #self.botones = []
        self.crear_interfaz()
    
    def limpiar_ventana(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def __del__(self):
        self.mi_socket.close()


if __name__ == "__main__":
    app = ClienteSocketApp()
