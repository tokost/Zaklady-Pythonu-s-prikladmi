# Files consists of data and EOF 
# Files are stored at the path, the path differs accros windows and unix
# File lines ends with line endings CR LF, \r\n (WINDOWS :'()) or just the LF \n (MAC)

file_reader = open('FileFolder/data_file.txt')
file_reader.close() # Dont forget to close PLEASE 

# Using the python manager syntax 
with open("FileFolder/data_file.txt", "r") as file:
    print(file) 

# Open file types r-read, w-write, rb-read in binary mode, wb-write in binary mode
with open("FileFolder/data_file.txt", "r") as file:
    print(file.readline(1))
    print(file.readline(1)) # Guess the output
    print(file.readline(2)) # Guess the output 

with open("FileFolder/data_file.txt", "r") as file:
    print(file.readlines())


with open("data_file.txt", "r") as file:
    for line in file.readlines():
        print(line, end='')

with open("new_data_file", "w") as file:
    for word in ["Michal", "HUcko", "is", "good", "teacher"]:
        file.write(word)

# open data file and write it backward to backwards_data_file.py
with open("data_file.txt", "r") as file:
    data = file.readlines()

with open("backwards_data_file.py", "w") as file:
    for line in reversed(data):
        file.write(line)

# Appending to file 
with open("backwards_data_file.py", "a") as file:
    for number in [10, 9]:
        file.write(str(number))

# File from the directory
print("Example")
with open("FileFolder/data_file.txt", "r") as file:
    for line in file.readlines():
        print(line, end="")

