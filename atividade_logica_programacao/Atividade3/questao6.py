
#Questão 6: O Erro de Verificação (Análise e Correção de Código)

#EXPLICAÇÃO DO ERRO
#O programa sempre responde False porque a função input() sempre retorna o dado digitado pelo usuário
# como uma String (texto / str), enquanto a variável senha_cadastrada foi definida como um Número Inteiro (int).
# Em Python, o número 1234 é estritamente diferente do texto "1234", fazendo com que a comparação de igualdade (==) falhe.
#Para corrigir esse erro, é necessário realizar a conversão de tipo (casting), transformando o texto digitado
# em um número inteiro antes de fazer a comparação.


# Código corrigido (convertendo a entrada para inteiro):
senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: ")) # Convertido de str para int
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)