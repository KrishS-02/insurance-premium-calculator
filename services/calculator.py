from data.mortality import MORTALITY_TABLE, get_age_group

class PremiumCalculator:

    def __init__(self, loading_factor = 1.25):
        self.loading_factor = loading_factor
    
    def calculate_premium(self, age, gender, coverage, risk_multiplier):
        age_group = get_age_group(age)
        base_rate = MORTALITY_TABLE[gender][age_group]

        base_premium = coverage * base_rate
        
        risk_adjusted = base_premium * risk_multiplier
        final_premium = risk_adjusted * self.loading_factor
        
        return {
            'age_group': age_group,
            'base_rate': base_rate,
            'base_premium': round(base_premium, 2),
            'final_premium': round(final_premium, 2),
            'monthly_premium': round(final_premium/12,2),
            'loading': self.loading_factor
        }