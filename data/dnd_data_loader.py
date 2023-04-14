# data/dnd_data_loader.py
import requests
import pandas as pd

def load_dnd_data():
    """
    Carrega dados de monstros da API 'https://www.dnd5eapi.co/api/monsters'
    e retorna um pandas DataFrame contendo as informações de cada monstro.
    """
    url = 'https://www.dnd5eapi.co/api/monsters'
    response = requests.get(url)
    data = response.json()
    monster_data = []
    for monster in data['results']:
        monster_url = monster['url']
        response = requests.get(monster_url)
        monster_data.append(response.json())
    df = pd.DataFrame(monster_data)
    return df

def preprocess_dnd_data(df):
    """
    Realiza o pré-processamento dos dados, incluindo a remoção de colunas irrelevantes e a
    codificação de colunas categóricas. Retorna um pandas DataFrame pronto para ser utilizado
    no treinamento de uma rede neural.
    """
    # Remove colunas irrelevantes
    columns_to_drop = ['_id', 'actions', 'legendary_actions', 'reactions', 'special_abilities', 'url']
    df = df.drop(columns=columns_to_drop)

    # Codifica colunas categóricas
    df['alignment'] = df['alignment'].astype('category').cat.codes
    df['challenge_rating'] = df['challenge_rating'].astype('category').cat.codes
    df['size'] = df['size'].astype('category').cat.codes
    df['type'] = df['type'].astype('category').cat.codes

    return df
