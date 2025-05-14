from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
service = Service('/usr/local/bin/geckodriver')
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get("http://10.12.1.13/#/login")
    wait = WebDriverWait(driver, 20)

    # Step 1: Login
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))  # Update ID if incorrect
    password = driver.find_element(By.ID, "password")  # Update ID if incorrect

    username.send_keys("root")
    password.send_keys("admin")
    password.send_keys(Keys.RETURN)  # or click login button if needed

    # Step 2: Wait for dashboard/nav to load and click "ONU"
    onu_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'ONU')]")))
    onu_button.click()

    # Step 3: Navigate to "ONU MAC" using the sidebar
    onu_mac_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'ONU MAC')]")))
    onu_mac_link.click()

    # Step 4: Wait for MAC Information Table to load
    table = wait.until(EC.presence_of_element_located((By.XPATH, "//table[contains(., 'MAC Information Table')]")))

    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows[1:]:  # Skip header row
        cols = row.find_elements(By.TAG_NAME, "td")
        data = [col.text for col in cols]
        print(data)

finally:
    driver.quit()
