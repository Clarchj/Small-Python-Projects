import json

store_location = 'PythonCrashCourse\\Favourite Number.json'
try:
        with open(store_location) as f_object:
                number = json.load(f_object)
except FileNotFoundError:
        x = input('What\'s your favourite number?')
        with open(store_location, 'w') as f_object:
                number = json.dump( x , f_object)
        print('We\'ll have ur number:'+ number +' when you comeback')
else:
        print('your number is already stored' + ' ' + number)
