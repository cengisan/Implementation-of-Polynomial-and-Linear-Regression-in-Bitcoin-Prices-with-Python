Hello!
 
In this project, I tried to estimate Bitcoin prices in the future. I used python-binance v1.0.15 and This is an unofficial Python wrapper for the Binance exchange REST API v3. You can read more via this link: https://python-binance.readthedocs.io/en/latest/

When I started to project, I needed to API key and API secret of my binance account for web scraping.

![apikey](https://user-images.githubusercontent.com/77883086/159115566-1505e6e0-97cb-4571-83b4-c99547ee73d1.png)

I did not share my API key and API secret because of security of my account but if you want to use this code, you should take your API requirements from Binance.

In this section, I scraped all daily datas of the Bitcoin from 1 January 2022 to today.

![alltimeprices](https://user-images.githubusercontent.com/77883086/159116142-1e00e898-164a-48cc-8a2c-99e99f3850b1.png)


I created a csv file that name is BTCUSDT and printed all datas of Bitcoin (Timestamps, Prices, Volumes, etc.). I should have made elimination in these datas. I opened BTCUSDT.csv file wtih genfromtxt and reached prices of Bitcoin with btc_data. I converted price datas to lista and printed again over BTCUSDT.csv.

![historicalprice](https://user-images.githubusercontent.com/77883086/159116416-a4f4eca0-5056-4dd9-b44b-92b09279c128.png)

