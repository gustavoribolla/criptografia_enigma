from flask import Flask, request, jsonify
from codificador_de_matrizes_rafaela_ribolla import *

app = Flask(__name__)

@app.route('/')
def index():
    return {"mensagem": "Api em funcionamento"}, 200

@app.route('/cifra', methods=['POST'])
def cifra():
    mensagem = request.json["mensagem"]
    matriz = para_one_hot(mensagem)
    mensagem = para_string(matriz)
    P = np.roll(np.eye(26, dtype=int), 1, axis=0)
    mensagem_cifrada = cifrar(mensagem, P)
    return {"mensagem_cifrada": mensagem_cifrada}, 200

@app.route('/decifra', methods=['POST'])
def decifra():
    mensagem_cifrada = request.json["mensagem_cifrada"]
    P = np.roll(np.eye(26, dtype=int), 1, axis=0)
    mensagem_original = de_cifrar(mensagem_cifrada, P)
    return {"mensagem_original": mensagem_original}, 200

@app.route('/enigma', methods=['POST'])
def cifra_enigma():
    mensagem = request.json["mensagem"]
    matriz = para_one_hot(mensagem)
    mensagem = para_string(matriz)
    P = np.roll(np.eye(26, dtype=int), 1, axis=0)
    E = np.roll(np.eye(26, dtype=int), 2, axis=1)
    mensagem_com_enigma = enigma(mensagem, P, E)
    return {"mensagem_com_enigma": mensagem_com_enigma}, 200

@app.route('/de_enigma', methods=['POST'])
def decifra_enigma():
    mensagem_com_enigma = request.json["mensagem_com_enigma"]
    P = np.roll(np.eye(26, dtype=int), 1, axis=0)
    E = np.roll(np.eye(26, dtype=int), 2, axis=1)
    mensagem_original = de_enigma(mensagem_com_enigma, P, E)
    return {"mensagem_original": mensagem_original}, 200

if __name__ == '__main__':
    app.run(debug=True, threaded=True)