# Desafio 74

Implementando um simples web scraper com Selenium

## Explicação

### Ferramentas Utilizadas

- `selenium`: Biblioteca para automação de navegadores web.
- `webdriver_manager`: Biblioteca para gerenciar drivers de navegador.

### Funções Principais

- `webdriver.Chrome()`: Cria uma instância do navegador Chrome.
- `driver.get(url)`: Navega para a URL especificada.
- `driver.find_element(By, value)`: Encontra um elemento na página.
- `element.send_keys()`: Envia teclas para um elemento.

## Resultado

```py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configura o driver do Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navega para o Google
    driver.get('https://www.google.com')

    # Encontra o campo de busca
    campo_de_busca = driver.find_element(By.NAME, 'q')

    # Digita 'Python' no campo de busca e pressiona Enter
    campo_de_busca.send_keys('Python')
    campo_de_busca.send_keys(Keys.RETURN)

    # Espera alguns segundos para ver os resultados
    driver.implicitly_wait(5)

    # Exibe o título da página
    print(driver.title)

finally:
    # Fecha o navegador
    driver.quit()