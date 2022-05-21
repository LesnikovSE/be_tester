import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://practice.automationtesting.in/')

driver.execute_script("arguments[0].scrollIntoView();",
                      driver.find_element(By.XPATH, '//a[@data-product_id="160"]'))
driver.find_element(By.XPATH, '//a[@data-product_id="160"]').click()
driver.find_element(By.CSS_SELECTOR, '[href^="#tab-reviews"]').click()

driver.find_element(By.CSS_SELECTOR, '.star-5').click()
time.sleep(2)
driver.find_element(By.ID, 'comment').send_keys('Nice book!')

driver.execute_script("arguments[0].scrollIntoView();",
                      driver.find_element(By.ID, 'author'))
driver.find_element(By.ID, 'author').send_keys('test_author')
driver.find_element(By.ID, 'email').send_keys('test_email@mail.com')
driver.find_element(By.ID, 'submit').click()

driver.quit()
