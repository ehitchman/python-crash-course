#9.1 - Restaurant
from exercises_classes_restaurant import Restaurant
from exercises_classes_restaurant import User
from exercises_classes_restaurant import IceCreamStand
from exercises_classes_restaurant import Admin
from exercises_classes_restaurant import Privileges


new_restaurant = Restaurant('milestones', 'bar/grill')
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

#9.3 - User
new_user = User(first_name = 'Eric', last_name = 'Hitchman', 
                user_name = 'ehitch',password = 'password',
                email = 'eh@address.com')
new_user.summarize_user()
new_user.greet_user()

#9.4 - Testing login attempts
new_user.increment_login_attempts()
print(new_user.login_attempts)

for i in range(19):
    new_user.increment_login_attempts()
print(new_user.login_attempts)

new_user.reset_login_attempts()
print(new_user.login_attempts)

for i in range(30):
    new_user.increment_login_attempts()
print(new_user.login_attempts)

#9.6 Ice Cream Stand -- Create class and display it
my_icecream_stand = IceCreamStand(
    name='Eric and Icecream', flavours = 'vanilla',
    cuisine_type = 'dessert'
    )  

my_icecream_stand.describe_restaurant()
my_icecream_stand.display_flavours()

#9.7 Admin User
new_admin = Admin(first_name = 'Eric', last_name = 'Hitchman', 
                  user_name = 'ehitch', password = 'pAssword',
                  email = 'email@address.com')

new_admin.summarize_user()
new_admin.privileges.show_privileges()


















