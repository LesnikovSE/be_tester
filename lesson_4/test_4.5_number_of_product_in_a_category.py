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
# click menu "HTML"
driver.find_element(By.XPATH, '//a[contains(text(), "HTML")]').click()
#
amount_product = driver.find_elements(By.CSS_SELECTOR, '.products.masonry-done li')
assert 3 == len(amount_product)
#
driver.quit()
