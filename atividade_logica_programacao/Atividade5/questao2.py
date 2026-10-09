# Questão 2: Classificador de Vogais e Consoantes

letra = input("Digite uma letra do alfabeto: ").lower()

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("Você digitou uma vogal.")
    case _:
        print("Não é uma vogal.")
