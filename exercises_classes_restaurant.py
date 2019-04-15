class Restaurant():
    """Basic model of a restaurant including the name and the cuisine type"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        long_description = self.name + " -- " + self.cuisine_type
        return(long_description)

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self, number_served):
        if number_served > self.number_served:
            self.number_served = number_served
        else: "You can't roll back total number served"

    def increment_number_served(self, number_served):
        if number_served > 0:
            self.number_served += number_served
        else: "You can't serve a negative amount..."

class User():
    def __init__(
            self, first_name, last_name, user_name, password, email='NA', age=0, 
            birthdate='NA'):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.email = email
        self.age = age
        self.birthdate = birthdate
        self.login_attempts = 0

    def summarize_user(self):
        long_name = self.first_name + " " + self.last_name 
        print('User Name: ' + self.user_name)
        print('Name: ' + long_name.title())
        print('Age: ' + str(self.age))
        print('Birth Date: ' + self.birthdate)
        print('Email: ' + self.email)

    def greet_user(self):
        print("Hello " + self.first_name + "!  Welcome to the pizza restaurant...")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



