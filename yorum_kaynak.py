from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def yorumlari_getir(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(), options=options)
    driver.get(url)

    yorumlar = []
    try:
        wait = WebDriverWait(driver, 20)

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "p")))
            tum_p = driver.find_elements(By.TAG_NAME, "p")

            for p in tum_p:
                text = p.text.strip()
                if text and "Bu değerlendirme" not in text and len(text) > 20:
                    if text not in yorumlar:
                        yorumlar.append(text)


            try:
                next_button = driver.find_element(By.XPATH, '//button[starts-with(@class, "hermes-Pagination-module_next")]')
                if "disabled" in next_button.get_attribute("class"):
                    break
                next_button.click()
                time.sleep(2)
            except:
                break

    except Exception as e:
        print("Yorumları çekerken hata oluştu:", e)

    driver.quit()
    return yorumlar
