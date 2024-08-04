from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

chrome.get("https://the-internet.herokuapp.com/inputs")

search_input = chrome.find_element(By.TAG_NAME, "input")
search_input.send_keys("1000", Keys.RETURN)
sleep(2)
search_input.clear()
sleep(2)
search_input.send_keys("999", Keys.RETURN)
sleep(2)