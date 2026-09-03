
#***Questão 8: Prova Real dos Tipos de Dados***

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))

print(type(nome))
print(type(idade))
print(type(altura))

#Explicação: usamos str() para garantir que o nome seja uma string, int() para
#transformar a idade em inteiro e float() para transformar a altura em número
#decimal. O type() comprova o tipo de cada variável.

