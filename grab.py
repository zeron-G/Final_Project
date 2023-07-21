#following code use python to grab the stock index data from Yahoo Finance
import yfinance as yf 
start_date = "2003-01-01"
end_date = "2023-01-01"
NASDAQ=yf.download('^IXIC', start=start_date, end=end_date)
SS=yf.download('000001.SS', start=start_date, end=end_date)
NASDAQ.to_csv('data/NASDAQ.csv')
SS.to_csv('data/000001ss.csv')
