import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def predict_storage(csv_data):
    # Load CSV data into a DataFrame
    df = pd.read_csv(csv_data)

    # Perform data preprocessing and feature engineering here

    # Split the data into features (X) and target (y)
    X = df.drop(columns=['Storage'])  # Replace 'Storage' with your target column name
    y = df['Storage']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)

    # Calculate evaluation metric (MAE for example)
    mae = mean_absolute_error(y_test, predictions)

    return {'predictions': predictions.tolist(), 'mae': mae}

# Example usage:
if __name__ == '__main__':
    # Replace 'data.csv' with the path to your CSV file
    result = predict_storage('/home/youssef/Desktop/stage_ete/A2SV/A2SV_RetailAI/web_app/app/test.csv')
    print(result)
