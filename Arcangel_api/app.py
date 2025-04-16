from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Cargar las letras
with open('lyrics.json', 'r', encoding='utf-8') as f:
    letras = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('q', '').lower()
    resultados = {
        titulo: letra for titulo, letra in letras.items() if query in titulo.lower()
    }
    if resultados:
        return jsonify(resultados)
    else:
        return jsonify({"mensaje": "Canción no encontrada."}), 404

if __name__ == '__main__':
    app.run(debug=True)