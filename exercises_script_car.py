##################################################
from exercises_classes_car import Car, ElectricCar

print('\n1) Create class instance from Car')
my_car = Car(make='hyundai', model='escape', year=1997)

print(my_car.get_descriptive_name())
print('---------------------')


#Create another class instance from Car
print('\n2) Create another class instance from Car')

my_new_car = Car(make='hyundai', model='escape', year=1997)
print(my_new_car.get_descriptive_name())
print('---------------------')

#Create a child-class instance from ElectricCar
print('\n3) Create a child-class instance from ElectricCar')
my_tesla = ElectricCar(make='testla', model='model s', year='2016')
print(my_tesla.get_descriptive_name())
print('---------------------')

#Test running some methods
print('\n4) Test running some methods')

print('\nRead Odometer')
my_new_car.read_odometer()

print('\nUpdate Odometer')
my_new_car.update_odometer(21)

print('\nRead Odometer')
my_new_car.read_odometer()

print('\nIncrement Odometer')
my_new_car.increment_odometer(100)

print('\nUpdate Odometer')
my_new_car.update_odometer(19)

print('\nRead Odometer')
my_new_car.read_odometer()

print('\nUpdate Odometer')
my_new_car.update_odometer(145)

print('\nRead Odometer')
my_new_car.read_odometer()
print('---------------------')


#9.9 -- battery upgrade
base_tesla_car = ElectricCar(make = 'Tesla', model = 'S12', year = 2019)
base_tesla_car.battery.describe_battery()
base_tesla_car.battery.get_range()
base_tesla_car.battery.upgrade_battery()
base_tesla_car.battery.get_range()
