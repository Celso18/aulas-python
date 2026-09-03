
#Questão 5: O Sistema de Desconto (Lógica OR)

# Entrada de dados da compra e status do cliente
valor_compra = float(input("Digite o valor total da compra: R$ "))
status_vip = int(input("Você possui o cartão VIP da loja? (Digite 1 para SIM ou 0 para NÃO): "))

# Conversão do número digitado (1 ou 0) para um valor Booleano (True ou False)
# O número 1 vira True (é VIP) e o número 0 vira False (não é VIP)
e_vip = bool(status_vip)

# Verificação do direito ao frete grátis usando o operador lógico 'or'
frete_gratis = (valor_compra > 200.00) or e_vip

# Exibição do resultado direto na tela
print("O cliente tem direito a frete grátis?", frete_gratis)

#Explicação da questão 5
# bool(status_vip): Em Python, o número 0 é considerado logicamente Falso (False),
# enquanto qualquer outro número inteiro (como o 1) é Verdadeiro (True).
# Fazer esse casting converte a resposta numérica do usuário diretamente em um estado booleano.Operador lógico or:
# Este operador é menos rígido que o and. Ele retorna True se qualquer uma das condições for verdadeira.
# O cliente terá frete grátis se gastar mais de R$ 200.00, se for VIP, ou se cumprir ambos os requisitos simultaneamente.