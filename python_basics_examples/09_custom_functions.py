"""
Functions are written in blocks, except the function declaration part which is not indented. 

Functions have: 
- Name a-z, A-Z, _
- Input parameters <optional> : can be everything also a function (will be explained in advanced tutorial)
- Output value <optional> : can be everything also a function (will be explained in advanced tutorial)

! Python is dynamically typed language so we dont have to define parameters types, but we can :)
"""

def addition(a, b):
    result = a + b
    return result

addition(5,4)
addition("Michal" , "Hucko")

# What if there is no return statement ? (besure to reload the function deffinition)

# x = 5 + 4 +3 
addition(addition(5, 4), 3)
addition(addition(addition(addition("Michal" , "Hucko"), "is"), "the"), "best")

def string_addition_with_delimiter(string1, string2, delimiter):
    return string1 + delimiter + string2

string_addition_with_delimiter("Michal" , "Hucko", ", ")
string_addition_with_delimiter(delimiter=" ", string2="Hucko", string1="Michal")

# Optional parameters 
def string_addition_with_delimiter(string1, string2, delimiter=" "):
    return string1 + delimiter + string2

string_addition_with_delimiter("Michal" , "Hucko")
string_addition_with_delimiter("Michal" , "Hucko", ", ")

## ! Optional arguments must be defined after positional non-default argument
# def string_addition_with_delimiter(delimiter=" ", string1, string2):
#     return string1 + delimiter + string2


# Function to sum the numbers in the list 
numbers = list(range(7))
print(numbers)

def sum_list(numbers): # you cannot call the parameter list its a reserved word !
    total = 0 
    for number in numbers:
        total += number
    return total

sum_list(numbers)
sum(numbers) # build in python function 
# sum_list(["M", "i", "c", "h", "a", "l"]) # why is this an error ? 

# Functions in if statements 
def simple_sum(a, b):
    return a+b

if simple_sum(4,3) > simple_sum(5,2):
    print("First is bigger")
else:
    print("Second is bigger")


"""
COMPLEX EXAMPLE 1
Given a list of numbers return a list containinng lists of ranges from that numbers 
(elements incrementor should be specified as a parameter, defult to 1)

in: list_of_ranges(number_list=[3, 4], increment=1)
out: [[1,2,3], [1,2,3,4]]
"""

def list_of_ranges(number_list, increment=1):
    result_list = []
    for number in number_list:
        temp_list = list(range(1, number, increment))
        result_list.append(temp_list)
    return result_list

list_of_ranges(number_list=[3, 4, 5, 2], increment=2)
