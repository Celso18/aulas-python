from pathlib import Path

import pandas as pd


DATA_ATUAL = pd.Timestamp("2026-10-27")
ARQUIVO_CSV = Path(__file__).with_name("estoque_supermercado.csv")


def limpar_preco(coluna):
    preco = (
        coluna.astype("string")
        .str.replace("R$", "", regex=False)
        .str.strip()
        .str.replace(",", ".", regex=False)
    )
    return pd.to_numeric(preco, errors="coerce")


df = pd.read_csv(ARQUIVO_CSV)

# Limpeza de preço: textos e valores ausentes recebem a média dos preços válidos.
df["preco"] = limpar_preco(df["preco"])
df["preco"] = df["preco"].fillna(df["preco"].mean())

# Apenas números são convertidos; palavras e vazios tornam-se zero.
df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce").fillna(0).astype(int)

# Padronização dos setores.
df["setor"] = (
    df["setor"]
    .astype("string")
    .str.strip()
    .str.lower()
    .fillna("sem setor")
    .replace("", "sem setor")
)

# Conversão das datas no formato dia/mês/ano.
for coluna in ["data_compra", "data_vencimento"]:
    df[coluna] = pd.to_datetime(df[coluna], format="%d/%m/%Y", errors="coerce")

df["valor_total_estoque"] = df["quantidade"] * df["preco"]

inicio_vencimentos = DATA_ATUAL
fim_vencimentos = DATA_ATUAL + pd.Timedelta(days=7)
vencendo_esta_semana = df[
    df["data_vencimento"].between(inicio_vencimentos, fim_vencimentos)
]

inicio_compras = DATA_ATUAL - pd.Timedelta(days=3)
compras_recentes = df[df["data_compra"].between(inicio_compras, DATA_ATUAL)]

sem_vencimento = df[df["data_vencimento"].isna()]

valor_por_setor = (
    df.groupby("setor", as_index=False)["valor_total_estoque"]
    .sum()
    .sort_values("valor_total_estoque", ascending=False)
)
maior_setor = valor_por_setor.iloc[0]

print("\n--- BASE DE DADOS LIMPA ---")
print(df.head())

print("\n--- PRODUTOS VENCENDO ESTA SEMANA ---")
print(vencendo_esta_semana[["nome", "quantidade", "data_vencimento"]].to_string(index=False))

print("\n--- MAIOR QUANTIDADE A VENCER ---")
if vencendo_esta_semana.empty:
    print("Nenhum produto vence nesta semana.")
else:
    maior_quantidade = vencendo_esta_semana.loc[
        vencendo_esta_semana["quantidade"].idxmax()
    ]
    print(
        f"{maior_quantidade['nome']} - "
        f"{maior_quantidade['quantidade']} unidades"
    )

print("\n--- COMPRAS RECENTES (24/10/2026 A 27/10/2026) ---")
print(compras_recentes[["nome", "data_compra"]].to_string(index=False))

print("\n--- PRODUTOS SEM VENCIMENTO ---")
print(sem_vencimento[["nome", "setor"]].to_string(index=False))

print("\n--- MAIOR VALOR PATRIMONIAL POR SETOR ---")
print(valor_por_setor.to_string(index=False))
print(
    f"\nSetor com maior valor em estoque: {maior_setor['setor']} "
    f"(R$ {maior_setor['valor_total_estoque']:.2f})"
)