import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
data = {'username': 'Admin', 'password': 'admin123'}
driver.get("https://opensource-demo.orangehrmlive.com/")

# login
driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys(data['username'])
driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys(data['password'])
driver.find_element(By.XPATH, "//input[@class='button']").click()
time.sleep(1)
# page - Employee list
pid_a_link = driver.find_element(By.XPATH, "//*[@id='mainMenuFirstLevelUnorderedList']/li[2]")
pid_a_link.click()
time.sleep(2)
# FIND 'testName testLastname'
driver.find_element(By.CSS_SELECTOR, 'input[id="empsearch_employee_name_empName"]').send_keys('testName testLastname')
driver.find_element(By.CSS_SELECTOR, 'input[id="searchBtn"]').click()
# press checkbox in table
checkbox_grid = driver.find_element(By.CSS_SELECTOR, 'input[id="ohrmList_chkSelectRecord_70"]')
checkbox_grid.click()
# press button 'Delete'
driver.find_element(By.ID, 'btnDelete').click()
# press button 'OK' in modal window
driver.find_element(By.ID, 'dialogDeleteBtn').click()
time.sleep(2)
driver.quit()
