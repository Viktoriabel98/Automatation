from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox = webdriver.Firefox()

firefox.get("http://the-internet.herokuapp.com/entry_ad")

wait = WebDriverWait(firefox, timeout=2)
close_button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, ".modal-footer")))
sleep(5)
close_button.click()
sleep(3)

firefox.quit()