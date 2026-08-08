# ==========================================
#Print Statement
# ==========================================
print("Hello, Sehrish")
#0utput: Hello, Sehrish

name = "Sehrish"
print("My name is", name)
#0utput: My name is Sehrish


# ============================================================
# BASIC PYTHON PROGRAMS
# ============================================================


# ------------------------------------------------------------
# Program 1: Multiply Two Numbers (Fixed Values)
# ------------------------------------------------------------
number1 = 5
number2 = 3

result = number1 * number2

print(number1, 'x', number2, '=', result)


# ------------------------------------------------------------
# Program 2: Multiply Two Numbers (User Input)
# ------------------------------------------------------------
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

product = num1 * num2

print('Product =', product)


# ------------------------------------------------------------
# Program 3: Add Two Numbers
# ------------------------------------------------------------
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))

sum_result = n1 + n2

print('Sum =', sum_result)


# ------------------------------------------------------------
# Program 4: Subtract Two Numbers
# ------------------------------------------------------------
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

result = a - b

print(a, '-', b, '=', result)


# ------------------------------------------------------------
# Program 5: Divide Two Numbers
# ------------------------------------------------------------
x = float(input('Enter first number: '))
y = float(input('Enter second number: '))

result = x / y

print(x, '/', y, '=', result)


# ------------------------------------------------------------
# Program 6: All Arithmetic Operations
# ------------------------------------------------------------
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

print('Addition:', a + b)
print('Subtraction:', a - b)
print('Multiplication:', a * b)
print('Division:', a / b)


# ------------------------------------------------------------
# Program 7: Average of Three Numbers
# ------------------------------------------------------------
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))

average = (n1 + n2 + n3) / 3

print('Average =', average)


# ------------------------------------------------------------
# Program 8: Area of Rectangle
# ------------------------------------------------------------
length = float(input('Enter length: '))
width = float(input('Enter width: '))

area = length * width

print('Area =', area)


# ------------------------------------------------------------
# Program 9: Simple Interest
# ------------------------------------------------------------
p = float(input('Enter principal: '))
r = float(input('Enter rate (%): '))
t = float(input('Enter time (years): '))

si = (p * r * t) / 100

print('Simple Interest =', si)
print('Total Amount =', p + si)


# ------------------------------------------------------------
# Program 10: Swap Two Numbers
# ------------------------------------------------------------
a = 5
b = 10

print('Before:', a, b)

a, b = b, a

print('After:', a, b)


# ------------------------------------------------------------
# Program 11: Even or Odd Checker
# ------------------------------------------------------------
num = int(input('Enter number: '))

if num % 2 == 0:
    print('Even Number')
else:
    print('Odd Number')


# ------------------------------------------------------------
# Program 12: Compare Two Number
# ------------------------------------------------------------
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

print(x > y)
print(y > x)
print(y == x)


# ------------------------------------------------------------
# Program 13: Minutes to Hours Converter
# ------------------------------------------------------------
minutes = int(input('Enter minutes: '))

hours = minutes // 60
remaining = minutes % 60

print(hours, 'hours and', remaining, 'minutes')


# ------------------------------------------------------------
# Program 14: Calculate Percentage
# ------------------------------------------------------------
obtained = float(input('Enter obtained marks: '))
total = float(input('Enter total marks: '))

percentage = (obtained / total) * 100

print('Percentage =', percentage, '%')


# ------------------------------------------------------------
# Program 15: Celsius to Fahrenheit
# ------------------------------------------------------------
c = float(input('Enter temperature in Celsius: '))

f = (c * 9/5) + 32

print('Fahrenheit =', f)


# ------------------------------------------------------------
# Program 16: Simple Calculator
# ------------------------------------------------------------
n1 = float(input('Enter first number: '))
n2 = float(input('Enter second number: '))

print('Addition:', n1 + n2)
print('Subtraction:', n1 - n2)
print('Multiplication:', n1 * n2)
print('Division:', n1 / n2)


# ------------------------------------------------------------
# Program 17: Quotient and Remainder
# ------------------------------------------------------------
dividend = int(input('Enter dividend: '))
divisor = int(input('Enter divisor: '))

q = dividend // divisor
r = dividend % divisor

print('Quotient =', q)
print('Remainder =', r)


# ------------------------------------------------------------
# Program 18: Area and Circumference of Circle
# ------------------------------------------------------------
radius = float(input('Enter radius: '))

pi = 3.14

area = pi * radius * radius
circumference = 2 * pi * radius

print('Area =', area)
print('Circumference =', circumference)
