


def generate_aliens_list(speed, color, points, list_size=1, *special_ability, **alien_details)    :
    """This function generates a list of alien dictionaries"""
    #@speed: the speed of the alien, slow/medium/fast
    #@param color: The color of the alien
    #@param points: Number of points for killing the alien
    #@param list_size=1: How many aliens should be created
    tempAliens = []
    
    for index in range(list_size):
    
        temp_alien = {'speed':speed, 'color':color, 'points':points}
    
        if special_ability:
            temp_alien['special_ability'] = list(special_ability)

        for key, value in alien_details.items():
            temp_alien[key] = value
            
        tempAliens.insert(index, temp_alien)

    return(tempAliens)
