


def generate_aliens_list(speed, color, points, list_size=1, special_ability=''):
    """This function generates a list of alien dictionaries"""
    #@speed: the speed of the alien, slow/medium/fast
    #@param color: The color of the alien
    #@param points: Number of points for killing the alien
    #@param list_size=1: How many aliens should be created
    tempAliens = []
    for alien_number in range(list_size):
        temp_alien = {'speed':speed, 'color':color, 'points':points}
        if special_ability:
            temp_alien['special_ability'] = special_ability
        tempAliens.append(temp_alien)
    print("List of aliens created:")
    #print(temp_alien)
    return(tempAliens)
