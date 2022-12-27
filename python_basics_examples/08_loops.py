# Loops 
numbers = [1, 2, 3, 4, 5, 10]
letters = ["M", "i", "c", "h", "a", "l"]

# The for loop
for number in numbers:
    print(number)

# Lazy to write the array 
range(4)
list(range(4))
list(range(0,4))
list(range(1,4))
list(range(0, 10, 2))
list(range(10, 1, -2))

for number in range(0, 10, 2):
    print(number)

# While loop
counter=0
while counter< 5:
    print(counter)
    counter+=1


# Break
counter = 0
while True: # the same as while 1==1:
    print(counter)  # What if we move this after break ? 
    if counter >= 5:
        break
    counter += 1

letters = ["M", "i", "c", "h", "a", "l"]
for letter in letters:
    if letter != 'c':
        print(letter)


# Continue
letters = ["M", "i", "c", "h", "a", "l"]
for letter in letters:
    if letter == 'c':
        continue
    print(letter)


# Else in loops
for letter in ["c"]:
    print(letter)
else: 
    print("For wont run a single time")

while False:
    print("My password is <password>")
else:
    print("While wont run a single time")