from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []
contador_id = 1

@app.route('/')
def home():
    return {'mensagem': 'API funcionando'}

@app.route('/usuarios', methods=['GET', 'POST'])
def gerenciar_usuarios():
    global contador_id

    if request.method == 'POST':
        dados = request.get_json()

        usuario = {
            'id': contador_id,
            'nome': dados.get('nome'),
            'email': dados.get('email')
        }

        usuarios.append(usuario)
        contador_id += 1

        return jsonify(usuario), 201

    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)

