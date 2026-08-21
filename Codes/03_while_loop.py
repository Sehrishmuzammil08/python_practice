#Program 1: Print Numbers from 1 to 10 
num = 1 
while num <= 10: 
  print(num, end=" ")      
  num += 1 
#end in print to keep content in same line 
print()   # for new line to get rid of same line as it don’t have end keyword in print 



#Program 2: Sum of First N Natural Numbers 
n = int(input("Enter a number: ")) 
sum = 0 
i = 1 
while i <= n: 
  sum += i 
  i += 1 
print(f"Sum of first {n} natural numbers is: {sum}") 



#Program 3: Multiplication Table 
num = int(input("Enter a number: ")) 
i = 1 
print(f"Multiplication Table of {num}:") 
while i <= 10: 
  print(f"{num} x {i} = {num * i}") 
  i += 1 


# 4: Factorial of a Number 
num = int(input("Enter a number: ")) 
factorial = 1 
i = 1 
while i <= num: 
  factorial *= i 
  i += 1 
print(f"Factorial of {num} is: {factorial}") 



#Program 5: Count Digits in a Number 
num = int(input("Enter a number: ")) 
original_num = num 
count = 0 
if num == 0: 
  count = 1 
else: 
  while num > 0: 
    num = num // 10  # Remove last digit 
    count += 1 
print(f"Number of digits in {original_num} is: {count}") 



#Program 6: Sum of Digits 
num = int(input("Enter a number: ")) 
original_num = num 
sum_of_digits = 0 
while num > 0: 
  digit = num % 10        
  # Get last digit 
  sum_of_digits += digit   # Add to sum 
  num = num // 10          
  # Remove last digit 
print(f"Sum of digits of {original_num} is: {sum_of_digits}") 

""" Explanation: 
• num % 10 gives the last digit (1234 % 10 = 4) 
• num // 10 removes the last digit (1234 // 10 = 123) 
• Loop continues until all digits are processed """


#Program 7: Print Even Numbers from 1 to 20 
num = 1 
print("Even numbers from 1 to 20:") 
while num <= 20: 
  if num % 2 == 0:    # Check if number is even 
  print(num, end=" ")       
  num += 1 
#end in print to keep content in same line 
print()  # for new line to get rid of same line as it don’t have end keyword in print 


# More efficient way - increment by 2 
num = 2 
while num <= 20: 
  print(num, end=" ") 
  num += 2 


#Program 8: Find Power of a Number 
base = int(input("Enter base number: ")) 
exponent = int(input("Enter exponent: ")) 
result = 1 
count = 1 
while count <= exponent: 
  result *= base   # Multiply result by base repeatedly 
  count += 1 
print(f"{base} raised to power {exponent} = {result}") 
"""
Explanation: 
• 3⁴ means 3 × 3 × 3 × 3 = 81 
• Loop runs 'exponent' number of times 
• Each time, multiply result by base 
"""


#Program 9: Calculate Average of Positive Numbers 
sum_numbers = 0 
count = 0 
print("Enter numbers (enter negative number to stop):") 
while True: 
    num = int(input("Enter number: ")) 
    if num < 0: 
        break  # Exit loop if negative number entered 
    sum_numbers += num 
    count += 1 
if count > 0: 
    average = sum_numbers / count 
    print(f"\nSum of numbers: {sum_numbers}") 
    print(f"Count of numbers: {count}") 
    print(f"Average: {average:.2f}") 
else: 
    print("No positive numbers were entered!") 
"""
Explanation: 
• while True creates an infinite loop 
• break stops the loop when condition is met 
• Only positive numbers are counted in the average 
"""


#Program 10: Simple Password Checker 
# Simple password checker with 3 attempts 
correct_password = "python123" 
attempts = 1 
max_attempts = 3 
print("Welcome! Please enter your password.") 
while attempts <= max_attempts: 
    password = input(f"Attempt {attempts}/{max_attempts}: ") 
    if password == correct_password: 
        print("Access Granted! Welcome to the system.") 
        break 
    else: 
        print("Incorrect password!") 
        attempts += 1 
        if attempts > max_attempts: 
            print("Sorry, you've used all attempts. Account locked!") 



# Program 11: Find Factors of a Number 
num = int(input("Enter a positive number: ")) 
i = 1 
print(f"Factors of {num} are: ") 
while i <= num: 
  if num % i == 0:    # If i divides num evenly 
    print(i, end=" ") 
    i += 1 
print() 
"""
Explanation: 
• A factor is a number that divides another number evenly 
• num % i == 0 checks if i divides num without remainder 
• Example: 12 ÷ 1, 2, 3, 4, 6, 12 all give whole numbers 
"""
