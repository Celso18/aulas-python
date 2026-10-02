carrinho = []
total = 0

while True:
    nome = input("Digite 'fim' para finalizar."
                 "\nDigite o nome do produto: ")
    if nome == "fim":
        break
    preco = float(input("Digite o valor desse produto:"))
    total += preco

    # adicionando uma LISTA dentro de uma LISTA
    carrinho.append([nome, preco])

with open("carrinho.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.write("RECIBO DO CARRINHO\n\n")

    arquivo.write(str(carrinho[0]))

    for produto in carrinho:
        nome_produto = produto[0]
        preco_produto = produto[1]

        arquivo.write(f"Produto: {nome_produto} R${preco_produto:.2f}\n")

    arquivo.write(f"\nTotal a pagar: {total:.2f}\n")