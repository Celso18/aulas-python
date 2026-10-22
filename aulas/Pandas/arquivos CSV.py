import csv # COMAND SEPARATED VALUE

# LISTAS
dados_lista = [
    ["nome", "idade", "cidade"],
    ["João", 22, "Luziânia"],
    ["Italo", 25, "Brasília"]
]

#criando e escrevendo um novo arquivo CSV
with open('dados_da_lista.csv', 'w', encoding="utf-8", newline='') as arquivo:
    escrita = csv.writer(arquivo)
    escrita.writerows(dados_lista)

print("ARQUIVO ESCRITO COM SUCESSO\n")

with open('dados_da_lista.csv', 'r', encoding="utf8", newline='') as arquivo:
    # next(arquivo)
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

print('\n\n')

dados_dicionario = [
    {"nome": "Rafael","idade": 21,"cidade": "Brasília"},
    {"nome": "Katia","idade": 19,"cidade": "París"}
]

colunas = ["nome", "idade", "cidade"]

with open("dados_do_dicionario.csv", "w", encoding="utf-8", newline='') as arquivo:
    escrita = csv.DictWriter(arquivo, fieldnames=colunas)
    escrita.writeheader()
    escrita.writerows(dados_dicionario)

with open("dados_do_dicionario.csv", "r", encoding="utf-8", newline='') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(f"Nome: {linha["nome"]}\n"
              f"Idade: {linha["idade"]}\n"
              f"Cidade: {linha["cidade"]}\n")