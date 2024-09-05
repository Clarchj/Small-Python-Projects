def readNames(file_cat='', file_dog=''):
        try:
                with open(file_cat) as cat_file:
                        cat_file_content = cat_file.readlines()
                        print('cat names:')
                        for name in cat_file_content:
                                print(name.rstrip())
                with open(file_dog) as dog_file:
                        dog_file_content = dog_file.readlines()
                        print('dog names:')
                        for name in dog_file_content:
                                print(name.rstrip())
        except FileNotFoundError:
                pass
                
location_1 = 'E:\\Study\\ComputerScience\\Coding\\Exercises\\Small-Python-Projects\\PythonCrashCourse\\Chap2\\Chap10_Files\\cat'
location_2 = 'E:\Study\ComputerScience\Coding\Exercises\Small-Python-Projects\PythonCrashCourse\Chap2\Chap10_Files\dogs'
readNames(location_1, location_2)