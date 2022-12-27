# Tuples are lists but not :D 
number_tuple = (1, 2, 3)
print(type(number_tuple))
number_tuple[0]

# They are immutable 
number_tuple[0] = 10 # NO !!!! use array 

# Tuples are faster BUT IMMUTABLE 
# Tuples are used in dictionaries
1,2,3 # You can create a tupple like this in certain places like funciton 

def funciton_returning_tupple(elemnt1, element2):
    return elemnt1, element2
funciton_returning_tupple(1, 2)

# Then we can UNPACK the touple
e1, e2 = funciton_returning_tupple(1, 2)
print(e1)
print(e2)

# No brain syntax 
not_a_tuple = (2)
a_tuple = (2,) # with only one element !!! 
print(type(not_a_tuple))
print(type(a_tuple))

# Some bonus tuples 
sneaky_tupe = 2,
print(sneaky_tupe)
pack_tuple = "Michal", "Hucko", "Is", "Amazing"
print(pack_tuple)
name, surname, word, another_word = pack_tuple # unpack 
print(name, surname, word, another_word) 
name, surname, _, _ = pack_tuple # unpack important and forget other (lazy to make up variable names)
print(name, surname)