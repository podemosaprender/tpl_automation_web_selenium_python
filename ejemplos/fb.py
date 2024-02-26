#INFO: controlar facebook

import pa_lib
from pa_lib.shortcuts import *
from selenium.webdriver.common.keys import Keys
from pa_lib.webdriver import get_browser

browser= get_browser()

browser.get('https://mbasic.facebook.com')
pa_lib.cookies_load(browser, may_not_exist=True)
browser.refresh()

def post(texto):
	global browser
	cn("view_privacy")
	ca("Solo io")
	kn("xc_message", texto)
	cn("view_withtag")
	kn("query", "Galileo\n")
	ct("Galileo Cappella")
	cn("done")
	cn("view_post")

def novedades():
	global browser
	ct("Notifiche")
	ct("Visualizza altre notifiche")
	el= es('#notifications_list')
	return el.get_attribute('innerHTML')
	#TODO: probar el.find_elements_by_css_selector('*')

#browser.quit()



