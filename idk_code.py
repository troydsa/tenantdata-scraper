import sys

import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd

BASE_URL = "https://rensselaercounty.prosgar.com"
SEARCH_URL = BASE_URL + "/PROSSearch/AdvancedSearchFilters"
AJAX_URL = BASE_URL + "/PROSSearch/GetAjax"

# Advanced search params
SALE_DATE_MIN = ""
SALE_DATE_MAX = ""
MUNICIPALITY = ""
NEIGHBORHOOD = ""
STREET = ""
OWNER = ""
PROPERTY_CLASS = ""
ACCOUNT_NUMBER = ""
SQUARE_FEET_MIN = ""
SQUARE_FEET_MAX = ""
YEAR_BUILT_MIN = ""
YEAR_BUILT_MAX = ""
SALE_PRICE_MIN = ""
SALE_PRICE_MAX = ""
LAND_AV_MIN = ""
LAND_AV_MAX = ""
TOTAL_AV_MIN = ""
TOTAL_AV_MAX = ""
HOUSE_STYLE = ""
BEDROOMS_MIN = ""
BEDROOMS_MAX = ""
BATHROOMS_MIN = ""
BATHROOMS_MAX = ""
CONDITION = ""
BASEMENT_TYPE = ""
WATERFRONT = ""
FILTER_WATERFRONTS = "false"

# AJAX params
DRAW = "1"
START = "0"
LENGTH = "100"
SEARCH_VALUE = ""
SEARCH_REGEX = "false"
SBL = ""
ADDRESS = ""
SCHOOL_DISTRICT = ""
FIREPLACES_MIN = ""
FIREPLACES_MAX = ""
FILTER_WATERFRONTS_AJAX = "False"

def search() -> list[dict]:
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; reproduction-script/1.0)",
        "Accept-Language": "en-US,en;q=0.5"
    })

    # GET the advanced search page to obtain cookies + __RequestVerificationToken
    get_res = session.get(SEARCH_URL, timeout=30)
    get_res.raise_for_status()

    # Parse anti-forgery token from HTML
    soup = BeautifulSoup(get_res.text, "html.parser")
    token_input = soup.find("input", {"name": "__RequestVerificationToken"})
    if not token_input:
        raise RuntimeError("Anti-forgery token not found on advanced-search page")
    csrf_token = token_input.get("value")

    # POST the advanced-search form
    adv_form = {
        "SaleDateMin": SALE_DATE_MIN,
        "SaleDateMax": SALE_DATE_MAX,
        "__RequestVerificationToken": csrf_token,
        "Municipality": MUNICIPALITY,
        "Neighborhood": NEIGHBORHOOD,
        "Street": STREET,
        "Owner": OWNER,
        "PropertyClass": PROPERTY_CLASS,
        "AccountNumber": ACCOUNT_NUMBER,
        "SquareFeetMin": SQUARE_FEET_MIN,
        "SquareFeetMax": SQUARE_FEET_MAX,
        "YearBuiltMin": YEAR_BUILT_MIN,
        "YearBuiltMax": YEAR_BUILT_MAX,
        "SalePriceMin": SALE_PRICE_MIN,
        "SalePriceMax": SALE_PRICE_MAX,
        "LandAVMin": LAND_AV_MIN,
        "LandAVMax": LAND_AV_MAX,
        "TotalAVMin": TOTAL_AV_MIN,
        "TotalAVMax": TOTAL_AV_MAX,
        "HouseStyle": HOUSE_STYLE,
        "BedroomsMin": BEDROOMS_MIN,
        "BedroomsMax": BEDROOMS_MAX,
        "BathroomsMin": BATHROOMS_MIN,
        "BathroomsMax": BATHROOMS_MAX,
        "Condition": CONDITION,
        "BasementType": BASEMENT_TYPE,
        "Waterfront": WATERFRONT,
        "FilterWaterfronts": FILTER_WATERFRONTS
    }

    post_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": SEARCH_URL,
        "Origin": BASE_URL
    }

    post_res = session.post(SEARCH_URL, data=adv_form, headers=post_headers, allow_redirects=True, timeout=30)
    post_res.raise_for_status()

    # POST the DataTables AJAX request to get result
    ajax_payload = {
        "draw": DRAW,
        "columns": [
            {"data": "Address", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
            {"data": "Address", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
            {"data": "Owner", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
            {"data": "SBL", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
            {"data": "MostRecentSaleDate", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
            {"data": "MostRecentSalePrice", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
            {"data": "LotSize", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
            {"data": "PropertyType", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
            {"data": "BuildingStyle", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
            {"data": "Zoning", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
            {"data": "YearBuilt", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
            {"data": "SFLA", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
            {"data": "RoomCounts", "name": "", "searchable": "true", "orderable": "false", "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX}},
        ],
        "start": START,
        "length": LENGTH,
        "search": {"value": SEARCH_VALUE, "regex": SEARCH_REGEX},
        "__RequestVerificationToken": csrf_token,
        "sbl": SBL,
        "address": ADDRESS,
        "owner": OWNER,
        "municipality": MUNICIPALITY,
        "street": STREET,
        "SaleDateMin": SALE_DATE_MIN,
        "SaleDateMax": SALE_DATE_MAX,
        "SalePriceMin": SALE_PRICE_MIN,
        "SalePriceMax": SALE_PRICE_MAX,
        "Neighborhood": NEIGHBORHOOD,
        "SchoolDistrict": SCHOOL_DISTRICT,
        "PropertyClass": PROPERTY_CLASS,
        "YearBuiltMin": YEAR_BUILT_MIN,
        "YearBuiltMax": YEAR_BUILT_MAX,
        "SquareFeetMin": SQUARE_FEET_MIN,
        "SquareFeetMax": SQUARE_FEET_MAX,
        "BedroomsMin": BEDROOMS_MIN,
        "BedroomsMax": BEDROOMS_MAX,
        "BathroomsMin": BATHROOMS_MIN,
        "BathroomsMax": BATHROOMS_MAX,
        "FireplacesMin": FIREPLACES_MIN,
        "FireplacesMax": FIREPLACES_MAX,
        "HouseStyle": HOUSE_STYLE,
        "Waterfront": WATERFRONT,
        "Condition": CONDITION,
        "BasementType": BASEMENT_TYPE,
        "LandAVMin": LAND_AV_MIN,
        "LandAVMax": LAND_AV_MAX,
        "TotalAVMin": TOTAL_AV_MIN,
        "TotalAVMax": TOTAL_AV_MAX,
        "FilterWaterfronts": FILTER_WATERFRONTS_AJAX,
        "AccountNumber": ACCOUNT_NUMBER,
    }

    ajax_headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": BASE_URL + "/PROSSearch/SearchIndex?FilterWaterfronts=False",
    }

    ajax_post = session.post(AJAX_URL, data=ajax_payload, headers=ajax_headers, timeout=30)
    ajax_post.raise_for_status()

    try:
        data: dict = ajax_post.json()
        print("AJAX response keys:", list(data.keys()))
        print("Number of rows returned:", len(data["data"]))
        return data["data"]
    except ValueError:
        print("AJAX response is not JSON; returning empty list", file=sys.stderr)
        return []
        # return ajax_post.text

if __name__ == "__main__":
    res = search()
    pprint.pprint(res)
    
    df = pd.DataFrame(res)
    df.to_csv('data/test_idk.csv')
    
