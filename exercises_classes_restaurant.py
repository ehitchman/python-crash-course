class Restaurant():
    """Basic model of a restaurant including the name and the cuisine type"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        long_description = self.name + " -- " + self.cuisine_type
        print('\n' + long_description)

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self, number_served):
        if number_served > self.number_served:
            self.number_served = number_served
        elif number_served == self.number_served:
            print("The current number of customres served is:" + 
            str(self.number_served))
        else: print("You can't roll back total number served")
            
    def increment_number_served(self, number_served):
        if number_served > 0:
            self.number_served += number_served
        else: "You can't serve a negative amount..."


class IceCreamStand(Restaurant):
    '''An Icecream stand is a type of restaurant with some slightly differenet 
       attributes.
       
       This is a good example of why you should not have default values in
       '''

    def __init__(self, name, cuisine_type, flavours: list, has_coffee: bool = None):
        super().__init__(name, cuisine_type)
        
        if isinstance(flavours, str):
            self.flavours = [flavours]
        else:
            self.flavours = flavours

        if has_coffee:
            self.has_coffee = has_coffee
        else: 
            self.has_coffee = False

    def display_flavours(self):
        print("We have these flavours:")
        for flavour in self.flavours:
            print('- ' + flavour)


class User():
    def __init__(
            self, first_name, last_name, user_name, password, email, 
            birthdate = None):

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.email = email
        if birthdate:
            self.birthdate = birthdate
        else:
            self.birthdate = 'N/A'
        self.login_attempts = 0

    def summarize_user(self):
        long_name = self.first_name.upper() + " " + self.last_name.upper()
        print('\n' + long_name)
        print('User Name: ' + self.user_name)
        print('Name: ' + long_name.title())
        print('Birth Date: ' + self.birthdate)
        print('Email: ' + self.email)

    def greet_user(self):
        print("Hello " + self.first_name.upper() + "! Welcome to the pizza restaurant")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    '''An admin has different privileges than a User'''

    def __init__(self, first_name, last_name, user_name, password, email):

        #seems redundant, unsure if var=val is necessary in subclass
        super().__init__(first_name, last_name, user_name, password, email)

        self.privileges = Privileges()


class Privileges():
    '''Houses privileges for admin users'''

    def __init__(self, privileges: list = None):
        if privileges:
            self.privileges = privileges
        else:
            self.privileges = ["None"]

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)







