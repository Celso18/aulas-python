# Atividade 8 — Análise de dados com opinião sobre os dados

## Arquivos

- `customers-10000.csv`: base usada na análise.
- `analise_assinaturas.py`: script para reproduzir os gráficos e os relatórios.
- `relatorio_analise_assinaturas.docx`: relatório executivo completo.
- `resumo_executivo_assinaturas.docx`: resumo executivo com os dois gráficos.
- `top_10_paises.png` e `evolucao_mensal.png`: gráficos da análise.

## Como reproduzir

Instale as dependências e execute o script nesta pasta:

```bash
python -m pip install pandas matplotlib python-docx
python analise_assinaturas.py customers-10000.csv
```

Os arquivos gerados serão salvos em `entregaveis_analise/`. Para gerar somente
o resumo executivo, sem substituir o relatório completo:

```bash
python analise_assinaturas.py customers-10000.csv --summary-only
```

## Opinião e ressalvas

A base contém 10.000 registros. A Coreia aparece com o maior volume por país,
mas representa apenas 0,84% do total, então é mais prudente testar campanhas
locais antes de ampliar o investimento. Agosto teve o maior volume agregado
nos anos completos; março também pode ser avaliado em uma campanha-piloto.

Os resultados representam registros por país, cidade, empresa e data. A base
não tem uma coluna de status da assinatura e, portanto, não permite confirmar
quais clientes estão ativos. Também não contém receita ou cancelamentos para
medir rentabilidade. As conclusões devem ser tratadas como sinais para testes,
não como prova de que uma campanha causou aumento nas vendas.

**Observação sobre os dados:** o CSV contém nomes, telefones e e-mails e está
incluído neste repositório público conforme solicitado. Compartilhe a base
somente se tiver autorização para publicá-la.
