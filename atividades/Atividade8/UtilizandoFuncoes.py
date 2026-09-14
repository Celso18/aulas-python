def avaliar_aluno(nome, nota1, nota2, nota3, nota4):
    # Calcula a média final
    media_final = (nota1 + nota2 + nota3 + nota4) / 4

    # Define a situação do aluno
    if media_final >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    # Imprime todos os valores na tela
    print(f"Nome do Aluno: {nome}")
    print(f"Nota 1º Bimestre: {nota1}")
    print(f"Nota 2º Bimestre: {nota2}")
    print(f"Nota 3º Bimestre: {nota3}")
    print(f"Nota 4º Bimestre: {nota4}")
    print(f"Média Final: {media_final:.2f}")
    print(f"Situação: {situacao}")


# Exemplo de uso da função:
avaliar_aluno("Celso Romão", 8.0, 6.5, 7.5, 7.0)

#A função avaliar_aluno recebe os 5 parâmetros solicitados (nome e as 4 notas).
#Ela soma as notas, divide por 4 e guarda o resultado na variável media_final.
#A estrutura condicional if/else testa se a média é maior ou igual a 7 para definir se o aluno passou ou não.
#O comando f"{media_final:.2f}" serve apenas para arredondar a exibição da média para duas casas decimais.
