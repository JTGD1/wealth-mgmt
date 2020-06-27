#update_files.py

# to allow for updating of csv files containing financial records

#with help from https://medium.com/swlh/adding-and-updating-data-in-csv-file-via-flask-api-252babbc6381
import os
import pandas as pd 


def delete_item(identifier, df, filepath):

    #isThere = False
    try:
        check_ticker = str(identifier)

    except ValueError:
        error = "Invalid format - please check and try again"
        print(error)
        return error
    
    exists = df["Identifier"].str.contains(identifier).any()

    if exists == True: 
        df.drop(df[df.Identifier == identifier].index, inplace=True)
        df.to_csv(filepath, index=False)
        action = "deleted"   

    elif exists != True:
        action = "not found"

    else:
        action = "error!"

    #print(identifier,action)
    return action


def update_etp(asset_class,identifier,units,purchase_price):
    #pull in data from csv
    isThere = False 
    etp_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")
    df_etp = pd.read_csv(etp_filepath)
    #check inputs
    try:
        check_asset_class = str(asset_class)
        check_identifier = str(identifier)
        check_units = int(units)
        check_purchase_price = float(purchase_price)
        
        if 0 > check_units or check_purchase_price < 0:
            invalid = "Invalid number - please check and try again"
            return invalid            

    except ValueError:
        error = "Invalid format - please check and try again"
        return error        
    #update or append
    for ind in df_etp.index:   
        if df_etp["Identifier"][ind] == identifier:              

        #if ticker already exists, just update units, purchase price
        
            df_etp.loc[df_etp["Identifier"] == identifier, ["Units"]] = units
            df_etp.loc[df_etp["Identifier"] == identifier, ["Purchase Price"]] = round(purchase_price,2)
            isThere = True
    
        #if ticker doesn't exist, add it to the end

        if isThere != True:
            df2 = pd.DataFrame({"Asset Class":[asset_class], 
            "Identifier":[identifier], 
            "Units":[units],"Purchase Price":[purchase_price]}) 

            dff = df_etp.append(df2, ignore_index = True)
            dff.to_csv(etp_filepath, index = False)

            action = "added"            
            
        else:
            
            df_etp.to_csv(etp_filepath, index = False) 
            action = "updated"
        
    #print(identifier,action)
    return action   

def delete_etp(identifier):
    
    filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")
    df = pd.read_csv(filepath)
    
    delete_item(identifier, df, filepath)
    return


def delete_asset(identifier):

    filepath = os.path.join(os.path.dirname(__file__),
                            "..", "data", "other_assets.csv")
    df = pd.read_csv(filepath)

    delete_item(identifier, df, filepath)
    return
    

def delete_liability(identifier):

    filepath = os.path.join(os.path.dirname(__file__),
                            "..", "data", "liabilities.csv")
    df = pd.read_csv(filepath)

    delete_item(identifier, df, filepath)
    return

def update_asset(asset_class,identifier,current_value):
    #pull in data from csv
    isThere = False 
    asset_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "other_assets.csv")
    df_asset = pd.read_csv(asset_filepath)
    #check inputs
    try:
        check_asset_class = str(asset_class)
        check_identifier = str(identifier)
        check_current_value = float(current_value)
        
        if check_current_value < 0:
            invalid = "Invalid number - please check and try again"
            return invalid            

    except ValueError:
        error = "Invalid format - please check and try again"
        return error        
    #update or append
    for ind in df_asset.index:   
        if df_asset["Identifier"][ind] == identifier:              

        #if ticker already exists, just update current value
        
            df_asset.loc[df_asset["Identifier"] == identifier, ["Current Value"]] = round(current_value,2)
            isThere = True
    
        #if ticker doesn't exist, add it to the end and make purchase price = current value

        if isThere != True:
            df2 = pd.DataFrame({"Asset Class":[asset_class], 
            "Identifier":[identifier], 
            "Purchase Value":[current_value],"Current Value":[current_value]}) 

            dff = df_asset.append(df2, ignore_index = True)
            dff.to_csv(asset_filepath, index = False)

            action = "added"            
            
        else:
            
            df_asset.to_csv(asset_filepath, index = False) 
            action = "updated"
        
    print(identifier, action)
    return action


def update_liability(asset_class, identifier, current_value):
    #pull in data from csv
    isThere = False
    liability_filepath = os.path.join(os.path.dirname(
        __file__), "..", "data", "liabilities.csv")
    df_liability = pd.read_csv(liability_filepath)
    #check inputs
    try:
        check_asset_class = str(asset_class)
        check_identifier = str(identifier)
        check_current_value = float(current_value)

        if check_current_value < 0:
            invalid = "Invalid number - please check and try again"
            return invalid

    except ValueError:
        error = "Invalid format - please check and try again"
        return error
    #update or append
    for ind in df_liability.index:
        if df_liability["Identifier"][ind] == identifier:

            #if ticker already exists, just update current value

            df_liability.loc[df_asset["Identifier"] == identifier,
                         ["Current Value"]] = round(current_value, 2)
            isThere = True

        #if ticker doesn't exist, add it to the end and make purchase price = current value

        if isThere != True:
            df2 = pd.DataFrame({"Asset Class": [asset_class],
                                "Identifier": [identifier],
                                "Purchase Value": [current_value], "Current Value": [current_value]})

            dff = df_liability.append(df2, ignore_index=True)
            dff.to_csv(liability_filepath, index=False)

            action = "added"

        else:

            df_liability.to_csv(asset_filepath, index=False)
            action = "updated"

    print(identifier, action)
    return action

