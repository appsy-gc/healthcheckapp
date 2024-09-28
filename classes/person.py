
# Parent class for creating a person
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Hi {self.name}, you are {self.sex} and {self.age} years old."

# Child class for females
class Female(Person):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.at_risk = "Your age group has a lower risk of chronic health conditions."
    # Increase to at risk person if 55 and over
    def risk_cat(self):
        if self.age >= 55:
            self.at_risk = "Your age group has a higher risk of chronic health conditions."
        return self.at_risk

    # def __str__(self):
    #     return self.at_risk

# # Child class for males
class Male(Person):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.at_risk = "Your age group has a lower risk of chronic health conditions."
    # Increase to at risk person if 45 and over
    def risk_cat(self):
        if self.age >= 45:
            self.at_risk = "Your age group has a higher risk of chronic health conditions."
        return self.at_risk
        
    # def __str__(self):
    #     return self.at_risk
