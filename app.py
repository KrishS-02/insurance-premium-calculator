from flask import Flask, render_template, request
from services.calculator import PremiumCalculator
from services.risk import (
    calculate_BMI,
    bmi_multiplier,
    SMOKING_RISK,
    ALCOHOL_RISK,
    TOBACCO_RISK
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    age = int(request.form['age'])
    gender = request.form['gender']

    height = ((float(request.form['height_feet']) * 12 + 
               float(request.form['height_inches'])) * 0.0254)
    weight = float(request.form['weight_kilogram']) + \
             float(request.form['weight_grams']) / 1000
    coverage = int(request.form['coverage'])
    bmi = calculate_BMI(weight, height)

    total_risk_multiplier = (
        bmi_multiplier(bmi) * 
        SMOKING_RISK[request.form['smoker']] *
        ALCOHOL_RISK[request.form['alcoholic']] *
        TOBACCO_RISK[request.form['chewer']]
    )
    calculator = PremiumCalculator()
    result = calculator.calculate_premium(
        age, gender, coverage, total_risk_multiplier
    )

    result['bmi'] = round(bmi,2)
    return render_template('result.html', result= result)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
