from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
from dotenv import load_dotenv
import argparse
import json
from utils import insert_into_db_olt_customer_mac

load_dotenv()

target_ip = os.getenv("TARGET_IP")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_sid = os.getenv("DB_SID")


if not target_ip or not db_host or not db_user or not db_pass or not db_sid:
    raise ValueError("Please set TARGET_IP, DB_HOST, DB_USER, DB_PASS, and DB_SID in the .env file.")

def scrape_onu_data(target_ip):
    # Initialize driver
    driver = webdriver.Firefox(executable_path='/home/maestro/bin/geckodriver')

    try:
        driver.get(f"http://{target_ip}/#/login")
        wait = WebDriverWait(driver, 20)

        # Step 1: Login
        username = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
        password = driver.find_element(By.XPATH, "//input[@type='password']")
        username.send_keys("root")
        password.send_keys("admin")
        password.send_keys(Keys.RETURN)

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
        onu_mac_link.click()

        # Step 4: Wait for MAC Information Table to load
        table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".el-table")))

        # Initialize list to store all data
        all_data = []

        # Set the initial current page variable
        current_page = 1

        # Pagination handling
        while True:
            # Check if the current page is the active page
            pager = driver.find_element(By.CSS_SELECTOR, ".el-pager")
            page_items = pager.find_elements(By.CSS_SELECTOR, "li.number")
            active_page = next((item.text for item in page_items if 'active' in item.get_attribute('class')), None)

            # If the active page matches the current page, continue scraping
            if active_page == str(current_page):
                # Scrape current page data
                rows = table.find_elements(By.CSS_SELECTOR, ".el-table__body tr")
                columns = [header.text for header in table.find_elements(By.CSS_SELECTOR, ".el-table__header th")]
                
                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    data = [col.text for col in cols]
                    raw = dict(zip(columns, data))

                    # Construct final cleaned data
                    cleaned = {
                        "OLT_ID": None,
                        "MAC": raw.get("MAC"),
                        "VLAN": raw.get("VLAN"),
                        "Port": f"{raw.get('Port').replace(' ', '')}/{raw.get('ONU')}",
                    }
                    all_data.append(cleaned)

                # Step 5: Find the pagination bar (ul with class "el-pager")
                pager = driver.find_element(By.CSS_SELECTOR, ".el-pager")
                page_items = pager.find_elements(By.CSS_SELECTOR, "li.number")
                
                # Get the total number of pages (the highest page number)
                max_page = max([int(item.text) for item in page_items])
                
                # If we are on the last page, break the loop
                if current_page == max_page:
                    break

                # Step 6: Scroll to the "Next" button and click it
                next_button = driver.find_element(By.CSS_SELECTOR, ".btn-next")
                driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                
                # Wait for the next button to be clickable and click it
                next_button.click()

                # Wait for the page content to load after clicking "Next"
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".el-table__body tr")))

                # Increase the current page counter after clicking next
                current_page += 1
            else:
                # If the active page doesn't match the current page, wait and retry
                print(f"Waiting for page {current_page} to load...")
                wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".el-pager li.active"), str(current_page)))

        # Save the data to a JSON file
        with open('scraper_output.json', 'w') as f:
            json.dump(all_data, f, indent=4)
            print(f"{len(all_data)} Data saved to scraper_output.json")
            

    finally:
        driver.quit()
        return all_data
        
def main():
    parser = argparse.ArgumentParser(description='Process ONU data from SNMP output and insert into database')
    parser.add_argument('-d', '--dry-run', action='store_true', help='Parse data but do not insert into database')
    args = parser.parse_args()
    
    # Scrape ONU data
    print("Scraping ONU data...")
    onu_data = scrape_onu_data(target_ip)
    print(f"Scraped {len(onu_data)} ONU devices from the web interface.")
    
    
    # Insert into database
    if not args.dry_run:
        print("Inserting data into database...")
        insert_into_db_olt_customer_mac(onu_data, target_ip, db_host, db_port, db_user, db_pass, db_sid)

if __name__ == "__main__":
    main()