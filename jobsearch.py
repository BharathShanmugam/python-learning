import requests
from bs4 import BeautifulSoup

def scrape_jobs():
    url = "https://in.indeed.com/jobs?q=python+developer&l=Hyderabad%2C+Telangana"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    for job in soup.find_all('div', class_='jobsearch-SerpJobCard'):  # Adjust according to the site's HTML structure
        title = job.find('h2', class_='title').text.strip()
        link = "https://in.indeed.com" + job.find('a')['href']  # Complete the URL for job link
        jobs.append({'title': title, 'link': link})

    return jobs

# Example usage
job_listings = scrape_jobs()
for job in job_listings:
    print(job['title'], job['link'])
