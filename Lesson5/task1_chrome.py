from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
for button in range(5):
    search_button = chrome.find_element(
        By.XPATH, '//button[text()="Add Element"]').click()
sleep(2)

delete_button = chrome.find_elements(By.XPATH, '//button[text()="Delete"]')

print(f"Размер списка: {len(delete_button)}")