from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# Setup
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(executable_path='/home/maestro/bin/geckodriver',firefox_options=options)

# Open the page
driver.get("https://books.toscrape.com/")
driver.implicitly_wait(10)

# Extract books from the first page
books = driver.find_elements(By.CLASS_NAME, "product_pod")

# Parse and print book details
for book in books:
    title = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
    price = book.find_element(By.CLASS_NAME, "price_color").text
    availability = book.find_element(By.CLASS_NAME, "availability").text.strip()
    
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Availability: {availability}")
    print("-" * 40)

# Cleanup
driver.quit()
