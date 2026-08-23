# ============================================================
# FOR LOOP PROGRAMS
# ============================================================


# ------------------------------------------------------------
# 1. Multiplication Table
# ------------------------------------------------------------

num = 7

for i in range(1, 11):
    result = num * i
    print(num, "*", i, "=", result)


# ------------------------------------------------------------
# 2. Sum of Numbers 1 to 20
# ------------------------------------------------------------

total = 0

for i in range(1, 21):
    total = total + i

print(f"Final Sum: {total}")


# ------------------------------------------------------------
# 3. Factorial Calculator
# ------------------------------------------------------------

num = 8
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print(f"{num}! = {factorial}")


# ------------------------------------------------------------
# 4. Leap Year Finder
# ------------------------------------------------------------

start_year = 2000
end_year = 2050

print(f"LEAP YEARS FROM {start_year} TO {end_year}")

leap_count = 0

for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
        leap_count += 1

print(f"Total leap years found: {leap_count}")


# ------------------------------------------------------------
# 5. Prime Number Checker
# ------------------------------------------------------------

num = 97

if num <= 1:
    print(f"{num} is NOT prime")

elif num == 2:
    print(f"{num} is PRIME")

else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            print(f"{num} is divisible by {i}")
            break

    if is_prime:
        print(f"{num} is PRIME!")
    else:
        print(f"{num} is NOT prime")
