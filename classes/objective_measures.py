
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
        self.bmi = self.weight / ((self.height / 100) ** 2)
        return self.bmi

    def __str__(self):
        return f"Your BMI is {self.bmi:.2f}"

# Child class that calculates waist circumference from all measurements
class WaistToHip(Measurements):
    def __init__(self, hip, waist):
        super().__init__(weight=None, height=None, hip=hip, waist=waist)

    def calculate(self):
        self.whr = self.waist / self.hip
        return self.whr
    
    def __str__(self):
        return f"Your waist to hip ratio is: {self.whr}"

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
        return self.hr_rating
        
    def __str__(self):
        return f"Your resting heart rate rating is: {self.hr_rating}"
