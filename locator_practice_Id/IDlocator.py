import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.ID,"firstname").send_keys("test")
driver.find_element(By.ID,"male").click()
driver.find_element(By.ID,'admorepass').click()
#driver.find_element(By.ID,'oneway').click()

driver.find_element(By.CSS_SELECTOR,'#oneway').click()
driver.find_element(By.CSS_SELECTOR,'#birthday').send_keys("07")
driver.find_element(By.CSS_SELECTOR,'#eamil').click()


time.sleep(5)
driver.close()