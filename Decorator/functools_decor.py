from functools import wraps

def currency(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"${result}"
    return wrapper

@currency
def net_price(price, tax):
    """ calculate the net price from the price
    and tax."""
    gst = 0.08
    cgst = 0.09
    tax_gst = gst +  cgst
    return price * (1+ tax_gst + tax)

help(net_price)
print(net_price(456, 0.05))
