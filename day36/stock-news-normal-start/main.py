import requests
import datetime as dt
from twilio.rest import Client

STOCK_NAME = "AMZN"
COMPANY_NAME = "Amazon.com, Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
account_sid = "???"
auth_token = "???"
today = dt.date.today()
yesterday = str(today - dt.timedelta(days=1))
before_yesterday = str(today - dt.timedelta(days=2))
actions_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": "OYKVCGUUOG7NFQ09"
}
actions_request = requests.get(url=STOCK_ENDPOINT, params=actions_parameters)
actions_request.raise_for_status()
actions_data_daily = actions_request.json()["Time Series (Daily)"]
slice_actions_data_daily = list(actions_data_daily.items())[:2]
# print(actions_data_daily)
# print(slice_actions_data_daily)

two_last_days_closing = {key: actions_data_daily[key]["5. adjusted close"] for (
    key, value) in slice_actions_data_daily[:2]}

diff_percentile = float(
    two_last_days_closing[yesterday]) / float(two_last_days_closing[before_yesterday]) * 100 - 100
print(diff_percentile)

if abs(diff_percentile) > 1:
    print("More than 1% of difference")
    print(diff_percentile)
# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# TODO 2. - Get the day before yesterday's closing stock price

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_params = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "sortBy": "popularity",
        "apiKey": '??'
    }

    news_request = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_request.raise_for_status()
    news_data = news_request.json()
    three_first_news = news_data["articles"][:3]
    # print(three_first_news)
# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    news_formatted_array = [(key["title"], key["description"])
                            for key in three_first_news]
    print(news_formatted_array)
# TODO 9. - Send each article as a separate me ssage via Twilio.
    client = Client(account_sid, auth_token)
    up_or_down = "🔺" if diff_percentile > 0 else "🔻"
    for news in news_formatted_array:
        message_to_send = f"""\n
            {STOCK_NAME}: {up_or_down}{round(diff_percentile, 2)}%
            Headline: {news[0]}
            Brief: {news[1]}
            """
        print(message_to_send)
        message = client.messages.create(
            body=message_to_send,
            from_="+14066413323",
            to="+5531984592603"
        )
        print(message.status)
# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
