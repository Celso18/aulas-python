# Questão 5: Calculadora Básica de Dois Números

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, * ou /): ")

match operador:
    case "+":
        print(f"Resultado: {numero1 + numero2}")
    case "-":
        print(f"Resultado: {numero1 - numero2}")
    case "*":
        print(f"Resultado: {numero1 * numero2}")
    case "/":
        print(f"Resultado: {numero1 / numero2}")
    case _:
        print("Operação inválida!")
