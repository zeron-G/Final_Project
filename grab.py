#following code use python to grab the stock index data from Yahoo Finance
import yfinance as yf
start_date = "1995-02-20"
end_date = "2023-07-17"
sz = yf.download('399001.SZ', start=start_date, end=end_date)
DJIA=yf.download('DJI', start=start_date, end=end_date)
NASDAQ=yf.download('^IXIC', start=start_date, end=end_date)
SS=yf.download('000001.SS', start=start_date, end=end_date)
sz.to_csv('data/399001sz.csv')
DJIA.to_csv('data/DJIA.csv')
NASDAQ.to_csv('data/NASDAQ.csv')
SS.to_csv('data/000001ss.csv')
