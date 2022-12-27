"""
Key value storages 
{
    <key>: <value>
}

Key: defined as a string or even numbers or booleans or some build in objects (but dont do it) :D . 
    Almost no restrictions 
Value: defined as any datatype even an another dictionary. Can be mixed.
"""

mixed_dict = {
    "Michal" : 23,
    "Felipe" : 32,
    0: "zero",
    True: "True",
    False: True,
    int: "True"
}

print(mixed_dict)
print(type(mixed_dict))

# Access
mixed_dict['Michal']
mixed_dict['Felipe']
mixed_dict[0] # Careful not the same as in lists this refers to name not to the position 
mixed_dict[True]
mixed_dict[int]
# mixed_dict['John'] # Error

# Adding and adjusting and deleting
mixed_dict['John'] = 40
mixed_dict['Felipe'] = 33
print(mixed_dict)
del mixed_dict['John']
print(mixed_dict)

# You can put arrays in dict or dict to dict  
person = { # DONT FORGET THE COMMAS
    "name" : "Michal", 
    "surname": "Hucko", 
    "languages": ["Python", "JavaScript", "Java"],
    "instagram": "@misohucko",
    "address": {
        "city": "New York",
        "street": "stret_name",
        "street_number": 45
    }
}

person['languages'][-1]
person['address']['street']

# (optional): All imutable types can be keys (tuples, strings), but not immutable ones like lists or dictionaries 
touple_dict={
    (1,2): "touple",
    # [1,2]: "array" # this is an error 
}
print(touple_dict[(1,2)])


# Operations
person = { # DONT FORGET THE COMMAS
    "name" : "Michal", 
    "surname": "Hucko", 
    "languages": ["Python", "JavaScript", "Java"],
    "instagram": "@misohucko",
    "address": {
        "city": "New York",
        "street": "stret_name",
        "street_number": 45,
    }
}
len(person) # number of keys
person.get("name") # the same as person['name'], but does not raise error in case of error 
person.get("not_existing_key", "PLESE NO") # returns default in case of not presented (default is second argument)
list(person.items()) # returns list of touples can be useful for iteration 
for key, value in person.items():
    print(f"Key: {key}, Value {value}")
person.keys() # list of keys, recommend to cast like list(person.keys())
person.values() # list of values,  recommend to cast like list(person.keys())
person.pop("name") # returns the item and removes from dict. Raise error if not presented
print(person) # name is no longer in dict 
person.popitem() # emoves the last key-value pair added from d and returns it as a tuple




