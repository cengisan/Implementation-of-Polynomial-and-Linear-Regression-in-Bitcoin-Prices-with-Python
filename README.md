Hello!
 
In this project, I tried to estimate future price of Bitcoin. I used python-binance v1.0.15 and This is an unofficial Python wrapper for the Binance exchange REST API v3. You can read more via this link: https://python-binance.readthedocs.io/en/latest/

When I started to project, I needed to API key and API secret of my binance account for web scraping.

```java
api_key = ("Your API KEY")
api_secret = ("Your API SECRET")
```

I did not share my API key and API secret because of security of my account but if you want to use this code, you should take your API requirements from Binance.

In this section, I scraped all daily datas of the Bitcoin from 1 January 2022 to today. (You can change the date.)

```java
def all_time_prices():
    #All Datas of Bitcoin
    client = Client(api_key, api_secret)
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2022", "now")
    candles = candlesticks
```


I created a csv file that name is BTCUSDT and printed all datas of Bitcoin (Timestamps, Prices, Volumes, etc.). I should have made elimination in these datas. I opened BTCUSDT.csv file wtih genfromtxt and reached prices of Bitcoin with btc_data. I converted price datas to lista and printed again over BTCUSDT.csv.

with open('BTCUSDT.csv', 'w', newline='') as csvfile:
        candlestick_writer = csv.writer(csvfile, delimiter=',')
        for candlestick in candles:
            candlestick_writer.writerow(candlestick)
        csvfile.close()
```java
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
 ```

After all these scraping and eliminations, I started to write regression codes. But first, I should have set x and y axis for regression and graph. In this section, I created a empty list that name is j. After that, I appended in this list that how much data that I scraped from binancea and I defined x is number of day and y is bitcoin prices as values.

```java
def ai_estimation_graph():
    j = []
    i = 0
    while i < len(genfromtxt('BTCUSDT.csv')):
        j.append(i)
        i += 1
    X = np.array(j).reshape(-1, 1)
    y = np.array(genfromtxt('BTCUSDT.csv')).reshape(-1, 1)
```


Finally, I wrote linear regression and polynomial regression codes and machine learning calculated an estimate about future price of Bitcoin with dataset. After that, I printed results in a graph.

```java
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
```

This is the graph between 01.01.2022 and 19.03.2022. I don't know how can I interpret this graph but maybe it can work or not. :)

![graph](https://user-images.githubusercontent.com/77883086/159135537-0c92fc7c-36f4-4030-b26d-74135e4efb14.png)

Thanks for reading. I hope it can be useful for your goal.



 
