import requests
from bs4 import BeautifulSoup



def extract_berlin_jobs(skill):
    base_url = "https://berlinstartupjobs.com/"
    userAgent = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
    all_jobs = []
    print(f"Scraping {base_url}")
    response = requests.get(f"{base_url}skill-areas/{skill}/", headers=userAgent)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find("ul",
                     class_="jobs-list-items").find_all('li',
                                                        class_='bjs-jlid')
    print(len(jobs))

    for job in jobs:
      company = job.find('a', class_="bjs-jlid__b").text
      main = job.find('h4', class_="bjs-jlid__h")
      title = main.text
      description = job.find('div', class_="bjs-jlid__description").text
      link = main.find('a')['href']
      job_data = {
          "company": company,
          "title": title,
          "description": description,
          "link": link
      }
      all_jobs.append(job_data)
    return all_jobs



