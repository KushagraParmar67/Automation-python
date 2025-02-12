import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv

load_dotenv()

SF_LOGIN_URL=os.getenv("SF_LOGIN_URL")
SF_DFS_USERNAME=os.getenv("SF_DFS_USERNAME")
SF_DFS_PASSWORD=os.getenv("SF_DFS_PASSWORD")
SF_CUSTOMER_NAME=os.getenv("SF_CUSTOMER_NAME")
SF_CUSTOMER_LANGUAGE=os.getenv("SF_CUSTOMER_LANGUAGE")

def create_driver(headless=False):
    os.environ["WDM_ARCH"] = "arm64"
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def login_to_salesforce(driver, username, password):
    driver.get(SF_LOGIN_URL)
    driver.find_element(By.ID, "username").send_keys(SF_DFS_USERNAME)
    driver.find_element(By.ID, "password").send_keys(SF_DFS_PASSWORD)
    driver.find_element(By.ID, "Login").click()
    print(f"Logged into Salesforce successfully as a {username}")
    time.sleep(3)
    return True

def lead_to_opportunity():
    driver = create_driver()

    if login_to_salesforce(driver,SF_DFS_USERNAME, SF_DFS_PASSWORD):
        driver.find_element(By.ID, "phSearchInput").click()
        driver.find_element(By.ID, "phSearchInput").send_keys(SF_CUSTOMER_NAME)
        time.sleep(3)
        driver.find_element(By.ID, "phSearchButton").click()
        driver.find_element(By.LINK_TEXT, SF_CUSTOMER_NAME).click()
        element = driver.find_element(By.ID, "lP:formId:editPb:cloneButtons")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        driver.find_element(By.ID, "lP:formId:editPb:editButtons").click()
        driver.find_element(By.ID, "lP:formId:editPb:j_id356").click()
        dropdown = driver.find_element(By.ID, "lP:formId:editPb:j_id124")
        dropdown.find_element(By.XPATH, f"//option[. = '{SF_CUSTOMER_LANGUAGE}']").click()
        dropdown = driver.find_element(By.ID, "lP:formId:editPb:j_id356")
        dropdown.find_element(By.XPATH, "//option[. = 'Is titleholder']").click()
        driver.find_element(By.ID, "lP:formId:editPb:j_id362").click()
        dropdown = driver.find_element(By.ID, "lP:formId:editPb:j_id362")
        dropdown.find_element(By.XPATH, "//option[. = 'Own']").click()
        driver.find_element(By.ID, "lP:formId:editPb:j_id383").click()
        dropdown = driver.find_element(By.ID, "lP:formId:editPb:j_id378")
        dropdown.find_element(By.XPATH, "//option[. = 'Comp Shingle']").click()
        dropdown = driver.find_element(By.ID, "lP:formId:editPb:j_id383")
        dropdown.find_element(By.XPATH, "//option[. = 'Normal']").click()
        driver.find_element(By.ID, "lP:formId:editPb:j_id388").click()
        dropdown = driver.find_element(By.ID, "lP:formId:editPb:j_id388")
        dropdown.find_element(By.XPATH, "//option[. = 'Acceptable']").click()
        driver.find_element(By.ID, "lP:formId:editPb:j_id398").click()
        dropdown = driver.find_element(By.ID, "lP:formId:editPb:j_id398")
        dropdown.find_element(By.XPATH, "//option[. = 'Pass - enough space']").click()
        driver.find_element(By.ID, "lP:formId:editPb:j_id393").click()
        dropdown = driver.find_element(By.ID, "lP:formId:editPb:j_id393")
        dropdown.find_element(By.XPATH, "//option[. = 'None']").click()
        driver.find_element(By.ID, "lP:formId:editPb:j_id433").click()
        dropdown = driver.find_element(By.ID, "lP:formId:editPb:j_id433")
        dropdown.find_element(By.XPATH, "//option[. = '$101-150']").click()
        driver.find_element(By.ID, "lP:formId:editPb:j_id505").click()
        dropdown = driver.find_element(By.ID, "lP:formId:editPb:j_id505")
        dropdown.find_element(By.XPATH, "//option[. = 'Above 650']").click()
        driver.find_element(By.ID, "lP:formId:editPb:j_id510").click()
        dropdown = driver.find_element(By.ID, "lP:formId:editPb:j_id510")
        dropdown.find_element(By.XPATH, "//option[. = 'Yes']").click()
        driver.find_element(By.ID, "lP:formId:saveButtonbo").click()
        time.sleep(10)
        driver.find_element(By.ID, "lP:formId:editPb:convertButtons").click()
        time.sleep(10)
        driver.quit()

lead_to_opportunity()
