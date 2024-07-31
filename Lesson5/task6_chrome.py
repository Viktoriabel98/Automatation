from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

chrome.get("https://the-internet.herokuapp.com/login")

username_field = chrome.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
sleep(1)

password_field = chrome.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")
sleep(1)

button_login = chrome.find_element(By.TAG_NAME, "button").click()
sleep(2)