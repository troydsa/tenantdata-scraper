from selenium import webdriver
from time import sleep

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options)

def html_from_url(url: str, delay_seconds: float=0) -> str:
    driver.get(url)
    sleep(delay_seconds)
    return driver.page_source

if __name__ == '__main__':
    x = html_from_url(
        'https://rensselaercounty.prosgar.com/PROSSearch/SearchIndex?municipality=3814&FilterWaterfronts=False',
        1
    )
    print(x)
    driver.quit()