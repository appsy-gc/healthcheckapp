class APSSLevel1:
    def __init__(self, q1, q2, q3, q4, q5, q6):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6

    def assess_questions(self):
        if self.q1 == "y" or self.q2 == "y" or self.q3 == "y" or self.q4 == "y" or self.q5 == "y" or self.q6 == "y":
            self.high_risk = True 
            self.health_risk = "Exercise presents a high risk to you. Please seek guidance from a general practitioner"
        else: 
            self.high_risk = False
            self.health_risk = "Exercise presents a low risk to you."
        
        apss_results = {
            "heart_condition": self.q1,
            "chest_pains": self.q2,
            "dizzy": self.q3,
            "asthma": self.q4,
            "diabetes": self.q5,
            "other_conditions": self.q6,
            "health_risk": self.health_risk
        }

        return apss_results

    # def __str__(self):
    #     return self.health_risk