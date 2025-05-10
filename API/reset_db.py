import sqlite3
from colorama import init, Fore, Style

def reiniciar_db():
    try:
        conexion = sqlite3.connect("mensajes.db")
        cursor = conexion.cursor()

        # Eliminar la tabla si existe
        cursor.execute("DROP TABLE IF EXISTS mensajes")

        # Volver a crear la tabla
        cursor.execute('''
        CREATE TABLE mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT NOT NULL,
            fecha_envio TEXT NOT NULL,
            ip_cliente TEXT NOT NULL
        )
        ''')

        conexion.commit()
        conexion.close()
        print(Fore.GREEN + "Base de datos reiniciada correctamente.")

    except sqlite3.Error as e:
        print(Fore.RED + f"Error al reiniciar la base de datos: {e}")

if __name__ == "__main__":
    reiniciar_db()