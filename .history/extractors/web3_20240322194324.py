import requests
from bs4 import BeautifulSoup



def extract_berlin_jobs(skill):
    url = f"https://web3.career/{skill}-jobs"
    userAgent = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
    all_jobs = []
    print(f"Scraping web3")
    response = requests.get(url, headers=userAgent)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find("tbody",class_="tbody").find_all('tr',class_=' table_row')

    for job in jobs:
        main = job.find('div', class_="job-title-mobile")
        title = main.text
        link = main.find('a')['href']
        sub = job.find_all('td', class_="job-location-mobile")
        company = sub.find('h3').text
        description = sub[-1].text
        job_data = {
            "company": company,
            "title": title,
            "description": description,
            "link": link
        }
        all_jobs.append(job_data)
    return all_jobs



