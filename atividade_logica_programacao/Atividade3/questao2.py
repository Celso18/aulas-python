
#Questão 2: A Fábrica de Caixas (Operador de Módulo)

# Entrada da quantidade total de maçãs colhidas
total_macas = int(input("Digite a quantidade total de maçãs colhidas no dia: "))

# Cálculo das maçãs restantes usando o operador de módulo (%)
macas_sobradas = total_macas % 12

# Cálculo opcional para enriquecer o resultado: quantidade de caixas cheias
caixas_cheias = total_macas // 12

# Exibição dos resultados na tela
print(f"Com {total_macas} maçãs, foram preenchidas {caixas_cheias} caixas completas.")
print(f"Quantidade de maçãs que sobrarão fora das caixas: {macas_sobradas}")

# Explicação da questão 2:
# total_macas % 12: O operador % divide o total de maçãs por 12 e devolve apenas o resto dessa divisão.
# Por exemplo, se o usuário digitar 25, o Python faz 25 ÷ 12 = 2 (com resto 1).
# O programa exibirá que sobrou 1 maçã.total_macas // 12: O operador // realiza a divisão inteira, descartando
# os números após a vírgula para nos dar exatamente o número de caixas completas.