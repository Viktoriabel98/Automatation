from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

firefox.get("http://uitestingplayground.com/classattr")

blue_button = firefox.find_element(
    By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
blue_button.click()
sleep(2)

firefox.switch_to.alert.accept()

firefox.quit()