from flask import Flask
import copy
from flask import request, redirect, url_for
import json

app = Flask(__name__)

dic_currencies = {1: [
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
    {"FJD": 2.2014},
    {"GBP": 0.8353},
    {"ILS": 3.4311}], 2: [
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
    {"FJD": 2.2014},
    {"GBP": 0.8353},
    {"ILS": 3.4311}], 3: [
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
    {"FJD": 2.2014},
    {"GBP": 0.8353},
    {"ILS": 3.4311}], 4: [
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
    {"FJD": 2.2014},
    {"GBP": 0.8353},
    {"ILS": 3.4311}], 5: [
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
    {"FJD": 2.2014},
    {"GBP": 0.8353},
    {"ILS": 3.4311}], 6: [
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
    {"FJD": 2.2014},
    {"GBP": 0.8353},
    {"ILS": 3.4311}], 7: [
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
    {"FJD": 2.2014},
    {"GBP": 0.8353},
    {"ILS": 3.4311}]}

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
    {"FJD": 2.2014},
    {"GBP": 0.8353},
    {"ILS": 3.4311}]


@app.route('/clear/<int:team_id>', methods=['GET'])
def clear_list(team_id):
    dic_currencies[team_id] =copy.deepcopy(currencies)
    return 'Done',200


@app.route('/currency/<int:team_id>', methods=['GET', 'POST'])
def getUsers(team_id):
    if request.method == 'GET':
        return json.dumps(dic_currencies[team_id])
    elif request.method == 'POST':
        currency = request.get_json()
        for c in dic_currencies[team_id]:
            if c.keys() == currency.keys() or list(currency.values())[0] <= 0:
                return 'currency Exist or the value is not valid 404 ', 404
        else:
            dic_currencies[team_id].append(currency)
        return json.dumps(dic_currencies[team_id]), 201


@app.route('/update_currency/<int:team_id>', methods=['POST'])
def update_currency(team_id):
    currency = request.get_json()
    if currency in dic_currencies[team_id]:
        key = list(currency.keys())[0]
        for c in dic_currencies[team_id]:
            if list(c.keys())[0] == key:
                c[key] = currency[key]
                return 'created',201
    else:
        dic_currencies[team_id].append(currency)
    return json.dumps(dic_currencies[team_id])


app.run()
