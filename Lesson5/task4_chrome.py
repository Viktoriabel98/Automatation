from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

chrome.get("http://the-internet.herokuapp.com/entry_ad")

wait = WebDriverWait(chrome, timeout=5)
close_button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, ".modal-footer")))
sleep(5)
close_button.click()
sleep(3)