import json
from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parent
ARQUIVO_BANCO = PASTA_PROJETO / "banco_livros.txt"
ARQUIVO_CATALOGO = PASTA_PROJETO / "catalogo.json"

NOVOS_LIVROS = [
    {
        "id": 31,
        "nome": "A Casa das Andorinhas",
        "descricao": "Uma restauradora descobre a historia de uma casa antiga.",
        "preco": 45.90,
        "em_estoque": 8,
    },
    {
        "id": 32,
        "nome": "Caminhos da Montanha",
        "descricao": "Um grupo de amigos percorre trilhas em busca de um vale.",
        "preco": 58.00,
        "em_estoque": 17,
    },
    {
        "id": 33,
        "nome": "O Laboratorio Secreto",
        "descricao": "Estudantes investigam os equipamentos de um laboratorio.",
        "preco": 49.50,
        "em_estoque": 6,
    },
    {
        "id": 34,
        "nome": "Atlas dos Oceanos",
        "descricao": "Uma introducao aos mares, correntes e vida marinha.",
        "preco": 96.00,
        "em_estoque": 10,
    },
    {
        "id": 35,
        "nome": "Uma Janela para o Inverno",
        "descricao": "Contos sobre encontros inesperados durante uma viagem.",
        "preco": 34.90,
        "em_estoque": 22,
    },
]


def ler_banco_legado():
    catalogo_livros = []
    with open(ARQUIVO_BANCO, "r", encoding="utf-8") as arquivo:
        for numero_linha, linha in enumerate(arquivo, start=1):
            linha = linha.strip()
            if not linha:
                continue

            campos = linha.split(";")
            if len(campos) != 5:
                raise ValueError(
                    f"Linha {numero_linha} de banco_livros.txt "
                    "deve conter cinco campos separados por ';'."
                )

            identificador, nome, descricao, preco, quantidade = campos
            catalogo_livros.append(
                {
                    "id": int(identificador),
                    "nome": nome,
                    "descricao": descricao,
                    "preco": float(preco),
                    "em_estoque": int(quantidade),
                }
            )
    return catalogo_livros


def salvar_catalogo(catalogo_livros):
    with open(ARQUIVO_CATALOGO, "w", encoding="utf-8") as arquivo:
        json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)


def adicionar_novos_livros(catalogo_livros):
    ids_existentes = {livro["id"] for livro in catalogo_livros}
    for livro in NOVOS_LIVROS:
        if livro["id"] in ids_existentes:
            raise ValueError(f"ID de livro duplicado: {livro['id']}")
        catalogo_livros.append(livro.copy())
        ids_existentes.add(livro["id"])


def exibir_resumo_do_catalogo():
    with open(ARQUIVO_CATALOGO, "r", encoding="utf-8") as arquivo:
        catalogo_lido = json.load(arquivo)

    livros_com_estoque_baixo = [
        livro["nome"] for livro in catalogo_lido if livro["em_estoque"] < 15
    ]
    valor_total = sum(
        livro["preco"] * livro["em_estoque"] for livro in catalogo_lido
    )

    print("Livros com menos de 15 unidades em estoque:")
    for nome in livros_com_estoque_baixo:
        print(f"- {nome}")
    print(f"Valor total do estoque: R$ {valor_total:.2f}")


def main():
    catalogo_livros = ler_banco_legado()
    salvar_catalogo(catalogo_livros)

    adicionar_novos_livros(catalogo_livros)
    salvar_catalogo(catalogo_livros)

    print(f"Catálogo atualizado com {len(catalogo_livros)} livros.")
    exibir_resumo_do_catalogo()


if __name__ == "__main__":
    main()
