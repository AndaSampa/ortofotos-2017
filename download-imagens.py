from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
prefs = {"download.default_directory" : "downloads/full"}
options.add_experimental_option("prefs",prefs)

browser = webdriver.Chrome(chrome_options=options)

with open('downloads/imagens-2017-url-download.csv') as f:
    datareader = csv.reader(f)
    for row in datareader:
        browser.get(row[0])
        print(row[0])
browser.close

