def uppercase(func):
    """ this is method decorator."""
    def wrapper(self):
        return func(self).upper()
    return wrapper

class MyPoem:
    @uppercase
    def read(self):
        return "smelly cat smelly cat what are they feeding you.."

obj = MyPoem()

help(uppercase)
print(obj.read())
