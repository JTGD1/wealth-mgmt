#update_files.py

# to allow for updating of csv files containing financial records

#with help from https://medium.com/swlh/adding-and-updating-data-in-csv-file-via-flask-api-252babbc6381
import os
import pandas as pd 


def update_ETP(asset_class,ticker,units,purchase_price):
    #pull in data from csv
    isThere = False 
    etp_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")
    df_etp = pd.read_csv(etp_filepath)
    
    try:
        check_asset_class = str(asset_class)
        check_ticker = str(ticker)
        check_units = int(units)
        check_purchase_price = float(purchase_price)
        
        if 0 > check_units or check_purchase_price < 0:
            invalid = "Invalid number - please check and try again"
            #print(invalid)
            return invalid            

    except ValueError:
        error = "Invalid format - please check and try again"
        #print(error)
        return error        

    for ind in df_etp.index:   
        if df_etp["Ticker"][ind] == ticker:              

        #if ticker already exists, just update units, purchase price
        
            df_etp.loc[df_etp["Ticker"] == ticker, ["Units"]] = units
            df_etp.loc[df_etp["Ticker"] == ticker, ["Purchase Price"]] = round(purchase_price,2)
            isThere = True
    
        #if ticker doesn't exist, add it to the end

        if isThere != True:
            df2 = pd.DataFrame({"Asset Class":[asset_class], 
            "Ticker":[ticker], 
            "Units":[units],"Purchase Price":[purchase_price]}) 

            dff = df_etp.append(df2, ignore_index = True)
            dff.to_csv(etp_filepath, index = False)

            action = "added"            
            
        else:
            
            df_etp.to_csv(etp_filepath, index = False) 
            action = "updated"
        
    #print(ticker,action)
    return action   

def delete_ETP(ticker):
    isThere = False
    etp_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")
    df_etp = pd.read_csv(etp_filepath)

    try:
        check_ticker = str(ticker)
        
    except ValueError:
        error = "Invalid format - please check and try again"
        print(error)
        return error
