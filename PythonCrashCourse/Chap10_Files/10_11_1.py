import json

store_location = 'PythonCrashCourse\\Favourite Number.json'
with open(store_location) as f_object:
        user_number = json.load(f_object)
print('Your number is' + ' ' + user_number)