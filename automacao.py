import pyautogui as py
import time 


py.PAUSE = (0.3)
#passo 1: abrir o navegador
#apertar a tecla win
py.press("win")
#digitar o navegador e dar enter
py.write("opera gx")
time.sleep(0.3)
py.press("enter")


#passo 2: entrar no site

#digitar o nome do site e dar enter
time.sleep(0.8)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
py.write(link)
time.sleep(1.5)
py.press("enter")
#passo 3: fazer login no site

py.click(x=725, y=350)
time.sleep(1.5)
py.write("joaohenrique@gmail.com")
time.sleep(0.4)
py.press("tab")
py.write("123456")
time.sleep(0.3)
py.press("tab")
py.press("enter")
#passo 4: cadastrar os produtos
import pandas as pd 
tabela = pd.read_csv('produtos.csv')
print(tabela)



for linha in range(50):
    py.click(x=725, y=226)
    codigo = tabela.loc[linha,"codigo"]
    py.write(str(codigo))
    py.press('tab')
    marca = tabela.loc[linha, "marca"]
    py.write(str(marca))
    py.press('tab')
    tipo = tabela.loc[linha,"tipo"]
    py.write(str(tipo))
    py.press('tab')
    categoria = tabela.loc[linha,"categoria"]
    py.write(str(categoria))
    py.press('tab')
    preco = tabela.loc[linha,"preco_unitario"]
    py.write(str(preco))
    py.press('tab')
    custo = tabela.loc[linha,"custo"]
    py.write(str(custo))
    py.press('tab')
    obs = tabela.loc[linha,"obs"]
    if not pd.isna(obs):
        py.write(str(obs))
    py.press('tab')
    py.press('enter')
    py.scroll(1000000)
time.sleep(0.5)
py.hotkey("Ctrl", "w")
py.hotkey("Ctrl", "w")


