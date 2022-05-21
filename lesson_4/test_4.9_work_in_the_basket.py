#  1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
#  2. Нажмите на вкладку "Shop"
#  3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
#     • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
#     • После добавления 1-й книги добавьте sleep
#  4. Перейдите в корзину
#  5. Удалите первую книгу
#     • Перед удалением добавьте sleep
#  6. Нажмите на Undo (отмена удаления)
#  7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
#     • Предварительно очистите поле с помощью локатор_поля.clear()
#  8. Нажмите на кнопку "UPDATE BASKET"
#  9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
#     используйте assert
# 10. Нажмите на кнопку "APPLY COUPON"
#     • Перед нажатимем добавьте sleep
# 11. -Добавьте тест, что возникло сообщение: "Please enter a coupon code."

import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('http://practice.automationtesting.in/')
# Click Shop
driver.find_element(By.CSS_SELECTOR, '[href$="shop/"]').click()
# Add books HTML5 WEB.. and JS..
driver.find_element(By.CSS_SELECTOR, '[href="/shop/?add-to-cart=182"]').click()
time.sleep(1)
driver.execute_script("arguments[0].scrollIntoView();",
                      driver.find_element(By.XPATH, '//a[@data-product_id="180"]'))
driver.find_element(By.XPATH, '//a[@data-product_id="180"]').click()
# Start shoping
driver.find_element(By.CSS_SELECTOR, '.wpmenucart-contents').click()
# Delete first item
time.sleep(2)
driver.find_element(By.XPATH, '//tbody/tr[1]/td[1]/a').click()
# Click Undo
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.woocommerce-message>a'))
)
driver.find_element(By.CSS_SELECTOR, '.woocommerce-message>a').click()
time.sleep(1)
# QTY

driver.find_element(By.XPATH, '//tbody/tr[2]/td[5]/div/input').click()
driver.find_element(By.XPATH, '//tbody/tr[2]/td[5]/div/input').send_keys(Keys.UP, Keys.UP)
driver.find_element(By.XPATH, '//input[@name="update_cart"]').click()
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr[2]/td[5]/div/input'))
)
assert '3' == driver.find_element(By.XPATH, '//tbody/tr[2]/td[5]/div/input').get_attribute('value')
# Apply coupon
time.sleep(1)
driver.find_element(By.XPATH, '//input[@name="apply_coupon"]').click()
#
assert True is driver.find_element(By.CSS_SELECTOR, '.woocommerce-error').is_displayed()

driver.quit()
