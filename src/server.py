from flask import request, jsonify
from model import Jogador
from app import app, db


@app.route("/")
def homepage():
    return "A API esta no ar!"


@app.route("/adicionar_stats", methods=["POST"])
def adicionar_stats():
    data = request.json

    jogador = Jogador.query.filter_by(nome=data["nome_jogador"]).first()

    if jogador:
        return jsonify({"message": "Stats adicionados com sucesso!"})

    jogador = Jogador(**data)
    jogador_nota = jogador.calcular_nota()
    jogador.nota = jogador_nota
    return jsonify({"message": f"{jogador.nome}-> {jogador.nota}"})


if __name__ == "__main__":
    app.run(debug=True)
