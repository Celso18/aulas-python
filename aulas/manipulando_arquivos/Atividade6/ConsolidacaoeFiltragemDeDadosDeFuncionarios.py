import json
from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parent
ARQUIVOS_BASE = [
    PASTA_PROJETO / "base1.json",
    PASTA_PROJETO / "base2.json",
    PASTA_PROJETO / "base3.json",
]

ARQUIVO_SAIDA = PASTA_PROJETO / "aniversariantes.json"


def consolidar_aniversariantes():
    lista_aniversariantes = []

    for caminho in ARQUIVOS_BASE:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            funcionarios = json.load(arquivo)

        for func in funcionarios:
            lista_aniversariantes.append({
                "nome": func["nome"],
                "aniversario": func["aniversario"],
            })

    # Certifique-se de salvar o arquivo de saída ao final da função
    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as arquivo_saida:
        json.dump(lista_aniversariantes, arquivo_saida, indent=4, ensure_ascii=False)


# Chame a função para executar o código
if __name__ == "__main__":
    consolidar_aniversariantes()
    print("Dados consolidados com sucesso!")
