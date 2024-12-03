from flask import Flask, jsonify

app = Flask(__name__)

# Ruta para recibir el Webhook, solo acepta POST
@app.route('/webhook', methods=['POST'])
def webhook():
    # Responder con un simple "Hola Mundo"
    return jsonify({"message": "Hello World from Webhook"}), 200

# Ejecutar el servidor en el puerto 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
