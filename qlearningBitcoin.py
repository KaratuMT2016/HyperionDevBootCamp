from distutils import errors
import numpy as np 
import pandas as pd 
import seaborn as sbn
import matplotlib.pyplot as plt 
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


file_path = 'C:/Users/Dr. Karatu Musa/Desktop/HyperionDevBootCamp2023/BTC-USD.csv'

data = pd.read_csv('/Users/Dr. Karatu Musa/Desktop/HyperionDevBootCamp2023/BTC-USD.csv')

#print(data)

data_columns = data.head()

print(data_columns)

data_info = data.info()
print(data_info)

data_describe = data.describe()
print(data_describe,"\n")


data_null = data.isnull().sum()
print(data_null)

# Convert date format
data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d", errors = 'coerce')

# Visualize data
# Time series plotr

plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Close'], label = 'Closing Price')
plt.title('BTC Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.show()


# Plot Trading Volume Over Time

plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Volume'], color = 'orange', alpha = 0.5)
plt.title('BTC Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume of BTC')
plt.legend()
plt.show()

# Histogram

colors = ['orange', 'blue', 'green', 'red']
plt.figure(figsize=(10,5))

for index, column in enumerate(['Open', 'High', 'Low', 'Close']):
    plt.hist(data[column], bins = 20, alpha = 0.7, color = colors[index], label = column)

plt.title('Histograms of BTC Prices')
plt.xlabel('Price (USD)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# Select only numeric columns for correlation matrix

number_of_columns = data.select_dtypes(include=['float64']).columns
correlation = data[number_of_columns].corr()

# Plot the correlation headmap

plt.figure(figsize=(10,5))
sbn.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


# Feature scaling using Min-Max scaling

#scaler = MinMaxScaler()
#fs = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

# Apply Min-Max scaling to selected features
#data[fs] = scaler.fit_tranform(data[fs])

# Feature engineering

window_size = 10
data['SMA'] = data['Close'].rolling(window=window_size).mean()

# Display the preprocessed data

print("Preprocessed Data : ")
print(data.head())
