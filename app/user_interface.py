# user_interface.py
# basic menus and decision-making around what user wants to do

from app.update_files import update_etp
from app.update_files import delete_etp

import os

asset_class = "Equity"
identifier = "GOOG"
units = 10
purchase_price = 100

#update_ETP(asset_class, identifier, units, purchase_price)

delete_etp(identifier)
