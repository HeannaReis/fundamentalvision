import pandas as pd

class DataFrameHandler:
    @staticmethod
    def ajustar_tipos_dataframe(df):
        for coluna in df.columns:
            if df[coluna].dtype == 'object':
                try:
                    df[coluna] = df[coluna].astype(float)
                except ValueError:
                    df[coluna] = df[coluna].astype(str)
            elif df[coluna].dtype in ['int64', 'float64']:
                df[coluna] = df[coluna].astype(float)
        return df