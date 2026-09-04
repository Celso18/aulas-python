#***Questão 3: O Validador de Idade para Votação***

# Solicita a idade do usuário e converte para número inteiro
idade = int(input("Digite a sua idade: "))

# Verifica se a idade é maior ou igual a 18 anos
if idade >= 18:
    print("Você é obrigado a votar.")
else:
    print("Você ainda não é obrigado a votar.")

#EXPLICAÇÃO DO CÓDIGO:

#>= 18: O operador >= significa "maior ou igual". Ele garante que quem tem exatamente 18 anos
# já entre na condição de voto obrigatório.int(input(...)): Como a idade é sempre um número inteiro
# (18, 19, 20...), usamos o int para a conversão.
