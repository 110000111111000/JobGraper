from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to your chromedriver (make sure chromedriver is installed)
chrome_driver_path = 'path_to_your_chromedriver'

# LinkedIn credentials
linkedin_username = 'your_email'
linkedin_password = 'your_password'

# Setup Chrome options (run headless if needed)
chrome_options = Options()
chrome_options.add_argument('--headless')  # Uncomment to run in headless mode (no UI)

# Setup WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to LinkedIn login page
driver.get('https://www.linkedin.com/login')

# Login to LinkedIn
username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')

username_field.send_keys(linkedin_username)
password_field.send_keys(linkedin_password)

password_field.send_keys(Keys.RETURN)  # Press Enter to log in

# Wait for login to complete (adjust as necessary)
time.sleep(5)

# Now that we're logged in, navigate to your LinkedIn profile
driver.get('https://www.linkedin.com/in/me')  # Change 'me' to your LinkedIn username if needed

# Wait for the profile to load
time.sleep(5)

# Extract profile details
try:
    # Example: Extract name and headline (job title)
    name = driver.find_element(By.XPATH, '//li[contains(@class, "inline t-24 t-black t-normal break-words")]').text
    headline = driver.find_element(By.XPATH, '//h2[contains(@class, "mt1 t-18 t-black t-normal")]').text
    
    print("Name:", name)
    print("Headline:", headline)

except Exception as e:
    print("Error extracting profile details:", e)

# Close the browser
driver.quit()
