import pytest
import pandas as pd
from fundamentalvision.dashboard import Dashboard
from unittest.mock import patch, MagicMock

@pytest.fixture
def dashboard():
    """Fixture para criar uma instância da classe Dashboard para os testes."""
    acoes = pd.DataFrame({
        'Papel': ['PETR3', 'VALE3'],
        'Preço': [30.0, 100.0],
        'DY': [0.05, 0.04]
    }).set_index('Papel')
    return Dashboard(acoes)

def test_formatar_numero(dashboard):
    """Teste para verificar a formatação de números."""
    assert dashboard.formatar_numero(1234.56) == '1.235'
    assert dashboard.formatar_numero('10%') == '10%'
    assert dashboard.formatar_numero('Texto') == 'Texto'

@patch('streamlit.sidebar.selectbox')
@patch('streamlit.columns')
def test_exibir_dashboard(mock_columns, mock_selectbox, dashboard):
    """Teste para verificar a exibição do dashboard."""
    mock_selectbox.return_value = 'PETR3'
    mock_columns.return_value = (MagicMock(), MagicMock())

    dashboard.exibir_dashboard()
    mock_selectbox.assert_called_once()
    assert mock_columns.call_count == 2  # Verifica se st.columns foi chamado duas vezes