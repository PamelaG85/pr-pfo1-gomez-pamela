import requests
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Conexión al servidor y envío de mensajes
def enviar_mensaje():
    url = 'http://localhost:5000/mensaje'

    while True:
        mensaje = input("Escriba su mensaje o 'éxito' para salir: ")

        if mensaje.lower()  == 'éxito':
            print(Fore.YELLOW + "Ha salido exitosamente.")
            break

        data = {"mensaje": mensaje}

        try:
            respuesta = requests.post(url, json=data)

            if respuesta.status_code == 200:
                contenido = respuesta.json() # Agregué estas 2 líneas para que el mensaje se vea con un formato más lindo en la terminal
                print(Fore.GREEN + f"Servidor: {contenido['mensaje']}, {contenido['timestamp']}")
            else:
                print(Fore.MAGENTA + f"Error: código de estado {respuesta.status_code}")

        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error de conexión: {e}")

if __name__ == "__main__":
    enviar_mensaje()            