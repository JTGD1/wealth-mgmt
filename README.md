**Portfolyo v1.0**  *by Justin Davda*

Tools to help with the monitoring and analysis of diverse financial asset portfolios, for Financial Advisors and HNW individuals.
This application offers the following features:

- Graphical display of point-in-time portfolio allocation across asset classes
- Graphical display of historical trends in net worth history & asset allocation
- Automatic email alerts for large prices moves on publically-traded assets
- In-application portfolio construction and maintenance tools

*Originally created as a term project for TECH 2335 (Programming in Python and the Fundamentals of Software Development) @ NYU Stern*


![](slide 1.PNG)
![](slide 2.PNG)
![](slide 3.PNG)
![](slide 4.PNG)
![](slide 5.PNG)
![](slide 6.PNG)
![](slide 7.PNG)
![](slide 8.PNG)
![](slide 9.PNG)
![](slide 10.PNG)

##
##

**To run:**

1) Create and activate a virtual environment e.g. in Gitbash (Anaconda is suggested):

```sh
conda create -n wealth-env
conda activate wealth-env
```


2) install packages required (e.g. using Pip):
   
```sh
pip install -r requirements.txt
```

   (Please ensure you are in the program root directory, i.e. not /app or /data)

3) populate a local *.env* file with the required API keys as follows:

*AlphaVantage*
```sh
ALPHAVANTAGE_API_KEY="ABC123XYZ"
```

(where ABC123XYZ is your private key)

*Sendgrid*
```sh
SENDGRID_API_KEY="ABC123XYZ"
```
and ensure that ".env" is a line in your *.gitignore* file (in the root directory for the application)

4) Also populate the *.env* file with **your** and **your client's** email addresses and preferred salutations:

```sh
MY_EMAIL_ADDRESS="justin.davda@stern.nyu.edu"
CLIENT_EMAIL_ADDRESS="barney@stinson.com"
MY_NAME="Justin Davda"
CLIENT_NAME="Barney Stinson Esq."
```

1) save the .env file in the main directory (i.e. not ~/app or ~/data)

2) from the Command Line, run the Python file app.py in the root (/wealth-mgmt) directory

```sh
python -m app.app
```

5) Follow the instructions on screen!


**To optionally set up automated alerting on large moves in the stocks and other exchange-traded products in your portfolio, follow steps below to setup a Heroku job:**

1) Clone the *wealth-mgmt* repo from Github to your local machine 
2) If you haven't yet done so, [install the Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up), and make sure you can login and list your applications.

```sh
heroku login # (first time access only)

heroku apps # (if using Heroku for the first time this may be empty) 
```    
3) Create a new Heroku application server
```sh
heroku create wealth-mgmt
```
4)  Configure Heroku environment variables using data from the *.env* file in the local environment
```sh
MV_API="blahblahblah"
SENDGRID_API_KEY="yadayadayada"

MY_EMAIL_ADDRESS="fred@flinstone.com"
CLIENT_EMAIL_ADDRESS="barney@rubble.com"

MY_NAME="Fred Flinstone"
CLIENT_NAME="Barney Rubble"
```
5) Deploy application source code to Heroku
```sh
git push heroku master
```
6) Finally, log in to the Heroku dashboard on the web and configure the "Heroku Scheduler" to run the *etp_update.py* program every day at 10pm UTC (5pm EST).  The command to execute is:
```sh
python -m app.etp_update
```
7) You will now receive an email update if any of the stocks or other exchange traded products in your portfolio move by more than 5% or 2.5 standard deviations (based on trailing 90 day volatility) on any given day.
    
    
  
    
>    Copyright (C) 2020  Justin Davda
>
>    This program is free software: you can redistribute it and/or modify
>    it under the terms of the GNU General Public License as published by
>    the Free Software Foundation, either version 3 of the License, or
>    (at your option) any later version.
>
>    This program is distributed in the hope that it will be useful,
>    but WITHOUT ANY WARRANTY; without even the implied warranty of
>    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
>    GNU General Public License for more details.
>
>    You should have received a copy of the GNU General Public License
>    along with this program.  If not, see <https://www.gnu.org/licenses/>.

To contact the author: justin.davda@stern.nyu.edu
