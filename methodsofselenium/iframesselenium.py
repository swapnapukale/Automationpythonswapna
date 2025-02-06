from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
print(driver.get_window_size())


iframe_element = driver.find_element(By.XPATH, "//iframe[@name='globalSqa']")

driver.switch_to.frame(iframe_element)

driver.find_element(By.ID,"mobile_menu_toggler").click()
driver.switch_to.default_content()
page_heading = driver.find_element(By.XPATH,"//div[@class = 'page_heading']").text
print(page_heading)

driver.find_element(By.XPATH, "//li[text()='Open New Tab']").click()
click_here_element = driver.find_element(By.XPATH, "//a[text()='Click Here']")



click_here_element.screenshot("click_here_element.png")

# take screenshot of active page.
driver.save_screenshot("iframe_testing_page.png")

click_here_element.click()


time.sleep(5)