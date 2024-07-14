from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


service = Service('E:/Github/DjangoFormFiller/formFiller/main/scripts/chromedriver/chromedriver.exe')  # Update this path to the location of your chromedriver
driver = webdriver.Chrome(service=service)

# Open the Google form
driver.get('https://forms.gle/WT68aV5UnPajeoSc8')

try:
    full_name = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    full_name.send_keys('Rajat Disawal')


    contact_number = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    contact_number.send_keys('1425364758')


    email_id = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    email_id.send_keys('rajatdisawal@example.com')


    full_address = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'))
    )
    full_address.send_keys('19, Example Gali, Chembur, Mumbai')


    pin_code = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    pin_code.send_keys('400074')


    dob = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'))
    )
    dob.send_keys('07/04/2004')

    gender = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    gender.send_keys('Male')


    verification_code = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    verification_code.send_keys('GNFPYC')


    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'))
    )
    submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'idZHHb'))
    )

    time.sleep(3)
    screenshot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'confirmation_page.png')
    driver.save_screenshot(screenshot_path)

finally:
    driver.quit()
