# 1 Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2 Перейдите в раздел "More" -> "Loader"
# 3 Реализуйте явное ожидание(EC) для отображения текста "Run"
# 4 Нажмите кнопку "Run"
# 5 Реализуйте явное ожидание(EC) что слово "Lorem" содержится в тексте модального окна
# 6 Реализуйте явное ожидание(EC) для нажатия в модальном окне на кнопку "Save Changes" и нажмите на неё

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
# 1
driver.get('http://demo.automationtesting.in/WebTable.html')
# 2
driver.find_element(By.CSS_SELECTOR, 'a[href^="#"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[href^="Loader"]').click()
# 3
driver.find_element(By.ID, 'loader').click()
# 4
WebDriverWait(driver, 26).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, '.modal-body p'), 'Lorem'))
# 5
driver.find_element(By.CSS_SELECTOR, '.modal-footer>button:last-child').click()

print("test passed successfully")
driver.quit()
