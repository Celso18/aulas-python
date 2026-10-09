# Questão 1: Lista de Funcionários

funcionarios = []

print("Digite os nomes dos funcionários.")
print('Digite "fim" quando terminar o cadastro.')

while True:
    nome = input("Nome do funcionário: ")
    if nome.lower() == "fim":
        break
    funcionarios.append(nome)

if funcionarios:
    print("\nFuncionários cadastrados:")
    for indice, funcionario in enumerate(funcionarios):
        print(f"{indice} - {funcionario}")

    entrada_indices = input(
        "\nDigite os índices dos funcionários que receberão aumento, "
        "separados por espaço: "
    )
    indices_aumento = set()

    for indice in entrada_indices.split():
        if indice.isdigit() and int(indice) < len(funcionarios):
            indices_aumento.add(int(indice))

    funcionarios_aumento = []
    funcionarios_demissao = []

    for indice in range(len(funcionarios)):
        if indice in indices_aumento:
            funcionarios_aumento.append(funcionarios[indice])
        else:
            funcionarios_demissao.append(funcionarios[indice])

    print("\nFuncionários que receberão aumento:")
    for funcionario in funcionarios_aumento:
        print(funcionario)

    print("\nFuncionários que serão demitidos:")
    for funcionario in funcionarios_demissao:
        print(funcionario)
else:
    print("Nenhum funcionário foi cadastrado.")
