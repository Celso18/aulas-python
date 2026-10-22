from pathlib import Path

import pandas as pd


PASTA_ATIVIDADE = Path(__file__).parent
ARQUIVO_FUNCIONARIOS = PASTA_ATIVIDADE / "funcionarios.csv"


def carregar_funcionarios():
    return pd.read_csv(ARQUIVO_FUNCIONARIOS)


def filtrar_dados(funcionarios):
    cargos_selecionados = [
        "Analista de Dados",
        "Analista de Sistemas",
        "Desenvolvedor Java",
        "Cientista de Dados",
    ]

    salarios_selecionados = funcionarios[
        (funcionarios["salário"] < 3000)
        | (funcionarios["salário"] > 5000)
        | (funcionarios["salário"] == 3100)
    ]

    cargos_selecionados_df = funcionarios[
        funcionarios["cargo"].isin(cargos_selecionados)
    ]

    salarios_maiores_que_6000 = funcionarios[
        funcionarios["salário"] > 6000
    ][["nome", "cargo"]]

    ids_pares = funcionarios[funcionarios["id"] % 2 == 0]

    return (
        salarios_selecionados,
        cargos_selecionados_df,
        salarios_maiores_que_6000,
        ids_pares,
    )


def exibir_resultados(resultados):
    nomes_resultados = (
        "Salários menores que 3000, maiores que 5000 ou iguais a 3100",
        "Cargos selecionados",
        "Funcionários com salário maior que 6000",
        "Funcionários com id par",
    )

    for nome_resultado, resultado in zip(nomes_resultados, resultados):
        print(f"\n{nome_resultado}:")
        print(resultado.to_string(index=False))


if __name__ == "__main__":
    dados_funcionarios = carregar_funcionarios()
    exibir_resultados(filtrar_dados(dados_funcionarios))
