import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME,"visadate").click()
driver.find_element(By.NAME,"firstname").send_keys("hello")
time.sleep(5)
driver.close()