from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get('http://localhost:5500/')
    
    time.sleep(10)
    # Fill out the form
    driver.find_element(By.ID, 'username').send_keys('test_user')
    driver.find_element(By.ID, 'password').send_keys('test_password')

    # Submit the form
    driver.find_element(By.ID, 'login-button').click()

    # Wait for the status message to appear
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'login-status'), 'Login successful!')
    )

    # Close the browser
    driver.quit()

test_login()