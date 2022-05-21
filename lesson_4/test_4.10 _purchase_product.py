#     В этом тесте логиниться не нужно
#  1. Откройте http://practice.automationtesting.in/
#  2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
#  3. Добавьте в корзину книгу "HTML5 WebApp Development"
#  4. Перейдите в корзину
#  5. Нажмите "PROCEED TO CHECKOUT"
#     • Перед нажатием, добавьте явное ожидание
#  6. Заполните все обязательные поля
#     • Перед заполнением first name, добавьте явное ожидание
#     • Для заполнения country нужно: нажать на селектор - >
#       ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
#     • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите
#       на неё, затем на вариант в списке ниже
#  7. Выберите способ оплаты "Check Payments"
#     • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
#  8. Нажмите PLACE ORDER
#  9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"

import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

driver = Chrome()
# driver.maximize_window()
driver.implicitly_wait(3)
driver.get('http://practice.automationtesting.in/')
# Click Shop and scroll 300px down
driver.find_element(By.CSS_SELECTOR, '[href$="shop/"]').click()
driver.execute_script("window.scrollTo(0, 300)")
# Add book "HTML5 ..."
# driver.execute_script('arguments[0].scrollIntoView();',
#                       driver.find_element(By.XPATH, '//a[@data-product_id="182"]'))
driver.find_element(By.XPATH, '//a[@data-product_id="182"]').click()
time.sleep(1)
# Click basket
driver.find_element(By.CSS_SELECTOR, '[title="View your shopping cart"]').click()
# Click "Proceed checkout"
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.wc-proceed-to-checkout>a'))
)
driver.find_element(By.CSS_SELECTOR, '.wc-proceed-to-checkout>a').click()
# Fill in all required fields
driver.find_element(By.ID, 'billing_first_name').send_keys('test_name')
driver.find_element(By.ID, 'billing_last_name').send_keys('test_lastname')
driver.find_element(By.ID, 'billing_email').send_keys('test@mail.com')
driver.find_element(By.ID, 'billing_phone').send_keys('79860000000')
Select(driver.find_element(By.ID, 'billing_country')).select_by_value('RU')
driver.execute_script('arguments[0].scrollIntoView();',
                      driver.find_element(By.ID, 'billing_address_1'))
driver.find_element(By.ID, 'billing_address_1').send_keys('Russia')
driver.find_element(By.ID, 'billing_city').send_keys('test_City')
driver.find_element(By.ID, 'billing_state').send_keys('MO')
driver.find_element(By.ID, 'billing_postcode').send_keys('111111')
# Click Check payment
driver.find_element(By.ID, 'payment_method_cheque').click()
# Click Place order
driver.find_element(By.ID, 'place_order').click()
#
time.sleep(2)
# assert driver.find_element(By.XPATH, '//tfoot/tr[3]/td').text == 'Check Payments'
WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.XPATH, '//tfoot/tr[3]/td'), 'Check Payments')
)

driver.quit()
