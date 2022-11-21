
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
from time import sleep

#Fechar a pagina
def close():
    input("")
    return driver.close()

#* Inicializando o WEBDRIVER (Simulador de Navegador)
# Instaciar o driver com a versão atualizada (a maioria das maquinas atualiza o navegador, não o driver)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)      #so preciso definir uma vez


#* 2 - Navegar ate o site
# driver.get('https://ge.globo.com/')
driver.get('https://cursoautomacao.netlify.app/')
# input('Aperte uma tecla para fechar')

#* 3 - Solicitando Informações
title = driver.title
print(title)

#* 4 - Estabelecendo uma Estratégia de Espera
sleep(3)

#* 5 - Clicar em um Elemento
# achar o elemento
botao_drop = driver.find_element(By.ID,'dropdownMenuButton')

sleep(3)

# 5.1 - Metodo 1
botao_drop.click()
# 5.2 - Metodo 2 (executa js)
# driver.execute_script('arguments[0].click()',botao_drop)

sleep(3)

#* 5 - Clicar em um Elemento Link
# quero clicar na pagina login, atributo unico é 'Login'
login = driver.find_element(By.LINK_TEXT,'Login')
login.click()

name = driver.find_element(By.ID,'email')
name.send_keys('victor1cg@hotmail.com')

sleep(3)

password = driver.find_element(By.ID,'senha')
password.send_keys('A1B2C3')
sleep(3)

bt2 = driver.find_element(By.XPATH,"//button[@class = 'btn btn-primary']")
bt2.click()

input("")
close()