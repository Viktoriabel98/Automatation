from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()
firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")

for button in range(5):
    search_button = firefox.find_element(
        By.XPATH, '//button[text()="Add Element"]').click()
sleep(2)

delete_button = firefox.find_elements(By.XPATH, '//button[text()="Delete"]')

print(f"Размер списка: {len(delete_button)}")