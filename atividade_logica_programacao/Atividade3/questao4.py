
#Questão 4: O Boletim Escolar Automático (Aritmética + Lógica AND)

# Entrada das notas e da frequência do aluno
nota1 = float(input("Digite a Nota 1 do aluno: "))
nota2 = float(input("Digite a Nota 2 do aluno: "))
frequencia = float(input("Digite a porcentagem de frequência do aluno (ex: 80): "))

# Cálculo da média das notas
media = (nota1 + nota2) / 2

# Verificação das duas condições obrigatórias usando o operador lógico 'and'
aprovado = (media >= 6.0) and (frequencia >= 75.0)

# Exibição dos resultados na tela
print(f"\nMédia final do aluno: {media:.1f}")
print("Aluno aprovado?", aprovado)

#Explicação da questão 4
# (nota1 + nota2) / 2: Os parênteses são obrigatórios para garantir que a soma das notas
# seja realizada antes da divisão por 2 (ordem de precedência dos operadores matemáticos).
# Operador lógico and: Este operador exige que todas as condições sejam verdadeiras para retornar True.
# Se o aluno tiver média maior que 6.0, mas faltar muito (frequência abaixo de 75%), o resultado final será False.