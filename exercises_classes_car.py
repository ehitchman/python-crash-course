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
        '''Print a summary of the Car'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print the vlue of odometer"""
        print("This car has " + str(self.odometer) + " miles on it!")

    def update_odometer(self, mileage):
        """update the mileage with the input amount"""
        if mileage > self.odometer:
            self.odometer = mileage
            print("Odomoter updated to: " + str(self.odometer))
        else:
            print("You can't roll back the odometer.  Odometer currently: " +
                   str(self.odometer))
        return self.odometer

    def increment_odometer(self, mileage):
        """update the mileage with the input amount"""
        if mileage > 0:
            self.odometer += mileage
            print('Odometer Updated to: ' + str(self.odometer))
        else:
            print("You can't drive negative miles...")
        return self.odometer


class Battery():
    """A simple attempte to model a battery for an ElectricCar"""

    def __init__(self, battery_size = 70):
        """Initialize the Battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print("\nThis car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        range = self.battery_size * 2.5
        print("\nbased on 2.5km per kWh, this car has a range of " + str(range))

    def upgrade_battery(self):
        '''Check battery size and update to 85 if battery size is currently less 
           than that '''

        if self.battery_size < 85:
            self.battery_size = 85
            print("\nBattery size updated: Currently at " + str(self.battery_size))
        else:
            print("\nBattery size is already >= 85.  Currently battery_size is " +
            str(self.battery_size))
        return self.battery_size


class ElectricCar(Car):
    """Represents aspects of a Car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initializes attributes of the parent class, then initializes default 
        and any other attributes, including the instance attribute"""
        super().__init__(make, model, year)
        self.battery = Battery()


