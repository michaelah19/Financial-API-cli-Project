# FinnhubApi-CLI-Project
 A command line interface used to pull financial/stock data based on user search/criteria. 
 
 The program uses the publicallly available API from finnhub, argparse and other python libraries.

The API Is available at: https://finnhub.io/

The Documentaton is available at: https://finnhub.io/docs/api/introduction

Library used: Argparse, Requests & finnhub-python

# Using finhubb python vs API calls with Request
Throughout the project, finhubb api library will be used over conventional requests calls.

For example finhubb python library allows us to use:

```python:

import finnhub
finnhub_client = finnhub.Client(api_key=config.API_KEY)
param = {'symbol': "GOOG"}
finnhub_client.company_profile2(param)

```

instead of using conventional api requests
```python:

import config
import requests

# Setting APIkey from config file
header = {'X-Finnhub-Token': config.API_KEY}
# Setting Parameters. Possible parameters/args for profile2 is symbol, isin and cusip.
param = {'symbol': "GOOG"}

response = (requests.get(
    # Endpoint for getting financial overview of stock
    url = config.BASE_URL + "/stock/profile2?",       
    # Header for API key             
    headers=header,
    # Parameter providing which stock
    params=param
    ))

```

# What it can do
