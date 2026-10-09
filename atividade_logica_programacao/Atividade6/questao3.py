# Questão 3: Somador de Números

soma = 0
numero = int(input("Digite um número inteiro (0 para encerrar): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite um número inteiro (0 para encerrar): "))

print(f"A soma dos números digitados é: {soma}")