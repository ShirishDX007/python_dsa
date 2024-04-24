class Employee:
    def __init__(self, ID, Salary): #all properties are public
        self.ID = ID
        self.__Salary = Salary #Salary is private property
        
    def displaySalary(self):
        print("Salary: ", self.__Salary)


steve = Employee(223990, 95000)
print(steve._Employee__Salary)


      
