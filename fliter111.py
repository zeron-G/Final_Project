print("Script started")
import pandas as pd
import numpy as np
import yfinance as yf
from statsmodels.tsa.stattools import adfuller
from pmdarima import auto_arima
import matplotlib.pyplot as plt

# Download historical data for NASDAQ Composite index
data = yf.download('^IXIC', start='1995-02-21')

# We will use "Close" price for analysis
data = data['Close']

print(data.head())  # This will print the first five rows of your data

# Function to perform the Augmented Dickey Fuller test
def ADF_Test(series):
    result = adfuller(series)
    return result[1]  # return p-value

best_aic = np.inf
best_order = None
best_model = None

# Check ARIMA models for different start dates
for start_date in pd.date_range(start='1995-02-21', end=data.index[-1]):

    # Filter data from start_date
    filtered_data = data[start_date:]

    # Skip if filtered_data has less than 100 observations
    if len(filtered_data) < 100:
        continue

    # Test stationarity using ADF test
    p_value = ADF_Test(filtered_data)
    if p_value > 0.05:
        # If series is non-stationary, take first difference and test again
        filtered_data = filtered_data.diff().dropna()
        p_value = ADF_Test(filtered_data)
        if p_value > 0.05:
            # If series is still non-stationary, skip this start date
            continue

    # Determine the ARIMA order using auto_arima (it uses AIC as default metric)
    model = auto_arima(filtered_data, seasonal=True, m=12, suppress_warnings=True)

    # Update best model, AIC, and order
    if model.aic() < best_aic:
        best_aic = model.aic()
        best_order = model.order
        best_model = model
        best_start_date = start_date

print(f'Best Start Date: {best_start_date}')
print(f'ARIMA Order: {best_order}')
print(f'Best AIC: {best_aic}')
