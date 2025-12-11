📊 Coletor Automático de Cotações – Selenium + Pandas

Este projeto automatiza a coleta de preços de commodities diretamente do site Melhor Câmbio, utilizando Python, Pandas e Selenium.
Ele lê uma planilha, consulta o preço atual de cada produto e gera um relatório atualizado 📈💰

🚀 Funcionalidades

📥 Lê automaticamente uma planilha Excel (commodities.xlsx)

🌐 Acessa o site melhorcambio.com com Selenium

🔎 Captura o valor comercial atual de cada commodity

✏ Atualiza a planilha com:

Preço Atual

Indicador se deve comprar (Sim/Não)

📤 Exporta tudo para ordemDeCompras.xlsx

🧩 Como funciona o código

Carrega os dados usando Pandas

Abre o Chrome com Selenium WebDriver

Percorre cada linha da planilha

Busca o preço atualizado no Melhor Câmbio

Converte o valor para float

Compara com o Preço Ideal

Gera um arquivo final atualizado

🛠 Tecnologias Utilizadas

🐍 Python 3

📦 Pandas

🌐 Selenium WebDriver

💻 Chrome / ChromeDriver

📑 Excel (.xlsx)

📘 Código Principal
´´´python
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
´´´
📂 Estrutura Recomendada do Projeto
📁 projeto-cotacoes
 ├── 📄 commodities.xlsx
 ├── 📄 ordemDeCompras.xlsx
 ├── 🐍 coletor.py
 └── 📄 README.md

⚠️ Observações Importantes

Certifique-se de ter o ChromeDriver instalado e compatível com sua versão do Google Chrome.

O site pode mudar o ID do input futuramente — nesse caso será necessário atualizar o XPATH.

Alguns produtos podem não existir no site → trate exceções!

🎯 Resultado Final

Ao terminar, você terá um Excel atualizado com:

Produto	Preço Ideal	Preço Atual	Comprar
ouro	350.00	320.50	✔ Sim
prata	50.00	55.20	❌ Não
🤝 Contribuição

Sinta-se à vontade para melhorar este projeto, enviar sugestões ou pedir funcionalidades novas! ✨
