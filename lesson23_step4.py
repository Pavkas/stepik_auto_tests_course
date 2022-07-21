from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

url = 'https://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.alert.accept()
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x_element)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.TAG_NAME, 'button').click()



finally:
	time.sleep(10)
	browser.quit()