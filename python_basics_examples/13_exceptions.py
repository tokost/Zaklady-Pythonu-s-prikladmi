def division(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("You cannot divide by 0 :P.")
        result=None
    except TypeError as e:
        print("Please only numbers :P")
        print(e)
        result=None
    return result

division("a",0)

# You can have multiple except points
# Catching exception in the function 

# Throwing an exception 
def division(x, y):
    try:
        result = x/y
    except Exception as e:
        print(f"Error in addition {e}")
        raise e
    return result

def addition(x, y):
    result = x+y
    return result

def calculator(x,y, function):
    """
    Take a breathe and process this black magic. We are passing a function as parameter.
    In order to use it we need to call the function with the ().
    """
    try:
        return function(x,y)
    except Exception as e: 
        print(f"Fix this pls {e}")
        return None

calculator(10, 5, division)
calculator(10, 5, addition)

# Now the fun part 
calculator(10, 0, division)
print(calculator(10, 10, addition))

def example_finally():
    try: 
        print("A")
        raise Exception()
        return "a" 
    except:
        print("B")
        return "b"
    print("C")

example_finally()