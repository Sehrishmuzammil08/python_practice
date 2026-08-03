#Print multiplication table for 7 
num = 7
print(f"Multiplication table of {num}")
for i in range(1, 11):
 result = num * i
 print(num, "*", i, "=", result)

 # Calculate sum of first 20 natural numbers
total = 0
print("Adding numbers 1 to 20:")
for i in range(1, 21):
 total = total + i
print(f"Final Sum: {total}")


# Calculate factorial of a number
num = 8
factorial = 1
for i in range(1, num + 1):
 factorial = factorial * i
print(f"{num}! = {factorial}")


# Find leap years in a range
start_year = 2000
end_year = 2050
print(f"LEAP YEARS FROM {start_year} TO {end_year}")
leap_count = 0
for year in range(start_year, end_year + 1):
 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 print(f"{year} is a leap year ")
 leap_count += 1

print(f"Total leap years found: {leap_count}")
