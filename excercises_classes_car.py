class Car():
    """A simple class storing information about the kind of car we're working
    with, and it will have a method that summarizes this information."""
    
    def __init__(self, make, model, year):
        """assign each parameter as an attribute to this class"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print the vlue of odometer"""
        print("This car has " + str(self.odometer) + " miles on it!")

    def update_odometer(self, mileage):
        """update the mileage with the input amount"""
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back the odometer")

