from typing import Any

import consts
from url_maker import url_from_params
import requests

def make_headers(url: str) -> dict[str, Any]:
    to_return = consts.headers.copy()
    to_return['Referer'] = url
    return to_return

def make_request(url: str) -> requests.Response: 
    ajax_url = 'https://rensselaercounty.prosgar.com/PROSSearch/GetAjax'
    
    req = requests.post(ajax_url, headers=make_headers(url), data=consts.form_data)
    
    return req

def page_from_url(url: str) -> str:
    
    req = make_request(url)
    
    print(req.headers)
    print(req.status_code)
    print(req.request.body)
    print('The above is the page')
    
    return req.text

def page_from_params(params: dict[str, Any]) -> str:
    url = url_from_params(params)
    return page_from_url(url)

def main():
    # params = {
    #     'Waterfront': 1
    # }
    # page = page_from_params(params)
    
    page = page_from_url('https://rensselaercounty.prosgar.com/PROSSearch/SearchIndex?owner=Scribe,%20Josh&municipality=3844&street=Beagle%20Run%20Way&SaleDateMin=02%2F01%2F1010%2000%3A00%3A00&SalePriceMin=5000&SalePriceMax=400000&Neighborhood=1&PropertyClass=110&YearBuiltMin=1912&YearBuiltMax=2010&SquareFeetMin=20&SquareFeetMax=20000&BedroomsMin=2&BedroomsMax=30&BathroomsMin=2&BathroomsMax=20&HouseStyle=04&Waterfront=5&Condition=5&BasementType=1&LandAVMin=100&LandAVMax=20000&TotalAVMin=1000&TotalAVMax=2000000&FilterWaterfronts=False')
    
    print(page)
    print(len(page))
    print('working 1')
    
    filename = 'data/' + 'test.html'
    print(page)
    with open(filename, 'w', encoding='utf-16') as f:
        print('writing')
        f.write(page)
    
        
    print('WORKING2')
    

if __name__ == '__main__':
    main()
    
    