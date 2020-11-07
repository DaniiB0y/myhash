import os
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from test.test_import.data.unwritable import x

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(PATH, chrome_options=options)
driver.get("https://www.bauruempregos.com.br/home/vagas")
dicionario = []
dicfiltro = []
dcvg = []
pgnt = 0 
c = 0
key = ""
vagas = 0 
key = str(input("Buscar por: "))
nv = int(input('Por quantas vagas?'))
for i in range(0, nv):
    vagas = driver.find_elements_by_tag_name("div")
    vagas = driver.find_elements_by_class_name("descricao-vaga")
    # Achando os links e os nomes das vagas
    descricaovaga = vagas[i]
    dcvg.append(descricaovaga)
    descricaovaga.click()
    vagas = driver.find_elements_by_class_name("descricao-vaga")
    # Entrando e pegando os elementos da descricao da vaga
    dicionario.append(vagas[0].text.lower())
    # Adicionando em uma lista.lower()
    href = "https://www.bauruempregos.com.br/home/vagas"
    driver.get(href)
    if key in dicionario[i]:
        print(dicionario[i])
    else:
        print("Não encontrado")
