import pytest
import pandas as pd
from fundamentalvision.data_handler import DataFrameHandler

def test_ajustar_tipos_dataframe():
    """Teste para verificar a conversão de tipos em um DataFrame."""
    df = pd.DataFrame({
        'Col1': ['1', '2', '3'],
        'Col2': ['1.1', '2.2', '3.3'],
        'Col3': ['Texto', 'Outro', 'Mais']
    })
    df_ajustado = DataFrameHandler.ajustar_tipos_dataframe(df)
    assert df_ajustado['Col1'].dtype == float
    assert df_ajustado['Col2'].dtype == float
    assert df_ajustado['Col3'].dtype == object