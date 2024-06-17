

def my_shopping(func):
    
    def wrapper(name, *args, **kwargs):
        print(f"WElcome to the {name}")
        total_bill = func(name, *args, **kwargs)
        message = f"I went to {name} mall for shopping."
        return message, total_bill
    return wrapper

@my_shopping
def my_shopping_bill(name, price, discount):
    total_bill = price - price * (discount/100)
    return total_bill

mall_message, total_bill = my_shopping_bill("IKEA", 5999, 20)
print(mall_message)
print(f"Total bill is : ${total_bill}")


