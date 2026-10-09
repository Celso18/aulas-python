#***Questão 3: O Problema da Concatenação***

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

# A soma é inserida como o segundo argumento do print
print("O resultado da soma é:", n1 + n2)

#Exemplo de execução
#Primeiro número: 10
#Segundo número: 10
#O resultado da soma é: 20
#Conclusão: o problema acontece porque input() retorna strings. Ao utilizar int(), os
#valores são convertidos para números inteiros, permitindo que o operador + faça
#uma soma matemática em vez de concatenar textos.
