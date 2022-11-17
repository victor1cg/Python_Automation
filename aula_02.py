
#! SELENIUM

""" 
Tudo que o Selenium faz é enviar comandos ao navegador de internet para fazer algo ou 
solicitar informações dele. A maior parte do que você irá fazer com o Selenium é uma 
combinação desses comandos básicos.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  

#* Inicializando o WEBDRIVER (Simulador de Navegador)
# Instaciar o driver com a versão atualizada (a maioria das maquinas atualiza o navegador, não o driver)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#* 2 - Navegar ate o site
# driver.get('https://ge.globo.com/')
driver.get('https://cursoautomacao.netlify.app/')
# input('Aperte uma tecla para fechar')

#* 3 - Solicitando Informações
title = driver.title
print(title)

#* 4 - Estabelecendo uma Estratégia de Espera
driver.implicitly_wait(1)

#* 5 - Clicar em um Elemento
# achar o elemento
botao_drop = driver.find_element(By.ID,'dropdownMenuButton')

# 5.1 - Metodo 1
botao_drop.click()
# 5.2 - Metodo 2 (executa js)
# driver.execute_script('arguments[0].click()',botao_drop)
input("")
driver.close()

#* 5 - Clicar em um Elemento Link
# quero clicar na pagina login, atributo unico é 'Login'
login = driver.find_element(By.LINK_TEXT,'Login')
login.click()

name = driver.find_element(By.NAME,'Name')
name.send_keys('victor1cg@hotmail.com')