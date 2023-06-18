import socket
import subprocess
import webbrowser
import time

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
            respuesta = "Respuesta a la palabra " + palabra
            self.cliente_socket.send(respuesta.encode())

        self.cerrar_conexion()

    def cerrar_conexion(self):
        self.cliente_socket.close()
        self.mi_socket.close()
        print("Conexiones cerradas. Servidor detenido.")

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
        else:
            print("Opcion invalida")
            

if __name__ == "__main__":
    servidor = ServidorSocket()
