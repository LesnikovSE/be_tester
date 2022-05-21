# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Реализуйте неявное ожидание поиска элементов
# 3. Перейдите в раздел "More" -> "File Upload"
# 4. Загрузите файл с картинкой
# 5. Нажмите на кнопку "Remove"
# 6. Загрузите пустой файл с расширением .txt
# 7. Закройте появившееся сообщение об ошибке
#    • Дополнительно: добавьте проверку что кнопка upload недоступна для нажатия (необязательная задача)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# driver.maximize_window()
# 1
driver.get('http://demo.automationtesting.in/WebTable.html')
# 2
driver.implicitly_wait(3)
# 3
driver.find_element(By.CSS_SELECTOR, 'a[href^="#"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[href^="FileUpload"]').click()
# 4
image_upload = r'C:\Users\GM\PycharmProjects\BeTesterAutomotion\lesson_3\loadImage.jpg'
driver.find_element(By.ID, 'input-4').send_keys(image_upload)
# 5
driver.find_element(By.CSS_SELECTOR, '[title="Clear selected files"]').click()
# 6
txt_upload = r'C:\Users\GM\PycharmProjects\BeTesterAutomotion\lesson_3\empty.txt'
driver.find_element(By.ID, 'input-4').send_keys(txt_upload)
# 7
btn_close = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.file-error-message>span')))
btn_close.click()
btn_upload = driver.find_element(By.CSS_SELECTOR, '[title="Upload selected files"]')
if btn_upload.get_attribute('disabled'):
    print('btn_upload deactivate')
else:
    print('btn_upload active')
#
print("test passed successfully")
driver.quit()
