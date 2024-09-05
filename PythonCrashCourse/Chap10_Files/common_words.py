def findCommonWords(file='', word=''):
        try:
                with open(file, encoding="utf-8") as file_object:
                        file_content = file_object.read()
                repeated_word = file_content.lower().count('word')
                print('The word' +' '
                      + word +' '
                      + ' appeared' +' '
                      + str(repeated_word) +' '
                      + 'times in this document')
        except FileNotFoundError:
                print('this document does not exist')   

file_location = "E:\\Download\\Python Data Science Handbook.txt"
findCommonWords(file_location, 'json')     
       