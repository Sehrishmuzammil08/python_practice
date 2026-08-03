#program 1: Check if a Year is a Leap Year
# leap_year.py - Leap Year Checker using Nested if-else
year = int(input("Enter Year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} is not a Leap Year")
    else:
        print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
