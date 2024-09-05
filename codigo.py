import pyautogui
import time
import pandas

pyautogui.PAUSE = 1.0

# abrir o navegador (chrome)
#time.sleep faz uma espera para abrir o navegador ou processar 
pyautogui.press("win")
time.sleep(2)
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
#entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)
#preenchendo os campos
pyautogui.click(x=1013, y=341)
pyautogui.hotkey("ctrl","a")
pyautogui.write("noriki@hotmail.com")
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.write("12345")
time.sleep(0.5)
#para clicar no botão de clicar
pyautogui.click(x=955, y=462)
time.sleep(3)

#ler a tabela/banco
tabela = pandas.read_csv("produtos.csv")
# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=950, y=261)
     # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    # passar para o proximo campo
    pyautogui.press("tab")
     # preencher o campo
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
            pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    #fazer rolar para cima
    pyautogui.scroll(50000)
