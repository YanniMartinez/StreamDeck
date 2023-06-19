import socket
import subprocess
import webbrowser
import time
import tkinter as tk
import pickle  # Módulo para serialización

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

            # Aquí puedes agregar la lógica que desees según la palabra recibida
            self.accion_stream(palabra)
            # Ejemplo: enviar una respuesta al cliente
            if(palabra != "config"):
                respuesta = "Respuesta a la palabra " + palabra
            else:
                pass
            self.cliente_socket.send(respuesta.encode())

        self.cerrar_conexion()

    def cerrar_conexion(self):
        self.cliente_socket.close()
        self.mi_socket.close()
        print("Conexiones cerradas. Servidor detenido.")

    def accion_stream(self, accion):
        if(accion=="config"):
            try:
                app = InterfazGrafica()
                print("El arreglo nuevo de config es:")
                arreglo = app.get_array()
                print("Valor del objeto")
                print(arreglo)
                self.enviar_arreglo(arreglo)

            except Exception as e:
                # Manejo de la excepción
                print("Config se cerró inesperadamente:", str(e))

        elif(accion == "visualstudio"):
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
        else:
            print("Opcion invalida")
    
    def enviar_arreglo(self, arreglo):
        print("Enviando el arreglo")
        try:
            arreglo_serializado = pickle.dumps(arreglo)
            print(arreglo_serializado)
            self.cliente_socket.send(arreglo_serializado)
            print("arreglo enviado")
        except Exception as e:
            print("Error al enviar el arreglo:", str(e))

class InterfazGrafica:
    def __init__(self):
        self.inputs = []
        self.arreglo = []
        self.ventana = tk.Tk()
        self.ventana.title("Interfaz con Tkinter")
        self.ventana.geometry("400x200")

        self.crear_interfaz()

        self.ventana.mainloop()

    def crear_interfaz(self):
        for i in range(4):
            label = tk.Label(self.ventana, text=f"Input {i+1}:")
            label.pack()

            entry = tk.Entry(self.ventana)
            entry.pack(pady=5)

            self.inputs.append(entry)

        boton = tk.Button(self.ventana, text="Verificar", command=self.verificar_inputs)
        boton.pack(pady=10)

    def verificar_inputs(self):
        valores = [entry.get() for entry in self.inputs]

        if len(set(valores)) != len(valores):
            tk.messagebox.showerror("Error", "Los valores no pueden ser nulos o iguales.")
            return

        if len(valores) == 4:
            self.cerrar_ventana()
            self.guardar_arreglo(valores)
        else:
            tk.messagebox.showerror("Error", "Debe ingresar valores en todos los inputs.")

    def guardar_arreglo(self, valores):
        print("Dentro guardar_arreglo")
        self.arreglo = valores  # Aquí puedes realizar cualquier procesamiento adicional con los valores ingresados
        print(self.arreglo)  # Muestra el arreglo en la consola


    def cerrar_ventana(self):
        self.ventana.destroy()

    def get_array(self):
        return self.arreglo


if __name__ == "__main__":
    servidor = ServidorSocket()
