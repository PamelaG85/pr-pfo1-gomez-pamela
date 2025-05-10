import sqlite3

# Inicializar base de datos
def inicializar_db():
    try:
        conexion = sqlite3.connect("mensajes.db")
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        ''')
        conexion.commit()
        conexion.close()
    except sqlite3.Error as e:
        print(f"[DB] Error al inicializar la base de datos: {e}")
        exit(1)

# Guardar mensaje en la base
def guardar_mensaje(contenido, fecha_envio, ip_cliente):
    try:
        conexion = sqlite3.connect("mensajes.db")
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)",
            (contenido, fecha_envio, ip_cliente)
        )
        conexion.commit()
        conexion.close()
    except sqlite3.Error as e:
        print(f"[DB] Error al guardar el mensaje: {e}")
