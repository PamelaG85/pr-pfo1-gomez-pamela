import socket
import sqlite3
from datetime import datetime
from init_db import inicializar_db, guardar_mensaje

# Inicialización del socket TCP/IP
def inicializar_socket():
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind(('localhost', 5000))
        servidor.listen(3)  # Máximo 3 conexiones en cola
        print("Servidor escuchando en localhost:5000")
        return servidor
    except OSError as e:
        print(f"Error al iniciar el servidor: {e}")
        exit(1)

# Aceptar conexiones y recibir mensajes
def manejar_conexiones(servidor):
    while True:
        cliente, direccion = servidor.accept()
        print(f"Conexión recibida de {direccion}")
        try:
            while True:
                mensaje = cliente.recv(1024).decode()
                if not mensaje:
                    break

                timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                guardar_mensaje(mensaje, timestamp, direccion[0])

                respuesta = f"Mensaje recibido: {timestamp}"
                cliente.sendall(respuesta.encode())

        except ConnectionResetError:
            print("Cliente desconectado.")
        finally:
            cliente.close()

# Ejecutar servidor
if __name__ == "__main__":
    inicializar_db()
    servidor = inicializar_socket()
    manejar_conexiones(servidor)
