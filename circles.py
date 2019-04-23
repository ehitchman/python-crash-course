

import math

class Circle():

    version = '0.1'

    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour

    def area(self):
        print( str(math.pi * self.radius ** 2))

    def summary(self):
        print("The circle has a radius of " + str(self.radius) + "and is " + self.colour)

new_circle = Circle(2, 'red')

new_circle.summary
new_circle.area