import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

data = {'username': 'Admin', 'password': 'admin123'}

driver.get("https://opensource-demo.orangehrmlive.com/")

username = driver.find_element(By.XPATH, "//input[@id='txtUsername']")
username.send_keys(data['username'])

password = driver.find_element(By.XPATH, "//input[@id='txtPassword']")
password.send_keys(data['password'])

time.sleep(1)

submit_button = driver.find_element(By.XPATH, "//input[@class='button']")
submit_button.click()

print("Test True")
driver.quit()
