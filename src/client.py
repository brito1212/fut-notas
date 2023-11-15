import requests

# URL do serviço web
nome = 'Yuri Alberto'
url = f'http://localhost:5000/nota/{nome}'

# Requisita o serviço web
requisicao = requests.get(url)
resposta_json = requisicao.json()

print(requisicao)
print(resposta_json)

# Exibe a nota do jogador
print(f'Nota do jogador: {resposta_json}')
