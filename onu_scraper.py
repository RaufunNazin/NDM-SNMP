from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(executable_path='/home/maestro/bin/geckodriver', firefox_options=options)

try:
    driver.get("http://10.12.1.13/#/login")
    wait = WebDriverWait(driver, 20)

    # Step 1: Login
    username = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))  # Locate username input field by type='text'
    password = driver.find_element(By.XPATH, "//input[@type='password']")  # Locate password input field by type='password'

    username.send_keys("root")
    password.send_keys("admin")
    password.send_keys(Keys.RETURN)  # or click login button if needed

    # Step 2: Wait for the "ONU" icon to be clickable and click it
    onu_icon = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//i[contains(@class, 'iconfont icon-ONU')]")
    ))
    onu_icon.click()

    # Step 3: Navigate to "ONU MAC" using the sidebar
    onu_mac_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//li[contains(@class, 'el-menu-item')]//span[text()='ONU MAC']")
    ))

    # Scroll the element into view using JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", onu_mac_link)

    # Now click on the element
    onu_mac_link.click()

    # Step 4: Wait for MAC Information Table to load
    table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".el-table")))

    # Find the table header and body
    header = table.find_element(By.CSS_SELECTOR, ".el-table__header")
    body = table.find_element(By.CSS_SELECTOR, ".el-table__body")

    # Get column names from the header
    header_columns = header.find_elements(By.TAG_NAME, "th")
    columns = [col.text for col in header_columns]

    # Get rows of data from the table body
    rows = body.find_elements(By.TAG_NAME, "tr")

    # Iterate through each row and print the data
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        data = [col.text for col in cols]
        print(dict(zip(columns, data)))  # Create a dictionary with column names as keys

finally:
    driver.quit()
