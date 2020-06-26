#update_files.py

#web app to allow for updating of csv files containing financial records

import pandas as pd 
 
def addETP(asset_class,ticker,units,purchase_price):
# Creating the first Dataframe using dictionary 
 isThere = False
 
# Creating the first Dataframe using dictionary 
etp_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")
df_etp = pd.read_csv(etp_filepath)
 
try:
new_asset_class = str(asset_class)
new_ticker = str(ticker)
new_units = int(units)
new_purchase_price = float(round(purchase_price,2))
print(new_asset_class,new_ticker,new_units,new_purchase_price)

if( 0 > new_units or new_purchase_price < 0):
invalid = “invalid”
return invalid

except ValueError:
error = “error”
return error

for index, row in df_etp.iterrows(): 
    print(row[‘Asset Class’], row[‘Ticker’]) 
    if str(row[‘Asset Class’]) == str(asset_class) and str(row[‘Ticker’]) == str(ticker):
        row['Units'] = units 
        row['Purchase Price'] = purchase_price
        isThere = True

#Creating the Second Dataframe using dictionary 

if isThere != True: 

df2 = pd.DataFrame({“user-id”:[userId], 
“event-id”:[eventId], 
“rating”:[rating]}) 

dff = df1.append(df2, ignore_index = True)
dff.to_csv(r’./rating.csv’, index = False)

add = “added”
return add

else:
df1.to_csv(r’./rating.csv’, index = False) 
update = “updated”
return update