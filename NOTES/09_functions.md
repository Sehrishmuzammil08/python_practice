# Python Functions

## 1. What is a Function?

A function is a reusable block of code that performs a specific task. Instead of writing the same code again and again, we define it once and reuse it.

## 2. Why Use Functions?

Functions are useful because they provide:

* **Code Reusability:** Write once and use many times.
* **Modularity:** Break complex problems into smaller parts.
* **Readability:** Make code easier to understand.
* **Maintainability:** Fix or update code in one place.
* **Testing:** Test individual parts of a program.
* **Abstraction:** Hide complex logic behind a simple interface.

## 3. Basic Syntax

```python
def function_name(parameters):
    # body of function
    return value
```

### Explanation

* `def` → Keyword used to define a function.
* `function_name` → Name given to the function.
* `parameters` → Inputs received by the function.
* `return` → Sends a value back to the caller. It is optional.

## 4. Parameters vs Arguments

* **Parameter:** A variable defined in the function definition.
* **Argument:** The actual value passed to a function when it is called.

Example:

```python
def greet(name):
    print("Hello", name)

greet("Ali")
```

Here:

* `name` is the **parameter**.
* `"Ali"` is the **argument**.

## 5. Default Arguments

A default argument `gives a parameter a default value if no value is provided.`

```python
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Ali")
```

Output:

```text
Hello Student
Hello Ali
```

## 6. Types of Functions

### 1. No Parameters, No Return

```python
def hello():
    print("Hi")

hello()
```

### 2. Parameters, No Return

```python
def add(a, b):
    print(a + b)

add(2, 3)
```

### 3. No Parameters, Return Value

```python
def get_value():
    return 10

print(get_value())
```

### 4. Parameters with Return Value

```python
def multiply(a, b):
    return a * b

print(multiply(3, 4))
```

## 7. Return Keyword

The `return` keyword sends a value back to the place where the function was called and stops the function's execution.

Example:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

Output:

```
8
```

## 8. Lambda Function

A lambda function is a small anonymous function written using the `lambda` keyword. It can have multiple arguments but contains only one expression.

Example:

```python
square = lambda x: x * x
print(square(5))
```

Output:

```text
25
```

### Lambda with Multiple Arguments

```python
multiply = lambda a, b: a * b
print(multiply(4, 5))

concat = lambda s1, s2: s1 + " " + s2
print(concat("Hello", "World"))
```

## 9. Recursion

Recursion is a `technique where a function calls itself` to solve a problem by breaking it into smaller, similar problems.

### Important Parts of Recursion

* **Base Case:** The stopping condition that prevents infinite recursion.
* **Recursive Case:** The part where the function calls itself with a modified value.

Example:

```python
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

## 10. Built-in Functions

Built-in functions are functions that are already provided by Python. We can use them without defining them ourselves.

| Function   | Purpose             | Example             |
| ---------- | ------------------- | ------------------- |
| `print()`  | Display output      | `print("Hello")`    |
| `input()`  | Get user input      | `input("Name: ")`   |
| `len()`    | Get length          | `len([1, 2, 3])`    |
| `type()`   | Get data type       | `type(5)`           |
| `int()`    | Convert to integer  | `int("123")`        |
| `str()`    | Convert to string   | `str(123)`          |
| `float()`  | Convert to float    | `float("3.14")`     |
| `list()`   | Convert to list     | `list("abc")`       |
| `range()`  | Generate a sequence | `range(5)`          |
| `sum()`    | Add values          | `sum([1, 2, 3])`    |
| `min()`    | Find minimum        | `min([1, 2, 3])`    |
| `max()`    | Find maximum        | `max([1, 2, 3])`    |
| `sorted()` | Sort values         | `sorted([3, 1, 2])` |
| `abs()`    | Get absolute value  | `abs(-5)`           |
| `round()`  | Round a number      | `round(3.14159, 2)` |

