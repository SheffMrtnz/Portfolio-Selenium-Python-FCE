from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.get("https://youtube.com")

wait = WebDriverWait(driver, 15)

search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
search_box.send_keys("Facturacion electronica ARCA" + Keys.ENTER)

first_video = wait.until(EC.element_to_be_clickable((By.ID, "video-title")))
first_video.click()

time.sleep(245)
