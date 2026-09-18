# Questão 1: Média Final do Aluno


def avaliar_aluno(nome, primeiro_bimestre, segundo_bimestre, terceiro_bimestre, quarto_bimestre):
    media_final = (
        primeiro_bimestre
        + segundo_bimestre
        + terceiro_bimestre
        + quarto_bimestre
    ) / 4

    print(f"\nAluno: {nome}")
    print(f"Nota do primeiro bimestre: {primeiro_bimestre:.2f}")
    print(f"Nota do segundo bimestre: {segundo_bimestre:.2f}")
    print(f"Nota do terceiro bimestre: {terceiro_bimestre:.2f}")
    print(f"Nota do quarto bimestre: {quarto_bimestre:.2f}")
    print(f"Média final: {media_final:.2f}")

    if media_final >= 7:
        print("Situação: Aprovado.")
    else:
        print("Situação: Reprovado.")


nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))

avaliar_aluno(nome, nota1, nota2, nota3, nota4)
