# etd_update.py


#initialise things

from statistics import mean
import datetime
import csv
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()
import pandas as pd 
from scipy import stats

#define basic functions

def to_usd(my_price):
    return f"${my_price: , .2f}"


#load list of exchange traded products held

#import csv file

csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")

df = pd.read_csv(csv_filepath)

#print(df.head())
#df = df.set_index("Ticker")
etp = df.to_dict("records")
#print(type(etp))
#print(etp)
#breakpoint()

#stock_list = etp.keys()
stock_list = [s["Ticker"] for s in etp]
#print(stock_list)

#exit()

for stock in stock_list:

    # make API request for stock prices

    #    print(stock)    #test we are getting the stock ticker in the loop
    request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + \
        stock+"&outputsize=compact&apikey=4E09ZJ6HEW1R7V41"
    response = requests.get(request_url)

    response_data = json.loads(response.text)

    #test api call is working
    #print(response.text)
    #print(response.status_code)
    #print(type(response_data))

    #exit()

    #figure out what keys we're dealing with
    key_list = list(response_data.keys())
    #print(key_list)

# error checking on API call

    if response.status_code not in range(200, 299):
        print("API call failure - Data for Ticker =",
              stock, "not found.  Please check ticker is correct in the csv file and try again.")
        continue
    # Alphavantage API returns this message if a GET request on an invalid ticker is successfully sent
    elif key_list[0] == 'Error Message':
        print("API call failure - Data for Ticker =",
              stock, "not found.  lease check ticker is correct in the csv file and try again.")
        continue

# extract data from json response

    last_day = response_data["Meta Data"]["3. Last Refreshed"]
    stock_ticker = response_data["Meta Data"]["2. Symbol"]
    last_close = float(response_data["Time Series (Daily)"][last_day]["4. close"])
    tsd = response_data["Time Series (Daily)"]
    dates = list(tsd.keys())

    #update dataframe with latest stock price
    df.loc[df["Ticker"] == stock, ["Last Price"]] = last_close

    #check if price has moved significantly
    alerts = {}   ##this may need to be changed back to []!!!!
    #print(type(alerts))
    
    close_prices = []

    for date in dates:
        close_price = tsd[date]["4. close"]
        close_prices.append(float(close_price))
    
    z_scores = stats.zscore(close_prices)
    #print(z_scores)
    #print("test")
    price_series = pd.Series(close_prices)
    #percent_change = pd.price_series.pct_change()
    pc_series = price_series.pct_change()
    percent_change = pc_series.iloc[-1]
    print(percent_change)
    z_score = z_scores[-1]
    print(z_score)
    if z_score >= 2.5 or z_score <= -2.5:
        send_alert = True
    elif percent_change >= 5 or percent_change <= -5:
        send_alert = True
    else:
        send_alert = False
    
    #why doesn't this write to the alerts file???
    alerts = alerts.update({"Ticker": stock, "% Change": percent_change, "Z Score": z_score})
    print(alerts)
    exit()
    #print(type(alerts))
    
    #dma_10 = mean(close_prices[0:10])
    #dma_50 = mean(close_prices[0:50])

    #create table of alerts


# update csv with modified dataframe


df.to_csv(csv_filepath, index = False, header = True)


