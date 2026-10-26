from pathlib import Path
import re

import pandas as pd


PASTA_ATIVIDADE = Path(__file__).parent
ARQUIVO_ENTRADA = PASTA_ATIVIDADE / "dados_despadronizados.csv"
ARQUIVO_SAIDA = PASTA_ATIVIDADE / "dados_padronizados.csv"


def formatar_cpf(cpf):
    """Mantém somente os dígitos do CPF."""
    return cpf.str.replace(r"\D", "", regex=True)


def validar_cpf(cpf):
    """Valida se o CPF formatado possui exatamente 11 dígitos."""
    return cpf.str.fullmatch(r"\d{11}", na=False)


def formatar_numero(numero):
    """Padroniza telefones brasileiros no formato (XX) XXXXX-XXXX."""
    numero_formatado = numero.str.replace(r"\D", "", regex=True)
    numero_formatado = numero_formatado.str.replace(
        r"^55(?=\d{10,11}$)", "", regex=True
    )
    numero_formatado = numero_formatado.str.replace(
        r"^(\d{2})(\d{5})(\d{4})$", r"(\1) \2-\3", regex=True
    )
    return numero_formatado.str.replace(
        r"^(\d{2})(\d{4})(\d{4})$", r"(\1) \2-\3", regex=True
    )


def formatar_salario(salario):
    """Converte valores brasileiros ou decimais para números reais."""

    def converter(valor):
        if pd.isna(valor):
            return pd.NA

        valor = re.sub(r"[^\d,.\-]", "", str(valor))
        if not valor:
            return pd.NA

        ultimo_ponto = valor.rfind(".")
        ultima_virgula = valor.rfind(",")
        if ultimo_ponto >= 0 and ultima_virgula >= 0:
            separador_decimal = (
                "," if ultima_virgula > ultimo_ponto else "."
            )
            separador_milhar = (
                "." if separador_decimal == "," else ","
            )
            valor = valor.replace(separador_milhar, "")
            valor = valor.replace(separador_decimal, ".")
        elif ultima_virgula >= 0:
            valor = valor.replace(".", "").replace(",", ".")
        elif ultimo_ponto >= 0:
            partes = valor.split(".")
            if len(partes[-1]) == 3 and len(partes) > 1:
                valor = "".join(partes)

        try:
            return float(valor)
        except ValueError:
            return pd.NA

    return salario.map(converter).astype("Float64")


def carregar_dados():
    dados = pd.read_csv(
        ARQUIVO_ENTRADA,
        dtype={
            "nome": "string",
            "cpf": "string",
            "numero": "string",
            "salario": "string",
        },
    )
    dados.columns = dados.columns.str.strip()
    return dados


def padronizar_dados(dados):
    dados = dados.copy()
    dados["cpf_formatado"] = formatar_cpf(dados["cpf"])
    dados["cpf_valido"] = validar_cpf(dados["cpf_formatado"])
    dados["numero_formatado"] = formatar_numero(dados["numero"])
    numeros_para_validar = dados["numero"].str.replace(r"\D", "", regex=True)
    numeros_para_validar = numeros_para_validar.str.replace(
        r"^55(?=\d{10,11}$)", "", regex=True
    )
    dados["numero_valido"] = numeros_para_validar.str.fullmatch(
        r"\d{10,11}", na=False
    )
    dados["salario_formatado"] = formatar_salario(dados["salario"])
    dados["salario_anual"] = (dados["salario_formatado"] * 12).round(2)

    colunas = [
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
    return dados[colunas]


def main():
    dados_padronizados = padronizar_dados(carregar_dados())
    dados_padronizados.to_csv(
        ARQUIVO_SAIDA,
        index=False,
        na_rep="",
        encoding="utf-8-sig",
    )
    dados_para_exibir = dados_padronizados.astype(object).where(
        pd.notna(dados_padronizados), ""
    )
    print(dados_para_exibir.to_string(index=False))
    print(f"\nArquivo gerado: {ARQUIVO_SAIDA}")


if __name__ == "__main__":
    main()