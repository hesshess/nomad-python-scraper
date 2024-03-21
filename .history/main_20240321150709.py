from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch()

page = browser.ner_page()

page.goto("https://google.com")