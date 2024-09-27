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
        else: 
            self.high_risk = False

    def __str__(self):
        return f"\nHigh Risk Client = {self.high_risk}\n"