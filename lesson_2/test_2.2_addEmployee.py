import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

data = {'username': 'Admin', 'password': 'admin123'}

driver.get("https://opensource-demo.orangehrmlive.com/")

# login
try:
    username = driver.find_element(By.XPATH, "//input[@id='txtUsername']")
    username.send_keys(data['username'])
    password = driver.find_element(By.XPATH, "//input[@id='txtPassword']")
    password.send_keys(data['password'])
    submit_button = driver.find_element(By.XPATH, "//input[@class='button']")
    submit_button.click()
except Exception as ex:
    print(ex)
time.sleep(1)

# page - Employee list
try:
    pid_a_link = driver.find_element(By.XPATH, "//*[@id='mainMenuFirstLevelUnorderedList']/li[2]")
    pid_a_link.click()
except:
    print('Employee list')
time.sleep(2)

# page - Add Employee
try:
    btn_add = driver.find_element(By.ID, 'btnAdd')
    btn_add.click()
except:
    print('Add Employee')
time.sleep(2)

# fill in the * fields
try:
    first_name = driver.find_element(By.CSS_SELECTOR, 'ol.fieldsInLine>li:nth-child(1)>input')
    first_name.send_keys('testName')
    last_name = driver.find_element(By.CSS_SELECTOR, 'ol.fieldsInLine>li:nth-child(3)>input')
    last_name.send_keys('testLastname')
except Exception:
    print("Impossible login")

# activate checkbox
try:
    checkbox_required_fields = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
    checkbox_required_fields.click()
except Exception:
    print('Checkbox not found')
time.sleep(1)

#  fill in * hidding fields
try:
    user_name = driver.find_element(By.CSS_SELECTOR, 'input[name="user_name"]')
    user_name.click()
    user_name.send_keys('testUserName')

    password = driver.find_element(By.CSS_SELECTOR, 'input[id="user_password"]')
    password.send_keys('testPassword')

    confirm_password = driver.find_element(By.CSS_SELECTOR, 'input[id="re_password"]')
    confirm_password.send_keys('testPassword')
except Exception:
    print("Impossible fill in * hidding fields")
time.sleep(1)

# click button "Save"
try:
    btn_Save = driver.find_element(By.CSS_SELECTOR, 'input[id="btnSave"]')
    btn_Save.click()
except Exception as ex:
    print("button 'Save'")

print('ADD..\nCongratulation!')
time.sleep(3)
driver.quit()
