from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://practice.automationtesting.in/')

driver.find_element(By.CSS_SELECTOR, 'ul.main-nav>li:nth-child(2)>a').click()
driver.find_element(By.ID, 'username').send_keys('testLSE@yandex.ru')
driver.find_element(By.ID, 'password').send_keys('Qwertyuiop1234567890!@#$%^&*')
driver.find_element(By.CSS_SELECTOR, '[value="Login"]').click()

WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Logout")]'))
)
driver.quit()
