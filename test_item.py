import time
from selenium.webdriver.common.by import By
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_item(browser):
    browser.get(link)
    try:
        assert browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
        print("Элемент найден")
    except AssertionError:
        print("Элемент не найден")

    time.sleep(5)
