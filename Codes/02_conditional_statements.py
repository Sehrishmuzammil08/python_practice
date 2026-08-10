# ======================================================================
# SECTION A: EASY (Single-level if / if-else / elif / match-case)
# ======================================================================

#------------------------------------------
# 1. Positive, Negative, or Zero
#------------------------------------------
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Number is zero")
    
#------------------------------------------
# 2. Even or Odd
#------------------------------------------
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
#------------------------------------------
# 3. Voting Eligibility (simple)
#------------------------------------------
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#------------------------------------------
# 4. Greater of Two Numbers
#------------------------------------------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both numbers are equal")
    
#------------------------------------------
# 5. Grade Calculator (elif chain)
#------------------------------------------
marks = int(input("Enter marks: "))
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

#------------------------------------------
# 6. Simple Calculator (if-elif)
#------------------------------------------
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == "+":
    print("Result =", num1 + num2)
elif op == "-":
    print("Result =", num1 - num2)
elif op == "*":
    print("Result =", num1 * num2)
elif op == "/":
    print("Result =", num1 / num2)
else:
    print("Invalid operator")
    
#------------------------------------------
# 7. Basic Number Match (match-case)
#------------------------------------------
num = int(input("Enter a number (1-3): "))
match num:
    case 1:
        print("You entered ONE")
    case 2:
        print("You entered TWO")
    case 3:
        print("You entered THREE")
    case _:
        print("Invalid number")
        
#------------------------------------------
# 8. Calculator using match-case
#------------------------------------------
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")
match op:
    case "+":
        print("Result =", num1 + num2)
    case "-":
        print("Result =", num1 - num2)
    case "*":
        print("Result =", num1 * num2)
    case "/":
        print("Result =", num1 / num2)
    case _:
        print("Invalid operator")
        
#------------------------------------------
# 9. Grade using Guards (match-case)
#------------------------------------------
marks = int(input("Enter marks: "))
match marks:
    case m if m >= 80:
        print("Grade A")
    case m if m >= 60:
        print("Grade B")
    case m if m >= 40:
        print("Pass")
    case _:
        print("Fail")
        
#----------------------------------------------------
# 10. (Practice - solved) Divisible by both 3 and 5
#----------------------------------------------------
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")


# ======================================================================
# SECTION B: MEDIUM (Logical Operators + Simple Nesting)
# ======================================================================

#------------------------------------------        
# 11. AND Operator - Voting + Citizenship
#------------------------------------------
age = int(input("Enter age: "))
citizen = input("Are you a citizen? (yes/no): ")
if age >= 18 and citizen == "yes":
    print("Eligible to vote")
else:
    print("Not eligible")

#------------------------------------------
# 12. OR Operator - Admission
#------------------------------------------
marks = int(input("Enter marks: "))
sports = input("Sports quota? (yes/no): ")
if marks >= 50 or sports == "yes":
    print("Admission allowed")
else:
    print("Admission denied")
    
#------------------------------------------
# 13. Range Checking (chained comparison)
#------------------------------------------
num = int(input("Enter number: "))
if 1 <= num <= 10:
    print("Number is between 1 and 10")
else:
    print("Number is outside range")

#------------------------------------------
# 14. (Practice - solved) Positive AND Even
#------------------------------------------
num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("Number is positive and even")
else:
    print("Number is not positive and even")

#-----------------------------------------------------------------------
# 15. (Practice - solved) Entry Allowed if Age >= 18 OR Guardian Present
#------------------------------------------------------------------------
age = int(input("Enter age: "))
guardian = input("Is a guardian present? (yes/no): ")
if age >= 18 or guardian == "yes":
    print("Entry Allowed")
else:
    print("Entry Denied")

#---------------------------------------------
# 16. (Practice - solved) Password Validation
#---------------------------------------------
password = input("Enter password: ")
if len(password) >= 8 and any(ch.isdigit() for ch in password):
    print("Valid password")
else:
    print("Invalid password: must be at least 8 characters and include a number")
    
#--------------------------------------------
# 17. Voting and ID Verification (nested if)
#--------------------------------------------
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible by age")
    has_id = input("Do you have ID? (yes/no): ")
    if has_id == "yes":
        print("You can vote")
    else:
        print("ID required to vote")
else:
    print("Not eligible to vote")
    
#-----------------------------------------------------
# 18. Student Result and Grade System (nested + elif)
#-----------------------------------------------------
marks = int(input("Enter marks: "))
if marks >= 40:
    print("You passed")
    if marks >= 80:
        print("Grade A")
    elif marks >= 60:
        print("Grade B")
    else:
        print("Grade C")
else:
    print("You failed")

#-----------------------------------------------------------------------------------
# 19. Login System (nested if) - also answers "login system using nested conditions"
#------------------------------------------------------------------------------------
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")

#----------------------------------------------------------------
# 20. Nested Conditions with Logical Operators - Promotion Check
#----------------------------------------------------------------
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance %: "))
if marks >= 40:
    if attendance >= 75 and marks >= 60:
        print("Promoted with good standing")
    else:
        print("Promoted")
else:
    print("Failed")

#--------------------------------------------------------
# 21. (Practice - solved) Loan Approval (Income AND Age)
#--------------------------------------------------------
income = int(input("Enter monthly income: "))
age = int(input("Enter age: "))
if age >= 21 and income >= 30000:
    print("Loan Approved")
else:
    print("Loan Not Approved")

#----------------------------------------------------------------------  
# 22. (Practice - solved) Nested Grading System with Distinction Level
#----------------------------------------------------------------------
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
    if marks >= 90:
        print("Distinction")
    elif marks >= 75:
        print("First Division")
    elif marks >= 60:
        print("Second Division")
    else:
        print("Third Division")
else:
    print("Fail")


# ======================================================================
# SECTION C: COMPLEX (Multi-level Nested Programs)
# ======================================================================

#----------------------------------------------------------------------------------------
# 23. Largest of Three Numbers - also answers "determine the largest among three numbers"
#----------------------------------------------------------------------------------------
num1 = 10
num2 = 25
num3 = 15
if num1 >= num2:
    if num1 >= num3:
        print(f"Largest number is: {num1}")
    else:
        print(f"Largest number is: {num3}")
else:
    if num2 >= num3:
        print(f"Largest number is: {num2}")
    else:
        print(f"Largest number is: {num3}")

#------------------------------------------
# 24. Leap Year Checker
#------------------------------------------
year = 2024
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

#------------------------------------------    
# 25. Grade Calculation (deep nesting)
#------------------------------------------
marks = 85
if marks >= 90:
    if marks >= 95:
        print("Grade: A+")
    else:
        print("Grade: A")
else:
    if marks >= 80:
        if marks >= 85:
            print("Grade: B+")
        else:
            print("Grade: B")
    else:
        if marks >= 70:
            print("Grade: C")
        else:
            print("Grade: F")

#------------------------------------------
# 26. Even/Odd with Divisibility Checks
#------------------------------------------
num = 24
if num % 2 == 0:
    print(f"{num} is Even")
    if num % 4 == 0:
        print(f"{num} is divisible by 4")
    if num % 6 == 0:
        print(f"{num} is divisible by 6")
else:
    print(f"{num} is Odd")
    if num % 3 == 0:
        print(f"{num} is divisible by 3")

#------------------------------------------
# 27. Triangle Type Checker
#------------------------------------------
side1 = 5
side2 = 5
side3 = 8
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("Valid Triangle")
    if side1 == side2 == side3:
        print("Equilateral Triangle")
    else:
        if side1 == side2 or side2 == side3 or side1 == side3:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
else:
    print("Invalid Triangle")

#------------------------------------------
# 28. ATM Withdrawal System
#------------------------------------------
balance = 5000
withdrawal_amount = 3000
daily_limit = 10000
daily_withdrawn = 2000
if withdrawal_amount <= balance:
    if withdrawal_amount <= (daily_limit - daily_withdrawn):
        if withdrawal_amount % 100 == 0:
            print("Transaction Successful!")
            print(f"Withdrawn: ${withdrawal_amount}")
            print(f"Remaining Balance: ${balance - withdrawal_amount}")
        else:
            print("Please enter amount in multiples of 100")
    else:
        print("Daily limit exceeded!")
else:
    print("Insufficient balance!")

#------------------------------------------    
# 29. Age-based Discount Calculator
#------------------------------------------
age = 65
is_member = True
if age < 18:
    print("Child: 20% discount")
    if is_member:
        print("Additional 5% for members")
        print("Total discount: 25%")
    else:
        print("Total discount: 20%")
elif age >= 60:
    print("Senior Citizen: 30% discount")
    if is_member:
        print("Additional 5% for members")
        print("Total discount: 35%")
    else:
        print("Total discount: 30%")
else:
    print("Adult: 10% discount")
    if is_member:
        print("Additional 5% for members")
        print("Total discount: 15%")
    else:
        print("Total discount: 10%")

#------------------------------------------
# 30. Number Range Checker (nested)
#------------------------------------------
num = 45
if num > 0:
    print("Positive Number")
    if num <= 10:
        print("Number is between 1-10")
    elif num <= 20:
        print("Number is between 11-20")
    elif num <= 50:
        print("Number is between 21-50")
        if num % 5 == 0:
            print("Number is divisible by 5")
    else:
        print("Number is greater than 50")
elif num < 0:
    print("Negative Number")
    if num < -10:
        print("Number is less than -10")
    else:
        print("Number is between -10 and 0")
else:
    print("Number is Zero")

#------------------------------------------
# 31. Login System with Role-based Access
#------------------------------------------
username = "admin"
password = "pass123"
role = "admin"
if username == "admin" and password == "pass123":
    print("Login Successful!")
    if role == "admin":
        print("Welcome Admin!")
        print("You have full access to all features")
    elif role == "editor":
        print("Welcome Editor!")
        print("You can edit content")
    else:
        print("Welcome Viewer!")
        print("You can only view content")
elif username == "admin":
    print("Incorrect password!")
else:
    print("Invalid username!")

#---------------------------------------------------------------
# 32. Temperature Alert System (most complex - deepest nesting)
#---------------------------------------------------------------
temperature = 38
unit = "C"  # C for Celsius, F for Fahrenheit
if unit == "C":
    print("Temperature in Celsius")
    if temperature <= 0:
        print("FREEZING! Water freezes")
    elif temperature <= 30:
        print("Normal temperature range")
        if temperature >= 25:
            print("Warm day")
        elif temperature <= 10:
            print("Cold day")
    else:
        print("HOT! Temperature above 30°C")
        if temperature >= 40:
            print("EXTREME HEAT WARNING!")
        else:
            print("Heat alert: Stay hydrated")
else:  # Fahrenheit
    print("Temperature in Fahrenheit")
    if temperature <= 32:
        print("FREEZING! Water freezes")
    elif temperature <= 86:
        print("Normal temperature range")
    else:
        print("HOT! Temperature above 86°F")
