import fileinput
import sys

for line in fileinput.input():
    print(line, end='')


def get_input():
    print("Please insert your number")
    x = int(sys.stdin.readline())
    return x 

while True:
    number=get_input()
    print(f"Your number is: {number}")
    if number == 99:
        print("Number is 99 ending the loop")
        break 

