from flask import Flask
from dotenv import load_dotenv
from typing import Any, Optional, Dict
import requests, os

load_dotenv(dotenv_path='../.env')
YAHOOFINANCE = os.getenv('YAHOOFINANCE-API-KEY')
app = Flask(__name__)

@app.route('/stock/<name>')
def stock(name):
    return getNewsArticles(name)

@app.route('/index-funds/<name>')
def indexFunds(name):
    return name


def getNewsArticles(name:str) -> Dict[str, Any]:
    print(YAHOOFINANCE)
    url = 'https://yfapi.net/ws/insights/v1/finance/insights?symbol={symb}'.format(symb=name)
    header = {
        'accept': 'application/json',
        'X-API-KEY': YAHOOFINANCE
    }
    insight_results = requests.get(url, headers=header)
    return insight_results.json()

if __name__ =='__main__':
    app.run()