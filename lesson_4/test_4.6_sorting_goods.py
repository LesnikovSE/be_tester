from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
# Select test
html_select = Select(driver.find_element(By.NAME, 'orderby'))
assert "menu_order" == html_select.options[0].get_attribute('value')
# Sort by price: "high to low"
html_select.select_by_value('price-desc')
#
html_select = Select(driver.find_element(By.NAME, 'orderby'))
assert "price-desc" == html_select.first_selected_option.get_attribute('value')

driver.quit()
