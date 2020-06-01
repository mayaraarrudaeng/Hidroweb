# -*- coding: utf-8 -*-
import time
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


#home = os.path.expanduser('~')

def wait_load_items(driver, xpath):

	n = 1
	p = 1
	while p: 
		try:
			driver.find_element_by_xpath(xpath)
			p = 0
		except:
			print(n, xpath)
			time.sleep(1)
			n += 1
		if n == 300:
			print('Tempo de espera excedito. Processo encerrado.')
			exit()

def click_css_selector(driver, css_selector):
	n = 0
	p = 1
	while p:
		try:
			driver.find_element_by_css_selector(css_selector).click()
			p = 0
		except:
			time.sleep(1)
			n += 1

		if n == 300:
			print('Tempo de espera excedido.')
			break

def download_hidroweb(id_station,  dir_out):

	# display = Display(visible=0, size=(800,600))
	# display.start()

	#carrega o Firefox
	fp = webdriver.FirefoxProfile()

	fp.set_preference("browser.download.folderList",2)
	fp.set_preference("browser.download.dir",dir_out)
	fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream")
	fp.set_preference("browser.download.manager.showWhenStarting", False)
	fp.set_preference("browser.download.manager.focusWhenStarting", False)  
	fp.set_preference("browser.download.useDownloadDir", True)
	fp.set_preference("browser.helperApps.alwaysAsk.force", False)
	fp.set_preference("browser.download.manager.alertOnEXEOpen", False)
	fp.set_preference("browser.download.manager.closeWhenDone", True)
	fp.set_preference("browser.download.manager.showAlertOnComplete", False)
	fp.set_preference("browser.download.manager.useWindow", False)
	fp.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
	fp.set_preference("pdfjs.disabled", True)

	#binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
	
	#Colocar aqui o caminho onde se encontra o firefox.exe
	binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
	driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)

	#driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
	url = 'http://www.snirh.gov.br/hidroweb/apresentacao.jsf'
	driver.get(url)
	time.sleep(1)
	driver.get(url)
	n = 0
	p = 1
	while  p:
		try:
			click_css_selector(driver, 'div.ng-star-inserted:nth-child(3) > mat-panel-title:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
			p = 0
		except:
			time.sleep(1)
			n += 1
		if n == 50:
			print('Tempo de espera excedido. Processo encerrado.')
			p = 0
			break

	wait_load_items(driver, '//*[@id="mat-input-0"]')
	driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys([id_station, Keys.ENTER])
	wait_load_items(driver, '//*[@id="mat-input-1"]')
	#driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys([name_estation, Keys.ENTER])
	click_css_selector(driver, 'button.mat-flat-button > span:nth-child(1)')
	wait_load_items(driver, '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/ng-component/form/mat-tab-group/div/mat-tab-body[1]/div/ana-card/mat-card/mat-card-content/ana-dados-convencionais-list/div/div[1]/table/tbody/tr/td[1]/mat-checkbox/label/div')
	time.sleep(2)

	try:
		driver.find_element_by_xpath('/html/body/app-root/mat-sidenav-container/mat-sidenav-content/ng-component/form/mat-tab-group/div/mat-tab-body[1]/div/ana-card/mat-card/mat-card-content/ana-dados-convencionais-list/div/div[1]/table/tbody/tr/td[1]/mat-checkbox/label/div').click()
		click_css_selector(driver, '#mat-radio-4 > label:nth-child(1) > div:nth-child(1)')
		click_css_selector(driver, 'a.mat-raised-button > span:nth-child(1)')
	except Exception as e:
		print(e)
		


#ID_ESTACAO = '47001000'
#NOME_ESTACAO = 'PORTO - TRAVESSIA DA BALSA'


arq = open('lista_estacoes.txt', 'r')
texto = arq.readlines()
for linha in texto :
    print(linha.rstrip())
    download_hidroweb(linha.rstrip(),  'out')
arq.close()


#download_hidroweb(ID_ESTACAO,  'out')