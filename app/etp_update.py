# etd_update.py


#initialise things

from statistics import mean
from datetime import datetime
import csv
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()
import pandas as pd 
from scipy import stats

from app.email_service import send_email
from app import CLIENT_NAME

#define basic functions

def to_usd(my_price):
    return f"${my_price: , .2f}"




#load list of exchange traded products held

#import csv file

csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")
df = pd.read_csv(csv_filepath)
etp = df.to_dict("records")
stock_list = [s["Ticker"] for s in etp]

# evaluate ETPs held with latest price data
MV_API = os.getenv("MV_API")

#create dictionary to be used to store stock alerts
alerts = []
alerts.append({"Ticker": "Ticker", "% Change": "% Change", "Z Score": "Z Score"})

for stock in stock_list:

    # make API request for stock prices

    request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + \
        stock+"&outputsize=compact&apikey="+str(MV_API)
    response = requests.get(request_url)

    response_data = json.loads(response.text)

    #test api call is working
    #print(response.text)
    #print(response.status_code)
    #print(type(response_data))


    #figure out what keys we're dealing with
    key_list = list(response_data.keys())
    
    
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
    tsd = response_data["Time Series (Daily)"]
    dates = list(tsd.keys())
    
    #last_day = response_data["Meta Data"]["3. Last Refreshed"]
    last_day = dates[0]
    
    stock_ticker = response_data["Meta Data"]["2. Symbol"]
    last_close = float(response_data["Time Series (Daily)"][last_day]["4. close"])
    
    
    #update dataframe with latest stock price
    df.loc[df["Ticker"] == stock, ["Last Price"]] = last_close

    #check if price has moved significantly
      
    close_prices = []

    for date in dates:
        close_price = tsd[date]["4. close"]
        close_prices.append(float(close_price))
    
    z_scores = stats.zscore(close_prices)
    price_series = pd.Series(close_prices)
    pc_series = price_series.pct_change()
    percent_change = pc_series.iloc[-1]
    z_score = z_scores[-1]
    
    
    if z_score >= 0.025 or z_score <= -0.025:
        send_alert = True
        alerts.append({"Ticker": stock, "% Change": round(percent_change,2), "Z Score": round(z_score,2)})
    elif percent_change >= 0.05 or percent_change <= -0.05:
        send_alert = True
        alerts.append({"Ticker": stock, "% Change": round(percent_change,2), "Z Score": round(z_score,2)})
    #else:
    #    send_alert = False
    
    #add to dictionary of alerts
    #alerts.append({"Ticker": stock, "% Change": round(percent_change,2), "Z Score": round(z_score,2)})
    
    

# update csv with modified dataframe

df.to_csv(csv_filepath, index = False, header = True)

#send email if needed

#CLIENT_NAME = os.getenv("CLIENT_NAME")

print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

if __name__ == "__main__":

    if send_alert == True:
        
        html = ""
        html += f"<h3>Good evening {CLIENT_NAME},</h3>"

        html += "<h4>Today's Date</h4>"
        #html += f"<p>{date.today().strftime('%A, %B %d, %Y')}</p>"
        html += f"<p>{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}</p>"

        html += f"<h4>This is a large price change alert on your stock and ETF portfolio</h4>"
        html += f"<h3>No action is needed from you, but you may wish to take a look at these positions:</h3>"
        html += f"<h2>[Please contact your Financial Advisor for more information]</h2>"
        html += "<ul>"
        for stock in alerts:
            html += f"<li>{stock['Ticker']} | {stock['% Change']} | {stock['Z Score'].upper()}</li>"
        html += "</ul>"

        send_email(subject="Important Portfolio Update: Large Price Change Alert", html=html)
