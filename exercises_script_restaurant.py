#9.1 - Restaurant
from exercises_classes_restaurant import Restaurant
from exercises_classes_restaurant import User

the_restaurant = Restaurant('milestones', 'bar/grill')
print(the_restaurant.describe_restaurant())
the_restaurant.open_restaurant()

#9.3 - User
the_user = User('Eric','Hitchman','ehitch','password', age=32,)
the_user.summarize_user()
the_user.greet_user()

#Testing login attempts
the_user.increment_login_attempts()
print(the_user.login_attempts)

for i in range(19):
    the_user.increment_login_attempts()
print(the_user.login_attempts)

the_user.reset_login_attempts()
print(the_user.login_attempts)

for i in range(30):
    the_user.increment_login_attempts()
print(the_user.login_attempts)

#
