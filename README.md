# 🏆 Data Wrangling I - Fortune 500  

Este projeto realiza a **extração, limpeza e análise de dados** das **100 maiores empresas** do ranking **Fortune 500**, convertendo os dados para um formato estruturado em um arquivo CSV.

## 📌 Objetivo  
- Extrair os dados do arquivo **fortune.html**  
- Limpar e padronizar os dados removendo caracteres indesejados  
- Salvar o resultado no arquivo **fortune-limpo.csv**  

---

## 💂 **Estrutura do Projeto**  
```
💃 Data_Wrangling_I  
│\── fortune.html                # Arquivo original com os dados em HTML  
│\── fortune.csv                 # Arquivo extraído (dados brutos)  
│\── fortune-limpo.csv           # Arquivo processado (dados limpos)  
│\── codigo-fortune.py           # Script para extração e processamento dos dados  
│\── README.md                   # Documentação do projeto  
```

---

## ⚙ **Tecnologias Utilizadas**  
- Python 🔭  
- Pandas 📊  
- BeautifulSoup4 🌐  
- CSV 📄  

---

## 🚀 **Como Executar o Projeto**  

### 1️⃣ **Instalar as dependências**
Antes de rodar o script, instale os pacotes necessários:  
```bash
pip install pandas beautifulsoup4
```

### 2️⃣ **Executar o script de extração**  
```bash
python codigo-fortune.py
```

### 3️⃣ **Verificar a saída**  
Após a execução, o arquivo **fortune-limpo.csv** será gerado contendo os dados estruturados.

---

## 📊 **Exemplo de Saída - fortune-limpo.csv**
```csv
rank;name;revenues;revenues-percent-change;profits;profits-percent-change;assets;market-value;employees
1;Walmart;559151.0;6.7;13510.0;-9.2;252496.0;382642.8;2300000
2;Amazon;386064.0;37.6;21331.0;84.1;321195.0;1558069.6;1298000
3;Apple;274515.0;5.5;57411.0;3.9;323888.0;2050665.9;147000
```

---

## 🛠 **Principais Funcionalidades**
✔ **Extração**: Coleta os dados do arquivo HTML da Fortune 500  
✔ **Transformação**: Remove caracteres `$`, `%`, `,` e converte para valores numéricos  
✔ **Salvamento**: Gera um CSV pronto para análise  

---

## 📝 **Notas Importantes**
- O código ignora os cabeçalhos do HTML e extrai apenas os **100 primeiros registros**.  
- Se houver valores faltantes no CSV final, eles serão preenchidos com `None`.  

📢 **Dúvidas ou sugestões?** Fique à vontade para entrar em contato! 🚀

