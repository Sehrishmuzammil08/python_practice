# ============================================================
# Pseudo Code - Python Examples
# ============================================================


# ============================================================
# Sum of Two Numbers
# ============================================================

# Pseudocode:
# BEGIN
#     INPUT number1
#     INPUT number2
#     SET sum = number1 + number2
#     DISPLAY sum
# END

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
sum = number1 + number2
print(f"Sum: {sum}")

# Sample run:
# Enter first number: 10
# Enter second number: 20
# Sum: 30


# ============================================================
# Example 1: Even or Odd Number
# ============================================================

# Pseudocode:
# START
#     INPUT number
#     IF number MOD 2 = 0 THEN
#         DISPLAY "Even"
#     ELSE
#         DISPLAY "Odd"
#     END IF
# END

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ============================================================
# Example 2: Student Grade Calculator
# ============================================================

# Pseudocode:
# START
#     INPUT marks
#     IF marks >= 90 THEN
#         DISPLAY "Grade A"
#     ELSE IF marks >= 80 THEN
#         DISPLAY "Grade B"
#     ELSE IF marks >= 70 THEN
#         DISPLAY "Grade C"
#     ELSE
#         DISPLAY "Fail"
#     END IF
# END

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")


# ============================================================
# Example 3: Find Factorial
# ============================================================

# Pseudocode:
# BEGIN
#     INPUT n
#     SET factorial = 1
#     FOR i = 1 TO n DO
#         SET factorial = factorial * i
#     END FOR
#     DISPLAY "Factorial is: ", factorial
# END

n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print(f"Factorial is: {factorial}")


# ============================================================
# Practice 1: FOR Loop - Sum of First 10 Numbers
# ============================================================

# Pseudocode:
# BEGIN
#     SET sum = 0
#     FOR i = 1 TO 10 DO
#         SET sum = sum + i
#     END FOR
#     DISPLAY sum
# END

total = 0

for i in range(1, 11):
    total = total + i

print(total)

# Output: 55


# ============================================================
# Practice 2: WHILE Loop - Countdown
# ============================================================

# Pseudocode:
# BEGIN
#     SET count = 10
#     WHILE count >= 1 DO
#         DISPLAY count
#         SET count = count - 1
#     END WHILE
#     DISPLAY "Blast Off!"
# END

count = 10

while count >= 1:
    print(count)
    count = count - 1

print("Blast Off!")

# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Blast Off!


# ============================================================
# Practice 3: Average Marks of a Class Having n Students
# ============================================================

# Pseudocode:
# BEGIN
#     INPUT n (number of students)
#     SET sum = 0
#     FOR i = 1 TO n DO
#         INPUT marks
#         SET sum = sum + marks
#     END FOR
#     SET average = sum / n
#     DISPLAY "Average marks: ", average
# END

n = int(input("Enter number of students: "))
total_marks = 0

for i in range(1, n + 1):
    marks = float(input(f"Enter marks for student {i}: "))
    total_marks = total_marks + marks

average = total_marks / n
print("Average marks:", average)
