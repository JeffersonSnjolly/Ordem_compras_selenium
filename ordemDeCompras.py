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