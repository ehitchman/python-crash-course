##################################
from excercises_classes import Car

my_car = Car(make='hyundai', model='escape', year=1997)

print(my_car.get_descriptive_name())

my_new_car = Car(make='hyundai', model='escape', year=1997)

my_new_car.read_odometer()

my_new_car.update_odometer(21)
my_new_car.read_odometer()

my_new_car.update_odometer(19)
my_new_car.read_odometer()

my_new_car.update_odometer(24)
my_new_car.read_odometer()
