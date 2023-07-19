import pandas as pd
import yfinance as yf 
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import numpy as np


start_date = "1995-02-20"
end_date = "2023-07-17"
data=pd.read_csv('data/DJIA.csv')
data['Date'] = pd.to_datetime(data['Date'])
log_data=np.log(data['Close'])
model = ARIMA(log_data, order=(5,1,0))
# Set 'Date' as the index
data.set_index('Date', inplace=True)

# # Plot the 'Close' column
# plt.figure(figsize=(10,6))
# plt.plot(log_data, color='blue')
# #plt.plot(data['Close'], color='red')
# plt.title('Dow Jones Industrial Average Closing Price')
# plt.xlabel('Date')
# plt.ylabel('Close Price')
# plt.grid(True)
# plt.show()

# Fit the model without the 'disp' parameter
model_fit = model.fit()

# Summary of the model
print(model_fit.summary())
# Forecast the next 10 days
forecast = model_fit.forecast(steps=10)

# Create a new dataframe to store the forecast
forecast_df = pd.DataFrame(forecast, columns=['Forecast'])

# Create a new date range
#forecast_df.index = pd.date_range(start=data.index[-1], periods=10)[1:]

# # Plot the original data and the forecast
# plt.figure(figsize=(10,6))
# plt.plot(data['Close'], label='Original Data')
# plt.plot(forecast_df, label='Forecast', linestyle='--')
# plt.title('Dow Jones Industrial Average Closing Price Forecast')
# plt.xlabel('Date')
# plt.ylabel('Close Price')
# plt.grid(True)
# plt.legend()
# plt.show()

