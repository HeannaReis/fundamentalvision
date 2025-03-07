import pytest
import pandas as pd
from fundamentalvision.acoes import Acao
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def acao():
    """Fixture para criar uma instância da classe Acao para os testes."""
    return Acao('PETR3')

def test_carregar_dados_fundamentais(acao):
    """Teste para verificar se os dados fundamentais são carregados corretamente."""
    acao.carregar_dados_fundamentais()
    assert acao.dados_fundamentais is not None
    assert isinstance(acao.dados_fundamentais, pd.DataFrame)
    assert not acao.dados_fundamentais.empty

def test_carregar_dados_fundamentais_invalido():
    """Teste para verificar o comportamento ao tentar carregar dados de uma ação inválida."""
    acao_invalida = Acao('INVALIDO')
    acao_invalida.carregar_dados_fundamentais()
    assert acao_invalida.dados_fundamentais.empty  # Verifica se o DataFrame está vazio

@patch('requests.get')
def test_obter_proventos_sucesso(mock_get, acao):
    """Teste para verificar se os proventos são obtidos corretamente com uma resposta simulada."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = """
    <table id="resultado">
        <tr><td>2023-01-01</td><td>1,00</td><td>Dividendo</td></tr>
    </table>
    """
    mock_get.return_value = mock_response

    acao.obter_proventos()
    assert not acao.proventos.empty  # Verifica se o DataFrame não está vazio
    assert 'Data' in acao.proventos.columns
    assert 'Valor' in acao.proventos.columns
    assert 'Tipo' in acao.proventos.columns
    
@patch('requests.get')
def test_obter_proventos_falha(mock_get, acao):
    """Teste para verificar o comportamento quando a requisição falha."""
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    acao.obter_proventos()
    assert acao.proventos.empty  # Verifica se o DataFrame está vazio

@patch('requests.get')
def test_obter_proventos_sucesso(mock_get, acao):
    """Teste para verificar se os proventos são obtidos corretamente com uma resposta simulada."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = """
    <table id="resultado">
        <tr><th>Data</th><th>Valor</th><th>Tipo</th></tr>
        <tr><td>2023-01-01</td><td>1,00</td><td>Dividendo</td></tr>
    </table>
    """
    mock_get.return_value = mock_response

    acao.obter_proventos()
    assert not acao.proventos.empty  # Verifica se o DataFrame não está vazio
    assert 'Data' in acao.proventos.columns
    assert 'Valor' in acao.proventos.columns
    assert 'Tipo' in acao.proventos.columns

@patch('requests.get')
def test_obter_oscilacoes_falha(mock_get, acao):
    """Teste para verificar o comportamento quando a requisição falha."""
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    acao.obter_oscilacoes()
    assert acao.oscilacoes.empty  # Verifica se o DataFrame está vazio

def test_remover_formatacao(acao):
    """Teste para verificar se a formatação dos dados fundamentais é removida corretamente."""
    acao.carregar_dados_fundamentais()
    acao.remover_formatacao()
    assert 'dy' in acao.dados_fundamentais.columns
    assert acao.dados_fundamentais['dy'].dtype in [float, int]

def test_formatar_moeda(acao):
    """Teste para verificar se a formatação de moeda funciona corretamente."""
    valor = 1234.56
    formatted_value = acao.formatar_moeda(valor)
    assert formatted_value == 'R$ 1.234,56'  # Verifique se o formato está correto de acordo com a localidade