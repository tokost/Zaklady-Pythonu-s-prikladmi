"""
Example:
Write an function called display_pattern that will based on the input number output following patter
****
***
**
* 
In case of number 4

input: number of rows 
output: None

example: display_pattern(4)
"""

def display_pattern(rows):
    for y_dimension in range(rows, 0, -1):
        for x_dimension in range(y_dimension):
            print("*", end='')
        print('')

display_pattern(6)

nested_list = [
    [0, 1,2],
    [3,4],
    [5,7,9, 10],
    [0]
]

print(nested_list[1][1])

# Print the grid
for row in nested_list:
    for element in row:
        print(element, end=" ")
    print()

# Find the size of the longest row and print the row
# 1. print the lenght for each row 
# 2. find the max lenght 
# 3. find the longest row
max=0
memory=[]
for row in nested_list:
    if len(row) > max:
        max = len(row)
        memory = row

print(f"Longest row is {memory} with the length of {max}")

# enumerate function 
names = ["Michal", "Felipe", "John", "Katarina"]
print(names)
print(list(enumerate(names)))

max=0
memory=[]
memory_index=0
for index,name in enumerate(names):
    if len(name) > max:
        max = len(name)
        memory = name
        memory_index=index
print(f"Longest name is {memory} with the length of {max} at the index {memory_index}")


