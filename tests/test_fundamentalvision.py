import pytest
from unittest.mock import patch
from fundamentalvision.app import main

@patch('streamlit.set_page_config')
@patch('streamlit.sidebar.title')
@patch('streamlit.sidebar.selectbox')
def test_main(mock_selectbox, mock_title, mock_page_config):
    """Teste para verificar a execução da função main."""
    mock_selectbox.return_value = 'PETR3'
    main()
    mock_page_config.assert_called_once()
    mock_title.assert_called_once()
    mock_selectbox.assert_called_once()