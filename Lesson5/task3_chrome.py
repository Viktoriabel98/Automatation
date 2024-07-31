from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

chrome.get("http://uitestingplayground.com/classattr")

blue_button = chrome.find_element(
    By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
blue_button.click()
sleep(2)

chrome.switch_to.alert.accept()