import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


data=pd.read_csv('retail_data.csv')

# you split data into features (X) and target (y)    
X=data[['Feature1', 'Feature2', ...]]  # u replace with your relevant features
y=data['Demand']  # u replace with your target variable

# Then split data into training and testing sets
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)


model=LinearRegression()
model.fit(X_train, y_train)


y_pred= model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")


