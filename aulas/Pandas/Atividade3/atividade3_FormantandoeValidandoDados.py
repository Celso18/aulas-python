from pathlib import Path

import pandas as pd


PASTA_ARQUIVOS = Path(__file__).parent
ARQUIVO_ENTRADA = PASTA_ARQUIVOS / "dados_despadronizados.csv"
ARQUIVO_SAIDA = PASTA_ARQUIVOS / "dados_padronizados.csv"


def formatar_salarios(salarios):
    salarios = salarios.str.strip().str.replace(r"[^\d,.\-]", "", regex=True)
    tem_virgula = salarios.str.contains(",", na=False)
    tem_ponto = salarios.str.contains(r"\.", na=False)
    virgula_decimal = (
        tem_virgula
        & tem_ponto
        & (salarios.str.rfind(",").fillna(-1) > salarios.str.rfind(".").fillna(-1))
    )
    ponto_decimal = tem_virgula & tem_ponto & ~virgula_decimal

    salarios_limpos = salarios.copy()
    salarios_limpos.loc[virgula_decimal] = (
        salarios.loc[virgula_decimal]
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )
    salarios_limpos.loc[ponto_decimal] = salarios.loc[ponto_decimal].str.replace(
        ",", "", regex=False
    )

    somente_virgula = tem_virgula & ~tem_ponto
    virgula_decimal = somente_virgula & salarios.str.contains(r",\d{1,2}$", na=False)
    virgula_milhar = somente_virgula & ~virgula_decimal
    salarios_limpos.loc[virgula_decimal] = salarios.loc[virgula_decimal].str.replace(
        ",", ".", regex=False
    )
    salarios_limpos.loc[virgula_milhar] = salarios.loc[virgula_milhar].str.replace(
        ",", "", regex=False
    )

    somente_ponto = tem_ponto & ~tem_virgula
    salarios_limpos.loc[somente_ponto] = salarios.loc[somente_ponto].str.replace(
        r"\.(?=\d{3}(?:\.|$))", "", regex=True
    )

    return pd.to_numeric(salarios_limpos, errors="coerce")


def padronizar_dados(dados):
    colunas_obrigatorias = {"nome", "cpf", "numero", "salario"}
    colunas_ausentes = colunas_obrigatorias.difference(dados.columns)
    if colunas_ausentes:
        nomes_ausentes = ", ".join(sorted(colunas_ausentes))
        raise ValueError(f"Colunas ausentes no arquivo de entrada: {nomes_ausentes}")

    dados = dados.copy()
    dados["cpf_formatado"] = dados["cpf"].str.replace(r"\D", "", regex=True)
    dados["cpf_valido"] = dados["cpf_formatado"].str.fullmatch(
        r"\d{11}", na=False
    )
    dados["numero_formatado"] = dados["numero"].str.replace(
        r"\D", "", regex=True
    )
    dados["numero_valido"] = dados["numero_formatado"].str.fullmatch(
        r"(?:55)?\d{10,11}", na=False
    )
    dados["salario_formatado"] = formatar_salarios(dados["salario"])
    dados["salario_anual"] = dados["salario_formatado"] * 12

    colunas_saida = [
        "nome",
        "cpf",
        "cpf_formatado",
        "cpf_valido",
        "numero",
        "numero_formatado",
        "numero_valido",
        "salario",
        "salario_formatado",
        "salario_anual",
    ]
    return dados[colunas_saida]


def main():
    dados = pd.read_csv(ARQUIVO_ENTRADA, dtype="string")
    dados_padronizados = padronizar_dados(dados)
    dados_padronizados.to_csv(ARQUIVO_SAIDA, index=False)
    print(f"Arquivo padronizado salvo em: {ARQUIVO_SAIDA}")


if __name__ == "__main__":
    main()
