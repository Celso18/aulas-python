
#Questão 7: O Formulário de Doação de Sangue (Múltiplas Condições)

# Entrada de dados do doador
idade = int(input("Digite a idade do doador: "))
peso = float(input("Digite o peso do doador (em kg, ex: 65.5): "))

# Validação das regras de doação usando operadores relacionais e lógicos
# Condição 1: idade maior ou igual a 16 anos
# Condição 2: idade menor ou igual a 69 anos
# Condição 3: peso estritamente maior que 50kg
apto_para_doar = (idade >= 16) and (idade <= 69) and (peso > 50.0)

# Exibição do resultado booleano direto na tela
print("O doador está apto para doar sangue?", apto_para_doar)

#Explicação da questão 7
# idade >= 16 and idade <= 69: Esta combinação estabelece o intervalo aceitável de idade (entre 16 e 69 anos inclusivos)
# .peso > 50.0: Como o enunciado pede que o doador pese mais que 50kg, utilizamos o operador de maior correspondente (>).
# Se a regra do hospital aceitasse exatamente 50kg, usaríamos \>=.Múltiplos operadores and: O Python avalia a linha inteira
# sequencialmente. O resultado só será True se todas as três condições individuais forem verdadeiras simultaneamente.
# Se qualquer uma falhar, o resultado será False.
