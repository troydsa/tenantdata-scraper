from typing import Any


import distutils
from selenium import webdriver
import pandas as pd
from time import sleep
from io import StringIO

import url_maker

DELAY_SECONDS_AFTER_REQUEST = 1

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options)

def raw_html_from_url(url: str) -> str:
    driver.get(url)
    sleep(DELAY_SECONDS_AFTER_REQUEST)
    return driver.page_source

def html_from_url(url: str) -> StringIO:
    return StringIO(raw_html_from_url(url))

"""Works so long as table is <50 elements"""
def table_from_url(url: str) -> pd.DataFrame:
    return pd.read_html(html_from_url(url))[0]

def table_from_params(params: dict[str, Any]) -> pd.DataFrame:
    return table_from_url(url_maker.url_from_params(params))

if __name__ == '__main__':
    x = table_from_url(
        'https://rensselaercounty.prosgar.com/PROSSearch/SearchIndex?municipality=3814&FilterWaterfronts=False'
    )
    
    
    
    x.to_csv('data/test.csv')
    
    
    
    params = {
        'owner': 'Scribe, Josh',
        'municipality': 3844,
        'street': 'Beagle Run Way',
        'SaleDateMin': '02/01/1010',
        'SaleDateMax': '04/04/2024',
        'SalePriceMin': 5000,
        'SalePriceMax': 400000,
        'Neighborhood': 1,
        'PropertyClass': 110,
        'YearBuiltMin': 1912,
        'YearBuiltMax': 2010,
        'SquareFeetMin': 20,
        'SquareFeetMax': 20000,
        'BedroomsMin': 2,
        'BedroomsMax': 30,
        'BathroomsMin': 2,
        'BathroomsMax': 20,
        'HouseStyle': 4,
        'Waterfront': 5,
        'Condition': 5,
        'BasementType': 1,
        'LandAVMin': 100,
        'LandAVMax': 20000,
        'TotalAVMin': 10000,
        'TotalAVMax': 2000000,
        'FilterWaterfronts': False
    }
    
    print(url_maker.url_from_params(params))
    
    y: pd.DataFrame = table_from_params(params)
    
    y.to_csv('data/test_from_params.csv')
    
    
    
    
    
    
    driver.quit()
    
    