import requests
import smtplib
import os
my_email=os.environ['SENDER_EMAIL'] #sender's email address
password=os.environ['EMAIL_PASS']
API_KEY_STK=os.environ['API_KEY'] #API key for platform getting stock prices https://www.alphavantage.co
STOCK = "TSLA" # replace with stock name
COMPANY_NAME = "Tesla Inc" #replace with the name of the company

API_KEY_NEWS=os.environ['API_KEY_NEWS'] #API key for platform to get news https://newsapi.org

receiver_email=os.environ['RECEIVER_EMAIL']

def is_relevant():
    parameters={
        'function':'TIME_SERIES_DAILY',
        'symbol':STOCK,
        'apikey':API_KEY_STK
    }
    response=requests.get(url='https://www.alphavantage.co/query',params=parameters)
    response.raise_for_status()
    data=response.json()
    #print(data)
    req_keys=list(data['Time Series (Daily)'].keys())
    direction=0
    price_yesterday=float(data['Time Series (Daily)'][req_keys[0]]['4. close'])
    price_before_yesterday=float(data['Time Series (Daily)'][req_keys[1]]['4. close'])
    percent_change= ((price_yesterday-price_before_yesterday)/price_before_yesterday)*100
    if percent_change<0:
        direction=-1
    else:
        direction=+1
    if abs(percent_change)>=5:
        return (get_news(),direction,abs(percent_change))
    return (None,None,None)

def get_news():
    parameters={
        'q':COMPANY_NAME,
        'language':'en',
        'pageSize':3,
        'apiKey':API_KEY_NEWS
    }
    response=requests.get(url='https://newsapi.org/v2/everything',params=parameters)
    response.raise_for_status()
    data=response.json()
    news_articles=data['articles']

    return news_articles

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    news_articles,direction,percentage=is_relevant()
    if news_articles is not None:
        i=0
        stock_direction='🔺' if direction==1 else '🔻'
        msg=f"Subject: News related to {STOCK} stock {stock_direction} by {percentage}% \n\n"
        for article in news_articles:
            i+=1
            msg+=f"{i}.{article['title']}:\n{article['description']}\n{article['url']}\n\n"
        connection.sendmail(from_addr=my_email,to_addrs=receiver_email,msg=msg.encode('utf-8'))




