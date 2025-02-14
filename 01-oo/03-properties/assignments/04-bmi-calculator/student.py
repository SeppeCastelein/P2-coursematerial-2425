class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.weight_in_kg = weight_in_kg
        self.height_in_m = height_in_m

    @property
    def bmi(self):
        return round(self.weight_in_kg / (self.height_in_m ** 2), 2)
    
    @property
    def category(self):
        bmi = self.bmi
        if bmi < 18.5:
            return "underweight"
        elif 18.5 <= bmi < 25:
            return "normal"
        else:
            return "overweight"

# Example usage:
calc = BMICalculator(weight_in_kg=93, height_in_m=1.80)
print(calc.bmi)       # Output: 24.69
print(calc.category)  # Output: normal