
import csv #
from dataclasses import fields

from aulas.manipulando_arquivos.LidandoComJson.SistemaDeGerenciamentoDeEstoque import dados_lidos

#LISTAS

dados_lidos = [

    ["nome", "idade", "cidade"],
    ["Celso",25,"Goiânia"],
    ["Rodrigo",35,"Rio de Janeiro"]

    #criando e escrevendo um novo arquivo

with open("arquivo_da_lista.csv", "w", encoding="utf-8", newline=as arquivo:
    escrita_csv = csv.writer(arquivo)
    escrita_csv.writerows(dados_lista)

print('arquivo_da_lista.csv criado com sucesso!')
with open('arquivo_da_lista.csv' "w", encoding="utf-8", newline=as arquivo:
    leitor = csv.wrinter(arquivo)
    for linha in leitor:
        print(linha)

        print('\n\n')

        dados_dicionario = [
            {'nome', 'idade', 'cidade'},
            {'Celso',25 'Brasilia-DF'},
            {'Rodrigo',35 'Rio de Janeiro'}


        ]
colunas = ['nome', 'idade', 'cidade']

with open('dados_do_funcionario.csv', "w", enconding="utf-8", newline=as arquivo:
    escrtia.csv.writer(arquivo, fields= dados_dicionario)
    escrita_csv = writerheader()
    escrita_csv.writerows(dados_lidos)