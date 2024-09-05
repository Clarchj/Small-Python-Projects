def get_city_function(city,country,population=''):
        if population:
                return(city + ', ' +country +'-population:' + str(population)).title()
        else:
                return(city + ', ' +country).title()

