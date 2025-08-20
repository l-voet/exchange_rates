import requests
import datetime
import os
from dotenv import load_dotenv

"""
Endpoints:

latest.json
currencies.json
historical/2013-02-16.json

Free plan heeft max 1000 requests per maand en kan geen andere base currency aangeven maar opzich is dat niet nodig 
want de default is USD.
https://docs.openexchangerates.org/reference/api-introduction
Hier hoort een .env file bij met daarin alleen 'APP_ID=jouwappid'
"""

load_dotenv()
APP_ID = os.environ['APP_ID']
base_path = 'https://openexchangerates.org/api/'
endpoint = 'latest'
path = f'{base_path}/{endpoint}.json?app_id={APP_ID}'

# dict_keys(['disclaimer', 'license', 'timestamp', 'base', 'rates'])
result = requests.get(path).json()
usd_to_eur = result['rates']['EUR']
eur_to_usd = 1/usd_to_eur
print(f"Timestamp: {datetime.datetime.fromtimestamp(result['timestamp'])}\n"
      f"1 USD = {usd_to_eur:.3f} EUR\n"
      f"1 EUR = {eur_to_usd:.3f} USD")
