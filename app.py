"""Forex Converter"""

from flask import Flask, request, render_template, redirect, flash, session
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'doesntmatter'


@app.route("/")
def currency_form():
    """Returns form for currency conversion"""

    return render_template('currency_form.html')

@app.route("/", methods=['POST'])
def currency_convert():
    """Handles currency form post request"""

    currency_rate = CurrencyRates()
    currency_code = CurrencyCodes()

    currency_from = request.form['currency_from']
    currency_to = request.form['currency_to']
    amount = float(request.form['amount'])

    symbol = currency_code.get_symbol(currency_to)

    try: 
        converted = currency_rate.convert(currency_from,currency_to,amount)

    except Exception as e:
        if 'Source Not Ready' in str(e):
            flash(f"{currency_from} is an invalid currency")
        if currency_to in str(e):
            flash(f"{currency_to} is an invalid currency")
        
        return render_template('currency_form.html')
    
    return render_template('currency_form.html',converted=converted,symbol=symbol)