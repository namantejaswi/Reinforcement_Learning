import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import yahoo_fin  as ya_fin 
from yahoo_fin import stock_info

msft=yf.Ticker("MSFT")

msft_hist=msft.history(period="max")

print(type(msft_hist))
print(msft_hist.head())
print(msft_hist.columns)

print(msft_hist['Close'])

sns.lineplot(data=msft_hist['Close']).set_title("MSFT Stock Price")
plt.show()



def visualise(ticker):
    ticker_hist=yf.Ticker(ticker).history(period="max")
    sns.lineplot(data=ticker_hist['Close']).set_title(ticker+" Stock Price")
    plt.show()

    dividend=yf.Ticker(ticker).dividends
    sns.lineplot(data=dividend).set_title(" Dividend Payout by"+ticker)
    plt.show()


ticker_list=["GOOG", "AAPL","TSLA","INTC","NVDA","AMZN"]

for stock in ticker_list:
    visualise(stock)

def indices():
    Dow_Jones = stock_info.tickers_dow()
    print("Dow_Jones",Dow_Jones)
    Snp_500 = stock_info.tickers_sp500()
    #print("Snp_500",Snp_500)
    Nasdaq = stock_info.tickers_nasdaq()
    #print("Nasdaq",Nasdaq)
    Nifty = stock_info.tickers_nifty50()
    #print("Nifty",Nifty)
    Bank_Nifty = stock_info.tickers_niftybank()
    #print("Bank_Nifty",Bank_Nifty)

indices()


def quote(stock):
    quote=yf.Ticker(stock).info
    #print(quote)

def valuations(stock):
    
    value=stock_info.get_stats_valuation(stock)
    print(value)

valuations("GOOG")
