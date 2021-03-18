from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import platform
import time
import random


arquivo = open('frases.txt', 'r')
linhas = arquivo.read()

for j in range(len(linhas)):
	frasesArray = linhas.split('.')
aux = []
print(frasesArray)

# para não pedir confirmação de uso de camera e microfone 
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")


# Abrir o navegador com o driver correto
if platform.system() == 'Linux':
	browser = webdriver.Chrome(executable_path='./driver/chromedriver', options=chrome_options) # Linux
else:
	browser = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)   # Windows

# abre o link do AVA para a sala desejada
browser.get("https://us.bbcollab.com/guest/d3c0bb8b107d4c9092488ff4f6383be7")

control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_id("guest-name")
		nomeElem.send_keys("Lucas Bot")
	except:
		print('[ERROR] Campo nome não encontrado. Outra tentativa acontecerá em %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Nome digitado com sucesso.')
		control = 0


# clica no botão next

control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="launch-html-guest"]')
		nomeElem.click()
	except:
		print('[ERROR] Campo nome não encontrado. Outra tentativa acontecerá em %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Botão encontrado.')
		control = 0



# fecha a configuração de audio e vídeo
time.sleep(2)

control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="techcheck-modal"]/button')
		nomeElem.click()

	except:
		print('[ERROR] botão não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Botão encontrado.')
		control = 0



# fecha o tutorial do AVA
time.sleep(2)


control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="announcement-modal-page-wrap"]/button')
		nomeElem.click()

	except:
		print('[ERROR] botão não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - Botão encontrado.')
		control = 0



# clicar na aba
time.sleep(2)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="side-panel-open"]')
		nomeElem.click()

	except:
		print('[ERROR] bate papo não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - bate papo encontrado.')
		control = 0


#encontra o bate papo todos
time.sleep(2)
control = 1
while control > 0:
	try:
		nomeElem = browser.find_element_by_xpath('//*[@id="chat-channel-scroll-content"]/ul/li/ul/li')
		nomeElem.click()

	except:
		print('[ERROR] bate papo todos não encontrado, tentando novamente em: %d' % (control))
		time.sleep(control)
		control += 1
	else:
		print('[OK] - bate papo todos encontrado.')
		control = 0
control = 1
falas=["","",""]
frases = {}
arquivo2 = open("PerguntaseRespostas.txt","r")
linhas2 = arquivo2.readlines()
for t in range(len(linhas2)):
	
	pergunta , resposta = linhas2[t].split(":")
	frases[pergunta] = resposta

#pega as mensagens do chat e salva 
while falas[-1] != "fechar" :
	time.sleep(1)
	nomeABC=browser.find_element_by_xpath('//*[@id="chat-channel-history"]')
	nomeABC.text
	falas = nomeABC.text.split('\n')
#digita a resposta da mensagem
	if falas[-1] in frases and count_mensagem != len(falas):
		imprimir = falas[-1]
		while control > 0:
			try:
				time.sleep(2)
				nomeElem = browser.find_element_by_id("message-input")
				time.sleep(2)
				nomeElem.send_keys(frases[imprimir])
				nomeElem.send_keys(Keys.ENTER)
			except:
				print('[ERROR] Não foi conseguido enviar a mensagem com sucesso %d' % (control))

				control += 1
			else:
				print(frases[imprimir])
				aux += frases[imprimir]
				print('[OK] -Mensagem enviada com sucesso')
				control = 0
		control = 1
	
	count_mensagem = len(falas)
