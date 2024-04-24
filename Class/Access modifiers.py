class Employee:
    def __init__(self, ID, Salary): #all properties are public
        self.ID = ID
        self.Salary = Salary

    def displayID(self):
        print("ID: ", self.ID)

steve = Employee(223990, 95000)
steve.displayID()
print(steve.Salary)


      
