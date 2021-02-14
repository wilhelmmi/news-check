import os

os.environ["FLASK_APP"] = "front.py"
os.environ["FLASK_DEBUG"] = "1"

os.system("flask run")
