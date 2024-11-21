import streamlit as st
import plotly.express as px
import pandas as pd

def exibir():
    path = "PyAnalytics-Streamlit/indicadores_saneamento.csv"
    data = pd.read_csv(path)
    data = data.drop(columns=["grupo", "subgrupo"])

    # sidebar
    st.sidebar.title("Saneamento")
    visualizacao = st.sidebar.radio(
        "Escolha a visualização",
        [
            "Cobertura de Abastecimento de Água",
            "Cobertura de Coleta de Esgoto",
        ],
    )

    anos_disponiveis = sorted(data["ano"].unique())
    anos_selecionados = (min(anos_disponiveis), max(anos_disponiveis))
    water_access = data[
        (data["indicador"] == "População com acesso à água")

    ]
    water_no_access = data[
        (data["indicador"] == "População sem acesso à água")

    ]

    sewage_access = data[
        (data["indicador"] == "População com coleta de esgoto")

    ]
    sewage_no_access = data[
        (data["indicador"] == "População sem coleta de esgoto")

    ]

    sewage_treated = data[
        (data["indicador"] == "Esgoto tratado")
    ]
    sewage_collected = data[
        (data["indicador"] == "Esgoto coletado")
    ]

    school_delay_with_sanitation = data[
        (data["indicador"] == "Atraso escolar dos jovens com saneamento")

    ]
    school_delay_without_sanitation = data[
        (data["indicador"] == "Atraso escolar dos jovens sem saneamento")

    ]

    if visualizacao == "Cobertura de Abastecimento de Água":
        st.title("Cobertura de Abastecimento de Água")
        st.write(
            "Esse painel apresenta a cobertura de abastecimento de água em Araranguá, SC. O acesso à água potável é um direito humano fundamental e um determinante essencial da saúde. A cobertura de abastecimento de água reflete a capacidade de uma comunidade de fornecer água limpa e segura a seus habitantes. Quando as pessoas não têm acesso a água tratada, aumentam os riscos de doenças transmitidas pela água, como diarreia e infecções gastrointestinais, que podem ser fatais, especialmente para crianças e populações vulneráveis. Além disso, a escassez de água pode levar à desidratação, afetando a saúde geral e a capacidade de enfrentar doenças. Melhorar a cobertura de abastecimento de água é, portanto, vital para garantir que todos tenham acesso a condições sanitárias adequadas, prevenindo surtos de doenças e promovendo um ambiente mais saudável. Aumentar a infraestrutura hídrica é uma prioridade para a saúde pública e a prosperidade das comunidades."
        )
        year_range = st.slider("Ano", data["ano"].min(), data["ano"].max(), (data["ano"].min(), data["ano"].max()), 1)
        combined_data_water = pd.concat([water_access, water_no_access])
        combined_data_water = combined_data_water[combined_data_water["ano"].between(year_range[0], year_range[1])]

        fig = px.bar(
            combined_data_water,
            x="ano",
            y="valor",
            color="indicador",
            labels={"ano": "Ano", "valor": "População", "indicador": "Indicador"},
            title="Cobertura de Abastecimento de Água ao longo dos anos",
        )

        fig.update_layout(
            xaxis_title="Ano",
            yaxis_title="População (em milhares)",
            legend_title="Indicador",
            template="plotly_white",
        )

        fig.update_xaxes(tickmode='linear')
        st.plotly_chart(fig)

    elif visualizacao == "Cobertura de Coleta de Esgoto":
        st.title("Cobertura de Coleta de Esgoto")
        st.write(
            "Esse painel apresenta a cobertura de coleta de esgoto em Araranguá, SC. O acesso a um sistema de esgoto eficiente é essencial para a saúde pública e o bem-estar das comunidades. A coleta de esgoto adequada ajuda a prevenir a contaminação do solo e da água, reduzindo a propagação de doenças infecciosas e melhorando a qualidade de vida. Quando o esgoto não é tratado, ele pode poluir o meio ambiente, causando danos à saúde e ao ecossistema. A falta de coleta de esgoto também pode levar a problemas de saneamento, como inundações e mau cheiro, afetando a qualidade de vida das pessoas. Investir em infraestrutura de esgoto é, portanto, uma prioridade para garantir a saúde pública e a sustentabilidade ambiental. A expansão da cobertura de coleta de esgoto é essencial para proteger a saúde das comunidades e promover um ambiente mais limpo e saudável."
        )
        year_range = st.slider("Ano", data["ano"].min(), data["ano"].max(), (data["ano"].min(), data["ano"].max()), 1)
        combined_data_sewage = pd.concat([sewage_access, sewage_no_access])
        combined_data_sewage = combined_data_sewage[combined_data_sewage["ano"].between(year_range[0], year_range[1])]

        fig = px.line(
            combined_data_sewage,
            x="ano",
            y="valor",
            color="indicador",
            labels={"ano": "Ano", "valor": "População", "indicador": "Indicador"},
            markers=True,
            title="Cobertura de Coleta de Esgoto ao longo dos anos",
        )

        fig.update_layout(
            xaxis_title="Ano",
            yaxis_title="População (em milhares)",
            legend_title="Indicador",
            template="plotly_dark",
        )

        fig.update_xaxes(tickmode='linear')
        st.plotly_chart(fig)

    st.markdown("---")
    st.write("""
    **Fonte dos dados:** [TRATABRASIL](https://tratabrasil.org.br/principais-estatisticas/dados-regionais/)
    """)
    st.write("""
    **Página feita por: [Matheus](https://github.com/matheuskolln)** 
    """)
