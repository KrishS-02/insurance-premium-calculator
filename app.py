# app.py

from flask import Flask, render_template, request
from services.calculator import PremiumCalculator
from services.risk import (
    calculate_bmi,
    bmi_multiplier,
    SMOKING_RISK,
    TOBACCO_RISK,
    ALCOHOL_RISK
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():

    age = int(request.form['age'])
    gender = request.form['gender']

    height_m = ((float(request.form['height_feet']) * 12 +
                 float(request.form['height_inches'])) * 0.0254)

    weight_kg = float(request.form['weight_kilogram']) + \
                float(request.form['weight_grams']) / 1000

    coverage = int(request.form['coverage'])

    bmi = calculate_bmi(weight_kg, height_m)

    total_risk_multiplier = (
        bmi_multiplier(bmi) *
        SMOKING_RISK[request.form['smoker']] *
        TOBACCO_RISK[request.form['chewer']] *
        ALCOHOL_RISK[request.form['alcoholic']]
    )

    calculator = PremiumCalculator()
    result = calculator.calculate_premium(
        age, gender, coverage, total_risk_multiplier
    )

    result["bmi"] = round(bmi, 2)

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
