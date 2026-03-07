import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import os 

link = "https://suninjuly.github.io/cats.html"

# 🔹 Берём путь к драйверу из кэша
# Если драйвер ещё не скачан, он будет загружен и закэширован
driver_path = ChromeDriverManager().install()
service = Service(driver_path)


try:

    # 🔹 Создаём объект браузера
    driver = webdriver.Chrome(service=service)

    driver.implicitly_wait(5)

    # 🔹 Открываем страницу
    driver.get(link)

    # 🔹 Небольшая пауза, чтобы страница точно загрузилась
    time.sleep(1)

 
    field1 = driver.find_element(By.ID, "button")
    
finally:
    time.sleep(3)
    # 🔹 Закрываем браузер в любом случае
    driver.quit()
