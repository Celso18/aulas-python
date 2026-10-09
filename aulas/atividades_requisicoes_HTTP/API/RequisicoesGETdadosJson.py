import json
import re
from pathlib import Path

import requests


ARQUIVO_HISTORICO = Path(__file__).with_name("historico_pesquisa.json")
URL_VIACEP = "https://viacep.com.br/ws/01001000/json/"


def normalizar_cep(cep_informado):
    cep_informado = cep_informado.strip()
    if not re.fullmatch(r"\d{5}-?\d{3}", cep_informado):
        raise ValueError("CEP inválido. Informe os 8 dígitos do CEP.")
    return cep_informado.replace("-", "")


def buscar_endereco(cep):
    resposta = requests.get(URL_VIACEP.format(cep), timeout=10)
    resposta.raise_for_status()
    dados = resposta.json()

    if not isinstance(dados, dict):
        raise ValueError("A resposta do ViaCEP está em um formato inesperado.")
    if dados.get("erro"):
        raise LookupError(f"O CEP {cep} não foi encontrado.")
    return dados


def exibir_endereco(endereco):
    print(f"Logradouro: {endereco.get('logradouro') or 'Não informado'}")
    print(f"Bairro: {endereco.get('bairro') or 'Não informado'}")
    print(f"Cidade: {endereco.get('localidade') or 'Não informada'}")
    print(f"Estado: {endereco.get('uf') or 'Não informado'}")


def carregar_historico():
    try:
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as arquivo:
            historico = json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as erro:
        raise ValueError("O arquivo de histórico contém JSON inválido.") from erro

    if not isinstance(historico, list):
        raise ValueError("O conteúdo do histórico precisa ser uma lista JSON.")
    return historico


def salvar_pesquisa(endereco):
    historico = carregar_historico()
    historico.append(
        {
            "cep": endereco.get("cep", ""),
            "logradouro": endereco.get("logradouro", ""),
            "bairro": endereco.get("bairro", ""),
            "cidade": endereco.get("localidade", ""),
            "estado": endereco.get("uf", ""),
        }
    )

    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, indent=4, ensure_ascii=False)


def main():
    try:
        cep = normalizar_cep(input("Digite o CEP (8 dígitos): ").strip())
        endereco = buscar_endereco(cep)
        exibir_endereco(endereco)
        salvar_pesquisa(endereco)
        print(f"Pesquisa salva em {ARQUIVO_HISTORICO.name}.")
    except ValueError as erro:
        print(f"Erro: {erro}")
    except LookupError as erro:
        print(f"Erro: {erro}")
    except requests.exceptions.RequestException as erro:
        print(f"Falha ao consultar o ViaCEP: {erro}")


if __name__ == "__main__":
    main()
