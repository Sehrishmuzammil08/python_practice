# Variables & Data Types in Python

## 1. What is a Variable?

A variable is `a container used to store data in memory`. It acts like a labeled box that holds a value which can be used later in a program.

- The **variable name** is the label
- The **value** is the data stored inside

>  The `=` symbol does **not** mean equality like in mathematics.
> It means **assignment** — "store the value on the right inside the variable on the left."

```python
age = 20 # age is label & 20 is value.
print(age)
# Output: 20
```

```python
# Assign multiple values at once
x, y, z = 10, 20, 30
```

### 📌 Variable Reassignment (Visualized)
```python
x = 10
print(x)        # Output: 10

x = 20
print(x)        # Output: 20

x = x + 5
print(x)        # Output: 25
```

**Execution flow:**
1. Retrieve current value of `x`
2. Perform calculation
3. Store the new result back into `x`

---

## 2. How Variables Work in Python

Python automatically determines the data type of a variable when you assign a value (this is called **dynamic typing**).

```python
x = 10        # Integer
y = 3.14      # Float
name = "John" # String
```

You can `check the data type` of a variable using the `type()` function.

```python
print(type(x))
print(type(y))
print(type(name))
```

```
Output:
<class 'int'>
<class 'float'>
<class 'str'>
```

---

## 3. Variable Naming Rules

-  Must start with a letter or underscore (`_`)
-  Can contain letters, numbers, and underscores
-  Cannot start with a number (invalid: `1name`)
-  Cannot contain spaces (invalid: `first name`)
-  Cannot use Python keywords (invalid: `class`, `True`, `False`, etc.)
-  Variable names are **case-sensitive** (`first_name` and `First_name` are different variables)

###  Valid Examples
```python
first_name = "Ali"
_age = 25
student1 = "Sara"
```

### Invalid Examples
```python
1name = "Ali"
first name = "Ali"
class = 10
```

>  **Naming convention tip:** Python style (PEP 8) recommends `snake_case` for variable names, e.g. `first_name`, `total_price`.
>   snake_case means writing multi-word names in lowercase with underscores between words:

> #  snake_case (recommended for Python)
first_name = "Ali"
#  Other styles (not Python convention)
firstName = "Ali"      # camelCase — common in JS/Java, not Python



### Python Keywords (Reserved Words)
```
False   def       elif      raise     class     from      if
finally is        nonlocal  while     and       return    None
continue for      del       or        yield     assert    global
else    not       import    pass      lambda    try       with
as      break     True      except    in
```

---
## Type Casting — converting one data type into another.

- Types:

**Implicit Casting (Automatic)**

Done by the compiler/interpreter
No data loss (usually smaller → larger type)
Example: int → float

**Explicit Casting (Manual)**

Done by the programmer
May cause data loss
Example: float → int (decimal part removed)

##  Core Data Types

- Numbers
- Strings
- Lists
- Dictionaries
- Tuples
- Files
- Sets

---
## Derived/Composite Types:

Array — collection of same type values
List — ordered, changeable collection
Tuple — ordered, unchangeable collection
Dictionary/Map — key-value pairs
Set — unordered, unique values

## Special Types:
Null/None — represents no value


## 4. Primitive Data Types in Python

Main primitive data types:
- **Numeric:** Integer (`int`) and Float (`float`)
- **String** (`str`)
- **Boolean** (`bool`)
- **None** (`NoneType`)

### 4.1 Integer (`int`)
Whole numbers, positive or negative.
```python
age = 25
temperature = -5
print(type(age))
# Output: <class 'int'>
```

### 4.2 Float (`float`)
Numbers with decimal points.
```python
price = 19.99
pi = 3.1416
print(type(price))
# Output: <class 'float'>
```

### 4.3 String (`str`)
Text values enclosed in single or double quotes.
```python
first = "John"
last = "Doe"
full = first + " " + last
print(full)
# Output: John Doe
```

### 4.4 Boolean (`bool`)
Boolean values represent `True` or `False`.
```python
is_logged_in = True
is_admin = False
print(10 > 5)
# Output: True
```

### 4.5 None (`NoneType`)
Used to represent the absence of a value or a null reference.
```python
result = None
default_value = None
user_input = None
```

## 5. Type Conversion (Casting)

Type casting is converting one data type into another.

### 5.1 Convert `int` to `float`
```python
x = 10
y = float(x)
print(y)
print(type(y))
# Output: 10.0
# <class 'float'>
```

### 5.2 Convert `float` to `int`
```python
price = 19.99
new_price = int(price)
print(new_price)
# Output: 19
```
>  Converting float → int **truncates** (cuts off) the decimal part, it does not round.

### 5.3 Convert `int` to `string`
```python
age = 25
text = str(age)
print("I am " + text + " years old")
# Output: I am 25 years old
```

### 5.4 Convert `string` to `int`
```python
num = "100"
number = int(num)
print(number + 50)
# Output: 150
```

---

## 6. Real-World Example (User Input)

```python
age = input("Enter your age: ")
print(type(age))

age = int(age)
print("Next year you will be", age + 1)
```

>  **Note:** `input()` always returns a **string**, so conversion to `int`/`float` is necessary before doing calculations.

###  Invalid Conversion Example
```python
num = "abc"
int(num)
# This will cause an error: ValueError
```

---

##  Key Points (Summary)

-  Variables store data values in memory.
-  Python automatically detects data types (**dynamic typing**).
-  Follow proper naming rules — use `snake_case`, avoid keywords.
-  Main primitive types: `int`, `float`, `str`, `bool`, `NoneType`.
-  Type casting converts data between types (`int()`, `float()`, `str()`).
-  `input()` always returns a **string** — convert before using in math.
-  Always compare `None` using `is` / `is not`, not `==`.
-  Invalid type conversions (e.g. `int("abc")`) raise a `ValueError`.
