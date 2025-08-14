from flask import Flask
from waitress import serve

app = Flask(__name__)

# Dados simulados (exemplo)
usuarios = [
    {"id": 1, "nome": "Gabriela"},
    {"id": 2, "nome": "João"},
]

# Rota principal (GET)
@app.route('/')
def home():
    return "API Flask rodando com Waitress no windows!"

# Rota para listar todos os usuários (GET)
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

# Rota para buscar usuário por id (GET)
@app.route('/usuarios/<int:id>', methods=['GET'])
def buscar_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# Rota para criar um novo usuário (POST)
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

# Rota para atualizar usuário (PUT)
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    dados = request.get_json()
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        usuario.update(dados)
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# Rota para deletar usuário (DELETE)
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    global usuarios
    usuarios = [u for u in usuarios if u['id'] != id]
    return jsonify({"msg": "Usuário deletado"})

if __name__ == '__main__':
    serve(app, host='0.0.0.0',
port=8000)