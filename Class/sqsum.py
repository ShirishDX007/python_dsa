class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        squares = (self.x**2, self.y**2, self.z**2)
        return squares, sum(squares)

points = Point(1 ,3, 5)
squares, total_sum = points.sqSum()
print(total_sum)




      
