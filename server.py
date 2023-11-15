# Importa o módulo Flask e pandas
from flask import Flask, request, jsonify
import pandas as pd

# Cria uma instância do Flask
app = Flask(__name__)

# Rota homepage
app.route('/')
def homepage():
    return 'A API esta no ar!'

# Rota para a para calcular a nota
@app.route('/jogadores/<nome>')
def calcular_nota(nome):
    dados = pd.read_csv('dados.csv')
    dados_json = dados.to_json()
    return jsonify(dados_json)

# Inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)
