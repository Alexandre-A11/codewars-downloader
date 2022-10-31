from selenium import webdriver
from manipulate_csv import generate_csv, compare_csv, clear
from selenium.webdriver.common.by import By
import time, math, re


level = "9"
while level not in "12345678" or int(level) > 8:
    clear()
    level = input(
        "8) 8 kyu\n7) 7 kyu\n6) 6 kyu\n5) 5 kyu\n4) 4 kyu\n3) 3 kyu\n2) 2 kyu\n1) 1 kyu\nSelecione o nível de dificuldade desejado: "
    )

print(f"Nível de dificuldade {level} kyu selecionado")
URL_KYU = f"https://www.codewars.com/kata/search/?q=&r[]=-{int(level)}&beta=false&order_by=satisfaction_percent%20desc,total_completed%20desc"

browser = webdriver.Firefox()
browser.get(URL_KYU)

qty_katas_info = browser.find_element(By.CSS_SELECTOR, '[class="ml-0 mt-0 mb-2 text-ui-text"]').text
total_katas = int(re.sub("[^0-9]", "", qty_katas_info))
print(f"{total_katas} katas disponíveis")

if compare_csv(level, total_katas) == 0:
    quit()

qty_pagedown = math.ceil(total_katas / 30)

for i in range(qty_pagedown):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    print(f"Quantidade de scrolldown restantes: {qty_pagedown - i}")


time.sleep(2)
katas = browser.find_elements(By.CSS_SELECTOR, '[class="list-item-kata bg-ui-section p-4 rounded-lg shadow-md"]')

katas_id = [kata.get_attribute("id") for kata in katas]

generate_csv(level, katas_id)
