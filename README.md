**Portfolio Performance & Reporting System v1.0**

Software to aid with the reporting and monitoring of financial asset portfolios, for Financial Advisors

*by Justin Davda*


**To run:**

1) Create and activate a virtual environment (Anaconda is suggested):

> conda create -n wealth-env
> conda activate wealth-env


2) install packages required (e.g. using Pip):
   
> pip install -r requirements.txt

   (Please ensure you are in the program root directory, i.e. not /app or /data)

3) populate a local *.env* file with the required API keys as follows:

*AlphaVantage*
> ALPHAVANTAGE_API_KEY="ABC123XYZ"
(where ABC123XYZ is your private key)

*Sendgrid*
> SENDGRID_API_KEY="ABC123XYZ"

4) Also populate the *.env* file with **your** and **your client's** email addresses and preferred salutations:

> MY_EMAIL_ADDRESS="justin.davda@stern.nyu.edu"
> CLIENT_EMAIL_ADDRESS="barney@stinson.com"
> 
> MY_NAME="Justin Davda"
> CLIENT_NAME="Barney Stinson Esq."

1) save the .env file in the main directory (i.e. not ~/app or ~/data)

2) from the Command Line, run the Python file app.py in the root (/wealth-mgmt) directory

> python -m app.app

5) Follow the instructions on screen!


**To optionally set up automated alerting on large moves in the stocks and other exchange-traded products in your portfolio, follow steps below to setup a Heroku job:**
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    Copyright (C) 2020  Justin Davda

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

To contact the author: justin.davda@stern.nyu.edu
