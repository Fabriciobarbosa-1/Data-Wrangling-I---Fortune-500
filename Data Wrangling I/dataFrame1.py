import pandas as pd

# Carregar o arquivo CSV em um DataFrame
fortune_df = pd.read_csv("fortune.csv", delimiter=";", encoding="utf-8")

# Exibir as primeiras linhas para verificar se foi carregado corretamente
print(fortune_df.head())
