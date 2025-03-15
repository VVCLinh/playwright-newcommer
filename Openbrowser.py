from selenium import webdriver
import time


def openandwaitforpageload(pageurl):
    global driver
    # Set up WebDriver
    driver = webdriver.Chrome()
    driver.get(pageurl)
    driver.maximize_window()
    print("Opening browser")
    time.sleep(5)


def closeBroserSession():
    if driver:
        time.sleep(5)
        driver.quit()
        print("Closed browser")


openandwaitforpageload("http://11.11.7.241:3001/")
