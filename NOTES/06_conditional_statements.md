# Python Control Structures: Conditional Statements

## 📌 Introduction to Control Structures

In programming, statements normally execute from top to bottom in sequence. However, real-world problems require decision-making. Programs must sometimes choose between different actions depending on conditions.

**Control structures** allow a program to change the flow of execution based on logical decisions.

Conditional statements help a program decide:
- **WHAT** to do
- **WHEN** to do it
- **WHICH** path to follow

---

## 📌 What are Conditional Statements?

Conditional statements execute certain blocks of code only when a condition is satisfied. A **condition** is an expression that evaluates to either `True` or `False`.

**Examples of conditions:**
```python
age >= 18
marks < 40
number % 2 == 0
```

> Python uses **indentation** (spaces at the beginning of a line) to define blocks of code. All statements under a condition must be properly indented.

---

## The `if` Statement

Used when we want to execute code **ONLY IF** a condition is true.

**Syntax:**
```python
if condition:
    statements
```

**Example — Checking Voting Eligibility:**
```python
age = 20  # variable storing age

# Check eligibility
if age >= 18:  # condition: is age greater than or equal to 18?
    print("You are eligible to vote")  # runs only if condition is True
```
**Output:**
```
You are eligible to vote
```

**Explanation:**
- The condition (`age >= 18`) is evaluated.
- If `True` → code inside `if` runs.
- If `False` → Python skips the block.

---

##  The `if–else` Statement

Allows a program to choose between **TWO** possible outcomes.

**Syntax:**
```python
if condition:
    statements_if_true
else:
    statements_if_false
```

**Example — Even or Odd Checker:**
```python
number = 8

# % gives remainder after division
if number % 2 == 0:  # if remainder is 0 → even number
    print("Even number")
else:  # runs when if condition is False
    print("Odd number")
```
**Output:**
```
Even number
```

**Explanation:**
- `number % 2` checks divisibility by 2.
- `==` means comparison (not assignment).
- `else` handles all remaining cases.

---

##  The `elif` (Else If) Ladder

Used when more than two conditions must be checked. Python evaluates conditions from top to bottom and executes the **FIRST true condition**.

**Syntax:**
```python
if condition1:
    statements
elif condition2:
    statements
else:
    statements
```

**Example — Grade Calculator:**
```python
marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 60:  # checked only if first condition is False
    print("Grade B")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
```
**Output:**
```
Grade B
```

>  **Important:** Conditions must be written in correct order (highest to lowest). Otherwise results may become incorrect.

---

## `match–case` Statement (Python Switch Alternative)

Introduced in **Python 3.10**, works similar to `switch` statements in other languages. Compares one variable against multiple possible values.

**Example — Day Selector:**
```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid day")  # _ acts as default case
```
**Output:**
```
Tuesday
```

---

## 📊 Comparison of Conditional Statements

| Statement | Purpose |
|-----------|---------|
| `if` | Executes code only when condition is true |
| `if–else` | Chooses between two outcomes |
| `elif` | Used for multiple conditions |
| `match–case` | Matches one variable against many values |

---

##  Common Beginner Mistakes

- Missing colon (`:`) after `if`, `elif`, or `else`
- Incorrect indentation
- Using `=` instead of `==` for comparison
- Writing conditions in the wrong order
- Forgetting that Python is case-sensitive

---

# Nested Conditional Statements & Logical Operators

## 📌 Introduction

Conditional statements help programs make decisions. In many real-world problems, a single condition is not enough. Programs often require multiple checks and combined conditions.

---

## Part 1: Nested Conditional Statements

### What are Nested Conditional Statements?

A **nested conditional statement** occurs when an `if` statement is placed inside another `if` statement. The inner condition executes only when the outer condition is `True`.

**General Syntax:**
```python
if condition1:
    # Outer block
    if condition2:
        # Inner block
        statements
```

### Example  — Voting and ID Verification
```python
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
```
**Sample Output:**
```
Enter age: 20
Eligible by age
Do you have ID? (yes/no): yes
You can vote
```
---
