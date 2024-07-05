class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1 + p2)