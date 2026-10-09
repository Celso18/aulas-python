#***Questão 2: O Radar de Velocidade***

# Solicita a velocidade atual do carro e converte para número decimal (float)
velocidade = float(input("Digite a velocidade atual do carro em km/h: "))

# Verifica se a velocidade ultrapassou o limite de 80 km/h
if velocidade > 80:
    print("Você foi multado por excesso de velocidade!")
else:
    print("Velocidade dentro do limite permitido. Boa viagem!")

    # EXPLICAÇÃO DO CÓDIGO:

#float(input(...)): Usamos float em vez de int porque a velocidade de um veículo pode ser um número quebrado
# (ex: 80.5 km/h ou 79.2 km/h).if velocidade > 80: O operador > (maior que) garante que o motorista só seja multado
# se estiver estritamente acima de 80 km/h. Se ele passar a exatamente 80 km/h, o sistema entra no else e não multa.