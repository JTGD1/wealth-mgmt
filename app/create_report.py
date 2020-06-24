#create_report.py
# creates asset allocation and net worth reporting

#initialise things

import os
import csv
import pandas as pd 


#create current asset allocation and net worth reporting

#calculate value of exchange traded products / stocks

#import csv file

etp_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")
df_etp = pd.read_csv(etp_filepath)
df_etp["Value"] = df_etp["Units"] * df_etp["Last Price"]
etp_total_value = df_etp["Value"].sum()
print(etp_total_value)
#etp = df.to_dict("records")
#etp_value = [s["Ticker"] for s in etp]

