import socket
from colorama import init, Fore, Style

# Conectar al servidor y enviar mensajes
def enviar_mensajes():
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(('localhost', 5000))
        print(Fore.GREEN + "Conectado al servidor.")

        while True:
            mensaje = input(Fore.LIGHTWHITE_EX + "Escriba su mensaje o 'éxito' para salir: ")
            if mensaje.lower() == 'éxito':
                print(Fore.YELLOW + "Ha salido exitosamente.")
                break

            cliente.sendall(mensaje.encode())
            respuesta = cliente.recv(1024).decode()
            print(Fore.GREEN + "Servidor:", respuesta)

        cliente.close()

    except ConnectionRefusedError:
        print(Fore.RED + "No se pudo conectar al servidor. ¿Está corriendo?")
    except Exception as e:
        print(f"Error: {e}")

# Ejecutar cliente
if __name__ == "__main__":
    enviar_mensajes()
