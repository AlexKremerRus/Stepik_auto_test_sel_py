import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) 

try:
	link="http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	# скролим до прайса
	txt=browser.find_element_by_id("price")
	browser.execute_script("return arguments[0].scrollIntoView(true);", txt)

	# активное ожидание в течении 12 сек, с шагом 0.5с ищет объект цена с указанным значением
	text = WebDriverWait(browser, 12).until(
	        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
	    )

	button = browser.find_element_by_id("book")
	#browser.execute_script("return arguments[0].scrollIntoView(true);", button)	
	button.click()

	#найдем Х 
	input_x=(browser.find_element_by_id("input_value")).text
	#browser.execute_script("return arguments[0].scrollIntoView(true);", input_x)
	# посчитаем функцию

	y=calc(input_x)

	# ответ
	answer=browser.find_element_by_id("answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", answer) # скролим 
	answer.send_keys(y)

	button = browser.find_element_by_id("solve")
	button.click()
	
finally:
	time.sleep(5)
	browser.quit()
