# Questão 4: Menu Interativo

opcao = 0

while opcao != 2:
    print("\n1 - Mostrar saudação")
    print("2 - Sair do programa")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Olá, seja muito bem-vindo(a)!")
    elif opcao != 2:
        print("Opção inválida!")

print("Programa encerrado.")