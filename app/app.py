#app.py

#from flask import Flask, request, jsonify
#from update_files import update_ETP
#
#app = Flask(__name__)
#
#@app.route("/etp", methods=["POST"])
#
#def addETP():
#    new_asset_class = request.form["asset_class"] 
#    new_ticker = request.form["ticker"]
#    new_units = request.form["units"]
#    new_purchase_price = request.form["purchase_price"]
#    print(asset_class," ",ticker," ",units)
#    status = addETP(asset_class,ticker,units,purchase_price)
#    return status
#
## Running the server in localhost:5000 
#if __name__ == "__main__":
#    app.run(debug=True, host="0.0.0.0", port=5000)
#
