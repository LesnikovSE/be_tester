#  1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
#  2. Реализуйте неявное ожидание поиска элементов
#  3. Перейдите в раздел "Switch to" - "Windows"
#  4. В разделе "Open New Tabbed Windows" нажмите кнопку "click"
#  5. Переключите драйвер на вторую вкладку - закройте её - переключитесь обратно на первую вкладку
#     - Чтобы закрыть вкладку: driver.close()
#  6. Перейдите в раздел "Separate Multiple Windows" и нажмите "click"
#  7. Переключите драйвер на вторую вкладку:
#     - здесь нужно будет использовать handles[2], тк ранее закрытая вкладка с шага 4 останется в памяти
#  8. Используя явное ожидание(EC) - проверьте что ссылка = "http://demo.automationtesting.in/Index.html"
#  9. Используя явное ожидание(EC) - проверьте что в браузере открыто 3 вкладки,
#     выведите в консоли результат проверки (True/False)
# 10. В поле "email" напишите любую почту и нажмите на кнопку в виде ">" справа от поля
# 11. Используя явное ожидание(EC), проверьте что ссылка = "http://demo.automationtesting.in/Register.html"
#     - Дополнительно (необязательно): для всех EC, вынесите часть проверки в переменную
#     (как на последнем слайде перед практикой)

import time
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
# 1
driver.get('http://demo.automationtesting.in/WebTable.html')
# 2
driver.implicitly_wait(3)
# 3
driver.find_element(By.CSS_SELECTOR, 'a[href^="SwitchTo"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[href^="Windows"]').click()
# 4
driver.find_element(By.CSS_SELECTOR, '.btn.btn-info').click()
# 5
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
# 6
driver.find_element(By.CSS_SELECTOR, '[href^="#Multiple"]').click()
time.sleep(1)
WebDriverWait(driver, 2).until(
    ec.element_to_be_clickable((By.XPATH, '//div/div[3]/button'))
    )
driver.find_element(By.XPATH, '//div/div[3]/button').click()
# 7
driver.switch_to.window(driver.window_handles[2])
# 8
url = r'http://demo.automationtesting.in/Index.html'
assert 'http://demo.automationtesting.in/Index.html' == driver.current_url
# WebDriverWait(driver, 3).until(ec.url_changes(url)
# 9
print("True" if WebDriverWait(driver, 1).until(ec.number_of_windows_to_be(3)) else "False")
# 10
driver.find_element(By.ID, 'email').send_keys('testMail@mail.com')
# driver.find_element(By.ID, 'logo').click()
driver.find_element(By.XPATH, '//span/a[@href="Register.html"]/img').click()
# 11
assert 'http://demo.automationtesting.in/Register.html' == driver.current_url

print("test passed successfully")
driver.quit()
