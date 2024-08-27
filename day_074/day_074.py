from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get('https://www.google.com')

    campo_de_busca = driver.find_element(By.NAME, 'q')

    campo_de_busca.send_keys('Python')
    campo_de_busca.send_keys(Keys.RETURN)

    driver.implicitly_wait(5)

    resultados = driver.find_elements(By.CSS_SELECTOR, 'h3')
    for i, resultado in enumerate(resultados, start=1):
        print(f"Resultado {i}: {resultado.text}")

finally:
    driver.quit()