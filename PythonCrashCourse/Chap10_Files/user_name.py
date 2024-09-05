file_name='PythonCrashCourse\\Chap2\\Chap10_Files\\guest.txt'
book_file='PythonCrashCourse\\Chap2\\Chap10_Files\\guest_book.txt'
with open(book_file,'a') as file_object:
        while True:
                p_lang=input('What\'s ur favourite programming language?')
                if p_lang.lower() == 'quit':
                        break
                print( p_lang + ', interesting choice')
                file_object.write(str(p_lang)+'\n')
                
        