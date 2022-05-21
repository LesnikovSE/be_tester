import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.implicitly_wait(5)
driver.get('http://practice.automationtesting.in/')

driver.find_element(By.CSS_SELECTOR, 'ul.main-nav>li:nth-child(2)>a').click()

username = driver.find_element(By.ID, 'reg_email')
username.send_keys('testLSE@yandex.ru')
password = driver.find_element(By.ID, 'reg_password')
for i in 'Qwertyuiop1234567890!@#$%^&*':
    password.send_keys(i)
    time.sleep(0.05)
driver.find_element(By.CSS_SELECTOR, '[value="Register"]').click()

driver.quit()
