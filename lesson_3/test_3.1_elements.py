# 1. Откройте https://opensource-demo.orangehrmlive.com
# 2. Залогиньтесь и перейдите в PIM - > Employee List
# 3. Нажмите на имя любого сотрудника (произойдёт переход в его карточку с данными)
# 4. Добавьте проверку, что радиокнопка с противоположным полом сотрудника в данный момент недоступна для выбора
# 5. Добавьте проверку, что селектор Nationality в данный момент недоступен для выбора
# 6. В карточке сотрудника, нажмите на кнопку "Edit"
# 7. Измените пол сотрудника на противоположный
# 8. Добавьте проверку, что радиокнопка с полом сотрудника действительно выбрана
#     (атрибут появится после 12-го шага)
# 9. В селекторе Nationality выберите самую последнюю страну в списке
# 10. Добавьте проверку, что в селекторе Nationality выбрана последняя страна в списке
#     (атрибут появится после 12-го шага)
# 11. Выберите первоначальный пол сотрудника, а в селекторе Nationality выберите вариант "-- Select --"
# 12. Сохраните изменения, нажав на кнопку "Save"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
data = {'username': 'Admin', 'password': 'admin123'}
driver.get("https://opensource-demo.orangehrmlive.com/")

# 1
driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys(data['username'])
driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys(data['password'])

driver.find_element(By.XPATH, "//input[@class='button']").click()
# 2
driver.find_element(By.XPATH, "//*[@id='mainMenuFirstLevelUnorderedList']/li[2]").click()
time.sleep(1)
# 3
driver.find_element(By.CSS_SELECTOR, '#resultTable>tbody>tr:nth-child(3)>td:nth-child(3)>a').click()
time.sleep(1)
# 4
gender = driver.find_elements(By.CSS_SELECTOR, '[type="radio"]')
for i in gender:
    if i.get_attribute('disabled') is not None:
        print("-> <radio buttons 'Gender'> is disabled")
    else:
        print("<radio buttons 'Gender'> is active")
# 5
nationality = driver.find_element(By.ID, 'personal_cmbNation')
if nationality.get_attribute('disabled') is not None:
    print('<select "Nationality"> is disabled')
else:
    print('<select "Nationality"> is active')
# 6
btnEdit_personalData = driver.find_element(By.ID, 'btnSave')
btnEdit_personalData.click()
time.sleep(1)
# 7 - reverse radio button 'Gender'
gender_male = driver.find_element(By.ID, 'personal_optGender_1')
gender_female = driver.find_element(By.ID, 'personal_optGender_2')
# for step 11
gender_flag = int()
if gender_male.get_attribute('checked'):
    gender_flag = 1
    gender_female.click()
elif gender_female.get_attribute('checked'):
    gender_flag = 2
    gender_male.click()
else:
    print("<radio button 'Gender'> not checked")
# 8 setup defaul gender "male"
if gender_male.get_attribute('checked') and gender_female.get_attribute('checked') is None:
    gender_male.click()
# 9
cmb_nationality = Select(driver.find_element(By.ID, 'personal_cmbNation'))
cmb_nationality.select_by_index(len(cmb_nationality.options) - 1)
# 10
if cmb_nationality.first_selected_option.text == 'Zimbabwean':
    print('<select "Nationality"> last option selected')
# 11
if gender_flag in [1, 2]:
    if gender_flag == 1:
        gender_male.click()
    else:
        gender_female.click()
else:
    print('No gender selected. Set default gender - male')
    gender_male.click()
# 12
driver.find_element(By.ID, "btnSave").click()
#
time.sleep(10)
driver.quit()
