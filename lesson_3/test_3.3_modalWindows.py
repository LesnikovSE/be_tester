# 1  Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2  Перейдите на вкладку "SwitchTo" - > "Alerts"
#    - Здесь используйте клики(их будет 2) вместо выбора по селектору
#    - Если не получится перейти на вкладку Alerts, тогда откройте страницу http://demo.automationtesting.in/Alerts.html
#      и выполняйте задание начиная с 3-го шага
# 3  Нажмите на кнопку "click the button to display an alert box:" # перед нажатием добавьте паузу
# 4  Выведите в консоль содержимое окна alert и нажмите "OK"
#    Дополнительно(если получится):
#    добавьте тест, что содержимое равно тексту "I am an alert box!" , а если не равно,
#    тогда в консоли выводится сообщение об ошибке
# 5  Получите адрес текущей ссылки
# 6  Откройте новую вкладку в браузере, введите ссылку из предыдущего шагаи перейдите по ней
#    (перед открытием добавьте паузу)
# 7  Нажмите на "Alert with OK & Cancel" -> "click the button to display a confirm box" # перед нажатием добавьте паузу
# 8  В модальном окне нажмите "Отмена"
# 9  Откройте новую вкладку в браузере, введите ссылку из шага 5 и перейдите по ней
#     (перед открытием добавьте паузу)
# 10 Нажмите на "Alert with Textbox"-> "click the button to demonstrate the prompt box"
#    (перед нажатием добавьте паузу)
# 11 В модальном окне, введите текст: "Ура! Задание выполнено!" и нажмите "OK"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
# 1
driver.get('http://demo.automationtesting.in/Register.html')

# 2 - click to 'Switch to -> Alerts'
driver.find_element(By.CSS_SELECTOR, 'a[href^="SwitchTo"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[href^="Alerts"]').click()

# 3 - click the button to display an alert box
driver.find_element(By.ID, 'OKTab').click()
# 4 - Print the contents of the window to the console
alert = driver.switch_to.alert
print(alert.text)
assert 'I am an alert box!' in alert.text
alert.accept()
time.sleep(1)
# 5 - Get the address of the current link
current_link = driver.current_url
# 6 - Open a new browser tab
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(current_link)
time.sleep(2)
# 7 - click to "Alert with OK & Cancel " -> "click the button to display a confirm box "
driver.find_element(By.XPATH, '//a[text()="Alert with OK & Cancel "]').click()
driver.find_element(By.XPATH, '//button[text()="click the button to display a confirm box "]').click()
# 8 -
modalWindow = driver.switch_to.alert
modalWindow.dismiss()
time.sleep(1)
# 9 - open new window and use 'current_url'
driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[2])
driver.get(current_link)
time.sleep(1)
# 10 -
driver.find_element(By.XPATH, '//a[text()="Alert with Textbox "]').click()
driver.find_element(By.XPATH, '//button[text()="click the button to demonstrate the prompt box "]').click()
# 11 -
modalWindow = driver.switch_to.alert
modalWindow.send_keys('Ура! Задание выполнено!')
modalWindow.accept()

time.sleep(2)
driver.quit()
