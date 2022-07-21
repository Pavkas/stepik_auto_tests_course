from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

url = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    element = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x_element)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#solve').click()

finally:
    time.sleep(20)
    browser.quit()



