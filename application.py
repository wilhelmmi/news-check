from sys import argv
from flask import Flask, render_template, request
import requests
import json
from datetime import date

application = Flask(__name__)

#api_key = open('NewsApi_key.txt', 'r')
#key_content = api_key.read()
#api_key.close()
key_content="Insert your own API Key here"
today = date.today()
counter = 100


def min_counter():
    global counter
    counter = counter - 1
    return counter

@application.route("/", methods=['POST', 'GET'])
@application.route("/news", methods=['POST', 'GET'])
def hello():
    # Für get requests
    #args = request.args
    #country = args.get("country")
    #keyword = args.get("keyword")

    return render_template("start.html", counter=counter)

@application.route("/counter")
def count():
    min_counter()
    print(counter)
    return "counter gezählt"

@application.route('/show_news', methods=['POST'])
def get_news():

    # Für POST requests
    country = request.form["country"]
    keyword = request.form["keyword"]
    category = request.form["category"]

    url = ('https://newsapi.org/v2/top-headlines?'
           'q={}&'
           'country={}&'
           'from={}&'
           'category={}&'
           'sortBy=popularity&'
           'apiKey={}'.format(keyword, country, today, category, key_content))

    min_counter()
    response = requests.get(url)
    news_data = json.loads(response.text)
    articles = news_data["articles"]

    return render_template("news.html", country=country, keyword=keyword, articles=articles)
