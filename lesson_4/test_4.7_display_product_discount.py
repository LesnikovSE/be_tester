import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = Chrome()
# driver.maximize_window()
driver.implicitly_wait(3)
driver.get('http://practice.automationtesting.in/')
# Login
driver.find_element(By.CSS_SELECTOR, 'ul.main-nav>li:nth-child(2)>a').click()
driver.find_element(By.ID, 'username').send_keys('testLSE@yandex.ru')
driver.find_element(By.ID, 'password').send_keys('Qwertyuiop1234567890!@#$%^&*')
driver.find_element(By.CSS_SELECTOR, '[value="Login"]').click()
# Shop
driver.find_element(By.CSS_SELECTOR, '[href$="shop/"]').click()
# Open the book
driver.find_element(By.CSS_SELECTOR, '[href$="android-quick-start-guide/"]').click()
# Test old price
price_old = driver.find_element(By.CSS_SELECTOR, '.price>del>span').text
assert '₹600.00' == price_old
# Test new price
price_old = driver.find_element(By.CSS_SELECTOR, '.price>ins').text
assert '₹450.00' == price_old
# Click on book cover
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '[itemprop="image"]').click()
# Explicit wait and close menu
WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.pp_pic_holder.pp_woocommerce'))
)
driver.quit()
