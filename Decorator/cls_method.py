class Person:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        Person.counter += 1
    def Greet(self):
        return f"Hi it's me {self.name}"

    @staticmethod
    def top_secret(n):
        return f"My PAN number is {n}"

    @classmethod
    def create_anynomus(cls):
        return Person('Annie', 23)

ananymus = Person.create_anynomus()
greetings = ananymus.Greet()
print(greetings)
print(ananymus.name, ananymus.age)
secrets = Person.top_secret(456)
print(secrets)