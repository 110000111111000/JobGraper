import requests
from bs4 import BeautifulSoup

# URL for LinkedIn job search results for data analysts
url = 'https://www.linkedin.com/jobs/search/?keywords=data%20analyst'

# Send an HTTP request to get the page content
response = requests.get(url)
print(response)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup) mess up :) just try once

    # Find all job listings on the page (you may need to inspect the HTML structure)
    job_elements = soup.find_all('div', class_='job-result-card')

    # Loop through all job listings and extract the necessary information
    for job in job_elements:
        print(job.prettify())
        job_title = job.find('h3', class_='job-result-card__title').text.strip() if job.find('h3', class_='job-result-card__title') else 'N/A'
        company_name = job.find('h4', class_='job-result-card__subtitle').text.strip() if job.find('h4', class_='job-result-card__subtitle') else 'N/A'
        # Print the extracted job title and company name
        print(f"Job Title: {job_title}")
        print(f"Company: {company_name}")
        print("-" * 40)  # Print a separator for better readability
