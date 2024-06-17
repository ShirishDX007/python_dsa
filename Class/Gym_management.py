class Gym_info:
    Gym_name = "Spartans"  # Class variable for gym name

    def __init__(self, member_name, age, weight, height):
        self.member_name = member_name
        self.age = age
        self.weight = weight
        self.height = height

    @staticmethod
    def calculate_BMI(weight, height):

        bmi = weight / (height**2)  # Correct BMI formula
        return round(bmi, 2)

    @classmethod
    def gym_membership(cls):
        """Returns the name of the gym.

        Returns:
            str: The gym name ("Spartans" in this case).
        """
        return cls.Gym_name  # Direct access to class variable

    @classmethod
    def member_info(cls, member_name, age, weight, height):  # Added arguments for member info
        member = cls(member_name, age, weight, height)  # Create an instance to access self
        return {"member_name": member.member_name, 
                "age": member.age,
                "weight": member.weight,
                "height": member.height
        }
# Usage
my_gym_name = Gym_info.gym_membership()
print("My gym name is: ", my_gym_name)
my_bmi = Gym_info.calculate_BMI(65, 1.75)
print("My BMI: ", my_bmi)
member_info = Gym_info.member_info("John Doe", 30, 65, 1.75)  # Provide member details
print("Member Info:", member_info)