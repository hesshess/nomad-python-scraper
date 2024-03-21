from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch()

page = browser.new_page()

page.goto("https://")