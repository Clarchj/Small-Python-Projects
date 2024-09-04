file_to_read = 'E:\Study\ComputerScience\Coding\Exercises\Small-Python-Projects\PythonCrashCourse\Chap2\Chap10_Files\learning_python.txt'
with open(file_to_read) as file_object:
        file_read = file_object.read()
        string_list = file_read.split('\n')
        print('First time printing:\n',file_read.strip())
        print("Second time printing:\n")
        for line in string_list:
                print( line.rstrip())

print('third time printing:\n',)
for line in string_list:
                print( line.rstrip())
print('Other language are the same:')
for line in string_list:
        print(line.replace('python','JavaScript'))
                