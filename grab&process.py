import pandas as pd
import yfinance as yf
# Load the data
start_date = "2012-01-01"
end_date = "2017-12-31"
spx=yf.download('^GSPC',start=start_date, end=end_date)
data=spx.reset_index()
three_years_data = data[data['Date'] > data['Date'].max() - pd.DateOffset(years=3)]
two_years_data = data[data['Date'] > data['Date'].max() - pd.DateOffset(years=2)]
freq_seven_data = data.iloc[::7, :]
freq_seven_mean_data = data.resample('7D', on='Date').mean()
freq_30_data = data.resample('30D', on='Date').mean()
five_years_data = data
three_years_data.to_csv('process/SPX_3years.csv')
two_years_data.to_csv('process/SPX_2years.csv')
freq_seven_data.to_csv('process/SPX_freq7.csv')
freq_seven_mean_data.to_csv('process/SPX_freq7_mean.csv')
five_years_data.to_csv('process/SPX_5years.csv')
freq_30_data.to_csv('process/SPX_freq30.csv')
NASDAQ=yf.download('^IXIC', start=start_date, end=end_date)
DJI=yf.download('DJI', start=start_date, end=end_date)
NASDAQ.to_csv('data/NASDAQ.csv')
DJI.to_csv('data/DJIA.csv')
spx.to_csv('data/SPX.csv')