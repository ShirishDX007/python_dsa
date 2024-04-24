class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / (height ** 2)

weight = 60
height = 1.5
print(BodyInfo.bmi(weight, height))

      
