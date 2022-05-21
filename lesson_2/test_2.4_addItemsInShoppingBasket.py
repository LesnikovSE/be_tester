import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

data = {'username': 'standard_user', 'password': 'secret_sauce'}
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, 'user-name').send_keys(data['username'])
driver.find_element(By.ID, 'password').send_keys(data['password'])
driver.find_element(By.ID, 'login-button').click()
time.sleep(1)
# find all buttons 'Add to cart'
btnsAddToCart = driver.find_elements(By.CLASS_NAME, 'btn')
for i, btn in enumerate(btnsAddToCart):
    if i + 1 <= 3:
        btn.click()
    else:
        break
# click 'Basket'
btnBasket = driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link')
btnBasket.click()
time.sleep(1)
#
countItemsInBasket = driver.find_elements(By.CLASS_NAME, 'cart_item')
if len(countItemsInBasket) != 3:
    print("False")
else:
    print("True")

driver.quit()
