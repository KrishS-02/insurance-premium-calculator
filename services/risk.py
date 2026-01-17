# services/risk.py

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def bmi_multiplier(bmi):
    if bmi < 18.5:
        return 1.1
    elif bmi <= 22:
        return 0.95
    elif bmi <= 25:
        return 1.0
    else:
        return 1.2

SMOKING_RISK = {
    "non-smoker": 1.0,
    "former-smoker": 1.1,
    "light-smoker": 1.2,
    "moderate-smoker": 1.3,
    "heavy-smoker": 1.5
}

TOBACCO_RISK = {
    "non-chewer": 1.0,
    "former-chewer": 1.1,
    "occasional-chewer": 1.2,
    "regular-chewer": 1.3,
    "heavy-chewer": 1.5
}

ALCOHOL_RISK = {
    "non-alcoholic": 1.0,
    "former-drinker": 1.1,
    "light-drinker": 1.15,
    "moderate-drinker": 1.25,
    "heavy-drinker": 1.4
}
