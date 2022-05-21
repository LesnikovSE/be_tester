# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Реализуйте неявное ожидание поиска элементов
# 3. Перейдите в раздел "More" -> "JQuery ProgressBar"
# 4. Реализуйте явное ожидание(EC) для проверки: кнопка "Close" невидима
#    • нажмите на кпоку "Start Download", в появившемся окне возьмите селектор кнопки "Close"
# 5. Нажмите кнопку "Start Download"
# 6. Реализуйте явное ожидание(EC) для проверки: кнопка называется "Cancel Download"
# 7. Закройте окно. Снова откройте
# 8. Реализуйте явное ожидание(EC) для проверки: в окне присутствует текст "Complete!"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
# 1
driver.get('http://demo.automationtesting.in/WebTable.html')
# 2
driver.implicitly_wait(2)
# 3
driver.find_element(By.CSS_SELECTOR, 'a[href^="#"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[href^="JqueryProgressBar"]').click()
# 4
WebDriverWait(driver, 2).until(
    ec.invisibility_of_element_located((By.CSS_SELECTOR, '[role="dialog"]>div:last-child>div>button')))
# 5
driver.find_element(By.ID, 'downloadButton').click()
# 6
WebDriverWait(driver, 2).until(
    ec.text_to_be_present_in_element((By.CSS_SELECTOR, '.ui-dialog-buttonset>button'), 'Cancel Download')
    )
# 7
driver.find_element(By.CSS_SELECTOR, '.ui-dialog-buttonset>button').click()
driver.find_element(By.ID, 'downloadButton').click()

WebDriverWait(driver, 10).until(
    ec.text_to_be_present_in_element((By.XPATH, '//*[@class="progress-label"]'), 'Complete!')
    )
print("test passed successfully")
driver.quit()
