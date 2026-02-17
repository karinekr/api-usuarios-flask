from flask import Flask, request, jsonify

app = Flask(__name__)

# "Banco de dados" em memória
usuarios = []

# Criar usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()

    if not dados or "nome" not in dados or "email" not in dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    usuario = {
        "id": len(usuarios) + 1,
        "nome": dados["nome"],
        "email": dados["email"]
    }

    usuarios.append(usuario)
    return jsonify(usuario), 201


# Listar usuários (com filtro por nome)
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    nome = request.args.get('nome')

    if nome:
        filtrados = [
            usuario for usuario in usuarios
            if nome.lower() in usuario["nome"].lower()
        ]
        return jsonify(filtrados), 200

    return jsonify(usuarios), 200


if __name__ == "__main__":
    app.run(debug=True)
