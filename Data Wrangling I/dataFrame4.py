import pandas as pd

# Carregar o arquivo CSV original
fortune_df = pd.read_csv("fortune.csv", delimiter=";", encoding="utf-8")

# 🔹 Lista de colunas numéricas que precisam ser convertidas
colunas_numericas = [
    "revenues", "revenues-percent-change", "profits", "profits-percent-change",
    "assets", "market-value"
]

# 🔹 Função para limpar os valores das colunas numéricas
def limpar_valor(valor):
    if isinstance(valor, str):  # Verifica se o valor é string
        valor = valor.replace("$", "").replace("%", "").replace(",", "").strip()
        return float(valor) if valor not in ["", "-"] else None  # Converte para float ou None
    return valor  # Retorna o valor original se não for string

# 🔹 Aplicar a função de limpeza às colunas necessárias
for coluna in colunas_numericas:
    fortune_df[coluna] = fortune_df[coluna].apply(limpar_valor)

# 🔹 Salvar o DataFrame no arquivo CSV limpo
fortune_df.to_csv("fortune-limpo.csv", sep=";", index=False, encoding="utf-8")

print("✅ Arquivo 'fortune-limpo.csv' salvo com sucesso!")
