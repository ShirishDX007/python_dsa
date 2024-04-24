class Student:
    def __init__(self,name, phy, chem, Bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.Bio = Bio
        

    def total_Obtained(self):
        totals = sum([self.phy, self.chem, self.Bio])
        return totals


    def percentage(self):
        total_marks = 300
        percentages = (self.total_Obtained()/total_marks)*100
        return percentages
Steve = Student("Steve", 75, 85, 78)
print(Steve.total_Obtained(), Steve.percentage())

    




      
