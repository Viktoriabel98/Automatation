from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

count = 0
firefox.get("http://uitestingplayground.com/dynamicid")

for button in range(3):
    blue_button = firefox.find_element(
        By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    count = count + 1

print(count)
sleep(2)
firefox.quit()