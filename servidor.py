import socket

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

            # Ejemplo: enviar una respuesta al cliente
            respuesta = "Respuesta a la palabra " + palabra
            self.cliente_socket.send(respuesta.encode())

        self.cerrar_conexion()

    def cerrar_conexion(self):
        self.cliente_socket.close()
        self.mi_socket.close()
        print("Conexiones cerradas. Servidor detenido.")


if __name__ == "__main__":
    servidor = ServidorSocket()
