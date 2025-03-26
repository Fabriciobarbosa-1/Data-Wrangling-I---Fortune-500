import pandas as pd

# Carregar o arquivo CSV
fortune_df = pd.read_csv("fortune.csv", delimiter=";", encoding="utf-8")

# 🔹 Lista de colunas que precisam ser convertidas (excluímos ranking e employees)
colunas_numericas = [
    "revenues", "revenues-percent-change", "profits", "profits-percent-change",
    "assets", "market-value"
]

# 🔹 Função para remover "$", "%" e substituir "-" por NaN, depois converter para float
def limpar_valor(valor):
    if isinstance(valor, str):  # Verifica se o valor é string
        valor = valor.replace("$", "").replace("%", "").replace(",", "").strip()
        return float(valor) if valor not in ["", "-"] else None  # Converte para float ou None
    return valor  # Retorna o valor original se não for string

# 🔹 Aplicar a função de limpeza às colunas necessárias
for coluna in colunas_numericas:
    fortune_df[coluna] = fortune_df[coluna].apply(limpar_valor)

# 🔹 Exibir os primeiros valores para conferir
print(fortune_df.head())
print("\n🔹 Tipos de dados atualizados:")
print(fortune_df.dtypes)
