from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import chromedriver_autoinstaller
from pyvirtualdisplay import Display

import os
ESTE_DIR= os.path.abspath('.')
PROFILE_DIR= ESTE_DIR+'/_browser_profile'

browser= None

def get_browser(quiereVisible= False, quiereVirtualDisplay= None):
	global browser
	if browser is None:
		quiereVirtualDisplay= os.environ.get('DISPLAY',None) is None if quiereVirtualDisplay is None else quiereVirtualDisplay
		if quiereVirtualDisplay:
			display = Display(visible=0, size=(800, 800)) 
			display.start()

		chromedriver_autoinstaller.install()

		chrome_options = webdriver.ChromeOptions()
		options = [
				"--disable-gpu",
				"--window-size=1920,1200",
				"--ignore-certificate-errors",
				"--disable-extensions",
				"--no-sandbox",
				"--disable-dev-shm-usage",
				"user-data-dir="+PROFILE_DIR, #A: Path to your chrome profile
		]

		if not quiereVisible and os.environ.get('P_VISIBLE',None) is None:
			options.append("--headless")

		for option in options:
				chrome_options.add_argument(option)

		browser= webdriver.Chrome(options=chrome_options)

	return browser

def free_browser(a_browser=None):
	global browser
	a_browser= a_browser or browser
	a_browser.quit()
	if a_browser==browser:
		browser= None
