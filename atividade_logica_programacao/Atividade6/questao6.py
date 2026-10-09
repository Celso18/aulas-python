# Questão 6: Jogo da Adivinhação com Tentativas

numero_secreto = 14
tentativas = 0
palpite = int(input("Tente adivinhar o número secreto: "))

while palpite != numero_secreto:
    tentativas += 1
    palpite = int(input("Você errou. Tente novamente: "))

tentativas += 1
print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas!")
