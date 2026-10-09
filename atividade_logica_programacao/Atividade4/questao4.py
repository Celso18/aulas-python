#***Questão 4: O Teste do Saldo Bancário***

# Define o saldo inicial do cliente (pode ser alterado)
saldo_atual = 500.00

# Solicita o valor que o cliente deseja sacar
valor_saque = float(input("Digite o valor que deseja sacar: R$ "))

# Verifica se o cliente tem saldo suficiente para o saque
if valor_saque <= saldo_atual:
    # Subtrai o valor do saque e atualiza o saldo
    saldo_atual = saldo_atual - valor_saque
    print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo_atual:.2f}")
else:
    print("Saldo insuficiente para realizar esta operação.")

    # EXPLICAÇÃO DO CÓDIGO:

#saldo_atual = saldo_atual - valor_saque: Esta linha atualiza a própria variável do saldo,
# guardando o novo valor após a retirada do dinheiro.:.2f dentro da chave: Esse comando formata
# o número decimal para exibir sempre duas casas após a vírgula (ex: mostra R$ 450.00 em vez de R$ 450.0).