class API():
    from selenium import webdriver
    driver = webdriver.Chrome() 
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()

    def Boot(text, password):
        from selenium import webdriver
        driver = webdriver.Chrome() 
        driver.minimize_window()
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        driver.get("https://coffeetox.ru/form?name=login&next=%2F")

        # Ожидание появления элемента для ввода Name
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']//form/div[@class='form-units']/div[@id='tag']/input")))
        name_input.send_keys(text)

        # Ожидание появления элемента для ввода Password
        pw_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/div[@class='form-units']/div[@id='pw']/input")))
        pw_input.send_keys(password)

        # Ожидание появления кнопки Submit
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/input[@class='button']")))
        submit_button.click()

    def Post(zagolovok, Text):
        from selenium import webdriver
        driver = webdriver.Chrome() 
        driver.minimize_window()
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        driver.get("https://coffeetox.ru/create_post")

        # Ожидание появления элемента для ввода Zagolovok
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/div[@class='form-units']/div[@id='title']/input")))
        name_input.send_keys(zagolovok)

        # Ожидание появления элемента для ввода Text
        pw_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/div[@class='form-units']/div[@id='text']/textarea")))
        pw_input.send_keys(Text)

        # Ожидание появления кнопки Post
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']/form/input[@class='button']")))
        submit_button.click()

    def Others():
        from selenium import webdriver
        driver = webdriver.Chrome() 
        driver.minimize_window()
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        driver.get("https://coffeetox.ru/")

        oth = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[@class='global-wrapper']/div[@class='main-grid']/main[@class='styled-scroll']")))
        print(oth.get_attribute("outerHTML"))