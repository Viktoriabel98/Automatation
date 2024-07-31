from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()
firefox.get("https://the-internet.herokuapp.com/login")

username_field = firefox.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
sleep(1)

password_field = firefox.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")
sleep(1)

button_login = firefox.find_element(By.TAG_NAME, "button").click()
sleep(2)

firefox.quit()