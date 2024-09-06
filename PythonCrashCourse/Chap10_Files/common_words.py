import re

def findSentencesWithWord(input_file='', word='', output_file='output.txt'):
    try:
        with open(input_file, encoding="utf-8") as file_object:
            file_content = file_object.read()

        # Use regex to split the file content into sentences
        sentences = re.split(r'(?<=[.!?]) +', file_content)
        
        # Create a list to store sentences containing the word
        matching_sentences = []

        # Search each sentence for the word (case insensitive)
        for sentence in sentences:
            if word.lower() in sentence.lower():
                matching_sentences.append(sentence.strip())
        
        # Write the matching sentences to a new file
        with open(output_file, 'w', encoding="utf-8") as output:
            for sentence in matching_sentences:
                output.write(sentence + '\n')

        print(f'Found {len(matching_sentences)} sentence(s) containing the word "{word}".')
        print(f'The results have been saved in "{output_file}".')
        
    except FileNotFoundError:
        print('The input file does not exist.')

input_file_location = "E:\\Download\\Tuyển dụng Archives - Giao hàng 6h trong ngày.html"
output_file_location = "E:\\Download\\sentences_with_python.txt"
findSentencesWithWord(input_file_location, 'python', output_file_location)