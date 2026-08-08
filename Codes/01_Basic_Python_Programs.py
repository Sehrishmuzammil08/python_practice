print("Hello, Sehrish")
#output: Hello, Sehrish

name = Sehrish 
print("Name =", name)
#output: Name = Sehrish


# ==========================================
# PROGRAM 1: ADD TWO NUMBERS
# ==========================================
# Input numbers
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
# Add
sum_result = n1 + n2
# Output
print('Sum =', sum_result)


# ==========================================
# PROGRAM 2: AREA OF RECTANGLE
# ==========================================
length = float(input('Enter length: '))
width = float(input('Enter width: '))

area = length * width

print('AREA =', area)


# ==========================================
# PROGRAM 3: AVERAGE OF THREE NUMBERS
# ==========================================
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))

average = (n1 + n2 + n3) / 3

print('AVERAGE =', average)


# ==========================================
# PROGRAM 4: SIMPLE INTEREST
# ==========================================
p = float(input('Enter principal: '))
r = float(input('Enter rate (%): '))
t = float(input('Enter time (years): '))

si = (p * r * t) / 100
total_amount = p + si

print('Simple Interest =', si)
print('Total Amount =', total_amount)


# ==========================================
# PROGRAM 5: MINUTES TO HOURS CONVERTER
# ==========================================
minutes = int(input('Enter minutes: '))

hours = minutes // 60
remaining = minutes % 60

print(f'{minutes} minutes = {hours} hours and {remaining} minutes')


# ==========================================
# PROGRAM 6: CELSIUS TO FAHRENHEIT
# ==========================================
c = float(input('Enter temperature in Celsius: '))

f = (c * 9 / 5) + 32

print('Fahrenheit =', f)


# ==========================================
# PROGRAM 7: SIMPLE CALCULATOR
# ==========================================
n1 = float(input('Enter first number: '))
n2 = float(input('Enter second number: '))

print('Addition:', n1 + n2)
print('Subtraction:', n1 - n2)
print('Multiplication:', n1 * n2)
print('Division:', n1 / n2)
