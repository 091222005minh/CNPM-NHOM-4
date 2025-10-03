from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


driver.get(r"D:\lab08\login.html")

driver.find_element(By.ID, "username").send_keys("user")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)
assert "Login success!" in driver.find_element(By.ID, "message").text

driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "username").send_keys("abc")
driver.find_element(By.ID, "password").send_keys("wrong")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)
assert "Login failed!" in driver.find_element(By.ID, "message").text

driver.quit()
