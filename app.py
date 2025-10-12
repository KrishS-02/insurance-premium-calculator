from flask import Flask, render_template, request

app = Flask(__name__)

class PremiumCalculator:
    def __init__(self):
        # Simplified mortality rates by age group and gender
        self.base_rate = {
            'male': {
                '18-30': 0.0010,
                '31-40': 0.0015,
                '41-50': 0.0025,
                '51-60': 0.0045,
                '61-65': 0.0080
            },
            'female': {
                '18-30': 0.0008,
                '31-40': 0.0012,
                '41-50': 0.0020,
                '51-60': 0.0038,
                '61-65': 0.0070
            }
        }
    def get_BMI(self, weight,height):
        return weight/(height*height)
    
    def get_age_group(self, age):
        if age <= 30:
            return '18-30'
        elif age <= 40:
            return '31-40'
        elif age <= 50:
            return '41-50'
        elif age <= 60:
            return '51-60'
        else:
            return '61-65'
    
    def calculate(self, age, gender, smoker, coverage,bmi):
        # Get base mortality rate
        age_group = self.get_age_group(age)
        base_rate = self.base_rate[gender][age_group]
        
        # Calculate base premium using actuarial formula
        # Premium = Coverage × Mortality Rate
        base_premium = coverage * base_rate
        
        # Add BMI factor
        bmi_multiplier = 1.0
        if bmi<18.5:
            bmi_multiplier = 1.1
        elif bmi>25:
            bmi_multiplier = 1.2

        # Apply risk factors
        smoking_multiplier = 1.0
        if smoker:
            smoking_multiplier = 1.3  # 30% increase for smokers
        
        risk_adjusted_premium = base_premium * smoking_multiplier * bmi_multiplier
        
        # Add loading for expenses and profit (25%)
        loading_factor = 1.25
        final_premium = risk_adjusted_premium * loading_factor
        
        return {
            'annual_premium': round(final_premium, 2),
            'monthly_premium': round(final_premium / 12, 2),
            'base_rate': base_rate,
            'base_premium': round(base_premium, 2),
            'smoking_factor': smoking_multiplier,
            'bmi_factor': bmi_multiplier,
            'loading': loading_factor,
            'age_group': age_group,
            'bmi': round(bmi,2)
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get form data
    age = int(request.form['age'])
    gender = request.form['gender']
    height_feet = float(request.form['height_feet'])
    height_inches = float(request.form['height_inches'])
    total_height = (height_feet*12 + height_inches) * 0.0254
    weight_kilogram = float(request.form['weight_kilogram'])
    weight_grams = float(request.form['weight_grams'])
    total_weight = weight_kilogram + (weight_grams/1000)
    weight = request.form['weight']
    smoker = request.form.get('smoker') == 'yes'
    coverage = int(request.form['coverage'])
    bmi = calc.get_BMI(total_weight,total_height)
    
    # Calculate premium
    calc = PremiumCalculator()
    result = calc.calculate(age, gender, smoker, coverage)
    
    # Pass both result and input data to template
    return render_template('result.html', 
                         result=result, 
                         age=age, 
                         gender=gender, 
                         smoker=smoker, 
                         coverage=coverage,
                         height_feet=height_feet,
                         height_inches=height_inches,
                         weight_kilogram=weight_kilogram,
                         weight_grams=weight_grams,
                         bmi=bmi)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
