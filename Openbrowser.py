from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def openandwaitforpageload(pageurl, element):
    global driver
    # Set up WebDriver
    driver = webdriver.Chrome()
    driver.get(pageurl)
    driver.maximize_window()
    print("Opening browser")
    time.sleep(5)
    element = driver.find_element(By.XPATH, element)
    element.click()


def clickElementById(element_id):
    try:
        element = driver.find_element(By.XPATH, element_id)
        element.click()
        print(f"Clicked element with ID: {element_id}")
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
