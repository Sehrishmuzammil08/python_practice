# ============================================================
# PYTHON WHILE LOOP PROGRAMS
# ============================================================


# Program 1: Print Numbers from 1 to 10

num = 1

while num <= 10:
    print(num, end=" ")
    num += 1

print()  # Move to a new line


# ------------------------------------------------------------
# Program 2: Sum of First N Natural Numbers

n = int(input("Enter a number: "))

total = 0
i = 1

while i <= n:
    total += i
    i += 1

print(f"Sum of first {n} natural numbers is: {total}")


# ------------------------------------------------------------
# Program 3: Multiplication Table

num = int(input("Enter a number: "))

i = 1

print(f"Multiplication Table of {num}:")

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1


# ------------------------------------------------------------
# Program 4: Factorial of a Number

num = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"Factorial of {num} is: {factorial}")


# ------------------------------------------------------------
# Program 5: Count Digits in a Number

num = int(input("Enter a number: "))

original_num = num
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count += 1

print(f"Number of digits in {original_num} is: {count}")


# ------------------------------------------------------------
# Program 6: Sum of Digits

num = int(input("Enter a number: "))

original_num = num
sum_of_digits = 0

while num > 0:
    digit = num % 10          # Get the last digit
    sum_of_digits += digit    # Add digit to sum
    num = num // 10            # Remove the last digit

print(f"Sum of digits of {original_num} is: {sum_of_digits}")

"""
Explanation:
- num % 10 gives the last digit.
  Example: 1234 % 10 = 4

- num // 10 removes the last digit.
  Example: 1234 // 10 = 123

- The loop continues until all digits are processed.
"""


# ------------------------------------------------------------
# Program 7: Print Even Numbers from 1 to 20

num = 1

print("Even numbers from 1 to 20:")

while num <= 20:
    if num % 2 == 0:
        print(num, end=" ")

    num += 1

print()  # Move to a new line


# More Efficient Way: Increment by 2

num = 2

while num <= 20:
    print(num, end=" ")
    num += 2

print()


# ------------------------------------------------------------
# Program 8: Find Power of a Number

base = int(input("Enter base number: "))
exponent = int(input("Enter exponent: "))

result = 1
count = 1

while count <= exponent:
    result *= base
    count += 1

print(f"{base} raised to power {exponent} = {result}")

"""
Explanation:
- 3^4 means 3 × 3 × 3 × 3 = 81
- The loop runs 'exponent' number of times.
- Each time, result is multiplied by base.
"""


# ------------------------------------------------------------
# Program 9: Calculate Average of Positive Numbers

sum_numbers = 0
count = 0

print("Enter numbers (enter a negative number to stop):")

while True:
    num = int(input("Enter number: "))

    if num < 0:
        break

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
- while True creates an infinite loop.
- break stops the loop when a negative number is entered.
- The entered non-negative numbers are included in the average.
"""


# ------------------------------------------------------------
# Program 10: Simple Password Checker

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


# ------------------------------------------------------------
# Program 11: Find Factors of a Number

num = int(input("Enter a positive number: "))

i = 1

print(f"Factors of {num} are:")

while i <= num:

    if num % i == 0:
        print(i, end=" ")

    i += 1

print()

"""
Explanation:
- A factor is a number that divides another number evenly.
- num % i == 0 checks whether i divides num without a remainder.
- Example:
  Factors of 12 are 1, 2, 3, 4, 6, and 12.
"""
