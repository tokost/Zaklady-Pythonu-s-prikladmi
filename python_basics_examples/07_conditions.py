is_programmer = True 
is_student = False
type(is_programmer)

'''
Basic conditions 
 - beware the double equal sign
 - beware the indentation (4 spaces = one tab after colon sign)
 - colon after if and else line
'''

if is_student == True:
    print("He is a programmer")

if is_programmer == False:
    print("He is a programmer")
else:
    print("He is not a programmer")

# Chaining the if else 
if is_programmer == False:
    print("Is not a programmer")
elif is_student == True:
    print("Is student")
else:
    print("Is a programmer and is not a student")

# Logical operators 
type(5 < 4)
5 >= 4
# 5 = 4 # an error it is an asignment 
5 == 5

# The is operator (matches not the values but the instances)
number_list1=[1, 2, 3]
number_list2=[1, 2, 3]

number_list1 is number_list2
number_list1 == number_list2


# The negation operator 
is_programmer = True
not is_programmer

# You dont have to write equals in case of booleans
if not is_programmer:
    print("He is not a programmer")
else: 
    print("He is a programmer")

# Chaining the logical operations with and, or
is_programmer = True 
is_student = True

if is_programmer and is_student:
    print("Is a student programmer")
else: 
    print("Is not a student programmer")

if is_programmer or is_student:
    print("Is either student or programmer or both")
else: 
    print("Is not a student nor a programmer")


# Implicit boolean values 
1 == True
0 == False
2 == False # No 2 == True
2 == True

if 1:
    print("Its True")
else: 
    print("Its false")

if 2 == True:
    print("Its True")
else: 
    print("Its false")

if 2:
    print("Its True")
else: 
    print("Its false")

[] == False
[1] == True

if []:
    print("Its True")
else: 
    print("Its false")

if [1,2,3]:
    print("Its True")
else: 
    print("Its false")


# One liners
is_programmer = False
is_programmer_string = "Is a programmer" if is_programmer          # You must provide the esle statement
print(is_programmer_string)

## Is the same as this
if is_programmer:
    is_programmer_string ="He is a programmer"
else:
    is_programmer_string ="He is not a programmer"