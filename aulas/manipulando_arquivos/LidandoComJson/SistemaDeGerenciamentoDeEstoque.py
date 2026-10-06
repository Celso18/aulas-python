import json
from pathlib import Path


ARQUIVO_ESTOQUE = Path(__file__).with_name("estoque.json")

loja = {
    "nome": "TechStore",
    "produtos": [
        {"nome": "Teclado Mecânico", "preco": 250.00, "quantidade": 12},
        {"nome": "Mouse Gamer", "preco": 150.00, "quantidade": 20},
        {"nome": "Monitor", "preco": 899.90, "quantidade": 8},
    ],
}

with open(ARQUIVO_ESTOQUE, "w", encoding="utf-8") as arquivo:
    json.dump(loja, arquivo, indent=4, ensure_ascii=False)

with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)

for produto in dados_lidos["produtos"]:
    print(f"O produto {produto['nome']} custa R$ {produto['preco']:.2f}")

dados_lidos["produtos"].append(
    {"nome": "Fone de Ouvido", "preco": 199.90, "quantidade": 15}
)

for produto in dados_lidos["produtos"]:
    if produto["nome"] == "Teclado Mecânico":
        produto["preco"] *= 0.90
        print(
            f"Desconto de 10% aplicado ao {produto['nome']}: "
            f"R$ {produto['preco']:.2f}"
        )
        break

with open(ARQUIVO_ESTOQUE, "w", encoding="utf-8") as arquivo:
    json.dump(dados_lidos, arquivo, indent=4, ensure_ascii=False)

print(f"Estoque de {dados_lidos['nome']} atualizado em {ARQUIVO_ESTOQUE.name}.")
