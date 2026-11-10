"""Analisa customers-10000.csv e gera gráficos e um relatório executivo Word."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from docx import Document
from docx.shared import Inches, Pt


MONTH_NAMES = {
    1: "Jan",
    2: "Fev",
    3: "Mar",
    4: "Abr",
    5: "Mai",
    6: "Jun",
    7: "Jul",
    8: "Ago",
    9: "Set",
    10: "Out",
    11: "Nov",
    12: "Dez",
}


def format_integer(value: int) -> str:
    return f"{value:,}".replace(",", ".")


def format_percent(value: float, decimals: int = 1) -> str:
    return f"{value:.{decimals}%}".replace(".", ",")


def load_data(csv_path: Path) -> pd.DataFrame:
    data = pd.read_csv(csv_path)
    required = {"Country", "City", "Company", "Subscription Date"}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {', '.join(sorted(missing))}")

    data["Subscription Date"] = pd.to_datetime(
        data["Subscription Date"], errors="coerce"
    )
    invalid_dates = int(data["Subscription Date"].isna().sum())
    if invalid_dates:
        raise ValueError(f"Foram encontradas {invalid_dates} datas inválidas.")
    return data


def make_charts(
    data: pd.DataFrame, output_dir: Path
) -> tuple[Path, Path, pd.Series, pd.Series, pd.Series]:
    output_dir.mkdir(parents=True, exist_ok=True)

    country_counts = data["Country"].value_counts().head(10).sort_values()
    country_chart = output_dir / "top_10_paises.png"
    fig, axis = plt.subplots(figsize=(9, 6))
    country_counts.plot.barh(ax=axis, color="#2878B5")
    axis.set_title("Top 10 países por número de clientes")
    axis.set_xlabel("Número de clientes")
    axis.set_ylabel("País")
    axis.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(country_chart, dpi=160)
    plt.close(fig)

    monthly_counts = (
        data.set_index("Subscription Date")
        .resample("MS")
        .size()
        .asfreq("MS", fill_value=0)
    )
    monthly_chart = output_dir / "evolucao_mensal.png"
    fig, axis = plt.subplots(figsize=(10, 5))
    axis.plot(monthly_counts.index, monthly_counts.values, marker="o", linewidth=1.8)
    axis.set_title("Assinaturas registradas por mês")
    axis.set_xlabel("Mês")
    axis.set_ylabel("Quantidade de registros")
    axis.grid(alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(monthly_chart, dpi=160)
    plt.close(fig)

    yearly_counts = data["Subscription Date"].dt.year.value_counts().sort_index()
    month_counts = (
        data.loc[data["Subscription Date"].dt.year < data["Subscription Date"].dt.year.max(),
                 "Subscription Date"]
        .dt.month.value_counts()
        .reindex(range(1, 13), fill_value=0)
        .sort_values(ascending=False)
    )
    return country_chart, monthly_chart, monthly_counts, yearly_counts, month_counts


def set_document_font(document: Document) -> None:
    for style_name in ("Normal", "Title", "Heading 1", "Heading 2"):
        style = document.styles[style_name]
        style.font.name = "Arial"
        style.font.size = Pt(12)
        style._element.rPr.rFonts.set(
            "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}eastAsia",
            "Arial",
        )
    for section in document.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)


def add_paragraph(document: Document, text: str) -> None:
    paragraph = document.add_paragraph(text)
    paragraph.paragraph_format.space_after = Pt(6)


def create_report(
    data: pd.DataFrame,
    output_path: Path,
    country_chart: Path,
    monthly_chart: Path,
    monthly_counts: pd.Series,
    yearly_counts: pd.Series,
    month_counts: pd.Series,
) -> None:
    document = Document()
    set_document_font(document)

    title = document.add_paragraph()
    title.paragraph_format.space_after = Pt(6)
    title_run = title.add_run("Relatório executivo — análise de assinaturas")
    title_run.bold = True
    title_run.font.name = "Arial"
    title_run.font.size = Pt(12)

    dates = data["Subscription Date"]
    country_counts = data["Country"].value_counts()
    city_counts = data["City"].value_counts()
    company_counts = data["Company"].value_counts()
    top_country = country_counts.index[0]
    top_city_names = sorted(city_counts[city_counts.eq(city_counts.max())].index)
    top_company_names = company_counts.head(5)
    top_month = int(month_counts.index[0])
    peak_month = monthly_counts.idxmax().strftime("%m/%Y")
    complete_years = [
        int(year)
        for year in yearly_counts.index
        if year < dates.dt.year.max()
    ]
    if len(complete_years) >= 2:
        first_year, second_year = complete_years[-2:]
        first_total = int(yearly_counts.loc[first_year])
        second_total = int(yearly_counts.loc[second_year])
        annual_comparison = (
            f"Os anos completos considerados registram "
            f"{format_integer(first_total)} entradas em {first_year} e "
            f"{format_integer(second_total)} em {second_year}, uma variação de "
            f"{format_percent(second_total / first_total - 1)}."
        )
    else:
        annual_comparison = (
            "Há menos de dois anos completos para comparar a evolução anual."
        )

    document.add_heading("Resumo executivo e plano de crescimento", level=1)
    paragraphs = [
        (
            f"A base contém {format_integer(len(data))} registros, distribuídos por "
            f"{format_integer(data['Country'].nunique())} países e "
            f"{format_integer(data['Company'].nunique())} empresas. Ela não possui coluna de "
            "status da assinatura; portanto, os resultados abaixo contam registros "
            "de clientes, não confirmam assinaturas ativas."
        ),
        (
            f"{top_country} lidera em volume, com "
            f"{format_integer(int(country_counts.iloc[0]))} registros "
            f"({format_percent(country_counts.iloc[0] / len(data), 2)} do total). A participação "
            "pequena do primeiro colocado mostra que a carteira é geograficamente "
            "dispersa, então esse dado justifica um piloto, não uma expansão ampla."
        ),
        (
            f"Não há uma cidade líder isolada: {len(top_city_names)} cidades empatam "
            f"com {format_integer(int(city_counts.max()))} registros cada. São elas: "
            f"{', '.join(top_city_names)}. A base não sustenta uma estratégia "
            "concentrada em uma cidade específica."
        ),
        (
            "No recorte B2B, cada uma das cinco empresas mais frequentes aparece "
            f"{format_integer(int(top_company_names.iloc[0]))} vezes: "
            f"{', '.join(top_company_names.index)}. Há "
            f"{format_integer(int(company_counts.eq(company_counts.max()).sum()))} "
            "empresas empatadas "
            "nesse máximo, sem evidência de concentração em poucas contas."
        ),
        (
            f"As datas vão de {dates.min():%d/%m/%Y} a {dates.max():%d/%m/%Y}. "
            f"{annual_comparison} O ano de {int(dates.dt.year.max())} é parcial "
            "na base e não deve ser comparado diretamente."
        ),
        (
            f"Para sazonalidade, a comparação dos anos completos aponta "
            f"{MONTH_NAMES[top_month]} como o mês de maior volume agregado "
            f"({format_integer(int(month_counts.iloc[0]))} registros em 2020 e 2021). "
            f"Agosto teve {format_integer(int(month_counts.loc[8]))} registros, "
            "com pico de 383 em cada um "
            "desses anos; março aparece logo atrás, com 735 no total."
        ),
        (
            f"No período inteiro, o maior ponto mensal ocorreu em {peak_month}, "
            f"com {format_integer(int(monthly_counts.max()))} registros. "
            "A leitura deve considerar "
            "a cobertura incompleta de 2022 e não prova, por si só, efeito de "
            "campanhas nem uma tendência recorrente."
        ),
        (
            "Recomendo iniciar um piloto de aquisição no fim de julho, preparando "
            "a comunicação para agosto, e manter uma segunda janela de teste em "
            "março. A repetição do pico de agosto nos dois anos completos é um sinal "
            "mais comparável do que o total mensal que inclui 2022 parcial."
        ),
        (
            f"Para expansão geográfica, priorize um teste controlado na região de "
            f"{top_country}, com mensagem e oferta adaptadas ao mercado local. "
            "Compare a conversão com regiões de controle antes de aumentar o "
            f"orçamento, pois o país líder representa "
            f"{format_percent(country_counts.iloc[0] / len(data), 2)} dos registros."
        ),
        (
            "No B2B, teste prospecção baseada em contas e ofertas de expansão para "
            "empresas com sinais observáveis de potencial; os nomes mais frequentes "
            "não revelam porte, setor, receita nem plano contratado. Esses atributos "
            "devem ser coletados antes de priorizar contas pelo valor esperado."
        ),
        (
            "Acompanhe conversão, receita recorrente, custo de aquisição, expansão "
            "de plano e cancelamento por país, mês e coorte. Use grupos de controle "
            "e uma janela de quatro a seis semanas para separar sazonalidade de "
            "efeito incremental da campanha."
        ),
        (
            "Antes de transformar os resultados em previsão comercial, enriqueça "
            "a base com status ativo, identificador de plano, receita, origem do "
            "cliente e cancelamentos. Sem esses campos, a análise mede volume de "
            "cadastros por data, e não vendas líquidas, clientes ativos ou "
            "rentabilidade."
        ),
    ]
    for text in paragraphs:
        add_paragraph(document, text)

    document.add_heading("Evidências visuais", level=1)
    add_paragraph(
        document,
        "O gráfico regional conta registros por país; o gráfico temporal mostra "
        "registros pela data de assinatura, sem filtrar status de atividade.",
    )
    document.add_picture(str(country_chart), width=Inches(6.2))
    document.add_picture(str(monthly_chart), width=Inches(6.2))

    document.add_heading("Resultados da análise", level=1)
    add_paragraph(
        document,
        f"País líder: {top_country} ({format_integer(int(country_counts.iloc[0]))}). "
        f"Maior contagem por cidade: {format_integer(int(city_counts.max()))} "
        f"({len(top_city_names)} cidades empatadas). "
        f"Cinco empresas mais frequentes: "
        f"{'; '.join(f'{name} ({format_integer(int(count))})' for name, count in top_company_names.items())}.",
    )
    add_paragraph(
        document,
        "Nota metodológica: cada linha foi tratada como um registro de cliente; "
        "não foi presumido um campo de assinatura ativa que não existe na base.",
    )
    document.save(output_path)


def create_summary(
    data: pd.DataFrame,
    output_path: Path,
    country_chart: Path,
    monthly_chart: Path,
    yearly_counts: pd.Series,
    month_counts: pd.Series,
) -> None:
    document = Document()
    set_document_font(document)

    title = document.add_paragraph()
    title.paragraph_format.space_after = Pt(8)
    title_run = title.add_run("Resumo executivo — análise de assinaturas")
    title_run.bold = True
    title_run.font.name = "Arial"
    title_run.font.size = Pt(12)

    dates = data["Subscription Date"]
    country_counts = data["Country"].value_counts()
    top_country = country_counts.index[0]
    top_month = int(month_counts.index[0])
    complete_years = [
        int(year) for year in yearly_counts.index if year < dates.dt.year.max()
    ]
    if len(complete_years) >= 2:
        first_year, second_year = complete_years[-2:]
        first_total = int(yearly_counts.loc[first_year])
        second_total = int(yearly_counts.loc[second_year])
        year_note = (
            f"Nos anos completos, os registros passaram de "
            f"{format_integer(first_total)} em {first_year} para "
            f"{format_integer(second_total)} em {second_year} "
            f"({format_percent(second_total / first_total - 1)})."
        )
    else:
        year_note = "A série disponível não contém dois anos completos para comparação."

    paragraphs = [
        (
            f"A base reúne {format_integer(len(data))} registros, mas não informa "
            "quais assinaturas estão ativas; portanto, os números representam "
            "cadastros, não clientes ativos confirmados."
        ),
        (
            f"A {top_country} lidera por país com "
            f"{format_integer(int(country_counts.iloc[0]))} registros "
            f"({format_percent(country_counts.iloc[0] / len(data), 2)} do total). "
            "Como a participação é pequena, recomenda-se testar campanhas locais "
            "antes de ampliar o investimento."
        ),
        (
            f"Agosto teve o maior volume agregado nos anos completos "
            f"({format_integer(int(month_counts.loc[top_month]))} registros), "
            f"seguido por {MONTH_NAMES[int(month_counts.index[1])].lower()}. "
            "Vale testar campanhas nesses períodos e comparar os resultados."
        ),
        year_note,
        (
            "Acompanhe conversão, receita e cancelamentos por região e período; "
            "a base não mostra concentração expressiva em uma cidade ou empresa. "
            "Use os resultados dos pilotos para decidir onde expandir."
        ),
    ]
    for text in paragraphs:
        add_paragraph(document, text)

    heading = document.add_paragraph()
    heading.paragraph_format.space_before = Pt(4)
    heading.paragraph_format.space_after = Pt(4)
    run = heading.add_run("Gráficos")
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(12)
    document.add_picture(str(country_chart), width=Inches(6.0))
    document.add_picture(str(monthly_chart), width=Inches(6.0))

    document.save(output_path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gera gráficos e relatório Word a partir da base de clientes."
    )
    parser.add_argument("csv", type=Path, help="Caminho para o arquivo CSV")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("entregaveis_analise"),
        help="Pasta de saída (padrão: entregaveis_analise)",
    )
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Gera somente o resumo executivo, sem substituir o relatório completo",
    )
    args = parser.parse_args()

    data = load_data(args.csv)
    country_chart, monthly_chart, monthly_counts, yearly_counts, month_counts = (
        make_charts(data, args.output_dir)
    )
    report_path = args.output_dir / "relatorio_analise_assinaturas.docx"
    if not args.summary_only:
        create_report(
            data,
            report_path,
            country_chart,
            monthly_chart,
            monthly_counts,
            yearly_counts,
            month_counts,
        )
    summary_path = args.output_dir / "resumo_executivo_assinaturas.docx"
    create_summary(
        data,
        summary_path,
        country_chart,
        monthly_chart,
        yearly_counts,
        month_counts,
    )
    if not args.summary_only:
        print(f"Relatório criado: {report_path.resolve()}")
    print(f"Resumo criado: {summary_path.resolve()}")
    print(f"Gráficos criados: {country_chart.resolve()} e {monthly_chart.resolve()}")


if __name__ == "__main__":
    main()
