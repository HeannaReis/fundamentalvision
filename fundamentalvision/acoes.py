import locale
import pandas as pd
import requests
from bs4 import BeautifulSoup
from fundamentus.detalhes import get_papel
import fundamentus
import logging

# Configura localidade
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Acao:
    def __init__(self, papel):
        self.papel = papel
        self.dados_fundamentais = None
        self.proventos = None
        self.detalhes = None
        self.oscilacoes = None  # Adicionando um atributo para oscilações

    def carregar_dados_fundamentais(self):
        try:
            self.dados_fundamentais = fundamentus.get_resultado().loc[[self.papel]]  # Use colchetes duplos para garantir que seja um DataFrame
            self.remover_formatacao()
        except KeyError:
            # Se a ação não for encontrada, defina dados_fundamentais como um DataFrame vazio
            self.dados_fundamentais = pd.DataFrame()

    def obter_detalhes(self):
        self.detalhes = get_papel(self.papel)
        if self.detalhes is None or self.detalhes.empty:
            logging.warning(f"Nenhum detalhe encontrado para o papel: {self.papel}")

    def obter_proventos(self):
        url = f"https://www.fundamentus.com.br/proventos.php?papel={self.papel}&tipo=2"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            self.proventos = pd.DataFrame(columns=['Data', 'Valor', 'Tipo'])  # Inicializa como DataFrame vazio
            return self.proventos

        soup = BeautifulSoup(response.text, 'html.parser')
        tabela = soup.find('table', {'id': 'resultado'})

        if not tabela:
            self.proventos = pd.DataFrame(columns=['Data', 'Valor', 'Tipo'])  # Inicializa como DataFrame vazio
            return self.proventos

        dados = []
        for linha in tabela.find_all('tr')[1:]:  # Ignora o cabeçalho da tabela
            colunas = linha.find_all('td')
            if len(colunas) >= 3:  # Verifica se há colunas suficientes
                try:
                    valor = float(colunas[1].text.strip().replace(',', '.'))
                except ValueError:
                    valor = None  # Se der erro, coloca None para evitar crash

                dados.append([colunas[0].text.strip(), valor, colunas[2].text.strip()])
        
        self.proventos = pd.DataFrame(dados, columns=['Data', 'Valor', 'Tipo'])
        return self.proventos

    def obter_oscilacoes(self):
        url = f"https://www.fundamentus.com.br/detalhes.php?papel={self.papel}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            self.oscilacoes = pd.DataFrame(columns=['Período', 'Oscilação'])  # Inicializa como DataFrame vazio
            return self.oscilacoes

        soup = BeautifulSoup(response.text, 'html.parser')
        conteudo_div = soup.find('div', class_='conteudo clearfix')

        if conteudo_div is None:
            self.oscilacoes = pd.DataFrame(columns=['Período', 'Oscilação'])  # Inicializa como DataFrame vazio
            return self.oscilacoes

        oscilacoes_data = []
        oscilacoes_section = conteudo_div.find('td', class_='nivel1', colspan='2')
        
        if oscilacoes_section:
            labels = oscilacoes_section.find_all_next('td', class_='label w1')
            dados = oscilacoes_section.find_all_next('td', class_='data w1')

            for label, dado in zip(labels, dados):
                label_text = label.get_text(strip=True)
                valor_text = dado.find('span', class_='oscil').get_text(strip=True)
                oscilacoes_data.append([label_text, valor_text])

        self.oscilacoes = pd.DataFrame(oscilacoes_data, columns=['Período', 'Oscilação'])
        return self.oscilacoes

    def remover_formatacao(self):
        colunas_percentuais = ['dy', 'mrgebit', 'mrgliq', 'roic', 'roe', 'c5y']
        for coluna in colunas_percentuais:
            if coluna in self.dados_fundamentais:
                try:
                    self.dados_fundamentais[coluna] = self.dados_fundamentais[coluna].astype(float)
                except ValueError as e:
                    logging.error(f"Erro ao converter coluna {coluna} para float: {e}")

    def formatar_moeda(self, valor):
        return locale.currency(valor, symbol=True, grouping=True)