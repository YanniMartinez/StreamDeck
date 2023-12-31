import socket
import subprocess
import tkinter as tk
import pickle  # Módulo para serialización
from tkinter import OptionMenu
import webbrowser

class ServidorSocket:
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.bind(("localhost", 8000))
        self.mi_socket.listen(1)
        print("Servidor iniciado. Esperando conexiones...")
        self.aceptar_conexion()

    def aceptar_conexion(self):
        self.cliente_socket, self.cliente_direccion = self.mi_socket.accept()
        print("Cliente conectado:", self.cliente_direccion)

        self.recibir_datos()

    def recibir_datos(self):
        while True:
            datos = self.cliente_socket.recv(1024)
            if not datos:
                break

            palabra = datos.decode()
            print("Palabra recibida:", palabra)
            
            if palabra == "config":
                arreglo = self.obtener_arreglo()
                print(arreglo)
                self.cliente_socket.send(arreglo.encode())
                print("Se envió el valor de nuevas configuraciones al cliente")
            else:
                self.accion_stream(palabra)
                #respuesta = "Respuesta a la palabra " + palabra
                #self.cliente_socket.send(respuesta.encode())

        self.cerrar_conexion()

    def cerrar_conexion(self):
        self.cliente_socket.close()
        self.mi_socket.close()
        print("Conexiones cerradas. Servidor detenido.")

    def obtener_arreglo(self):
        app = InterfazGrafica()
        arreglo = app.get_array()
        return arreglo
    
    def accion_stream(self, accion):
        if(accion == "visualstudio"):
            # Comando para abrir Visual Studio Code
            comando = "code"
            # Ejecuta el comando
            subprocess.run(comando, shell=True)
        elif(accion == "notepad"):
            # Comando para abrir el Bloc de notas con el archivo de script
            comando = "notepad.exe"

            # Ejecuta el comando
            subprocess.run(comando, shell=True)
        elif(accion == "powerpoint"):
            # Comando para abrir Microsoft PowerPoint
            comando = "start powerpnt"

            # Ejecuta el comando
            subprocess.run(comando, shell=True)
        elif(accion == "word"):
            # Comando para abrir Microsoft Word
            comando = "start winword"

            # Ejecuta el comando
            subprocess.run(comando, shell=True)
        elif(accion == "excel"):
            # Comando para abrir Microsoft Excel
            comando = "start excel"

            # Ejecuta el comando
            subprocess.run(comando, shell=True)
        elif(accion == "steam"):
            # Ruta al ejecutable de Steam
            ruta_steam = "C:\Program Files (x86)\Steam\steam.exe"

            # Comando para abrir Steam Launcher
            comando = f'"{ruta_steam}"'

            # Ejecuta el comando
            subprocess.run(comando, shell=True)
        elif(accion == "epic"):
            # Ruta al ejecutable de Epic Games Launcher
            ruta_epicgames = "C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"

            # Comando para abrir Epic Games Launcher
            comando = f'"{ruta_epicgames}"'

            # Ejecuta el comando
            subprocess.run(comando, shell=True)
        elif(accion == "apagar"):
            # Comando para apagar el equipo definitivamente
            comando = "shutdown /s"

            # Ejecuta el comando
            subprocess.run(comando, shell=True)
        elif(accion == "suspender"):
            # Comando para suspender el equipo
            comando = "shutdown /h"

            # Ejecuta el comando
            subprocess.run(comando, shell=True)
        elif(accion == "navegador"):
            # URL que se abrirá en el navegador predeterminado
            url = "https://www.google.com"

            # Abrir la URL en el navegador predeterminado
            webbrowser.open(url)
        else:
            print("Opcion invalida")



class InterfazGrafica:
    def __init__(self):
        self.inputs = []
        self.arreglo = []
        self.palabras = ""
        self.ventana = tk.Tk()
        self.ventana.title("Interfaz con Tkinter")
        self.ventana.geometry("600x400")

        self.crear_interfaz()

        self.ventana.mainloop()

    def crear_interfaz(self):
        opciones = ['word', 'visualstudio', 'excel', 'powerpoint', 'steam', 'epic', 'notepad', 'suspender', 'apagar', 'navegador']  # Cambia las opciones según tus necesidades

        for i in range(4):
            label = tk.Label(self.ventana, text=f"Input {i+1}:")
            label.pack()

            opcion_var = tk.StringVar(self.ventana)
            opcion_var.set(opciones[0])  # Establece el valor inicial
            opcion_menu = OptionMenu(self.ventana, opcion_var, *opciones)
            opcion_menu.pack(pady=5)

            self.inputs.append(opcion_var)

        boton = tk.Button(self.ventana, text="Verificar", command=self.verificar_inputs)
        boton.pack(pady=10)

    def verificar_inputs(self):
        valores = [opcion.get() for opcion in self.inputs]

        if len(set(valores)) != len(valores):
            tk.messagebox.showerror("Error", "Los valores no pueden ser nulos o iguales.")
            return

        if len(valores) == 4:
            self.cerrar_ventana()
            self.guardar_arreglo(valores)
            print(self.palabras)
        else:
            tk.messagebox.showerror("Error", "Debe ingresar valores en todos los inputs.")

    def guardar_arreglo(self, valores):
        self.arreglo = valores
        for valor in valores:
            self.palabras += ","+valor
        self.palabras = self.palabras[1:]

    def cerrar_ventana(self):
        self.ventana.destroy()

    def get_array(self):
        return self.palabras


if __name__ == "__main__":
    servidor = ServidorSocket()
