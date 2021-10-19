from flask import Flask
from type import Any, Optional, Dict

app = Flask(__name__)

@app.route('/stock/<name>')
def stock(name):
    return name

@app.route('/index-funds/<name>')
def indexFunds(name):
    return name


def getNewsArticles(name:str):
    pass

if __name__ =='__main__':
    app.run()