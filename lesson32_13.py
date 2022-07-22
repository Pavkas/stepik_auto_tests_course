from selenium import webdriver
from selenium.webdriver.common.by import By
import time, unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def unique_selectors(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '//label[text()="First name*"]/following::input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//label[text()="Last name*"]/following::input')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//label[text()="Email*"]/following::input')
    input3.send_keys("test@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    return welcome_text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта    
class UniqueSelectors(unittest.TestCase):
    def test_link1(self):
        welcome_text = unique_selectors(link1)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_link2(self):
        welcome_text = unique_selectors(link2)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()
