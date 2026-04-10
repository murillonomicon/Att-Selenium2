from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

options = Options()

options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)

print("Acessando a primeira aba...")
driver.get("https://the-internet.herokuapp.com/dropdown")

print("Abrindo outra aba...")
driver.execute_script("window.open('https://the-internet.herokuapp.com/dynamic_loading/2');")
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

print("Abrindo a ultima aba...")
driver.execute_script("window.open('https://pt.wikipedia.org');")
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))

driver.switch_to.window(driver.window_handles[0])
elemento_dropdown = driver.find_element(By.ID, "dropdown")
menu = Select(elemento_dropdown)
menu.select_by_visible_text("Option 1")
opcao = menu.first_selected_option
opcao_selecionada = opcao.get_attribute("value")
print(f"Opção selecionada: {opcao_selecionada}")

driver.switch_to.window(driver.window_handles[1])
botao = driver.find_element(By.CSS_SELECTOR, "#start button")
botao.click()
msg = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, "finish")))
print(f"Mensagem depois de o botão carregar: {msg.text}")

driver.switch_to.window(driver.window_handles[2])
barra_pesquisa = driver.find_element(By.NAME, "search")
barra_pesquisa.send_keys("Automação")
botao = driver.find_element(By.ID, "vector-main-menu-dropdown-checkbox").click()
link_texto = driver.find_element(By.LINK_TEXT, "Esplanada")
texto = link_texto.text
destino = link_texto.get_attribute("href")
driver.save_screenshot("evidencia_wiki.png")
print(f"texto do link: {texto}")
print(f"link oculto: {destino}")

driver.close()
driver.quit()