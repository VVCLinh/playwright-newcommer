from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import yaml


def openandwaitforpageload(url):
    global driver
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    print("Browser opened successfully")
    return driver


def clickElementByXpath(element_id):
    try:
        element = driver.find_element(By.XPATH, element_id)
        element.click()
        print(f"Clicked element with Xpath: {element_id}")
    except Exception as e:
        print(f"Element with ID {element_id} doesnt exist: {e}")


def closeBroserSession():
    if driver:
        time.sleep(5)
        driver.quit()
        print("Closed browser")


def inputValue(element, value):
    try:
        field = driver.find_element(By.XPATH, element)
        field.send_keys(value)
        print(f"Input value {value}")
    except Exception as e:
        print("Cant find element")


def loadyamlfile(yml_file):
    with open(yml_file, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validatetextinpage(text):
    if text in driver.page_source:
        print(f"✅ Text '{text}' is visible in page.")
    else:
        raise Exception(f"❌ Text '{text}' NOT found in page!")


def checkelementvisible(locator_value):
    try:
        element = driver.find_element(By.XPATH, locator_value)
        print("Element is visible in page")
        return element.is_displayed()
    except:
        print("Element is invisible in page")
        return False