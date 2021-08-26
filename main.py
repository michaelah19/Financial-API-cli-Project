# %%
from api_handler import *
import requests
import argparse
import datetime
import config
import pandas as pd
import plotly.graph_objects as go

# Setting Dates and time for pulls from API
today = datetime.datetime.now().strftime("%Y-%m-%d")
lastyear = (datetime.datetime.now() - datetime.timedelta(days=365)).strftime("%Y-%m-%d")

# Setting APIkey from config file
API_KEY = config.API_KEY

# Setting up Argparse
parser = argparse.ArgumentParser()

# Adding Arguments
parser.add_argument("--profile", '-p',
                    action="store_true",
                    help = "Displays basic stock information such as price, market cap and website to screen"
                    )
                
parser.add_argument("--metrics", '-m',
                    help = "Basic financial fundamentals related to stock price",
                    action = "store_true")

parser.add_argument("--news", "-n",
                    help = "Displays the latest new related to stock",
                    action = "store_true")

parser.add_argument("--plot",
                    help = "Plots a candlestick chart based on user spciefied timeframe. Please enter any of the following choices such as 1 5 15 30 60 D W M timeframes.",
                    type = str,
                    nargs=1,
                    choices=['1', '5', '15', '30','60', 'D', 'W', 'M'],
                    default = '0')

# Positional Argument (required arg)
parser.add_argument("stock", help = "Symbol of stock to analyze")

# Parsing Arguments
args = parser.parse_args()


# Using API Handler (User Defined Class) for calls to Finhub API
handle = ApiHandler(API_KEY,args.stock)

# Check if stock name exist if not print and exit
if not handle.is_valid():
    print(f"{args.stock} is not a valid stock symbol")
    exit()

# Now Doing work based on Argparse arguments. All the following methods grabs data from the API

# Printing messages based on user input
if args.profile:
    profile_data = pd.json_normalize(handle.get_profile()).T
    profile_data.index.names = ['Attribute']
    profile_data.columns = ['Value']
    print(profile_data)

if args.news:
    news_data = handle.get_news(lastyear,today) # In Json format
    date = datetime.datetime.utcfromtimestamp(news_data[1]['datetime']).strftime("%Y-%m-%d")
    print(f"\nThe latest news about {args.stock} released on {date} published by {news_data[0]['source']} is \n '{news_data[0]['summary']}'")

if args.metrics:
    # print(handle.get_metrics(lastyear,today))
    metrics_data = pd.json_normalize(handle.get_metrics(lastyear,today)["earningsCalendar"])
    print(f"\n The last metrics data for the quarter are \n {metrics_data.to_string(index=False)}\n ")

if args.plot != '0':
    today = int(datetime.datetime.now().timestamp())
    lastyear = int((datetime.datetime.now() - datetime.timedelta(days=365)).timestamp())

    candle_data = pd.json_normalize(handle.get_candles(args.plot,lastyear,today))
    fig = go.Figure(data=[go.Candlestick(
                                        x=[datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d") for t in candle_data['t'][0]],
                                        open=candle_data['o'][0],
                                        high=candle_data['h'][0],
                                        low=candle_data['l'][0],
                                        close=candle_data['c'][0])
                        ]
                    )

    fig.update_layout(
    title=f'Candle Stick for {args.stock} in the {args.plot} timeframe',
    yaxis_title=f'{args.stock} Stock Price $USD'
    )
    fig.show()

















