from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def openandwaitforpageload(pageurl):
    global driver
    # Set up WebDriver
    driver = webdriver.Chrome()
    driver.get(pageurl)
    driver.maximize_window()
    print("Opening browser")
    time.sleep(5)
    element = driver.find_element(By.XPATH, '//*[@id="VIP_BUNDLE"]/div[2]/div/picture[1]/img')
    element.click()

def clickElementById(driver, element_id):
    try:
        element = driver.find_element(By.ID, element_id)
        element.click()
        print(f"Clicked element with ID: {element_id}")
    except Exception as e:
        print(f"Element with ID {element_id} doesnt exist: {e}")

def closeBroserSession():
    if driver:
        time.sleep(5)
        driver.quit()
        print("Closed browser")

