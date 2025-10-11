# Insurance Premium Calculator

A web application that calculates life insurance premiums using actuarial principles, providing complete transparency in how premiums are determined.

## 🎯 Features

- Premium calculation based on age, gender, and lifestyle factors
- **Actuarial transparency** - detailed breakdown of how each factor affects cost
- Based on standard mortality tables and actuarial formulas
- Clean, responsive user interface
- Educational tool demonstrating InsurTech application

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Bootstrap
- **Methodology:** Actuarial science principles

## 📊 Actuarial Methodology

The calculator uses:
- Standard mortality rates by age group and gender
- Risk adjustment factors (smoking: +30%)
- Industry-standard loading factors for expenses and profit (25%)
- Formula: `Premium = (Coverage × Mortality Rate × Risk Factors) × Loading`

## 🚀 Live Demo

https://insurance-premium-calculator-emtf.onrender.com/

## 💻 Local Setup
```bash
# Clone the repository
git clone https://github.com/KRISHS02/insurance-premium-calculator.git
cd insurance-premium-calculator

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Open browser and visit
http://localhost:5000
