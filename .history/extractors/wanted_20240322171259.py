from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

def extract_wanted_jobs(keyword):
    p = sync_playwright().start()
    browser = p.chromium.launch()
    page = browser.new_page()
    # page.goto("https://www.wanted.co.kr/jobfeed")
    # # page.screenshot(path="screenshot.png")
    # time.sleep(5)
    # page.click("button.Aside_searchButton__Xhqq3")
    # # page.locator("button.Aside_searchButton__Xhqq3").click()
    # time.sleep(5)
    # page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
    # time.sleep(5)
    # page.keyboard.down("Enter")
    # time.sleep(5)
    # page.click("a#search_tab_position")
    page.goto(f"https://www.wanted.co.kr/search?query={keyword}")
    for x in range(5):
        time.sleep(3)
        page.keyboard.down("End")
    content = page.content()
    p.stop()
    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.find_all("div", class_="JobCard_container__FqChn")
    
    print(len(jobs))
    
    jobs_db=[]
    for job in jobs:
        link = F"https://www.wanted.co.kr{job.find('a')['href']}"
        title = job.find("strong", class_="JobCard_title__ddkwM").text
        company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
        reward = job.find("span", class_="JobCard_reward__sdyHn").text 
        job = {
    "link" : link,
    "title" : title,
    "company_name" : company_name,
    "reward" : reward,
        }
        jobs_db.append(job)
    return jobs_db
        
