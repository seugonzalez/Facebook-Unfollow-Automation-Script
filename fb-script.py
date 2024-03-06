from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os
import time

# Configuração do Edge WebDriver
browser = webdriver.Edge()
browser.maximize_window()  # Maximiza a janela do navegador

# Acessa o Facebook
browser.get('https://www.facebook.com')
wait = WebDriverWait(browser, 20)  # Aumenta o tempo de espera para 20 segundos

# Faz login
email = browser.find_element(By.ID, 'email')
email.send_keys('YOUR_LOGIN')
password = browser.find_element(By.ID, 'pass')
password.send_keys('YOUR_PASSWORD')
password.send_keys(Keys.RETURN)

# Espera pela transição de página
wait = WebDriverWait(browser, 15)

try:
    # Aguarda a conclusão do login verificando a URL
    wait.until(lambda driver: "facebook.com" in driver.current_url)
    print("Login bem-sucedido, na página inicial do Facebook.")

    # Checa se há algum pop-up ou alerta e os fecha, se necessário
    # (Adicione o código aqui se necessário)

    # Aumenta o tempo de espera antes de ir para a próxima página
    time.sleep(10)

    # Vai para as páginas curtidas
    browser.get('https://www.facebook.com/pages/?category=liked&ref=bookmarks')
    print("Navegando para a página de páginas curtidas.")

    # Espera até que os botões iniciais de menu "Mais ações" sejam carregados
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@aria-label, "Mais ações")]')))
    print("Na página de páginas curtidas.")

    processed = 0
    last_count = 0

    while True:
        # Rola para baixo para ativar o lazy loading
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Espera para que novos itens possam ser carregados

        # Carrega todos os botões de menu "Mais ações" visíveis
        menu_buttons = browser.find_elements(By.XPATH, '//div[contains(@aria-label, "Mais ações")]')


        # Verifica se novos botões foram carregados
        if last_count == len(menu_buttons):
            # Espera um pouco mais para garantir que não haja mais carregamentos
            time.sleep(5)
            menu_buttons = browser.find_elements(By.XPATH, '//div[contains(@aria-label, "Mais ações")]')
            if last_count == len(menu_buttons):
                # Se a contagem não mudar, todos os botões foram processados
                break

        last_count = len(menu_buttons)

        # Processa cada botão
        for i in range(processed, len(menu_buttons)):
            # Garante que o botão esteja na viewport
            ActionChains(browser).move_to_element(menu_buttons[i]).perform()

            # Aguarda até que o botão seja clicável
            wait.until(EC.element_to_be_clickable(menu_buttons[i]))

            # Clica no botão, considerando possíveis elementos sobrepostos
            try:
                menu_buttons[i].click()
            except Exception as click_exception:
                browser.execute_script("arguments[0].click();", menu_buttons[i])

            # Espera pela visibilidade da opção "Curtiu"
            try:
                like_option = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Curtiu"]')))
                browser.execute_script("arguments[0].click();", like_option)
                print(f"Menu item #{i + 1}: Página não curtida com sucesso.")
            except TimeoutException:
                print(f"Menu item #{i + 1}: Opção 'Curtiu' não encontrada no menu.")
            browser.find_element(By.TAG_NAME, 'body').click()
            time.sleep(2)  # Pequena pausa antes de processar o próximo botão

            processed = i + 1

    print("Todos os menus disponíveis foram processados.")

except NoSuchElementException:
    print("Algum elemento não foi encontrado, verifique os seletores.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    browser.quit()
