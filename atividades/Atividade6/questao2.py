# Questão 2: Validação de Senha

senha_correta = "123456"
senha_digitada = input("Digite a senha: ")

while senha_digitada != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha_digitada = input("Digite a senha: ")

print("Acesso permitido!")
