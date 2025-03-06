import streamlit as st
import pandas as pd
from acoes import Acao
from data_handler import DataFrameHandler
import plotly.express as px

class Dashboard:
    def __init__(self, acoes):
        self.acoes = acoes

    @staticmethod
    def formatar_numero(valor):
        if isinstance(valor, (int, float)):
            # Formata números inteiros e floats com separadores de milhar
            return f"{valor:,.0f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        elif isinstance(valor, str) and valor.endswith('%'):
            # Se for uma string que termina com '%', retorna como está
            return valor
        return valor  # Retorna o valor inalterado se não for numérico ou porcentagem

    def exibir_dashboard(self):
        st.sidebar.title("📊 Dashboard de Análise de Ações")
        st.sidebar.write("Selecione um papel para visualizar detalhes.")
        papel_selecionado = st.sidebar.selectbox("Escolha uma ação", self.acoes.index)
        acao = Acao(papel_selecionado)
        acao.carregar_dados_fundamentais()
        acao.obter_proventos()
        acao.obter_detalhes()
        acao.obter_oscilacoes()
        
        # Alinhando Dados Fundamentais e Detalhes lado a lado
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"📌 Dados Fundamentais - {papel_selecionado}")
            dados_fundamentais_df = DataFrameHandler.ajustar_tipos_dataframe(acao.dados_fundamentais.T)
            st.dataframe(dados_fundamentais_df, width=400)
        
        with col2:
            st.subheader("🔍 Detalhes")
            if acao.detalhes is not None and not acao.detalhes.empty:
                detalhes_df = pd.DataFrame(acao.detalhes).T.reset_index()
                detalhes_df.columns = ['Descrição', 'Valor']
                
                # Remover caracteres de interrogação dos nomes das colunas
                detalhes_df['Descrição'] = detalhes_df['Descrição'].str.replace('?', '', regex=False)
                
                # Formatar valores numéricos
                detalhes_df['Valor'] = detalhes_df['Valor'].apply(self.formatar_numero)
                
                # Exibir a tabela formatada
                st.dataframe(detalhes_df, width=400)
            else:
                st.warning("Nenhum detalhe encontrado para essa ação.")
        
        # Gráfico de Proventos
        st.subheader("💰 Gráfico de Proventos")
        if acao.proventos is not None and not acao.proventos.empty:
            proventos_df = DataFrameHandler.ajustar_tipos_dataframe(acao.proventos)

            # Criar gráfico interativo com Plotly
            fig = px.bar(proventos_df, x='Data', y='Valor', title=f'Proventos de {papel_selecionado}', 
                          labels={'Data': 'Data', 'Valor': 'Valor (R$)'}, 
                          color='Valor', color_continuous_scale=px.colors.sequential.Cividis)
            st.plotly_chart(fig)
        else:
            st.warning("Nenhum provento encontrado para essa ação.")
        
        # Alinhando Dividendos e Oscilações lado a lado
        col_dividendos, col_oscilacoes = st.columns(2)
        with col_dividendos:
            st.subheader("💰 Dividendos")
            if not acao.proventos.empty:
                st.write(proventos_df)
        with col_oscilacoes:
            st.subheader("📉 Oscilações")
            if acao.oscilacoes is not None and not acao.oscilacoes.empty:
                oscilacoes_df = DataFrameHandler.ajustar_tipos_dataframe(acao.oscilacoes)
                st.write(oscilacoes_df)
        
        # Tabela Geral de Ações
        st.subheader("📈 Tabela Geral de Ações")
        st.dataframe(self.acoes)