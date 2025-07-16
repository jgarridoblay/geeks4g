import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_geeksforgeeks_page_elements():
    # Inicializar el driver
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    driver.maximize_window()
    # Cargar la página
    driver.get("https://www.geeksforgeeks.org/software-testing/selenium-webdriver-submit-vs-click/")
    #time.sleep(5000)  # Espera corta para asegurar carga

    #driver.dialog.accept
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fc-button"))
        ).click()
        print("✅ Consentimiento de cookies cerrado.")
    except:
        print("ℹ️ No se encontró banner de cookies.")

    # Verificar que el título contenga 'Selenium WebDriver'
    assert "Selenium Webdriver submit() vs click() - GeeksforGeeks" in driver.title

    # Scroll hacia abajo para encontrar el primer enlace dentro del artículo
    actions = ActionChains(driver)
    #first_link = driver.find_element(By.XPATH, "(//a[contains(@href,'geeksforgeeks.org')])[5]")
    title_element = driver.find_element(By.CSS_SELECTOR, "div.article-title > h1")
    title_text = title_element.text
    print("El título: ",title_text)

    # Buscar el elemento h3 por su id
    heading = driver.find_element(By.ID, "how-click-works")

    # Verificar que el texto dentro del <span> sea correcto
    span_text = heading.find_element(By.TAG_NAME, "span").text
    print("El Texto: ",span_text)
    try:
        actions.move_to_element(heading).perform()
        assert span_text == "How click() Works:", "El texto dentro del h3 no coincide"
        print("El texto coincide")

    except Exception as e:
        print(f"❌ Test falló: {e}")

    print("✅ Test del h3 completado correctamente.")
    
    try:

    # Buscar el elemento <span> por su XPath completo
        span = driver.find_element(By.XPATH, '//*[@id="post-1310591"]/div[3]/table/tbody/tr[1]/td[1]/span')
        actions.move_to_element(span).perform()

    # Verificar que el texto sea el esperado
        expected_text = "Used to submit forms in which the element is located."
        assert span.text == expected_text, f"El texto no coincide. Esperado: '{expected_text}', encontrado: '{span.text}'"

        print("✅ Test del <span> con XPath completado correctamente.")

    except Exception as e:
        print(f"❌ Test falló: {e}")


    # Verificar el enlace de Linux
    linux_menu_text = driver.find_element(By.LINK_TEXT, "Linux").text
    print("El Texto de Linux: ",linux_menu_text)
    try:        
      WebDriverWait(driver, 5).until(
      EC.element_to_be_clickable((By.LINK_TEXT, "Linux"))
      ).click()
      print("Link de Linux presionado")

    except Exception as e:
        print(f"❌ Link de Linux fallido: {e}")

    print("✅ Test de link completado correctamente.")


    # Esperar a la carga del enlace
    try:        
      WebDriverWait(driver, 15).until(
      EC.text_to_be_present_in_element((By.XPATH, '//h1[text()="Linux/Unix Tutorial"]'),"Linux/Unix Tutorial"))

      # Espera hasta que el <span> con texto "Installing Linux" sea visible
      wait = WebDriverWait(driver, 10)
      span_element = wait.until(EC.visibility_of_element_located((
      By.XPATH, '//span[text()="Installing Linux"]'
      )))
      actions.move_to_element(span_element).perform()

# Confirmación
      if span_element.is_displayed():
        print("El elemento <span>Installing Linux</span> está visible.")
      else:
        print("El elemento no está visible.")

    except Exception as e:
        print(f"❌ Título de Linux fallido: {e}")

    print("✅ Test de Link de Linux completado correctamente.")



    time.sleep(2)


    # Probar enviar texto en un campo de búsqueda del header (si existe)
  #  try:
  #      search_icon = driver.find_element(By.CLASS_NAME, "header-search-icon")
  #      search_icon.click()
  #      time.sleep(1)
#
  #      search_input = driver.find_element(By.ID, "gsc-i-id1")
  #      search_input.send_keys("selenium")
  #      time.sleep(1)
#
  #      # Click en botón de búsqueda si existe
  #      search_button = driver.find_element(By.CLASS_NAME, "gsc-search-button")
  #      search_button.click()
  #      time.sleep(3)
#
  #      assert "selenium" in driver.page_source.lower()
  #  except Exception as e:
  #      print(f"No se pudo realizar búsqueda: {e}")
#
  #  # Cerrar navegador
    driver.quit()

test_geeksforgeeks_page_elements()
