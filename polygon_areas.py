# Create class and sub-class objects which represent different geometrical shapes, such as rectangles and squares.
# Represent geometry shapes as classes and give them the ability to compute routine geometry calculations in the 
# forms of class methods. Leverage class parent/child relationships to extend class functionality.

class Polygon:
    def __init__(self, num_of_sides, length, width, height):
        self.num_of_sides = num_of_sides
        self.length = length
        self.width = width
        self.height = height

class Square(Polygon):
    def __init__(self, num_of_sides, length, width, height):
        super().__init__(num_of_sides, length, width, height)
    def area():
        self.length^2

class Rectangle(Polygon):
    def __init__(self, num_of_sides, length, width, height):
        super().__init__(num_of_sides, length, width, height)