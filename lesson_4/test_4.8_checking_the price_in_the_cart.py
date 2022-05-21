from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('http://practice.automationtesting.in/')
# Login
driver.find_element(By.CSS_SELECTOR, 'ul.main-nav>li:nth-child(2)>a').click()
driver.find_element(By.ID, 'username').send_keys('testLSE@yandex.ru')
driver.find_element(By.ID, 'password').send_keys('Qwertyuiop1234567890!@#$%^&*')
driver.find_element(By.CSS_SELECTOR, '[value="Login"]').click()
# Shop
driver.find_element(By.CSS_SELECTOR, '[href$="shop/"]').click()
# Add book to basket
driver.find_element(By.CSS_SELECTOR, '[href="/shop/?add-to-cart=182"]').click()
# Check
assert "1 Item"  == driver.find_element(By.XPATH, '//span[@class="cartcontents"]').text
assert "₹180.00" == driver.find_element(By.XPATH, '//span[@class="amount"]').text
# Click basket
driver.find_element(By.CSS_SELECTOR, '[title="View your shopping cart"]').click()
# Subtotal and Total price displayed
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//tr[@class="cart-subtotal"]/td/span'))
)
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//td[1][@data-title="Total"]'))
)

driver.quit()
