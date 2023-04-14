import pandas as pd

def load_data(file_path):
    # Carregar os dados de um arquivo CSV
    df = pd.read_csv(file_path)

    # Limpar os dados (por exemplo, remover linhas vazias, converter tipos de dados)
    df = df.dropna()
    df['price'] = df['price'].astype(float)

    return df

def save_data(df, file_path):
    # Salvar os dados em um arquivo CSV
    df.to_csv(file_path, index=False)
