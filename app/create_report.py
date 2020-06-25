#create_report.py
# creates asset allocation and net worth reporting

#initialise things

import os
import csv
import pandas as pd 


#create current asset allocation and net worth reporting

#calculate value of exchange traded products / stocks
etp_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")
df_etp = pd.read_csv(etp_filepath)
df_etp["Value"] = df_etp["Units"] * df_etp["Last Price"]
etp_total_value = df_etp["Value"].sum()

#calculate value of liabilities
liability_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "liabilities.csv")
df_liability = pd.read_csv(liability_filepath)
df_liabilities_by_asset = df_liability.groupby("Asset Class").sum().reset_index()
df_liabilities_by_asset["Current Value"] = df_liabilities_by_asset["Current Value"] * -1

#calculate value of other assets 
assets_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "other_assets.csv")
df_other_assets = pd.read_csv(assets_filepath)
df_assets_by_asset = df_other_assets.groupby("Asset Class").sum().reset_index()
df_assets_by_asset = df_assets_by_asset.drop(["Purchase Value"], axis = 1)

#add ETP assets to other assets
etp_assets_row = {"Asset Class": "Equity", "Current Value": etp_total_value}
df_assets_by_asset = df_assets_by_asset.append(etp_assets_row, ignore_index=True)

#add assets to liabilities to create net worth
df_net_assets = pd.concat([df_assets_by_asset, df_liabilities_by_asset],axis=0)
df_net_assets = df_net_assets.groupby("Asset Class").sum().reset_index()
pd.options.display.float_format = '${:,.2f}'.format
print(df_net_assets.head())
