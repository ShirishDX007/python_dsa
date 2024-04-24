def currency(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Total Bill: ${result}"
    return wrapper

@currency
def net_price(price, tax):
    return price * (1 + tax)
print(net_price(123, 0.05))
print(net_price.__name__)
