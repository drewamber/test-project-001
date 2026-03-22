from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

def test_button_add_to_cart_should_be_visible(browser):
    browser.get(link)

    wait = WebDriverWait(browser, 10)

    button = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
    )

    assert button, "Кнопка добавления в корзину не найдена или не видна"