# 1 Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2 Реализуйте неявное ожидание поиска элементов
# 3 Перейдите в раздел "More" -> "Dynamic Data"
#   • Здесь и в дальнейших заданиях используйте клики(их будет 2) вместо выбора по селектору
# 4 Добавьте проверку, что заголовок окна равен "Loading the data Dynamically"
# 5 Нажмите на кнопку "Get Dynamic Data"
# 6 Выведите в консоли адрес ссылки, которая сгенерируется в теге img
#   (похожий на: https://randomuser.me/api/portraits/...)
#   • Чтобы это сделать, используйте метод .get_attribute("атрибут")
#   • Если адрес ссылки сильно отличается от примера в шаге 6, тогда после нажатия
#     на кнопку из шага 5 добавьте паузу time.sleep(3)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# 1
driver.get('http://demo.automationtesting.in/WebTable.html')
# 2
driver.implicitly_wait(5)
# 3
driver.find_element(By.CSS_SELECTOR, 'a[href^="#"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[href^="DynamicData"]').click()
# 4
title_page = driver.find_element(By.CSS_SELECTOR, '.cont_box_center>h3')
assert "Loading the data Dynamically" in title_page.text
# 5
driver.find_element(By.ID, 'save').click()
# 6
time.sleep(2)
img = driver.find_element(By.CSS_SELECTOR, '[id="loading"]>img')
print(img.get_attribute('src'))

print("test passed successfully")
driver.quit()
