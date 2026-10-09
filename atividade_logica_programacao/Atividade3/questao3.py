
#Questão 3: A Catraca do Parque (Operadores de Comparação)

# Entrada da altura da criança em metros
altura = float(input("Digite a altura da criança em metros (ex: 1.45): "))

# Verificação se a altura é maior ou igual a 1.40m
pode_entrar = altura >= 1.40

# Exibição do resultado booleano direto na tela
print("A criança pode entrar na montanha-russa?", pode_entrar)

#Explicação da questão 3
# float(input(...)): Transforma o texto digitado (como "1.35") em um número decimal (float),
# permitindo a comparação com casas decimais.>=: Este é o operador relacional de maior ou igual.
# Ele analisa o valor da variável altura contra o limite de 1.40 e gera automaticamente
# o tipo bool (True se a condição for verdadeira ou False caso contrário).
