import requests

link = 'http://192.168.205.100:8080/usuarios'
resposta = requests.get(link)

print(resposta.json())

#chaves aceitas na API da aula: 'nome' 'email'


meus_dados ={
    "nome": "Celso",
    "email":"celso.batista@semnai.com;br"
    }

envio = requests.post(link, json=meus_dados)
print(f'STATUS ENVIO DE DADOS {envio}')