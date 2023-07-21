#following code use python to grab the stock index data from Yahoo Finance
import yfinance as yf 
start_date = "2003-01-01"
end_date = "2023-01-01"
NASDAQ=yf.download('^IXIC', start=start_date, end=end_date)
DJI=yf.download('DJI', start=start_date, end=end_date)
NASDAQ.to_csv('data/NASDAQ.csv')
DJI.to_csv('data/DJIA.csv')
SPX=yf.download('^GSPC', start=start_date, end=end_date)
SPX.to_csv('data/SPX.csv')
