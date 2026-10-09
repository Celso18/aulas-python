
#Questão 1: A Divisão da Conta (Calculadora)

# Entrada de dados pelo usuário
valor_total = float(input("Digite o valor total da conta (ex: 150.00): R$ "))
quantidade_pessoas = int(input("Digite a quantidade de pessoas na mesa: "))

# Cálculo da divisão da conta
valor_dividido = valor_total / quantidade_pessoas

# Exibição do resultado formatado com duas casas decimais
print(f"O valor total foi de R$ {valor_total:.2f}, e cada pessoa deve pagar R$ {valor_dividido:.2f}")

#️ Explicação da questão 1:
# float(input(...)): Converte o texto digitado pelo usuário em um número decimal,
# permitindo centavos.int(input(...)): Converte a quantidade de pessoas em um número inteiro.:.2f:
# Formata a saída dentro da f-string para garantir que os valores monetários sempre exibam exatamente duas casas decimais.