import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Step 1: Create Temporary Email using Temp-Mail API (or other similar services)
def create_temp_email():
    response = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
    email = response.json()[0]
    return email

# Step 2: Function to create Facebook account using the temporary email
def create_fb_account(temp_email, temp_password):
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Change path to your WebDriver
    driver.get("https://www.facebook.com/reg")

    time.sleep(3)

    # Fill sign-up form
    driver.find_element(By.NAME, "firstname").send_keys("Test")
    driver.find_element(By.NAME, "lastname").send_keys("User")
    driver.find_element(By.NAME, "reg_email__").send_keys(temp_email)
    driver.find_element(By.NAME, "reg_email_confirmation__").send_keys(temp_email)
    driver.find_element(By.NAME, "reg_passwd__").send_keys(temp_password)
    driver.find_element(By.ID, "day").send_keys("15")
    driver.find_element(By.ID, "month").send_keys("Apr")
    driver.find_element(By.ID, "year").send_keys("1990")
    driver.find_element(By.XPATH, "//input[@value='2']").click()  # Male

    # Submit form
    driver.find_element(By.NAME, "websubmit").click()

    time.sleep(5)
    driver.quit()

# Step 3: Mass Reporting Function
def mass_report(profile_url, fb_email, fb_password):
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get("https://www.facebook.com/login")

    time.sleep(3)

    # Log into Facebook
    driver.find_element(By.NAME, "email").send_keys(fb_email)
    driver.find_element(By.NAME, "pass").send_keys(fb_password)
    driver.find_element(By.NAME, "login").click()

    time.sleep(5)

    # Go to the profile to report
    driver.get(profile_url)

    time.sleep(3)

    # Report Profile (update Xpath if necessary)
    report_button = driver.find_element(By.XPATH, '//div[contains(text(), "Report")]')
    report_button.click()

    time.sleep(2)

    # Choose report reason (update Xpath as needed)
    offensive_option = driver.find_element(By.XPATH, '//span[contains(text(), "It’s offensive")]')
    offensive_option.click()

    time.sleep(2)

    # Submit the report
    submit_button = driver.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
    submit_button.click()

    time.sleep(2)
    driver.quit()

# Step 4: Bypass Verification (Optional)
def bypass_verification(fb_email, fb_password):
    # This step would depend on the service you are working with, typically involving captcha bypasses
    # or automating code input from email/SMS services. Example below assumes a bypass for a simple verification.
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get("https://www.facebook.com/login")

    # Log into Facebook
    driver.find_element(By.NAME, "email").send_keys(fb_email)
    driver.find_element(By.NAME, "pass").send_keys(fb_password)
    driver.find_element(By.NAME, "login").click()

    time.sleep(5)

    # Check for verification page and bypass if possible
    # Here you can handle any SMS/Email verification automatically, using a service like Temp-Mail or any SMS API.

    driver.quit()

# Main Execution
if __name__ == "__main__":
    # Create temporary email
    temp_email = create_temp_email()
    temp_password = "SecurePassword123"

    print(f"Temporary Email: {temp_email}")

    # Create Facebook account with temp email
    create_fb_account(temp_email, temp_password)

    # Mass report a profile
    fb_email = temp_email  # Use the temp email for login
    fb_password = temp_password
    profile_url = "https://www.facebook.com/someprofile"  # Replace with the target profile URL
    mass_report(profile_url, fb_email, fb_password)

    # Optional: Bypass verification
    bypass_verification(fb_email, fb_password)
