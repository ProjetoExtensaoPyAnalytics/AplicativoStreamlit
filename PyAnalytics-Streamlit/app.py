import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import vacina
import saneamento
import obitos
import medicamentos
import base64
import internacoes

# Função para converter uma imagem para Base64
def image_to_base64(img_path):
    with open(img_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

#página inicial
def pagina_inicial():
    logo_esquerda_base64 = image_to_base64("PyAnalytics-Streamlit/logo-py.png")
    logo_direita = Image.open("PyAnalytics-Streamlit/logo-ufsc.png")

    col1, col2, col3 = st.columns([1, 6, 1])


    with col1:
        # Exibir a imagem como um link clicável
        st.markdown(
            f"""
            <a href="https://www.linkedin.com/company/pyanalytics/posts/?feedView=all" target="_blank">
                <img src="data:image/png;base64,{logo_esquerda_base64}" alt="Logo PyAnalytics" style="width:100px;">
            </a>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="text-align: center; font-size: 36px; font-weight: bold; color: #0066CC;">
                Portal de Dados de Saúde de Araranguá
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.image(logo_direita, width=100)

    st.markdown(
        """
        <style>
        .subtitle {
            font-size: 20px;
            font-weight: 400;
            color: #333333;
            text-align: center;
            margin-bottom: 25px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
  
    st.markdown('<div class="subtitle">Acesse informações essenciais de saúde pública de forma prática e rápida.</div>', unsafe_allow_html=True)


    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background-color:#939290; padding:20px; border-radius:10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1); text-align:center;">
            <h3 style="color:#FFFFFF; font-size:22px; margin: 0;"> Vacinas</h3>
            <p style="font-size:20px; color:#E0E0E0; margin-top:10px;">Consulte informações sobre as vacinas disponíveis no município.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color:#007cc2; padding:20px; border-radius:10px; margin-bottom:15px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1); text-align:center;">
            <h3 style="color:#FFFFFF; font-size:22px; margin: 0;"> Saneamento</h3>
            <p style="font-size:20px; color:#E0E0E0; margin-top:10px;">Confira os dados relacionados ao saneamento básico em Araranguá.</p>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div style="background-color:#fff500; padding:20px; border-radius:10px; margin-bottom:15px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1); text-align:center;">
            <h3 style="color:#333333; font-size:22px; margin: 0;"> Óbitos</h3>
            <p style="font-size:20px; color:#555555; margin-top:10px;">Veja informações sobre óbitos registrados no município.</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="background-color:#da251c; padding:20px; border-radius:10px; margin-bottom:15px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1); text-align:center;">
            <h3 style="color:#FFFFFF; font-size:22px; margin: 0;"> Medicamentos</h3>
            <p style="font-size:20px; color:#E0E0E0; margin-top:10px;">Verifique a disponibilidade de medicamentos na rede pública.</p>
        </div>
        """, unsafe_allow_html=True)


    st.markdown(
        """
        <div style="text-align: center; font-size: 14px; color: #333;">
        <br>
        <p>Use o menu de navegação à esquerda para acessar cada seção detalhadamente.</p>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown(
    """
    <hr style="margin-top: 25px; margin-bottom: 25px; border: none; border-top: 2px solid #CCCCCC;">
    <div style="text-align: center; color: #666666; font-size: 16px;">
        Esta aplicação é uma iniciativa do <strong><a href="https://www.linkedin.com/company/pyanalytics/posts/?feedView=all" target="_blank" style="color: #0066CC; text-decoration: none;">PyAnalytics</a></strong>, 
        projeto de extensão da Universidade Federal de Santa Catarina, Campus Araranguá, coordenado pela Professora Andréa Sabedra Bordin. 
        O objetivo é promover o acesso a dados de saúde pública em Araranguá e contribuir com a sociedade através de soluções de análise de dados. Você pode ver todo o código fonte dessa aplicação em nosso <strong><a href="https://github.com/ProjetoExtensaoPyAnalytics" target="_blank" style="color: #0066CC; text-decoration: none;">Github.</a></strong>
    </div>
    """,
    unsafe_allow_html=True
    )
#sidebar
page = st.sidebar.radio(
    "Selecione um painel",
    ["Início", "Vacina", "Saneamento", "Óbitos", "Medicamentos","Internações"],
    format_func=lambda x: f" {x}" if x == "Início" else f"{' Vacinas' if x == 'Vacina' else ' Saneamento' if x == 'Saneamento' else ' Óbitos' if x == 'Óbitos' else ' Internações' if x == 'Internações' else ' Medicamentos'}"
)

#vai p/ pagina selecionada
if page == "Início":
    # CSS específico para a página inicial
    st.markdown(
        """
        <style>
        .main {background-color: #ffffff; padding: 20px; border-radius: 8px;}
        p, h1, h2, h3, h4, h5, h6, li, div {color: #333333 !important;}
        .stMarkdown h1 {color: #007BFF;}
        .option-icon {font-size: 28px; vertical-align: middle; padding-right: 8px;}
        </style>
        """,
        unsafe_allow_html=True
    )
    # HTML específico para a página inicial
    st.write('<div class="inicio-page">', unsafe_allow_html=True)
    st.write('</div>', unsafe_allow_html=True)
    pagina_inicial()
elif page == "Vacina":
        # CSS específico para a página inicial
    st.markdown(
        """
        <style>
        .main {background-color: #ffffff; padding: 20px; border-radius: 8px;}
        p, h1, h2, h3, h4, h5, h6, li, div {color: #333333 !important;}
        .stMarkdown h1 {color: #007BFF;}
        .option-icon {font-size: 28px; vertical-align: middle; padding-right: 8px;}
        </style>
        """,
        unsafe_allow_html=True
    )
    # HTML específico para a página inicial
    st.write('<div class="inicio-page">', unsafe_allow_html=True)
    st.write('</div>', unsafe_allow_html=True)
    vacina.exibir()
elif page == "Saneamento":
    saneamento.exibir()
elif page == "Óbitos":
    obitos.exibir()
elif page == "Internações":
    internacoes.exibir()
elif page == "Medicamentos":
        # CSS específico para a página inicial
    st.markdown(
        """
        <style>
        .main {background-color: #fffFFF; padding: 20px; border-radius: 8px;}
        p, h1, h2, h3, h4, h5, h6, li, div {color: #333333 !important;}
        .stMarkdown h1 {color: #007BFF;}
        .option-icon {font-size: 28px; vertical-align: middle; padding-right: 8px;}
        </style>
        """,
        unsafe_allow_html=True
    )
    # HTML específico para a página inicial
    st.write('<div class="inicio-page">', unsafe_allow_html=True)
    st.write('</div>', unsafe_allow_html=True)
    medicamentos.exibir()  # Chama a função que exibe o conteúdo da página de medicamentos


#esse é o tema do streamlit usado
#[theme]
#base="light"
#primaryColor="#4ba3ff"
#secondaryBackgroundColor="#ffffff"
#textColor="#000000"
