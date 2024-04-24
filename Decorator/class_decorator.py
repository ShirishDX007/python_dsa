from functools import wraps

class star:
    def __init__(self, n):
        self.n = n

    def __call__(self,func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(self.n*'*')
            result = func(*args, **kwargs)
            print(result)
            print(self.n*'*')
            return result
        return wrapper

@star(5)
def add(a , b):
    return (a + b)

add(3, 23)

