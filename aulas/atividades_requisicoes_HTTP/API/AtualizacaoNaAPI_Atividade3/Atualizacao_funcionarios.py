# Importa as bibliotecas usadas no programa
import requests
import json


# Endereço da API de funcionários
link_funcionarios = "http://192.168.205.100:8080/funcionarios"

# Nome do arquivo que será criado
arquivo_saida = "dados_funcionarios_atualizados.json"


# Verifica se um valor está vazio
def campo_vazio(valor):
    return valor is None or (
        isinstance(valor, str) and valor.strip() == ""
    )


# Consulta e valida o CEP na API ViaCEP
def consultar_cep(cep):
    # Remove espaços e hífen do CEP
    cep = cep.strip().replace("-", "")

    # Verifica se o CEP possui oito números
    if not cep.isdigit() or len(cep) != 8:
        raise ValueError(
            "O CEP deve conter exatamente 8 números."
        )

    # Monta o endereço da consulta
    link_cep = f"https://viacep.com.br/ws/{cep}/json/"

    # Faz a requisição para a API
    resposta_cep = requests.get(link_cep)

    # Verifica se a requisição foi realizada com sucesso
    if resposta_cep.status_code != 200:
        raise ValueError(
            "Não foi possível consultar o CEP."
        )

    # Converte a resposta para um dicionário
    endereco = resposta_cep.json()

    # Verifica se o CEP existe e possui cidade e estado
    if (
        endereco.get("erro")
        or campo_vazio(endereco.get("localidade"))
        or campo_vazio(endereco.get("uf"))
    ):
        raise ValueError(
            "O CEP não foi encontrado ou não possui endereço válido."
        )

    # Retorna o CEP e os dados do endereço
    return cep, endereco


# Solicita um CEP até que o usuário informe um válido
def solicitar_cep(nome):
    while True:
        cep_digitado = input(
            f"Digite um CEP válido para {nome}: "
        )

        try:
            # Consulta o CEP informado
            return consultar_cep(cep_digitado)

        except ValueError as erro:
            # Mostra o motivo pelo qual o CEP foi rejeitado
            print(f"CEP inválido: {erro}")


# Preenche cidade e estado quando esses campos estão vazios
def preencher_dados_vazios(funcionario, endereco):
    # Seleciona os dados necessários do endereço
    dados_endereco = {
        "cidade": endereco.get("localidade"),
        "estado": endereco.get("uf"),
    }

    # Percorre os campos de endereço
    for campo, valor in dados_endereco.items():
        # Altera somente os campos vazios
        if (
            campo in funcionario
            and campo_vazio(funcionario[campo])
            and not campo_vazio(valor)
        ):
            funcionario[campo] = valor


# Busca os dados dos funcionários
resposta = requests.get(link_funcionarios)

# Verifica se a requisição foi realizada com sucesso
if resposta.status_code != 200:
    print("Não foi possível buscar os funcionários.")

else:
    # Converte a resposta para uma lista de funcionários
    lista_funcionarios = resposta.json()

    print(
        "--- LISTA DE FUNCIONÁRIOS COM DADOS VAZIOS ---\n"
    )

    # Percorre todos os funcionários
    for funcionario in lista_funcionarios:
        nome = funcionario.get("nome", "funcionário")
        cep = funcionario.get("cep")

        # Verifica se cidade e estado estão vazios
        cidade_vazia = campo_vazio(
            funcionario.get("cidade")
        )

        estado_vazio = campo_vazio(
            funcionario.get("estado")
        )

        # Processa funcionários que possuem CEP vazio
        # ou cidade/estado vazios.
        if campo_vazio(cep) or cidade_vazia or estado_vazio:

            # Solicita um CEP quando o funcionário não possui um
            if campo_vazio(cep):
                print(
                    f"O funcionário(a) {nome} "
                    "não tem CEP cadastrado."
                )

                cep, endereco = solicitar_cep(nome)

            else:
                try:
                    # Consulta o CEP que já está cadastrado
                    cep, endereco = consultar_cep(str(cep))

                except ValueError as erro:
                    # Informa que o CEP cadastrado é inválido
                    print(
                        f"CEP inválido para {nome}: {erro}"
                    )

                    print(
                        f"Informe um novo CEP válido para {nome}."
                    )

                    # Solicita um novo CEP válido
                    cep, endereco = solicitar_cep(nome)

            # Salva o CEP validado no funcionário
            funcionario["cep"] = cep

            # Altera somente cidade e estado vazios
            preencher_dados_vazios(
                funcionario,
                endereco
            )

    print("\n--- BASE DE DADOS ATUALIZADA ---\n")

    # Exibe a lista atualizada
    for funcionario in lista_funcionarios:
        print(funcionario)

    # Abre o arquivo para salvar os dados
    with open(
        arquivo_saida,
        "w",
        encoding="utf-8"
    ) as arquivo:
        # Salva a lista em formato JSON
        json.dump(
            lista_funcionarios,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

    # Informa o nome do arquivo criado
    print(
        f"\nArquivo salvo como: {arquivo_saida}"
    )
