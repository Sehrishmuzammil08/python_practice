# Pseudo Code - Notes

## What is Pseudo Code?
Pseudo code is a simplified, human-readable description of an algorithm using plain language and basic programming concepts.

### Pseudo Code Example (Not actual code)
```
BEGIN
    INPUT number1
    INPUT number2
    SET sum = number1 + number2
    DISPLAY sum
END
```

### Actual Python Code
```python
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
sum = number1 + number2
print(f"Sum: {sum}")
```
**Output**
```
Enter first number: 10
Enter second number: 20
Sum: 30
```

---

## Why Use Pseudo Code?

| Benefit | Explanation |
|---|---|
| Language Independent | Can be converted to any programming language |
| Easy to Understand | Uses plain English |
| Focus on Logic | No syntax distractions |
| Planning Tool | Plan before coding |
| Communication | Share ideas without code |
| Documentation | Explain algorithm logic |

---

## Example 1: Even or Odd Number

**Pseudocode**
```
START
    INPUT number
    IF number MOD 2 = 0 THEN
        DISPLAY "Even"
    ELSE
        DISPLAY "Odd"
    END IF
END
```

**Python Program**
```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Example 2: Student Grade Calculator

**Pseudocode**
```
START
    INPUT marks
    IF marks >= 90 THEN
        DISPLAY "Grade A"
    ELSE IF marks >= 80 THEN
        DISPLAY "Grade B"
    ELSE IF marks >= 70 THEN
        DISPLAY "Grade C"
    ELSE
        DISPLAY "Fail"
    END IF
END
```

**Python Program**
```python
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")
```

---

## Example 3: Find Factorial

**Pseudo Code**
```
BEGIN
    INPUT n
    SET factorial = 1

    FOR i = 1 TO n DO
        SET factorial = factorial * i
    END FOR

    DISPLAY "Factorial is: ", factorial
END
```

**Python Code**
```python
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print(f"Factorial is: {factorial}")
```

---

## Practice

### FOR Loop Example - Sum of First 10 Numbers
```
BEGIN
    SET sum = 0
    FOR i = 1 TO 10 DO
        SET sum = sum + i
    END FOR
    DISPLAY sum
END
```

### WHILE Loop Example - Countdown
```
BEGIN
    SET count = 10
    WHILE count >= 1 DO
        DISPLAY count
        SET count = count - 1
    END WHILE
    DISPLAY "Blast Off!"
END
```

### Average Marks of a Class Having n Students
```
BEGIN
    INPUT n (number of students)
    SET sum = 0

    FOR i = 1 TO n DO
        INPUT marks
        SET sum = sum + marks
    END FOR

    SET average = sum / n
    DISPLAY "Average marks: ", average
END
```

---

## Quick Recap
- Pseudo code describes an algorithm's **logic** in plain language, without worrying about any particular language's syntax.
- Common keywords: `START/BEGIN`, `INPUT`, `SET`, `IF...THEN...ELSE`, `FOR...DO...END FOR`, `WHILE...DO...END WHILE`, `DISPLAY`, `END`.
- Writing pseudo code first is a great habit — it lets you nail down the logic before getting distracted by Python syntax.
- `FOR i = 1 TO n` maps naturally to Python's `for i in range(1, n + 1):`, and `WHILE condition DO` maps to `while condition:`.
