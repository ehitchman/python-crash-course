#8-12 Sandwhiches
#Sandwhiches: Write a function that accepts a list of items a person wants on a 
# sandwhich. The function should have one parameter that colelcts as many items 
# as the function call provides, and it should print a summary of the sandwhich 
# that is being ordered. Call the function three times....

def sandwhich_toppings(*toppings):
    '''summarize the pizza u gonna make wit hsome printouts of the toppings'''
    print("this is your sandwhich:")
    for topping in toppings:
        print("- " + topping)

#sandwhich_toppings('ham','cucumber')


#8-13 User Profile
# Start with a copy of user_profile.py from page153.  Build a profile of 
# yourslef by calling the build_profile(), using your first and last names and 
# three other key value paris that describe you
def user_profile_create(first_name, last_name, **attributes):
    """create a user profile with mandatory first_name, last_name and optional
    attributes attached in the function call"""
    user_profile = {'first_name':first_name, 'last_name':last_name}
    for key, value in attributes.items():
        user_profile[key] = value
    return(user_profile)

#user_profile_create(first_name='Eric',last_name='Hitchman',birth_city='London, 
# Ontario', birth_date='1986-11-11')


#8-14 Cars
# Write a function that stores information about a car in a dictionary.  The 
# function should always receive a manufacturer and a model name.  it should 
# then accept an arbitrary number of keyword arguments.  Call the functoin with 
# req'd info and two other name-value pairs
def cars_input_details(manufacturer, model, **car_attributes):
    """creats a car dictionary with mandatory manufacturer and model parameters,
    and optional attributes attached in the function call"""
    car_dictionary = {'manufacturer':manufacturer, 'model':model}
    for key, value in car_attributes.items():
        car_dictionary[key] = value
    return(car_dictionary)
    
#cars_input_details(manufacturer='honda', model='camry', trim='blue', 
# type='sedan')
