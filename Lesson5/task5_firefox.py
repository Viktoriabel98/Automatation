from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firefox = webdriver.Firefox()
firefox.get("https://the-internet.herokuapp.com/inputs")

search_input = firefox.find_element(By.TAG_NAME, "input")
search_input.send_keys("1000", Keys.RETURN)
sleep(2)
search_input.clear()
sleep(2)
search_input.send_keys("999", Keys.RETURN)
sleep(2)

firefox.quit()