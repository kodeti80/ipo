from flask import Flask, render_template, request
from ipo_data import ipo_details

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    company = request.form['company'].strip()
    lots = int(request.form['lots'])
    info = ipo_details.get(company)

    if not info:
        return render_template('result.html', error=f"Company '{company}' not found.")

    chance = min(95, max(5, 10 + lots * 8))

    return render_template('result.html',
                           company=company,
                           info=info,
                           lots=lots,
                           chance=chance)

if __name__ == '__main__':
    app.run()
