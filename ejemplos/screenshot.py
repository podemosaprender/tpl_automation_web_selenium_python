#INFO: como subir un archivo
#VER: http://the-internet.herokuapp.com/

from pa_lib.webdriver import get_browser, free_browser

dst_fname= 'resultados/x_ej_screenshot.png'

browser= get_browser()
browser.get('http://timeanddate.com')
browser.save_screenshot(dst_fname)
print(f'Screenshot guardado como {dst_fname}')
free_browser()



