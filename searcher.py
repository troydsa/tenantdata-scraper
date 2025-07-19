from selenium import webdriver
import pandas as pd
from time import sleep

DELAY_SECONDS_AFTER_REQUEST = 1

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options)

def html_from_url(url: str) -> str:
    driver.get(url)
    sleep(DELAY_SECONDS_AFTER_REQUEST)
    return driver.page_source

def table_from_url(url: str) -> pd.DataFrame:
    return pd.read_html(html_from_url(url))[0]

if __name__ == '__main__':
    x = table_from_url(
        'https://rensselaercounty.prosgar.com/PROSSearch/SearchIndex?municipality=3814&FilterWaterfronts=False'
    )
    x.to_csv('data/test.csv')
    
    driver.quit()