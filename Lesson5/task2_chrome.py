from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

count = 0
chrome.get("http://uitestingplayground.com/dynamicid")

for button in range(3):
    blue_button = chrome.find_element(
        By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    count = count + 1

sleep(2)
print(count)