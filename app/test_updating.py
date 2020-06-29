#test updates.py


from app.update_files import update_etp
from app.update_files import update_asset
from app.update_files import update_liability
from app.update_files import delete_etp
from app.update_files import delete_liability
from app.update_files import delete_asset
import os
import pandas as pd

from app.etp_update import update_etps
from app.create_report import report_create

asset_input = "Equity"
id_input = "BAC"
units_input = 1000
purchase_input = 10


update_etp(asset_input, id_input, units_input, purchase_input)
print("file updated")
