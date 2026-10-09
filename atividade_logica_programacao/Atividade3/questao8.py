
#Questão 8: A Calculadora de Lucro da Empresa

# Entrada dos dados comerciais do produto
nome_produto = input("Digite o nome do produto: ")
custo_fabrica = float(input("Digite o custo de fábrica do produto (R$): "))
preco_venda = float(input("Digite o preço de venda na loja (R$): "))

# Cálculo do lucro líquido em reais
lucro = preco_venda - custo_fabrica

# Verificação se o lucro atinge a meta da loja (maior que 20 reais)
lucro_bom = lucro > 20.00

# Exibição do relatório final formatado
print(f"\n--- Relatório Comercial: {nome_produto} ---")
print(f"Lucro obtido por unidade: R$ {lucro:.2f}")
print("O lucro foi bom (maior que R$ 20.00)?", lucro_bom)

#Explicação da questão 8
# Preco_venda - custo_fabrica: Operação aritmética simples que deduz os custos para extrair o valor real que sobra
# em caixa por produto vendido.lucro > 20.00: Utiliza o operador relacional de maior que.
# Caso o lucro seja de exatamente R$ 20.00, a resposta ainda será False, pois a condição exige que o valor
# seja estritamente superior a esse limite.{lucro:.2f}: Técnica de formatação que fixa a exibição do dinheiro
# em duas casas decimais, evitando que dízimas ou arredondamentos incorretos poluam o relatório do comerciante.
