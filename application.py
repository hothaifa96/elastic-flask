from flask import Flask
from flask import request, redirect, url_for
import json

app = Flask(__name__)

currencies = [
    {"ANG": 1.7900},
    {"USD": 1},
    {"AED": 3.6725},
    {"AFN": 89.6941},
    {"ALL": 114.2457},
    {"AOA": 429.9365},
    {"ARS": 129.051},
    {"AMD": 413.2282},
    {"AUD": 1.4426},
    {"AWG": 1.7900},
    {"AZN": 1.6941},
    {"BAM": 1.9178},
    {"BBD": 2.0000},
    {"BTN": 79.9633},
    {"EUR": 0.9806},
    {"FJD":2.2014},
    {"GBP": 0.8353},
    {"ILS": 3.4311}]

@app.route('/currency', methods=['GET', 'POST'])
def getUsers():
    if request.method == 'GET':
        return json.dumps(currencies)
    elif request.method == 'POST':
        currency = request.get_json()
        # user["id"]=request.form['id';
        # user["id"]=request;
        # user["id"]=re;
        print(currency)
        currencies.append(currency)
        return json.dumps(currencies)


@app.route('/users/<int:id>', methods=['GET'])
def getUSerById(id):
    if request.method == 'GET':
        if id < len(currencies):
            return json.dumps(currencies[id - 1])
        else:
            return 'we dont have this currency '


app.run()
