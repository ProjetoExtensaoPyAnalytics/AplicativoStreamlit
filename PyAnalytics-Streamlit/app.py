import streamlit as st
from PIL import Image
import vacina
import saneamento
import doencas
import medicamentos

st.markdown(
    """
    <style>
    .main {background-color: #FFFFFF; padding: 20px; border-radius: 8px;}
    p, h1, h2, h3, h4, h5, h6, li, div {color: #333333 !important;}
    .stMarkdown h1 {color: #007BFF;}
    .option-icon {font-size: 28px; vertical-align: middle; padding-right: 8px;}
    </style>
    """,
    unsafe_allow_html=True
)

#página inicial
def pagina_inicial():
    st.title("🌐 Bem-vindo aos Dados de Saúde de Araranguá!")
    st.markdown("""
        <div style="background-color:#E9F5FF; padding: 20px; border-radius: 10px; margin-bottom: 15px;">
        <p style="font-size:16px; color:#333333;">
            Este sistema permite que você consulte dados essenciais de saúde pública de Araranguá.
            Explore informações sobre vacinas, saneamento, doenças e medicamentos disponíveis no município.
        </p>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.write("### Seções disponíveis:")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background-color:#0000FF; padding:15px; border-radius:8px;">
            <h3>💉 Vacinas</h3>
            <p style="font-size:14px; color:#555555;">Consulte informações sobre as vacinas disponíveis no município.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color:#FFD9D4; padding:15px; border-radius:8px;">
            <h3>🚰 Saneamento</h3>
            <p style="font-size:14px; color:#555555;">Confira os dados relacionados ao saneamento básico em Araranguá.</p>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div style="background-color:#FFF6D3; padding:15px; border-radius:8px;">
            <h3>🦠 Doenças</h3>
            <p style="font-size:14px; color:#555555;">Veja informações sobre doenças registradas no município.</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="background-color:#D4E7FF; padding:15px; border-radius:8px;">
            <h3>💊 Medicamentos</h3>
            <p style="font-size:14px; color:#555555;">Verifique a disponibilidade de medicamentos na rede pública.</p>
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

#sidebar
st.sidebar.title("Navegação")
page = st.sidebar.radio(
    "Selecione uma página",
    ["Início", "Vacina", "Saneamento", "Doenças", "Medicamentos"],
    format_func=lambda x: f"🏠 {x}" if x == "Início" else f"{'💉 Vacinas' if x == 'Vacina' else '🚰 Saneamento' if x == 'Saneamento' else '🦠 Doenças' if x == 'Doenças' else '💊 Medicamentos'}"
)

#vai p/ pagina selecionada
if page == "Início":
    pagina_inicial()
elif page == "Vacina":
    vacina.exibir()
elif page == "Saneamento":
    saneamento.exibir()
elif page == "Doenças":
    doencas.exibir()
elif page == "Medicamentos":
    medicamentos.exibir()


#esse é o tema do streamlit usado
#[theme]
#base="light"
#primaryColor="#4ba3ff"
#secondaryBackgroundColor="#ffffff"
#textColor="#000000"
