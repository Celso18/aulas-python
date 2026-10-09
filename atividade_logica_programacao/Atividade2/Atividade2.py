nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
plano = input("Você tem plano de saúde? (True/False): ")

plano = plano == "True"

aceito = idade >= 18 and idade < 60 and plano

print(f"Seu nome é {nome}, você tem {idade} anos. "
      f"Tem plano? {plano}. Você foi aceito? {aceito}")