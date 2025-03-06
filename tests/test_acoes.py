import pytest
import pandas as pd
from fundamentalvision.acoes import Acao

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

def test_obter_detalhes(acao):
    """Teste para verificar se os detalhes da ação são obtidos corretamente."""
    acao.obter_detalhes()
    assert acao.detalhes is not None
    assert isinstance(acao.detalhes, pd.DataFrame)
    assert not acao.detalhes.empty

def test_obter_proventos(acao):
    """Teste para verificar se os proventos da ação são obtidos corretamente."""
    acao.obter_proventos()
    assert acao.proventos is not None
    assert isinstance(acao.proventos, pd.DataFrame)
    assert not acao.proventos.empty

def test_obter_oscilacoes(acao):
    """Teste para verificar se as oscilações da ação são obtidas corretamente."""
    acao.obter_oscilacoes()
    assert acao.oscilacoes is not None
    assert isinstance(acao.oscilacoes, pd.DataFrame)
    assert not acao.oscilacoes.empty

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

def test_carregar_dados_fundamentais_invalido():
    """Teste para verificar o comportamento ao tentar carregar dados de uma ação inválida."""
    acao_invalida = Acao('INVALIDO')
    acao_invalida.carregar_dados_fundamentais()
    assert acao_invalida.dados_fundamentais.empty  # Verifica se o DataFrame está vazio