import requests
import json
from datetime import date

api_key = open('NewsApi_key.txt', 'r')
key_content = api_key.read()
api_key.close()

today = date.today()

country = input(
    "Für Deutschland = de \n Für England = en \n Für USA = us \n Von welchem Land möchtest du News?...")
keyword = input("Nach was möchtest du suchen?...")


url = ('http://newsapi.org/v2/everything?'
       'q={}&'
       'country={}&'
       'from={}&'
       'sortBy=popularity&'
       'apiKey={}'.format(keyword, country, today, key_content))

response = requests.get(url)

news_data = json.loads(response.text)

print(news_data)
for articles in news_data["articles"]:
    print(articles["url"])
