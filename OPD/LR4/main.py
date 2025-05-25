from flask import Flask, render_template, request

app = Flask(__name__)


mock_rates = {
    'USD': {'EUR': 0.92, 'RUB': 90.0},
    'EUR': {'USD': 1.09, 'RUB': 97.0},
    'RUB': {'USD': 0.011, 'EUR': 0.0103}
}


def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount

    if from_currency in mock_rates and to_currency in mock_rates[from_currency]:
        rate = mock_rates[from_currency][to_currency]
        return round(amount * rate, 2)
    else:
        raise ValueError("Валютная пара недоступна")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_currency = request.form['from']
            to_currency = request.form['to']
            result = convert_currency(amount, from_currency, to_currency)
        except Exception as e:
            result = f"Ошибка: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
