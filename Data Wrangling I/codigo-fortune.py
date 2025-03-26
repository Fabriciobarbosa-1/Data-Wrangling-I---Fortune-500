import csv
from bs4 import BeautifulSoup

# Caminho do arquivo HTML
caminho_arquivo = "fortune.html.html"

# Ler o arquivo HTML
with open(caminho_arquivo, "r", encoding="utf-8") as file:
    conteudo = file.read()

# Criar o objeto BeautifulSoup
pagina = BeautifulSoup(conteudo, "html.parser")

# Encontrar a tabela de dados
tabela = pagina.find('div', {'class': 'rt-table'})

if not tabela:
    print("Erro: A tabela não foi encontrada no arquivo HTML.")
    exit()

# Encontrar as linhas da tabela
linhas = tabela.find('div', {'class': 'rt-tbody'})

if not linhas:
    print("Erro: O corpo da tabela não foi encontrado.")
    exit()

# Definir cabeçalho das colunas
header = [
    'rank', 'name', 'revenues', 'revenues-percent-change', 'profits',
    'profits-percent-change', 'assets', 'market-value', 'employees'
]

# Lista para armazenar os dados extraídos
dados_extraidos = []

# Extrair o conteúdo das linhas da tabela
for linha in linhas.find_all('div', {'role': 'row'}):
    colunas = linha.find_all('div', {'class': 'rt-td'})
    valores = [col.get_text(strip=True) for col in colunas]

    if len(valores) == len(header):  # Certifica-se de que todas as colunas estão presentes
        dados_extraidos.append(valores)

# Escrever os dados no arquivo CSV
with open("fortune.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(header)  # Escrever o cabeçalho
    writer.writerows(dados_extraidos)  # Escrever os dados

print("Arquivo fortune.csv criado com sucesso!")
