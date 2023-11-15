from flask import request, jsonify
from model import Jogador
from app_settings import app, db
from insert_data import insert_csv


@app.route("/")
def homepage():
    insert_csv(r'c:\Users\JorgeFerreira\Downloads\dados.csv')
    return "A API esta no ar!"


@app.route("/adicionar_stats", methods=["POST"])
def adicionar_stats():
    data = request.json

    try:
        jogador = Jogador.query.filter_by(nome=data["nome"]).first()
    except Exception as e:
        raise e
    
    if jogador:
        return jsonify({"message": "Stats adicionados com sucesso!"})

    jogador = Jogador(**data)
    jogador.calcular_nota()
    db.session.add(jogador)
    db.session.commit()
    return jsonify({"message": f"{jogador.nome}-> {jogador.nota}"})

@app.route('/nota/<nome>', methods=['GET'])
def obter_nota(nome):
    jogador = Jogador.query.filter_by(nome=nome).first()

    if jogador:
        return jsonify({'nome': jogador.nome, 'nota': jogador.nota})
    else:
        return jsonify({'message': 'Jogador não encontrado'}), 404
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
