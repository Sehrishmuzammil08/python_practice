# Basic Program Structure in Python — Complete Guide

## 1. Statements and Execution Order

### 📌 What is a Statement?
A statement is a `single instruction that Python can execute` — like a complete sentence in English.

```python
# Examples of statements:
x = 5
print("Hello")
y = x + 10
```

### 📌 Execution Order: Top-to-Bottom, Left-to-Right
Python executes code in the order it appears — **from top to bottom**, and within a line, **from left to right**.

```python
print("Step 1: Starting the program")
name = "Alice"
age = 25
print("Step 2: Name is", name)
print("Step 3: Age is", age)
result = age * 2
print("Step 4: Double age is", result)
print("Step 5: Program complete")
```

>  **Important:** Variables must be defined *before* they are used.

```python
#  WRONG
print(x)
x = 10

#  CORRECT
x = 10
print(x)
```

---

## 2. Comments in Python

>  Comments explain **WHY** code does something, not just *what* it does.

### Single-line Comments (`#`)
```python
# This is a comment
x = 5  # Inline comment

# Good comment example:
age = 25  # Default age for new users
```

### Multi-line Comments (Triple Quotes)
```python
"""
This is a multi-line comment.
Often used for documentation.
"""
```

## Docstrings
A docstring (documentation string) is a special `string written inside triple quotes` (""" """ or ''' ''') to explain what a module, function, class, or method does.
EXAMPLE:
def add(a, b):
    """This function adds two numbers."""  (Its docstring/ triple quotes)
return a + b

### Docstrings Example
```python
def calculate_area(radius):
    """Calculate area of a circle"""
    area = 3.14159 * radius ** 2
    return area
```

---

## 3. Indentation and Whitespace
**Whitespace** refers to the spaces, tabs, and blank lines used in Python code. Python uses whitespace (especially indentation) to define blocks of code
`1 Indentation = 4 spaces`

>  Python uses **indentation** (not braces `{}`) to define blocks of code.
> Standard practice is **4 spaces** per indentation level.

```python
x = 10
if x > 5:
    print("x is greater than 5")
    y = x * 2
print("Outside block")
```

---

## 4. Basic Input and Output

### Using `print()`
```python
print("Hello, World!")
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")
```

### Using `input()`
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Next year you will be {age + 1}")
```

>  **Note:** `input()` always returns a **string** — convert it (e.g., `int()`) if you need a number.

---

##  Key Points (Summary)

-  Statements execute **in order**, top to bottom.
-  Comments explain **WHY**, not just what.
-  **Indentation** defines code blocks in Python.
-  `input()` always returns a **string**.
-  Use **f-strings** (`f"..."`) for clean formatting.
