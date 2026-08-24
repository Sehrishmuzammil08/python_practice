# ============================================================
#                    PYTHON FUNCTIONS
# ============================================================


# ============================================================
# 1. BASIC FUNCTION
# ============================================================

# Write a function that prints "Hello, World!"

def say_hello():
    print("Hello, World!")


say_hello()


# ============================================================
# 2. FUNCTION WITH ONE PARAMETER
# ============================================================

# Write a function that takes a name and prints a greeting.

def greet(name):
    print(f"Hello, {name}!")


greet("Ali")
greet("Sara")


# ============================================================
# 3. FUNCTION WITH RETURN VALUE
# ============================================================

# Write a function that takes a number and returns its double.

def double(num):
    return num * 2


result = double(5)
print("Double of 5 =", result)

print("Double of 10 =", double(10))


# ============================================================
# 4. FUNCTION WITH TWO PARAMETERS
# ============================================================

# Write a function that takes two numbers and returns their sum.

def add(a, b):
    return a + b


print("3 + 5 =", add(3, 5))
print("10 + 20 =", add(10, 20))
print("100 + 200 =", add(100, 200))


# ============================================================
# 5. FUNCTION WITH MULTIPLE OPERATIONS
# ============================================================

# Write a function to calculate the area of a rectangle.

def rectangle_area(length, width):
    print("Calculating area...")

    area = length * width

    return area


result = rectangle_area(5, 3)

print("Area of rectangle =", result)


# ============================================================
# 6. FUNCTION WITH CONDITIONAL LOGIC
# ============================================================

# Write a function that checks whether a number is even or odd.

def is_even(num):

    if num % 2 == 0:
        return True
    else:
        return False


print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))


# ============================================================
# 7. FUNCTION WITH DEFAULT PARAMETER
# ============================================================

# Write a function with a default greeting.

def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet_user("Ali")
greet_user("Sara", "Hi")
greet_user("Ahmed", "Good morning")


# ============================================================
# 8. FUNCTION CALLING ANOTHER FUNCTION
# ============================================================

# Write a function to find the square of a number.
# Then use it inside another function to find
# the sum of two squares.

def square(num):
    return num * num


def sum_of_squares(a, b):
    return square(a) + square(b)


print("Square of 4 =", square(4))
print("Sum of squares of 3 and 4 =", sum_of_squares(3, 4))


# ============================================================
# 9. RETURN VS NO RETURN
# ============================================================

# Function without return
# It only displays the result.

def add_and_print(a, b):
    result = a + b
    print("Sum is:", result)


# Function with return
# It sends the result back to the caller.

def add_and_return(a, b):
    result = a + b
    return result


print("\nFunction without return:")
add_and_print(5, 3)


print("\nFunction with return:")
result = add_and_return(5, 3)
print("Returned value:", result)


# ============================================================
# 10. LAMBDA FUNCTION
# ============================================================

# Create a lambda function that multiplies
# a number by 3.

triple = lambda x: x * 3


print("Triple of 4 =", triple(4))
print("Triple of 10 =", triple(10))
print("Triple of 7 =", triple(7))


# ============================================================
# 11. FUNCTION THAT TAKES INPUT FROM USER
# ============================================================

# Write a function that takes two numbers from
# the user and returns their sum.

def get_and_add():

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    return num1 + num2


print("\nAdd two numbers")

result = get_and_add()

print("The sum is:", result)
