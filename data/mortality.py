# data/mortality.py

MORTALITY_TABLE = {
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

def get_age_group(age):
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
