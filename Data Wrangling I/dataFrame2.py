import pandas as pd

# Carregar o arquivo CSV em um DataFrame
fortune_df = pd.read_csv("fortune.csv", delimiter=";", encoding="utf-8")

# 🔹 Listar as 10 primeiras linhas do DataFrame
print("🔹 10 Primeiras Linhas do DataFrame:")
print(fortune_df.head(10))

# 🔹 Listar os tipos de dados armazenados nas colunas
print("\n🔹 Tipos de Dados das Colunas:")
print(fortune_df.dtypes)

# 🔹 Listar o número de linhas e colunas do DataFrame
print("\n🔹 Número de Linhas e Colunas:")
print(f"Linhas: {fortune_df.shape[0]}, Colunas: {fortune_df.shape[1]}")
