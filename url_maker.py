import urllib.parse
import urllib.request
from typing import Any

# Used for making URL's to the webpage itself, not the AJAX file it gets data from.
# However, pretty sure requests to the AJAX file use this link to indicate what
# data to get, so it's still useful to have

# For checking if the URL we make follows approximately the same format, though it doesn't need to be exact
# (+ works just as well as %20 for encoding a space, for example. Our code does the latter, while theirs does the former, see Franklin%20St in the example URL)

url_without_params = 'https://rensselaercounty.prosgar.com/PROSSearch/SearchIndex'



def filter_out_keys_with_none_values(params: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}

    
def url_from_params(params: dict[str, Any]) -> str:
    # This is so that later we can just set the values to None if we don't want that param to be considered, rather than having to remove it from the dict
    params = filter_out_keys_with_none_values(params)
    params_string = urllib.parse.urlencode(params)
    
    return url_without_params + '?' + params_string


if __name__ == '__main__':
    
    date_url = ('https://rensselaercounty.prosgar.com/PROSSearch/SearchIndex?'
                'SaleDateMin=01%2F01%2F0101%2000%3A00%3A00&SaleDateMax=03%2F03%2F3303%2000%3A00%3A00&FilterWaterfronts=False')
    
    original_url = ('https://rensselaercounty.prosgar.com/PROSSearch/SearchIndex?'
                    'owner=Scribe,%20Josh&'
                    'municipality=3844&'
                    'street=Beagle%20Run%20Way&'
                    'SaleDateMin=02%2F01%2F1010%2000%3A00%3A00&'
                    # SaleDateMax doesn't exist? I thought I'd clicked it but guess not
                    'SalePriceMin=5000&'
                    'SalePriceMax=400000&'
                    'Neighborhood=1&'
                    'PropertyClass=110&'
                    'YearBuiltMin=1912&'
                    'YearBuiltMax=2010&'
                    'SquareFeetMin=20&'
                    'SquareFeetMax=20000&'
                    'BedroomsMin=2&'
                    'BedroomsMax=30&'
                    'BathroomsMin=2&'
                    'BathroomsMax=20&'
                    'HouseStyle=04&'
                    'Waterfront=5&'
                    'Condition=5&'
                    'BasementType=1&'
                    'LandAVMin=100&'
                    'LandAVMax=20000&'
                    'TotalAVMin=1000&'
                    'TotalAVMax=2000000&'
                    'FilterWaterfronts=False')
    
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
    
    params2 = {
        'Waterfront': 5
    }
    
    print(url_from_params(params2))
