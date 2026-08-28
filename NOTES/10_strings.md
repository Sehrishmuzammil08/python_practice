# 1. String Basics

### What are Strings?
Strings in Python are immutable sequences of Unicode characters. Once created, they cannot be modified.

```python
# Basic string characteristics
text = "Hello, World!"
print(f"Type: {type(text)}")        # <class 'str'>
print(f"Length: {len(text)}")       # 13
print(f"Is immutable? Yes - try text[0] = 'J' -> TypeError")
```
**Output**
```
Type: <class 'str'>
Length: 13
Is immutable? Yes - try text[0] = 'J' -> TypeError
```

---

## 2. String Creation and Initialization

```python
# Single quotes
name = 'John Doe'

# Double quotes (preferred for containing apostrophes)
message = "It's a beautiful day"

# Triple quotes for multi-line strings
multi_line = """This is line 1
This is line 2
This is line 3"""

# Using str() constructor
number_str = str(12345)     # "12345"  convert number (int) to string
float_str = str(3.14159)    # "3.14159" convert number (float) to string
bool_str = str(True)        # "True"   convert bool (true) to string

# Empty string
empty = ""

print(f"Name: {name}")
print(f"Message: {message}")
print(f"Multi-line:\n{multi_line}")
```
**Output**
```
Name: John Doe
Message: It's a beautiful day
Multi-line:
This is line 1
This is line 2
This is line 3
```

---

## 3. String Operations

### 3.1 Concatenation
```python
# Method 1: Using + operator
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
print(f"Concatenation: {full_name}")

# Method 2: f-strings (Python 3.6+)
age = 30
description = f"{full_name} is {age} years old"
print(f"f-string: {description}")
```
**Output**
```
Concatenation: John Smith
f-string: John Smith is 30 years old
```

### 3.2 Repetition
```python
# Using * operator
separator = "-" * 50
print(separator)

# Create pattern
pattern = ".*" * 10
print(f"Pattern: {pattern}")

# Practical example - creating table borders
border = "+" + "---+" * 3
print(border)
```
**Output**
```
--------------------------------------------------
Pattern: .*.*.*.*.*.*.*.*.*.*
+---+---+---+
```

### 3.3 Slicing (Indexing)
```python
text = "Python Programming"

# Basic indexing
print(f"First character: {text[0]}")     # P
print(f"Last character: {text[-1]}")     # g
print(f"Second last: {text[-2]}")        # n

# Slicing syntax: [start:stop:step]
print(f"Every 2nd char between 1-9: {text[1:9:2]}")
print(f"First 6 chars: {text[:6]}")       # Python
print(f"From index 7: {text[7:]}")        # Programming
print(f"Chars 7-18: {text[7:18]}")        # Programming
print(f"Every 2nd char: {text[::2]}")     # Pto rgamn
print(f"Reverse string: {text[::-1]}")    # gnimmargorP nohtyP
```
**Output**
```
First character: P
Last character: g
Second last: n
Every 2nd char between 1-9: yhnP
First 6 chars: Python
From index 7: Programming
Chars 7-18: Programming
Every 2nd char: Pto rgamn
Reverse string: gnimmargorP nohtyP
```

---

## 4. String Methods

### 4.1 Case Conversion Methods
```python
text = "Python Is AWESOME!"

print(f"Lower: {text.lower()}")
print(f"Upper: {text.upper()}")
print(f"Title: {text.title()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Swap case: {text.swapcase()}")
```
**Output**
```
Lower: python is awesome!
Upper: PYTHON IS AWESOME!
Title: Python Is Awesome!
Capitalize: Python is awesome!
Swap case: pYTHON iS awesome!
```

### 4.2 Strip Methods
```python
messy_string = "***Hello***World***"

# Removing characters from ends
print(f"Strip '*': {messy_string.strip('*')}")
print(f"Lstrip '*': {messy_string.lstrip('*')}")
print(f"Rstrip '*': {messy_string.rstrip('*')}")

# Whitespace removal
whitespace_text = " \t Hello World \n "
print(f"Strip whitespace: '{whitespace_text.strip()}'")
print(f"Lstrip whitespace: '{whitespace_text.lstrip()}'")
print(f"Rstrip whitespace: '{whitespace_text.rstrip()}'")
```
**Output**
```
Strip '*': Hello***World
Lstrip '*': Hello***World***
Rstrip '*': ***Hello***World
Strip whitespace: 'Hello World'
Lstrip whitespace: 'Hello World 
 '
Rstrip whitespace: ' 	 Hello World'
```

### 4.3 Replace Methods
```python
text = "The cat sat on the mat"

# Simple replace
print(f"Replace 'cat' with 'dog': {text.replace('cat', 'dog')}")

# Replace with count limit
print(f"Replace first 2 spaces: {text.replace(' ', '_', 2)}")

# Chain replacements
cleaned = text.replace('cat', 'dog').replace('mat', 'rug')
print(f"Chained replace: {cleaned}")
```
**Output**
```
Replace 'cat' with 'dog': The dog sat on the mat
Replace first 2 spaces: The_cat_sat on the mat
Chained replace: The dog sat on the rug
```

---

## 5. Escape Sequences
```python
print("Newline: Hello\nWorld")
print("Tab: Hello\tWorld")
print("Backslash: C:\\Users\\Name")
print("Single quote: 'Hello'")
print("Double quote: \"Hello\"")
print("Carriage return: Hello\rWorld")   # Overwrites Hello
print("Backspace: Hello\bWorld")         # Removes 'o'

# Raw strings (ignore escape sequences)
path = r"C:\new_folder\test.txt"
print(f"Raw string: {path}")
```
**Output**
```
Newline: Hello
World
Tab: Hello	World
Backslash: C:\Users\Name
Single quote: 'Hello'
Double quote: "Hello"
Carriage return: World
Backspace: HellWorld
Raw string: C:\new_folder\test.txt
```

---

## Quick Recap
- Strings are **immutable** — every "modification" method returns a *new* string.
- Use `f"{ }"` f-strings for clean formatting.
- `[start:stop:step]` slicing works the same on any sequence, and `[::-1]` reverses a string.
- `.strip() / .lstrip() / .rstrip()` clean unwanted characters or whitespace from the ends.
- `r"..."` raw strings stop `\n`, `\t`, `\\` etc. from being treated as escape sequences — handy for file paths.
