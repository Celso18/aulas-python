
#Questão 5: Sistema de Cálculo de Idade

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = int(input("Digite o ano em que estamos: "))
idade = ano_atual - ano_nascimento

print("Olá! Você tem aproximadamente", idade, "anos de idade.")

#Explicação do código
#A função input() recebe os valores digitados pelo usuário como texto. Por isso,
#utilizamos int() para converter esses valores em números inteiros:
#ano_nascimento = int(input("Digite o seu ano de nascimento: "))
#Em seguida, calculamos a idade:
#idade = ano_atual - ano_nascimento
#Por fim, exibimos uma mensagem amigável:
#print("Olá! Você tem aproximadamente", idade, "anos de idade.")
