import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

apii_key = "applyhere"
account_sid = "applyhere"
auth_token = "applyhere"

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": apii_key,
}

url = requests.get("https://www.alphavantage.co/query", params=parameters)
url.raise_for_status()
data = url.json()["Time Series (Daily)"]
data_list = [day for day in data.items()]
daily_yesterday = data_list[0]
daily_yesterday_before = data_list[1]
daily_yesterday_close_price = daily_yesterday[1]["4. close"]
daily_yesterday_close_before_price = daily_yesterday_before[1]["4. close"]

daily_yesterday_value = float(daily_yesterday_close_price)
daily_yesterday_before_value = float(daily_yesterday_close_before_price)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
percentage_diff = (daily_yesterday_value - daily_yesterday_before_value)
up_down = None
if percentage_diff > 0:
    up_down = "⬆️"
else:
    up_down = "🔻"

difference_in_proc = round((percentage_diff / float(daily_yesterday_value)) * 100, 2)

if abs(difference_in_proc) >= 5:
    print("Get News")
    news_appi_key = "applyhere"

    querystring = {"q": "\"Tesla Inc\"", "lang": "en", "sort_by": "relevancy", "page": "1"}

    headers = {
        "x-api-key": news_appi_key,
    }
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_url = requests.request("GET", "https://api.newscatcherapi.com/v2/search", headers=headers, params=querystring)
    news_url.raise_for_status()
    news_data = news_url.json()["articles"]
    newest_3_articles = news_data[0:3]

    formatted_articles = [f"{STOCK}: {up_down}{difference_in_proc}%\nHeadline: {article['title']}. \nBrief: " \
                          f"{article['summary']}" for article in newest_3_articles]

    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+yournr",
            to="+yournr"
        )
        print(message.status)
