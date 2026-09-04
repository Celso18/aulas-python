#***Questão 5: A Catraca VIP de Eventos (Uso de AND e OR no if)***

# Solicita as informações do usuário
idade = int(input("Digite a sua idade: "))

# Recebe 1 para Sim ou 0 para Não e converte para valor Booleano (True ou False)
tem_vip = input("Possui convite VIP? (1 para Sim, 0 para Não): ") == "1"
e_organizador = input("É organizador(a) do evento? (1 para Sim, 0 para Não): ") == "1"

# Valida as regras de entrada em uma única estrutura condicional
if (idade >= 18 and tem_vip) or e_organizador:
    print("Entrada PERMITIDA! Seja bem-vindo(a).")
else:
    print("Entrada NEGADA! Você não atende aos requisitos.")

    # EXPLICAÇÃO DO CÓDIGO:

#Os Parênteses (idade >= 18 and tem_vip): Eles isolam a primeira regra. O Python vai checar primeiro
# se a pessoa tem 18 anos ou mais E (and) se ela possui o VIP. As duas coisas precisam ser verdadeiras
# juntas para essa parte dar certo.O Operador or: Ele separa as duas grandes condições de entrada.
# O acesso será liberado se o grupo dos parênteses for verdadeiro OU (or) se a variável e_organizador for verdadeira.
# A conversão == "1": Ao comparar o que o usuário digitou com "1", transformamos a resposta diretamente
# em um valor Booleano (True ou False). Isso deixa a leitura dentro do if muito mais limpa.

