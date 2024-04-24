from functools import wraps

def my_shopping(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"${result}"
    return wrapper

@my_shopping
def my_shopping_bill(price, discount):
    return price * (discount/100)
print(my_shopping(599, 8))

