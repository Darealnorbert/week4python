filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    try:
        content = file.read()
        content_upper = content.upper()
    except FileNotFoundError:
        print(f'{filename} has not been found, please check the file name .')
