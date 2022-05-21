from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://practice.automationtesting.in/')
# Login
driver.find_element(By.CSS_SELECTOR, 'ul.main-nav>li:nth-child(2)>a').click()
driver.find_element(By.ID, 'username').send_keys('testLSE@yandex.ru')
driver.find_element(By.ID, 'password').send_keys('Qwertyuiop1234567890!@#$%^&*')
driver.find_element(By.CSS_SELECTOR, '[value="Login"]').click()
# Shop
driver.find_element(By.XPATH, '//*[contains(text(), "Shop")]').click()
# Open the book "HTML5 Forms"
driver.execute_script("arguments[0].scrollIntoView();",
                      driver.find_element(By.CSS_SELECTOR, '[href$="html5-forms/"]')
                      )
driver.find_element(By.CSS_SELECTOR, '[href$="html5-forms/"]').click()
#
title = driver.find_element(By.CSS_SELECTOR, '.product_title').text
assert "HTML5 Forms" == title
driver.quit()
