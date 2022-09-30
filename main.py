from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/tony/Documents/Development/chromedriver"

ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

big_cookie = driver.find_element(by="id", value="cookie")

#5 seconds after current time
upgrade_time = time.time() + 5

# 5 minutes after current time
stop_time = time.time() + 60*5

while True:
    big_cookie.click()
    if time.time() > upgrade_time:
        cookies = int(driver.find_element(by="id", value="money").text.replace(",", ""))
        all_upgrades = driver.find_elements(by="css selector", value="#store b")[0:-1]
        all_upgrades.reverse()
        for upgrade in all_upgrades:
            price = int(upgrade.text.split()[-1].replace(",", ""))
            if cookies > price:
                upgrade.click()
                break
        upgrade_time = time.time() + 5
    if time.time() > stop_time:
        break

cps = driver.find_element(by="id", value="cps").text
print(f"This is the total cps after the program has run: {cps}")
driver.close()


