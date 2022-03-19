# @Cengisan
from binance.client import Client
import csv
from numpy import genfromtxt
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

api_key = ("Your API KEY")
api_secret = ("Your API SECRET")

def all_time_prices():
    #All Datas of Bitcoin
    client = Client(api_key, api_secret)
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2022", "now")
    candles = candlesticks

    with open('BTCUSDT.csv', 'w', newline='') as csvfile:
        candlestick_writer = csv.writer(csvfile, delimiter=',')
        for candlestick in candles:
            candlestick_writer.writerow(candlestick)
        csvfile.close()

    def get_historical_price():
        my_data = genfromtxt('BTCUSDT.csv', delimiter=',')
        #Data Elimination
        btc_data = my_data[:,4]
        Listformat = btc_data.tolist()
        with open('BTCUSDT.csv', 'w', newline='') as file:
            index_writer = csv.writer(file, delimiter=',')
            for i in Listformat:
                index_writer.writerow([i])
            csvfile.close()
    get_historical_price()

def ai_estimation_graph():
    j = []
    i = 0
    while i < len(genfromtxt('BTCUSDT.csv')):
        j.append(i)
        i += 1
    X = np.array(j).reshape(-1, 1)
    y = np.array(genfromtxt('BTCUSDT.csv')).reshape(-1, 1)
    #Fitting Linear Regression to the dataset
    
    lin = LinearRegression()
    lin.fit(X, y)
    # Fitting Polynomial Regression to the dataset
    
    poly = PolynomialFeatures(degree=4)
    X_poly = poly.fit_transform(X)
    lin2 = LinearRegression()
    lin2.fit(X_poly, y)
    # Visualising the Polynomial and Linear Regression results
    plt.scatter(X, y, color='blue')
    plt.plot(X, lin2.predict(poly.fit_transform(X)),lin.predict(X), color='red')
    plt.title('GRAPH')
    plt.xlabel('Day Numbers of the Year')
    plt.ylabel('Price')
    plt.show()
all_time_prices()
ai_estimation_graph()
