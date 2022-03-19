Hello!
 
In this project, I tried to estimate Bitcoin prices in the future. I used python-binance v1.0.15 and This is an unofficial Python wrapper for the Binance exchange REST API v3. You can read more via this link: https://python-binance.readthedocs.io/en/latest/

When I started to project, I needed to API key and API secret of my binance account for web scraping.

![apikey](https://user-images.githubusercontent.com/77883086/159115566-1505e6e0-97cb-4571-83b4-c99547ee73d1.png)

I did not share my API key and API secret because of security of my account but if you want to use this code, you should take your API requirements from Binance.

In this section, I scraped all daily datas of the Bitcoin from 1 January 2022 to today. (You can change the date.)

![alltimeprices](https://user-images.githubusercontent.com/77883086/159116142-1e00e898-164a-48cc-8a2c-99e99f3850b1.png)


I created a csv file that name is BTCUSDT and printed all datas of Bitcoin (Timestamps, Prices, Volumes, etc.). I should have made elimination in these datas. I opened BTCUSDT.csv file wtih genfromtxt and reached prices of Bitcoin with btc_data. I converted price datas to lista and printed again over BTCUSDT.csv.

![historicalprice](https://user-images.githubusercontent.com/77883086/159116416-a4f4eca0-5056-4dd9-b44b-92b09279c128.png)

After all these scraping and eliminations, I started to write regression codes. But first, I should have set x and y axis for regression and graph. In this section, I created a empty list that name is j. After that, I appended in this list that how much data that I scraped from binancea and I defined x is number of day and y is bitcoin prices as values.

![list](https://user-images.githubusercontent.com/77883086/159135022-8bab57ba-8783-4fb2-aaf0-481dd1aca583.png)

Finally, I wrote linear regression and polynomial regression codes and machine learning calculated an estimate about future price of Bitcoin with dataset. After that, I printed results in a graph.

![regression](https://user-images.githubusercontent.com/77883086/159135367-82d68145-cb92-4fc1-8700-f29d53ef7f33.png)

This is the graph between 01.01.2022 and 19.03.2022. I don't know how can I interpret this graph but maybe it can work or not. :)

![graph](https://user-images.githubusercontent.com/77883086/159135537-0c92fc7c-36f4-4030-b26d-74135e4efb14.png)

Thanks for reading. I hope it can be useful for your goal.



 
