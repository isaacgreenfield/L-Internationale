#chop and pray
#you sold me my own wealth
#now you gonna pay
#10 737 418 240
#the mission awaits

from selenium import webdriver
driver = webdriver.Chrome() 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("https://coffeetox.ru/form?name=login&next=%2F")
tag = "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']//form/div[@class='form-units']/div[@id='tag']/input"
pw = "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/div[@class='form-units']/div[@id='pw']/input"
buttonq = "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/input[@class='button']"

# Ожидание появления элемента для ввода Name
name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']//form/div[@class='form-units']/div[@id='tag']/input")))
name_input.send_keys("revolution")

# Ожидание появления элемента для ввода Password
pw_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/div[@class='form-units']/div[@id='pw']/input")))
pw_input.send_keys("REVOLUTION")

# Ожидание появления кнопки Submit
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/input[@class='button']")))
submit_button.click()
while True:
    

    driver.get("https://coffeetox.ru/")

    # Ожидание появления кнопки Post
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/nav/a[@class='button'][5]")))
    submit_button.click()

    driver.get("https://coffeetox.ru/create_post")

    # Ожидание появления элемента для ввода Name
    name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/div[@class='form-units']/div[@id='title']/input")))
    name_input.send_keys("REVOLUTION")

    # Ожидание появления элемента для ввода Password
    pw_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/div[@class='form-units']/div[@id='text']/textarea")))
    pw_input.send_keys("REVOLUTION")

    # Ожидание появления кнопки Post
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/input[@class='button']")))
    submit_button.click()