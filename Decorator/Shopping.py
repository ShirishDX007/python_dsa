from functools import wraps

def my_shopping(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"${result}"
    return wrapper

@my_shopping
def my_shopping_bill(price, discount):
    return price + price * (discount/100)

total_bill = my_shopping_bill(599, 8)
print(f"Total bill is : {total_bill}")

