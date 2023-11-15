import requests

# URL do serviço web
url = 'http://localhost:5000/jogadores'


# Requisita o serviço web
requisicao = requests.get(url)
resposta_json = requisicao.json()

print(requisicao)
print(resposta_json)

# Exibe a nota do jogador
print(f'Nota do jogador: {resposta_json["nota"]}')
