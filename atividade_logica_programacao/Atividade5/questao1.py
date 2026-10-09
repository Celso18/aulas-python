# Questão 1: Menu da Lanchonete

codigo = int(input("Digite o código do item (1 a 4): "))

match codigo:
    case 1:
        print("Produto: Cachorro-quente")
        print("Preço: R$ 10,00")
    case 2:
        print("Produto: Hambúrguer")
        print("Preço: R$ 15,00")
    case 3:
        print("Produto: Batata Frita")
        print("Preço: R$ 8,00")
    case 4:
        print("Produto: Refrigerante")
        print("Preço: R$ 5,00")
    case _:
        print("Código inválido. Escolha um código de 1 a 4.")
