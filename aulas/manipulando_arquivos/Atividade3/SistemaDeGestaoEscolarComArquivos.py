
from pathlib import Path

ARQUIVO_ALUNOS = Path(__file__).with_name("alunos.txt")


def calcular_media(notas):
    return sum(notas) / len(notas)


def status_aprovacao(media):
    return "Aprovado" if media >= 7.0 else "Reprovado"


def ler_alunos():
    try:
        with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.read().strip().splitlines()
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo alunos.txt não encontrado.")

    alunos = []
    for linha in linhas:
        if not linha.strip():
            continue
        dados = [campo.strip() for campo in linha.split(";")]
        if len(dados) != 7:
            continue
        nome, turma, bim1, bim2, bim3, bim4, status = dados
        alunos.append({
            "nome": nome,
            "turma": turma,
            "notas": [float(bim1), float(bim2), float(bim3), float(bim4)],
            "status": status,
        })
    return alunos


def buscar_aluno_por_nome(nome_busca):
    for aluno in ler_alunos():
        if aluno["nome"].lower() == nome_busca.lower():
            return aluno
    return None


def mostrar_menu():
    print("\n===== SISTEMA DE GESTÃO ESCOLAR =====")
    print("1 - Acrescentar aluno")
    print("2 - Calcular média de um aluno")
    print("3 - Consultar status de aprovação")
    print("4 - Mostrar a maior média da turma")
    print("5 - Sair")
    print("====================================")


def acrescentar_aluno():
    nome = input("Digite o nome do aluno: ").strip()
    turma = input("Digite a turma: ").strip()

    notas = []
    for indice in range(1, 5):
        nota = float(input(f"Digite a nota do bimestre {indice}: ").strip().replace(",", "."))
        notas.append(nota)

    media = calcular_media(notas)
    situacao = status_aprovacao(media)

    linha = f"{nome};{turma};{notas[0]};{notas[1]};{notas[2]};{notas[3]};{situacao}\n"

    with open(ARQUIVO_ALUNOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(linha)

    print(f"Aluno {nome} adicionado com sucesso.")
    print(f"Média: {media:.2f} - Status: {situacao}")


def calcular_media_aluno():
    nome = input("Digite o nome do aluno: ").strip()
    try:
        aluno = buscar_aluno_por_nome(nome)
        if aluno is None:
            raise ValueError(f"Aluno '{nome}' não encontrado.")
        media = calcular_media(aluno["notas"])
        print(f"A média de {aluno['nome']} é {media:.2f}")
    except FileNotFoundError as erro:
        print(f"Erro: {erro}")
    except ValueError as erro:
        print(f"Erro: {erro}")


def consultar_status_aluno():
    nome = input("Digite o nome do aluno: ").strip()
    try:
        aluno = buscar_aluno_por_nome(nome)
        if aluno is None:
            raise ValueError(f"Aluno '{nome}' não encontrado.")
        print(f"{aluno['nome']} está {aluno['status']}")
    except FileNotFoundError as erro:
        print(f"Erro: {erro}")
    except ValueError as erro:
        print(f"Erro: {erro}")


def maior_media_turma():
    turma = input("Digite a turma: ").strip()
    try:
        alunos = [aluno for aluno in ler_alunos() if aluno["turma"] == turma]
        if not alunos:
            raise ValueError(f"Nenhum aluno encontrado na turma {turma}.")

        melhor_aluno = max(alunos, key=lambda aluno: calcular_media(aluno["notas"]))
        media = calcular_media(melhor_aluno["notas"])
        print(f"A maior média da turma {turma} é de {melhor_aluno['nome']} com {media:.2f}.")
    except FileNotFoundError as erro:
        print(f"Erro: {erro}")
    except ValueError as erro:
        print(f"Erro: {erro}")


def main():
    while True:
        mostrar_menu()
        try:
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                acrescentar_aluno()
            elif opcao == "2":
                calcular_media_aluno()
            elif opcao == "3":
                consultar_status_aluno()
            elif opcao == "4":
                maior_media_turma()
            elif opcao == "5":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError as erro:
            print(f"Erro de valor: {erro}")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")


if __name__ == "__main__":
    main()