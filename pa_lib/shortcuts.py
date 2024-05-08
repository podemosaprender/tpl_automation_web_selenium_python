#INFO: nombres cortos para controlar desde interactivo

browser= None
from selenium.webdriver.common.by import By

def es(sel, parent=None):
	el= (parent or browser).find_element(By.CSS_SELECTOR, sel)
	return el

def cn(name, parent=None):
	el= (parent or browser).find_element(By.CSS_SELECTOR, f'[name="{name}"]')
	el.click()
	return el

def ca(name, parent=None):
	el= (parent or browser).find_element(By.CSS_SELECTOR, f'[aria-label="{name}"]')
	el.click()
	return el

def ct(name, parent=None):
	el= (parent or browser).find_element(By.XPATH, f"//*//*[text()='{name}']")
	el.click()
	return el

def kn(name,txt, parent=None):
	txt2= txt.replace('\n',Keys.ENTER)
	el= cn(name)
	el.send_keys(txt2)
	return el


