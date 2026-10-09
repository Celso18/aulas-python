# Questão 3: Turno de Estudo

turno = input("Digite o turno em que você estuda (M, V ou N): ").upper()

match turno:
    case "M":
        print("Bom Dia!")
    case "V":
        print("Boa Tarde!")
    case "N":
        print("Boa Noite!")
    case _:
        print("Turno inválido!")
