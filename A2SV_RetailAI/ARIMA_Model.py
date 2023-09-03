import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

#(ensure it includes a timestamp and demand)
data = pd.read_csv('retail_data.csv')
data['Timestamp'] = pd.to_datetime(data['Timestamp'])  # Convert timestamp column to datetime

# Set the timestamp as the index
data.set_index('Timestamp', inplace=True)

# resample data to a daily frequency (or the appropriate frequency)
daily_data = data['Demand'].resample('D').sum()  # u can change the frequency ('D' for daily)

# split data into training and testing sets
train_size = int(len(daily_data) * 0.8)
train, test = daily_data[:train_size], daily_data[train_size:]


model = ARIMA(train, order=(5,1,0))  # u guys can tune the order parameters
model_fit = model.fit(disp=0)


predictions = model_fit.forecast(steps=len(test))[0]

# Mean Squared Error
mse = mean_squared_error(test, predictions)
print(f"Mean Squared Error: {mse}")

# Plot
plt.plot(test.index, test.values, label='Actual Demand')
plt.plot(test.index, predictions, color='red', label='Predicted Demand')
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Demand')
plt.show()

