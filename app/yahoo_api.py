import requests
import json


def get_security_details(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"
    querystring = {"region": "US", "lang": "en", "symbol": ticker}
    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "538f35aacbmsh7a007be0718027bp13effdjsn802e4e45cfeb"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response
