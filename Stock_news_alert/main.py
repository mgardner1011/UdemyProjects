import requests
import datetime as dt
from twilio.rest import Client

account_sid = 'Twilio_api_sid'
auth_token = 'twilio_auth_token'

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api_key = 'alpha_vantage_api_key'
news_api_key = 'news_api_key'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

today = dt.datetime.now().date()
lag_1day = str(today - dt.timedelta(days=1))
lag_2day = str(today - dt.timedelta(days=2))
up_down = ''
percent_change = 0

stock_parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': stock_api_key,
    'pageSize': 3,
    'page': 1,
}

news_parameters = {
    'q': COMPANY_NAME,
    'from': lag_2day,
    'to': lag_1day,
    'sortBy': 'publishedAt',
    'apiKey': news_api_key,
}

# Make api request to stock api
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

# Get closing price
try:
    lag_1day_close = float(stock_data['Time Series (Daily)'][lag_1day]['4. close'])
except KeyError:
    lag_1day_close = None
try:
    lag_2day_close = float(stock_data['Time Series (Daily)'][lag_2day]['4. close'])
except KeyError:
    lag_2day_close = None

# Find percent change, and set up_down symbol
if lag_1day_close is not None and lag_2day_close is not None:
    difference = lag_1day_close - lag_2day_close
    percent_change = round((difference / lag_1day_close) * 100)
    if difference < 0:
        up_down = '🔻'
    else:
        up_down = '🔺'

# Make api request to get news articles
news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
top_news = news_data['articles'][:3]
news_title_list = [top_news[_]['title'] for _ in range(len(top_news))]
news_description_list = [top_news[_]['description'] for _ in range(len(top_news))]

# Send text messages
if percent_change >= 5 or percent_change <= -5:
    for i in range(len(news_title_list)):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f'{STOCK}: {up_down}{percent_change}%\nHeadline: {news_title_list[i]}\nBrief: {news_description_list[i]}',
            from_='+19257226085',
            to='+15551234567'
        )
