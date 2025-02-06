from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome
driver.maximize_window()
driver.get("https://www.globalsqa.com/testers-hub/")


