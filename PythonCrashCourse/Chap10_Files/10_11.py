import json

user_favourite = input('What\'s your favourite number?')
store_location = 'PythonCrashCourse\Favourite Number.json'
with open(store_location, 'w') as f_object:
        json.dump(user_favourite ,f_object )
