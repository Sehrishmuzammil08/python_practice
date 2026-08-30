# Python Tuples - Notes

## 1. What is a Tuple?
A tuple is an **immutable, ordered** collection of items that can hold different data types.

```python
# Basic tuple example
fruits = ("apple", "banana", "cherry")
print(f"Tuple: {fruits}")
print(f"Type: {type(fruits)}")
```
**Output**
```
Tuple: ('apple', 'banana', 'cherry')
Type: <class 'tuple'>
```

---

## 2. Key Characteristics of Tuples
```python
# 1. Ordered - items have a specific order
fruits = ("apple", "banana", "orange")
print(f"Ordered: {fruits[0]}")   # Always "apple"

# 2. Immutable - cannot be changed after creation
colors = ("red", "green", "blue")
# colors[0] = "yellow"  # TypeError: 'tuple' object does not support item assignment

# 3. Allow duplicates
numbers = (1, 2, 2, 3, 3, 3)
print(f"Duplicates allowed: {numbers}")

# 4. Can hold mixed types
mixed = (1, "hello", 3.14, True)
print(f"Mixed types: {mixed}")
```
**Output**
```
Ordered: apple
Duplicates allowed: (1, 2, 2, 3, 3, 3)
Mixed types: (1, 'hello', 3.14, True)
```

---

## 3. Tuple Creation

### Method 1: Parentheses (Most Common)
```python
# Empty tuple
empty = ()
print(f"Empty tuple: {empty}")

# Tuple with one element (note the comma!)
single = (5,)         # Comma is necessary!
single_wrong = (5)    # This is an integer, not a tuple!
print(f"Single element tuple: {single}, Type: {type(single)}")
print(f"Without comma: {single_wrong}, Type: {type(single_wrong)}")

# Tuple with multiple elements
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "orange")
mixed = (1, "hello", 3.14, True)
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")
```
**Output**
```
Empty tuple: ()
Single element tuple: (5,), Type: <class 'tuple'>
Without comma: 5, Type: <class 'int'>
Numbers: (1, 2, 3, 4, 5)
Fruits: ('apple', 'banana', 'orange')
Mixed: (1, 'hello', 3.14, True)
```
> ⚠️ `(5)` is just the integer `5` in parentheses. You need a trailing comma — `(5,)` — to make a one-element tuple.

### Method 2: `tuple()` Constructor
```python
# From list
list_data = [1, 2, 3, 4]
tuple_from_list = tuple(list_data)
print(f"From list: {tuple_from_list}")

# From string
string_data = "hello"
tuple_from_string = tuple(string_data)
print(f"From string: {tuple_from_string}")

# From range
tuple_from_range = tuple(range(5))
print(f"From range: {tuple_from_range}")

# Empty tuple
empty = tuple()
print(f"Empty: {empty}")
```
**Output**
```
From list: (1, 2, 3, 4)
From string: ('h', 'e', 'l', 'l', 'o')
From range: (0, 1, 2, 3, 4)
Empty: ()
```

### Method 3: Without Parentheses (Tuple Packing)
```python
# Python automatically creates tuples
fruits = "apple", "banana", "cherry"
print(f"Without parentheses: {fruits}")
print(f"Type: {type(fruits)}")

# Multiple assignment is tuple unpacking
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")
```
**Output**
```
Without parentheses: ('apple', 'banana', 'cherry')
Type: <class 'tuple'>
a=1, b=2, c=3
```

---

## 4. Accessing Elements

### Indexing (Positive and Negative)
```python
fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Positive indexing (from start)
print(f"First: {fruits[0]}")
print(f"Second: {fruits[1]}")
print(f"Third: {fruits[2]}")

# Negative indexing (from end)
print(f"Last: {fruits[-1]}")
print(f"Second last: {fruits[-2]}")
print(f"Third last: {fruits[-3]}")
```
**Output**
```
First: apple
Second: banana
Third: cherry
Last: elderberry
Second last: date
Third last: cherry
```

### Slicing Tuples
```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(f"First 3: {numbers[:3]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Index 2 to 6: {numbers[2:7]}")
print(f"Every 2nd: {numbers[::2]}")
print(f"Reverse: {numbers[::-1]}")
```
**Output**
```
First 3: (0, 1, 2)
Last 3: (7, 8, 9)
Index 2 to 6: (2, 3, 4, 5, 6)
Every 2nd: (0, 2, 4, 6, 8)
Reverse: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```

### Looping Through Tuples
```python
fruits = ("apple", "banana", "cherry")

# Method 1: Direct iteration
print("Method 1:")
for fruit in fruits:
    print(fruit)

# Method 2: With index
print("\nMethod 2:")
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Method 3: With enumerate (best)
print("\nMethod 3:")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```
**Output**
```
Method 1:
apple
banana
cherry

Method 2:
0: apple
1: banana
2: cherry

Method 3:
0: apple
1: banana
2: cherry
```

---

## 5. Tuple Operations

### Concatenation (`+`)
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Combined: {combined}")
```
**Output**
```
Combined: (1, 2, 3, 4, 5, 6)
```

### Repetition (`*`)
```python
numbers = (1, 2, 3)
repeated = numbers * 3
print(f"Repeated: {repeated}")
```
**Output**
```
Repeated: (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

### Membership (`in` / `not in`)
```python
fruits = ("apple", "banana", "cherry")
print(f"Is 'apple' in fruits? {'apple' in fruits}")
print(f"Is 'grape' in fruits? {'grape' in fruits}")
print(f"Is 'orange' not in fruits? {'orange' not in fruits}")
```
**Output**
```
Is 'apple' in fruits? True
Is 'grape' in fruits? False
Is 'orange' not in fruits? True
```

### Length (`len()`)
```python
numbers = (1, 2, 3, 4, 5)
print(f"Length: {len(numbers)}")
```
**Output**
```
Length: 5
```

---

## 6. Tuple Methods
Tuples have only **two** methods (since they're immutable):

### `count()` - Count Occurrences
```python
numbers = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
print(f"Count of 1: {numbers.count(1)}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Count of 3: {numbers.count(3)}")
print(f"Count of 4: {numbers.count(4)}")
print(f"Count of 5: {numbers.count(5)}")
```
**Output**
```
Count of 1: 1
Count of 2: 2
Count of 3: 3
Count of 4: 4
Count of 5: 0
```

### `index()` - Find First Occurrence
```python
fruits = ("apple", "banana", "cherry", "banana", "date")
print(f"Index of 'apple': {fruits.index('apple')}")
print(f"Index of 'banana': {fruits.index('banana')}")   # First occurrence
print(f"Index of 'cherry': {fruits.index('cherry')}")
print(f"Index of 'date': {fruits.index('date')}")

# Search in a range
print(f"Index of 'banana' after index 2: {fruits.index('banana', 2)}")
```
**Output**
```
Index of 'apple': 0
Index of 'banana': 1
Index of 'cherry': 2
Index of 'date': 4
Index of 'banana' after index 2: 3
```

---

## 7. Tuple Packing and Unpacking

### Packing (Creating a Tuple)
```python
# Packing values into a tuple
person = "John", 30, "New York"
print(f"Packed tuple: {person}")
print(f"Type: {type(person)}")
```
**Output**
```
Packed tuple: ('John', 30, 'New York')
Type: <class 'tuple'>
```

### Unpacking (Extracting Values)
```python
person = ("John", 30, "New York")
name, age, city = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
```
**Output**
```
Name: John
Age: 30
City: New York
```

### Swapping Variables (Tuple Magic)
```python
# Classic swap using tuple unpacking
a = 10
b = 20
print(f"Before swap: a={a}, b={b}")

# Swap without temporary variable
a, b = b, a
print(f"After swap: a={a}, b={b}")
```
**Output**
```
Before swap: a=10, b=20
After swap: a=20, b=10
```

### Unpacking with Asterisk (`*`)
```python
# Collect remaining items
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")

# Another example
fruits = ("apple", "banana", "cherry", "date", "elderberry")
first, second, *rest = fruits
print(f"First: {first}")
print(f"Second: {second}")
print(f"Rest: {rest}")
```
**Output**
```
First: 1
Middle: [2, 3, 4]
Last: 5
First: apple
Second: banana
Rest: ['cherry', 'date', 'elderberry']
```

---

## Quick Recap
- Tuples are **ordered** and **immutable** — once created, items can't be changed, added, or removed.
- A single-element tuple needs a trailing comma: `(5,)` not `(5)`.
- Only two built-in methods exist: `count()` and `index()`.
- Tuple unpacking is the classic Python way to swap variables (`a, b = b, a`) or split a tuple into named parts, including with `*` to grab "the rest".
- Because they're immutable, tuples are useful when you want data that shouldn't accidentally change (e.g. coordinates, RGB values, fixed records).
