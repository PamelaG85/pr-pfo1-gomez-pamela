Hola Profe, le dejo este archivo con algunas anotaciones.

### Librerías de Python necesarias:
* flask
* requests
* colorama

### Ejecución inicial:

1. La base de datos se crea automáticamente al iniciar el servidor por primera vez.
2. Cada mensaje se guarda con el contenido, fecha y la IP de cliente.

### Pruebas
<p>Para realizar las pruebas envíe distintos mensajes a través de Postman, estos mensajes que se fueron guardando en la BD luego tuve que borrarlos varias veces</p>
<p>Finalmente me fue más fácil resetearla, para ello cree el script de reset_db.py.</p>

### Resetear base de datos:
Se ejecuta el script con el comando:
```bash
    python reset_db.py
```