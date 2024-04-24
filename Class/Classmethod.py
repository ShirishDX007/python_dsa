class BodyInfo:
    Gym_name = "BodyZone"
   
    def __init__(self,weight, height):
        self.weight = weight
        self.height = height

    @staticmethod
    def bmi_calculator(weight, height):
        return weight / (height ** 2)
        

    @classmethod
    def bmi(cls):
        return cls.Gym_name

weight = 60
height = 1.5
print(BodyInfo.bmi_calculator(weight, height))
print(BodyInfo.bmi())

      
