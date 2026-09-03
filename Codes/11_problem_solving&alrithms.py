# ============================================================
# Problem Solving & Algorithms - Example
# ============================================================

# Problem: Calculate the area of a rectangle
# ============================================================
# Steps:
# 1. Get length from user
# 2. Get width from user
# 3. Multiply length and width
# 4. Display area

length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area =", area)

# Test Case:
# Input:  Length = 5, Width = 4
# Output: Area = 20.0




# ============================================================
# Problem: Check whether a number is even or odd
# ============================================================
# Steps:
# 1. Get a number from user
# 2. Divide the number by 2
# 3. Check the remainder
# 4. If remainder is 0, number is even
# 5. Otherwise, number is odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# Test Case:
# Input:  Number = 8
# Output: Number is Even





# ============================================================
# Problem: Calculate Simple Interest
# ============================================================
# Steps:
# 1. Get principal amount from user
# 2. Get rate from user
# 3. Get time from user
# 4. Calculate simple interest
# 5. Display the result

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)

# Test Case:
# Input:  Principal = 1000, Rate = 5, Time = 2
# Output: Simple Interest = 100.0
