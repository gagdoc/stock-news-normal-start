import requests
STOCK_NAME = "APP"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "AB124KBG8TTJ6Y3J"
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "slice": "year1month1",
    "apikey": STOCK_API_KEY,
}
# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TLSA&interval=5min&apikey=AB124KBG8TTJ6Y3J
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (60min)"]
data_list = [value for (key, value) in data.items()] #dict to list !!!!!
last_data = data_list[0]
last_day_closing_price = last_data["4. close"]
#TODO 2. - Get the day before yesterday's closing stock price
last_data_before = data_list[7]
last_data_before_price = last_data_before['4. close']
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(float(last_day_closing_price) - float(last_data_before_price))
print(f"오늘 마지막 종가 : {last_day_closing_price} - 어제 마지막 종가 : {last_data_before_price} = {difference}")

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_percent = (difference / float(last_day_closing_price)) * 100
print(f"증감% : {difference_percent} %")
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if difference_percent > 1 :
    print("get News")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

