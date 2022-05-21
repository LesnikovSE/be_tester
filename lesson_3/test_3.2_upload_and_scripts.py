#   Настройте открытие окон в полный размер, с помощью команды из предыдущего урока: driver.maximize_window()
# 1 Откройте страницу http://demo.automationtesting.in/Register.html
# 2 Заполните произвольными данными только обязательные поля(*) в регистрации(а так же поля:
#   - Date of Birth, Password, Confirm Password)
#   - Поле телефон должно содержать: 10 цифр, без +, например: 1234567890;
#     если номер уже существует в системе – появится ошибка
#   - Значение в селекторе country, date of birth выбирайте с помощью класса Select из библиотеки WebDriver
#   - Если будет отображаться селектор "country", состоящий из 1-го варианта, тогда его можно не заполнять,
#     и также можно пропустить 7-й пункт этого задания
#   - Поля password, confirm password должны содержать: не менее 6 символов,
#     маленькую букву, большую букву, цифру
# 4 Загрузите любой файл в раздел "Photo" вверху справа
# 5 Проскролльте страницу вниз на 300 пикселей
# 6 Нажмите на кнопку Submit # если будет селектор "country", состоящий из 1-го варианта,
#   тогда кнопка не нажмется, в таком варианте будет окей. Просто добавьте код для её нажатия.
# 7 Добавьте проверку, что произошёл переход на страницу: http://demo.automationtesting.in/WebTable.html
#   Дополнительно:
#   улучшите проверку таким образом, чтобы в консоли выводилось содержательное
#   сообщение, из которого можно понять, на какой странице находимся сейчас
#   и на какой странице ожидаем находиться.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('http://demo.automationtesting.in/Register.html')

image = r'C:\Users\GM\PycharmProjects\BeTesterAutomotion\lesson_3\loadImage.jpg'
driver.find_element(By.ID, 'imagesrc').send_keys(image)
driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').send_keys('testFirstName')
driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]').send_keys('testLastName')
driver.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys('testEmail@mail.com')
driver.find_element(By.CSS_SELECTOR, '[ng-model="Phone"]').send_keys('9860000000')
driver.find_element(By.CSS_SELECTOR, '[value="Male"]').click()

driver.execute_script("return arguments[0].scrollIntoView(true);", driver.find_element(By.ID, 'country'))

Select(driver.find_element(By.ID, 'country')).select_by_index(7)
Select(driver.find_element(By.ID, 'yearbox')).select_by_value('2000')
Select(driver.find_element(By.CSS_SELECTOR, '[placeholder="Month"]')).select_by_value('January')
Select(driver.find_element(By.ID, 'daybox')).select_by_value('20')

password_first = driver.find_element(By.ID, 'firstpassword')
password_first.click()
password_first.send_keys('Qqq111qqQ')
driver.find_element(By.ID, 'secondpassword').send_keys('Qqq111qqQ')

driver.find_element(By.ID, 'submitbtn').click()
time.sleep(3)

print('Страница на которой находимся -', driver.current_url)
print('Страница где должны нахождиться -', "http://demo.automationtesting.in/WebTable.html")
driver.quit()
