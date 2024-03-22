import requests
from bs4 import BeautifulSoup



def extract_wwr_jobs(skill):
    url = f"https://weworkremotely.com/remote-jobs/search?term={skill}"
    userAgent = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
    all_jobs = []
    print(f"Scraping {url}")
    response = requests.get(url, headers=userAgent)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find_all('li',class_='feature')
    print(len(jobs))

    for job in jobs:
      company = job.find('span', class_="company").text
      title = job.find('span', class_="title").text
      description = job.find('span', class_="region").text
      link = job.find('a')['href']
      job_data = {
          "company": company,
          "title": title,
          "description": description,
          "link": f"https://weworkremotely.com/{link}"
      }
      all_jobs.append(job_data)
    return all_jobs



