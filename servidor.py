from flask import Flask, request, jsonify
from init_db import inicializar_db, guardar_mensaje
from datetime import datetime

# Crear la app de Flask
app = Flask(__name__)

# Inicializar la BD
inicializar_db()

# Ruta para recibir mensajes
@app.route ('/mensaje', methods=['POST'])
def recibir_mensaje():
    try:
        if not request.is_json: # verifica que venga un JSON
            return jsonify({'error': 'El contenido debe ser JSON'}), 400
    
        datos = request.get_json()
        mensaje = datos.get('mensaje')
        ip_cliente = request.remote_addr

        if not mensaje:
            return jsonify({'error': 'Falta el campo "mensaje"'}), 400
    
        #timestamp actual
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        # Guardar en la base de datos
        guardar_mensaje(mensaje, timestamp, ip_cliente)

        return jsonify({
            'mensaje': 'Mensaje recibido exitosamente',
            'timestamp': timestamp
        }), 200
    
    except Exception as e:
        print(f"[ERROR] {e}")
        return jsonify({'error': 'Error interno del servidor'}), 500
    
# Ruta para comprobar que el esvidor está vivo
@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'Servidor funcionando correctamente'}), 200

# Levantar la app
if __name__ == '__main__':
    app.run(debug=True, port=5000)