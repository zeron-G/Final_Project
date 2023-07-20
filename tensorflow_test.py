from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.callbacks import EarlyStopping
# Select the 'Close' column as the target variable
data=pd.read_csv('data/DJIA.csv')
data['Date'] = pd.to_datetime(data['Date'])
data_close = data['Close'].values

# Normalize the data
scaler = MinMaxScaler(feature_range=(0,1))
data_close_scaled = scaler.fit_transform(data_close.reshape(-1,1))

# Convert time series data into supervised learning problem
window_size = 60
X, Y = [], []
for i in range(window_size, len(data_close_scaled)):
    X.append(data_close_scaled[i-window_size:i, 0])
    Y.append(data_close_scaled[i, 0])
X, Y = np.array(X), np.array(Y)

# Reshape X to fit the model
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, shuffle=False)

# Define the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=False, input_shape=(X_train.shape[1], 1)))
model.add(Dense(units=1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Define the early stopping
early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Display the model summary
model.summary()
# Train the model
history = model.fit(
    X_train, Y_train, 
    epochs=50, 
    batch_size=32, 
    validation_data=(X_test, Y_test), 
    callbacks=[early_stop], 
    shuffle=False
)
# Predict the 'Close' prices
predictions = model.predict(X_test)

# Apply inverse transformation to get back original scale
predictions = scaler.inverse_transform(predictions)