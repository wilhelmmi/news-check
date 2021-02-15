# Project Title

Simple Web-App to get the latest news

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Prerequisites

The App is build on the Python based  Flask-Framework. So you need Python3 and pip3 running.
The App also uses the newsapi.org so to make things work, you have to get your own newsapi key from newsapi.org and replace it in the NewsApi_Key.txt or just with
the key_content variable in the application.py file. If you want to use the .txt the just uncomment the api_key part in the application.py file.

### Installing

It is recommended to use a virtual environment. The use of a venv allows you to manage the dependencies for the project. 
To create a environment navigate into the /FLASK2 project folder then

for Windows

```
py -3 -m venv venv
```
to activate your venv 

for Windows

```
venv\Scripts\activate
```

Now to install all the requirements run 
```
pip3 install -r requirements.txt
```
### Start flask 

Open the terminal in the project folder and 
```
set FLASK_APP=application.py
```
to run the flask server simply 
```
flask run
```