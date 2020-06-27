# user_interface.py
# basic menus and decision-making around what user wants to do

from update_files import update_ETP
import os

asset_class = "Equity"
ticker = "C"
units = 10
purchase_price = 100

update_ETP(asset_class, ticker, units, purchase_price)
