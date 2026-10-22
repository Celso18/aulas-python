import pandas as pd

# VERIFICAR VERSÃO PANDAS
# print(pandas.__version__)

# SERIES
# Uma dimensão -> Vetor
nomes =   ["João"   , "Felipe",  "André"]
indexes = ["pessoa1", "pessoa2", "pessoa3"]
nomes_series = pd.Series(nomes, index=indexes)
print(nomes_series) # series do pandas

coluna_idades = pd.Series([25,30,35,40,45],
                          index=['a', 'b', 'c', 'd', 'e'])
#print(coluna_idades[coluna_idades < 30])# retorna uma linha
#print(coluna_idades.loc['a'])           # retorna o valor

# DATAFRAMES
# valores com várias dimensões -> Matriz
# converte dicionário em DataFrame
notas = {
    'nome': ["italo", "Bruno", "Charlie", "Maikon"],
    'turma':["Python", "Java", "Baco de Dados", "Front-end"],
    'notas': [10,8,5,6]
}
# adiciona nomes para index
df = pd.DataFrame(notas,
                  index=["aluno1", "aluno2", "aluno3", "aluno4"])
print("=== PRIMEIRA LISTA ===")
print(df)
# print(df.loc["aluno1"]) # procura pela chave
# print(df.iloc["aluno1"]) # procura pelo index da lista
print('\n')
print("=== LISTA ATUALIZADA - COLUNA NOVA ===")
df["status"] = ["Aprovado", "Aprovado", "Reprovado", "Reprovado"]
print(df)

nova_linha = pd.DataFrame([{
    'nome': "Victor",
    'turma': "Python",
    'notas': 9,
    'status': "Aprovado",
},
{
    'nome': "Nael",
    'turma': "JavaScript",
    'notas': 2,
    'status': "Reprovado",
}
], index=["aluno5", "aluno6"])

# faz a concatenação de valores no dicionário
df = pd.concat([df, nova_linha])

print('\n')
print("=== LISTA ATUALIZADA - LINHA NOVA ===")
print(df)

print('\n')
print("=== LISTA ALUNOS APROVADOS ===")
filtro= df[['nome',"turma"]]
print(filtro)

print('\n')
print("=== NOME E TURMA ===")

for indice in df.index:
    if df.loc[indice, "turma"] == "Python":
        print(df.loc[indice, "nome"], df.loc[indice, "turma"])
