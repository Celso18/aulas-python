
def cadastrar_venda():
    vendedor = input('Digite o nome do vendedor: ')
    produto = input('Digite o nome do produto: ')

    # Tratamento para garantir que o usuário digite um número válido
    try:
        valor = float(input('Digite o valor do produto: '))
    except ValueError:
        print("Erro: O valor do produto deve ser um número válido.")
        return

    # Salva no arquivo usando ';' como separador padronizado
    with open("vendas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{vendedor};{produto};{valor:.2f}\n")

    print("\nVenda cadastrada com sucesso!\n")


def listar_vendas():
    try:
        with open("vendas.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            if not linhas:
                print("Nenhuma venda cadastrada ainda.\n")
                return

            for linha in linhas:
                # Remove espaços em branco/quebras de linha e divide pelo ';'
                dados = linha.strip().split(";")

                # Exibe os dados formatados de forma organizada
                print(f"Vendedor: {dados[0]}")
                print(f"Produto : {dados[1]}")
                print(f"Valor   : R$ {dados[2]}")
                print("-" * 30)  # Linha divisória entre as vendas

    except FileNotFoundError:
        print("Arquivo 'vendas.txt' não encontrado. Cadastre uma venda primeiro.\n")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}\n")

while True:
    print("\n--- SISTEMA DE COMPRAS ---")
    print("1) Cadastrar venda nova")
    print("2) Listar todas as vendas")
    print("3) Finalizar programa")

    try:
        opcao = int(input("\nEscolha uma das opções: "))
    except ValueError:
        print("Por favor, digite apenas números!")
        continue

    match opcao:
        case 1:
            cadastrar_venda()
        case 2:
            listar_vendas()
        case 3:
            print("Finalizando o programa. Até logo!")
            break
        case _:
            print("Opção inválida! Tente novamente.")
