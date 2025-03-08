from operator import attrgetter , itemgetter, methodcaller

class Product():
    def __init__(self, name, weight, price, discount):
        self.name = name
        self.weight = weight
        self.price = price
        self.discount = discount
    def __repr__(self):
        return repr((self.name, self.weight, self.price))

    def discountedPrice(self):
        return self.price - (self.price * self.discount)

prodList = [
    Product("Iphone 12", 26, 2999, 0.05),
    Product("Macbook Pro", 71, 4999, 0.02),
    Product("Motorola", 12.5, 1999, 0.05),
    Product("Hawaie", 8.9, 1459, 0.15),
    Product("Nothing Phone", 18.9, 2459, 0.25),

]

inventory= [("widget A", 6), ("widget B", 10), ("widget C", 1)]

#attrgetter() retrieves a given attribute or property from an object
print("using attrgetter method: ")
print(sorted(prodList, key=attrgetter('weight'), reverse=True))
print("_"*100)

#itemgetter() retrieves an item at a given index in a collection
print("using itemgetter method: ")
print(sorted(inventory, key=itemgetter(1)))
print("_"*100)

#methodcaller() calls a given method on an object
print("using methodcaller method: ")
print(sorted(prodList, key=methodcaller('discountedPrice'), reverse=True))
print("_"*100)

#from python shell
#>>> from operator import attrgetter , itemgetter, methodcaller
#getcount = itemgetter(1)
#lis(map(getcount, inventory))

