from pathlib import Path

import pandas as pd


# Localiza a pasta deste script para encontrar os arquivos CSV sem depender
# da pasta de onde o programa foi executado.
PASTA_ATIVIDADE = Path(__file__).parent
ARQUIVO_FUNCIONARIOS = PASTA_ATIVIDADE / "funcionarios.csv"
ARQUIVO_CARGOS_ALTOS = PASTA_ATIVIDADE / "cargos_altos.csv"
# Salário mínimo exigido para incluir um funcionário em cargos_altos.csv.
LIMITE_SALARIAL_CARGOS_ALTOS = 6000


def carregar_funcionarios():
    # Lê o arquivo CSV e cria um DataFrame com os dados dos funcionários.
    funcionarios = pd.read_csv(ARQUIVO_FUNCIONARIOS)
    # Remove espaços extras dos nomes das colunas, se houver.
    funcionarios.columns = funcionarios.columns.str.strip()
    # Padroniza o cabeçalho caso "salário" esteja escrito com acento.
    if "salario" not in funcionarios.columns and "salário" in funcionarios.columns:
        funcionarios = funcionarios.rename(columns={"salário": "salario"})
    return funcionarios


def filtrar_dados(funcionarios):
    # Lista de cargos que serão usados no filtro por cargo.
    cargos_selecionados = [
        "Analista de Dados",
        "Analista de Sistemas",
        "Desenvolvedor Java",
        "Cientista de Dados",
    ]

    # Seleciona funcionários com salário menor que 3000, maior que 5000
    # ou exatamente igual a 3100. O operador | representa "ou".
    salarios_selecionados = funcionarios[
        (funcionarios["salario"] < 3000)
        | (funcionarios["salario"] > 5000)
        | (funcionarios["salario"] == 3100)
    ]

    # Mantém somente os funcionários cujo cargo está na lista acima.
    cargos_selecionados_df = funcionarios[
        funcionarios["cargo"].isin(cargos_selecionados)
    ]

    # Filtra salários acima de 6000 e exibe apenas nome e cargo.
    salarios_maiores_que_6000 = funcionarios[
        funcionarios["salario"] > 6000
    ][["nome", "cargo"]]

    # Seleciona funcionários cujo id é divisível por 2, ou seja, par.
    ids_pares = funcionarios[funcionarios["id"] % 2 == 0]

    # Retorna os quatro DataFrames filtrados na ordem em que foram criados.
    return (
        salarios_selecionados,
        cargos_selecionados_df,
        salarios_maiores_que_6000,
        ids_pares,
    )


def salvar_cargos_altos(funcionarios):
    # Seleciona os funcionários com salário acima do limite definido.
    cargos_altos = funcionarios[
        funcionarios["salario"] > LIMITE_SALARIAL_CARGOS_ALTOS
    ]
    # Salva o resultado em CSV sem criar uma coluna extra para o índice.
    cargos_altos.to_csv(ARQUIVO_CARGOS_ALTOS, index=False)


def exibir_resultados(resultados):
    # Títulos correspondentes aos quatro DataFrames retornados por filtrar_dados.
    nomes_resultados = (
        "Salários menores que 3000, maiores que 5000 ou iguais a 3100",
        "Cargos selecionados",
        "Funcionários com salário maior que 6000",
        "Funcionários com id par",
    )

    # Associa cada título ao respectivo resultado e imprime ambos.
    for nome_resultado, resultado in zip(nomes_resultados, resultados):
        print(f"\n{nome_resultado}:")
        # Exibe a tabela sem os índices numéricos do DataFrame.
        print(resultado.to_string(index=False))


# Executa este bloco somente quando o arquivo é iniciado diretamente.
if __name__ == "__main__":
    # Carrega os dados, gera o CSV de salários altos e exibe os filtros.
    dados_funcionarios = carregar_funcionarios()
    salvar_cargos_altos(dados_funcionarios)
    exibir_resultados(filtrar_dados(dados_funcionarios))
