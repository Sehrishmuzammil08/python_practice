#program 1: Add Two Numbers
#Add two numbers given by the user.
# Input numbers
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
# Add
sum_result = n1 + n2
# Output
print('Sum =', sum_result)



#program 2: Area of Rectangle
#Calculate area using length and width.
# Input values
length = float(input('Enter length: '))
width = float(input('Enter width: '))
# Area formula
area = length * width
print("AREA =" , area)



#program 3: Average of Three Numbers
#Find average of three numbers.
# Input three numbers
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))
# Calculate average
average = (n1 + n2 + n3) / 3)
print("AVERAGE = " , average)


#program 4: Simple Interest
#Calculate simple interest and total amount.
# Input principal, rate and time
p = float(input('Enter principal: '))
r = float(input('Enter rate (%): '))
t = float(input('Enter time (years): '))
# Calculate interest
si = (p * r * t) / 100
# Calculate total amount
total_amount = p + si
# Display results
print('Simple Interest =', si)
print('Total Amount =', total_amount)
print('Multiplication:', a * b)
print('Division:', a / b)


#program 5: Minutes to Hours Converter
#Convert minutes into hours and minutes.
# Input minutes
minutes = int(input('Enter minutes: '))
# Calculate
hours = minutes // 60
remaining = minutes % 60
print(f'{minutes} minutes = {hours} hours and {remaining} minutes')


#program 6: Celsius to Fahrenheit
#Convert Celsius temperature to Fahrenheit.
# Input temperature
c = float(input('Enter temperature in Celsius: '))
# Formula
f = (c * 9/5) + 32
# Output
print('Fahrenheit =', f)


#program 7: Simple Calculator
#Perform +, -, *, / operations.
# Input numbers
n1 = float(input('Enter first number: '))
n2 = float(input('Enter second number: '))
# Output results
print('Addition:', n1 + n2)
print('Subtraction:', n1 - n2)
print('Multiplication:', n1 * n2)
print('Division:', n1 / n2)
