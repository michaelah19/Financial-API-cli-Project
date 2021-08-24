# %%
import config
import requests

# Setting Parameters for endpoint required
# Possible parameters/args for profile2 is symbol, isin and cusip.
param = {'symbol': "GOOG"}

# 
header = {'X-Finnhub-Token': config.API_KEY}

# Example using the Profile2 endpoint to get general data of a stock.
response = (requests.get(
    # Endpoint for getting financial overview of stock
    url = config.BASE_URL + "/stock/profile2?",       
    # Header for API key             
    headers=header,
    # Parameter providing which stock
    params=param
    ))

if response.ok:
    data = response.json()
    print(data)
else:
    print(response.status_code)
# %%
requests.get