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
import pandas

#define basic functions

def to_usd(my_price):
    return f"${my_price: , .2f}"


#load list of exchange traded products held
#import csv file
csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")

df = pandas.read_csv(csv_filepath)

print(df.head())

etp = df.to_dict("records")
print(type(etp))

print(etp)
