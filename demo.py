import requests
from flask import Flask

app = Flask(__name__)

def fetch_price(ticker):
    data = requests.get('https://financialmodelingprep.com' \
    '/api/v3/stock/real-time-price/{}' \
    .format(ticker.upper()), params={'apikey': 'demo'}).json()
    return data["price"]

@app.route('/stocks/')
def stock(ticker):
    stock_price = fetch_price(ticker)
    return "The price of {} is {}".format(ticker, stock_price)

@app.route('/')
def home():
    return "This is the home page. Try going to /stocks/AAPL"
