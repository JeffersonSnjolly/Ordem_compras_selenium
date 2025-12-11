# 📊 Coletor Automático de Cotações – Selenium + Pandas  

![Banner do Projeto](https://raw.githubusercontent.com/github/explore/main/topics/python/python.png)

---

## 🧿 **Badges do Projeto**
<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Selenium-Automation-green?logo=selenium">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-yellow?logo=pandas">
  <img src="https://img.shields.io/badge/Status-Ativo-success?style=flat">
  <img src="https://img.shields.io/github/license/jefferson/projeto?color=lightgrey">
</p>

---

# 🦾 **Descrição do Projeto**

Este projeto automatiza a coleta de preços de commodities diretamente do site **Melhor Câmbio**, utilizando **Python + Selenium + Pandas** — gerando automaticamente um relatório Excel atualizado.  
Ele é ideal para estudos de **web scraping, automação, análise de dados e RPA** 🤖📈

---

# 🔥 **Demonstração Visual**
> Painel ilustrativo (exemplo apenas)

![Demonstração](https://raw.githubusercontent.com/github/explore/main/topics/selenium/selenium.png)

---

# 🚀 **Funcionalidades**
- 📥 Importa a planilha `commodities.xlsx`
- 🌐 Acessa automaticamente o site do Melhor Câmbio
- 🔎 Extrai o valor comercial de cada commodity
- ✏ Atualiza o Excel com:
  - ✔ Preço Atual  
  - ✔ Indicador **Comprar**
- 📤 Gera um arquivo final `ordemDeCompras.xlsx`

---

# 📘 **Código Base do Projeto**

```python
import pandas as pd
from selenium import webdriver

df = pd.read_excel('commodities.xlsx')
nave = webdriver.Chrome()
print(df)

for linha in df.index:
    produto = df.loc[linha, 'Produto']
    nave.get(f'https://www.melhorcambio.com/{produto}-hoje')
    cotacao = nave.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace('.','').replace(',','.')
    cotacao = float(cotacao)
    df.loc[linha, 'Preço Atual'] = cotacao
    print(produto, cotacao)
print(df)

df['Comprar'] = df['Preço Atual'] < df['Preço Ideal']
print(df)

nave.quit()

df.to_excel('ordemDeCompras.xlsx')
```

---

# 🗂 **Estrutura Sugerida**

```
📁 projeto-cotacoes
 ├── 📄 commodities.xlsx
 ├── 📄 ordemDeCompras.xlsx
 ├── 🐍 coletor.py
 └── 📄 README.md
```

---

# 🛠 **Tecnologias Usadas**
- 🐍 Python  
- 🐼 Pandas  
- 🤖 Selenium WebDriver  
- 🧭 ChromeDriver  
- 📑 Excel  

---

# ⚠️ Requisitos

Certifique-se de ter instalado:

```
pip install pandas selenium openpyxl
```

E também o **ChromeDriver** compatível com sua versão do Chrome.

---

# 💡 Exemplo de Resultado Final

| Produto | Preço Ideal | Preço Atual | Comprar |
|--------|-------------|-------------|---------|
| ouro   | 350.00      | 320.50      | ✔ Sim |
| prata  | 50.00       | 55.20       | ❌ Não |

---

# 🤝 **Contribuindo**
Pull requests são muito bem-vindos!  
Achou um bug? Abra uma issue 🐛  
Quer melhorar o design? Manda ver 🎨  

---

# 📜 **Licença**
Este projeto está sob licença MIT.  

---

# 🎁 Personalizações
Se quiser, posso criar também:
- Uma capa em estilo **e-book**  
- Uma logo personalizada  
- Uma versão com dark mode  
- Badges com seu nome de usuário do GitHub  

Só pedir! 🚀

