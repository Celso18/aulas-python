# ***Questão 1: O Verificador de Par ou Ímpar***

# Solicita ao usuário que digite um número inteiro e converte para o tipo int
numero = int(input("Digite um número inteiro: "))

# Verifica se o resto da divisão por 2 é igual a zero
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")

# EXPLICAÇÃO DO CÓDIGO:
#int(input(...)): O input sempre recebe o que você digita como texto (string).
# Usamos o int() para transformar esse texto em um número inteiro, permitindo fazer cálculos matemáticos.% 2:
# O operador de resto (%) divide o número por 2 e devolve apenas o que sobrou. Se a divisão for exata (resto 0),
# o número é par.f"O número {numero}...": Essa é uma f-string. Ela permite que você coloque a variável numero direto
# dentro do texto usando as chaves {}, deixando o código mais limpo.