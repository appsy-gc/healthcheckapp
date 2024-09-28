
# Parent class that gains all measurements
class Measurements:
    def __init__(self, weight, height, hip=None, waist=None, heart_rate=None):
        self.weight = weight
        self.height = height
        self.hip = hip
        self.waist = waist
        self.heart_rate = heart_rate

    def calculate(self):
        return "Calculate based on measurement"

    def __str__(self):
        return f"\nThank you for those measurements.\n"

# Child class that calculates BMI from all measurements
class BodyMassIndex(Measurements):
    def __init__(self, weight, height):
        super().__init__(weight, height)

    def calculate(self):
        self.bmi = round(self.weight / ((self.height / 100) ** 2), 2)
        if self.bmi >= 40:
            self.bmi_rating = "Obese III"
        elif self.bmi > 35:
            self.bmi_rating = "Obese II"
        elif self.bmi > 30:
            self.bmi_rating = "Obese I"
        elif self.bmi > 25:
            self.bmi_rating = "Overweight"
        elif self.bmi > 18.5:
            self.bmi_rating = "Healthy weight"
        else:
            self.bmi_rating = "Underweight"

        self.bmi_data = {
            "weight": self.weight,
            "height": self.height,
            "bmi": self.bmi,
            "bmi_rating": self.bmi_rating
        }

        return self.bmi_data

    def __str__(self):
        return f"Your BMI is {self.bmi:.2f}"

# Child class that calculates waist circumference from all measurements
class WaistToHip(Measurements):
    def __init__(self, hip, waist, sex):
        super().__init__(weight=None, height=None, hip=hip, waist=waist)
        self.sex = sex

    def calculate(self):
        self.whr = round(self.waist / self.hip, 2)

        if self.sex == "f":
            if self.whr <= 0.8:
                self.whr_rating = "Low Health Risk"
            if self.whr < 0.86:
                self.whr_rating = "Moderate Health Risk"
            else:
                self.whr_rating = "High Health Risk"
        else:
            if self.whr <= 0.95:
                self.whr_rating = "Low Health Risk"
            if self.whr < 1.0:
                self.whr_rating = "Moderate Health Risk"
            else:
                self.whr_rating = "High Health Risk"

        self.whr_data = {
            "hip": self.hip,
            "waist": self.waist,
            "whr": self.whr,
            "whr_rating": self.whr_rating
        }
        return self.whr_data
    
    def __str__(self):
        return f"Your waist to hip ratio is: {self.whr:.2f}, {self.whr_rating}"

# Child class that calculates max heart rate
class HeartRate(Measurements):
    def __init__(self, heart_rate):
        super().__init__(weight=None, height=None, heart_rate=heart_rate)

    def calculate(self):
        if self.heart_rate > 80:
            self.hr_rating = "High Heart Rate"
        elif self.heart_rate <= 80 and self.heart_rate >= 60:
            self.hr_rating = "Normal Heart Rate"
        else:
            self.hr_rating = "Low Heart Rate"

        self.hr_data = {
            "heart_rate": self.heart_rate,
            "hr_rating": self.hr_rating
        }
        return self.hr_data
        
    def __str__(self):
        return f"Your resting heart rate rating is: {self.hr_rating}"
