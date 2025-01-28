from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# ✅ Step 1: Hardcode your LinkedIn Profile URL (no need for input)
linkedin_profile_url = "https://www.linkedin.com/in/vajiheh-sabzali-9b013b208/"  # Replace with your LinkedIn profile URL
print ("You are logging into:", linkedin_profile_url)

# ✅ Step 2: Use Chrome with an existing session (Make sure you are logged in!)
chrome_options = webdriver.ChromeOptions()
# Update the profile path here to your actual Chrome profile path (the path where you are logged into LinkedIn)
chrome_options.add_argument("user-data-dir=/Users/baharspring/Library/Application Support/Google/Chrome/Profile 1")  # 🔹 Update for your system

# ✅ Step 3: Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# ✅ Step 4: Open LinkedIn Profile (to check login status)
driver.get(linkedin_profile_url)

time.sleep(3)  # Wait for the page to load

# ✅ Step 5: Check if the user is logged in
if "LinkedIn" in driver.title:
    print("✅ You are logged in! Proceeding with job search...\n")
else:
    print("⚠️ WARNING: You must be logged into LinkedIn in your browser session!")
    driver.quit()
    exit()

# ✅ Step 6: Open LinkedIn Jobs with filters applied
job_search_url = "https://www.linkedin.com/jobs/search/?currentJobId=4058245610&distance=25.0&geoId=104508036&keywords=Data%20Analyst&origin=HISTORY"
print("job_search_url####", job_search_url)
driver.get(job_search_url)
print("driver####", driver)

time.sleep(5)  # Allow page to load

# ✅ Step 7: Extract job details
job_data = []
print("job_data####", job_data)

try:
    # Wait for job cards to load
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'job-card-container')))
    job_listings = driver.find_elements(By.CLASS_NAME, 'job-card-container')
    
    for job in job_listings:
        try:
            title = job.find_element(By.CLASS_NAME, 'job-card-list__title').text.strip()
            company = job.find_element(By.CLASS_NAME, 'job-card-container__company-name').text.strip()
            date_posted = job.find_element(By.CLASS_NAME, 'job-card-container__metadata-item').text.strip()

            job_data.append({
                'Title': title,
                'Company': company,
                'Date Posted': date_posted
            })

        except Exception as e:
            print(f"Skipping a job due to error: {e}")

except Exception as e:
    print(f"⚠️ Error loading job listings: {e}")

# ✅ Step 8: Convert to DataFrame & Save as CSV
if job_data:
    df = pd.DataFrame(job_data)
    df.to_csv('linkedin_data_analyst_jobs.csv', index=False)
    print("✅ Job data successfully saved to 'linkedin_data_analyst_jobs.csv'!")
else:
    print("⚠️ No jobs found or failed to extract data.")

# ✅ Step 9: Close Browser
driver.quit()
