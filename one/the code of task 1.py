import os

print(os.getcwd())

os.chdir(r'C:\Users\LENOVO\Downloads\ir\section\tasks\one')

print(os.getcwd())

file_list = os.listdir()

search_word = input('enter the word')

for file_name in file_list:
    with open(file_name, 'r') as file:
        contents = file.read()
        if search_word in contents:
            print(f"The word '{search_word}' was found in '{file_name}'")
            x = file_name
            y = file_list.index(file_name)
            print(f'the index is : {y}')
            #print(y)