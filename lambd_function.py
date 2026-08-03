#Q multiplies a number by 3. 
triple = lambda x: x * 3 
print(f" {triple(5)}")    


# 1. Multiply two numbers
multiply = lambda a, b: a * b
print(multiply(4, 6))



# 2. Return the larger of two numbers
maximum = lambda a, b: a if a > b else b
print(maximum(15, 9))



# 3. Cube of a number
cube = lambda x: x ** 3
print(cube(5))



# 4. Divide two numbers
divide = lambda a, b: a / b
print(divide(20, 4))



# 5. Check if a number is positive
is_positive = lambda x: x > 0
print(is_positive(7))
print(is_positive(-3))



# 6. Remainder of two numbers
remainder = lambda a, b: a % b
print(remainder(17, 5))
