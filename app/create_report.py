#create_report.py
# creates asset allocation and net worth reporting

#initialise things

import os
import csv
import pandas as pd 
from datetime import datetime
import altair as alt
import plotly
import plotly.graph_objects as go
import plotly.express as px

#create current asset allocation and net worth reporting

def report_create():

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
    
    #write data to records
    date = datetime.now().strftime("%m/%d/%Y")
    
    net_worth_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "net_worth_history.csv")
    df_net_worth = pd.read_csv(net_worth_filepath)
    last_date = df_net_worth.iloc[-1]["Date"]
    

    if last_date == date:
        print("Data is up to date")
        
    else:
        df_net_assets.insert(0, "Date", date)
        #print(df_net_assets.head())
        df_net_assets.to_csv(net_worth_filepath, mode="a", header=False, index=False)

    #create charts

    history = alt.Chart(df_net_worth).mark_bar().encode(
        x="Date",
        y="Current Value",
        color="Asset Class"
    ).properties(title="Historical Net Worth + Asset Allocation")
    history.configure_title(
    fontSize=20,
    font='Courier',
    anchor='start',
    color='gray'
    )

    history.show()

    # n.b. browser window for second chart (plotly) will not be created until
    # the browser window for the first one (altair) is closed!

    fig = px.pie(df_net_assets, values="Current Value", names="Asset Class",
     title="Current Asset Allocation as of "+date, hover_data=["Current Value"], labels=["Asset Class"])
    fig.update_traces(textposition="inside", textinfo="value+label")
    fig.show()

if __name__ == "__main__":
    report_create()
    print("run directly")
