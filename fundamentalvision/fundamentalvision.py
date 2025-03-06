import locale
import pandas as pd
import streamlit as st
import fundamentus
from acoes import Acao
import plotly.express as px
from dashboard import Dashboard

def main():
    # Configura localidade
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    # Configuração do layout do Streamlit
    st.set_page_config(
        page_title="Análise de Ações",
        layout="wide",
        page_icon="📈"
    )

    acoes = fundamentus.get_resultado()
    dashboard = Dashboard(acoes)
    dashboard.exibir_dashboard()

if __name__ == "__main__":
    main()