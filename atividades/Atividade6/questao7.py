# Questão 7: Controle de Orçamento

orcamento = 500

while orcamento > 0:
    gasto = float(input("Digite o valor do gasto: R$ "))
    orcamento -= gasto
    print(f"Saldo restante: R$ {orcamento:.2f}")

print("Atenção: Você ficou sem saldo ou estourou seu orçamento!")
