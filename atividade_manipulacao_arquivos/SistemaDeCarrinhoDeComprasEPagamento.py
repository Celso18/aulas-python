# Questão 1: Sistema de Carrinho de Compras e Pagamento

usuario = input("Digite seu nome para iniciar a compra: ")
produtos = []
total = 0

while True:
    nome_produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")

    if nome_produto.lower() == "fim":
        break

    preco_produto = float(input("Digite o preço do produto: R$ "))
    produtos.append([nome_produto, preco_produto])
    total += preco_produto

print("\n--- FINALIZANDO COMPRA ---")

with open("pagamento.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Cliente: {usuario}\n")
    arquivo.write("Produtos:\n")

    for produto in produtos:
        arquivo.write(f"{produto[0]}: R$ {produto[1]:.2f}\n")

    arquivo.write(f"TOTAL: R$ {total:.2f}\n")

print("\n--- PROCESSANDO PAGAMENTO ---")

with open("pagamento.txt", "r", encoding="utf-8") as arquivo:
    recibo = arquivo.read()

marcador_total = "TOTAL: R$ "
inicio_total = recibo.find(marcador_total)
valor_total = recibo[inicio_total + len(marcador_total):].splitlines()[0]

print(f"Compra processada com sucesso! Valor cobrado: R$ {valor_total}")
