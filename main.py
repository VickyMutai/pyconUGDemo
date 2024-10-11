import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("test_log.log"),  # Save logs to a file
        logging.StreamHandler()               # Print logs to console
    ]
)

def test_login(username, password):
    driver = webdriver.Chrome()
    logging.info(f"Starting test for user: {username}")

    try:
        driver.get('http://localhost:5500/')
        logging.info("Opened the login page")

        time.sleep(3)
        logging.info("Filling out the login form")

        # Fill out the form
        driver.find_element(By.ID, 'username').send_keys(username)
        driver.find_element(By.ID, 'password').send_keys(password)

        # Submit the form
        driver.find_element(By.ID, 'login-button').click()
        logging.info("Submitted the login form")

        # Wait for the dashboard page to load
        WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.XPATH, "//h4[text()='Welcome to PYCON UGANDA 2024']"))
        )
        logging.info("Dashboard page loaded")

        # Check if the dashboard is displayed correctly
        dashboard_heading = driver.find_element(By.XPATH, "//h4[text()='Welcome to PYCON UGANDA 2024']")
        assert dashboard_heading.is_displayed()
        logging.info("Dashboard is displayed correctly")

    except AssertionError:
        logging.error(f"Test failed for user: {username} - Dashboard not displayed correctly")
    except Exception as e:
        logging.error(f"An error occurred for user: {username}: {e}")
    else:
        logging.info(f"Test passed for user: {username}")
    finally:
        time.sleep(5)
        driver.quit()
        logging.info("Browser closed")

# Run tests with different credentials
test_login('test_ser', 'test_password')
test_login('test_user', 'test_assword')
test_login('test_user', 'test_password')
