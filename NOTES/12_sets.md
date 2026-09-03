# Python Sets - Notes

## 1. What is a Set?
A set is an **unordered, mutable** collection of **unique** elements.

```python
# Basic set example
fruits = {"apple", "banana", "cherry"}
print(f"Set: {fruits}")
print(f"Type: {type(fruits)}")
```
**Output**
```
Set: {'cherry', 'banana', 'apple'}
Type: <class 'set'>
```
>  Sets are **unordered** — the printed order of elements can be different each time you run the code. Don't rely on it.

---

## 2. Key Characteristics of Sets
```python
# 1. Unordered - elements have no specific order
my_set = {1, 2, 3}
print(f"Set order is not guaranteed: {my_set}")

# 2. Unique elements - no duplicates allowed
numbers = {1, 2, 2, 3, 3, 3, 4}
print(f"Duplicates removed: {numbers}")

# 3. Mutable - can add/remove elements
my_set = {1, 2, 3}
my_set.add(4)
print(f"After adding: {my_set}")

# 4. Can hold different data types
mixed = {1, "hello", 3.14, True}
print(f"Mixed types: {mixed}")
```
**Output**
```
Set order is not guaranteed: {1, 2, 3}
Duplicates removed: {1, 2, 3, 4}
After adding: {1, 2, 3, 4}
Mixed types: {1, 3.14, 'hello'}
```

---

## 3. Set Creation

### Method 1: Curly Braces (Most Common)
```python
# Empty set - Note: {} creates empty dictionary, not set!
empty_set = set()   # Correct way
empty_dict = {}      # This is a dictionary!
print(f"Empty set: {empty_set}, Type: {type(empty_set)}")
print(f"Empty dict: {empty_dict}, Type: {type(empty_dict)}")

# Set with values
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True}
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
```
**Output**
```
Empty set: set(), Type: <class 'set'>
Empty dict: {}, Type: <class 'dict'>
Fruits: {'cherry', 'banana', 'apple'}
Numbers: {1, 2, 3, 4, 5}
Mixed: {1, 3.14, 'hello'}
```

### Method 2: `set()` Constructor
```python
# From list
list_data = [1, 2, 2, 3, 3, 3, 4]
set_from_list = set(list_data)
print(f"From list: {set_from_list}")

# From tuple
tuple_data = (1, 2, 2, 3, 3)
set_from_tuple = set(tuple_data)
print(f"From tuple: {set_from_tuple}")

# From string
string_data = "hello"
set_from_string = set(string_data)
print(f"From string: {set_from_string}")

# From range
set_from_range = set(range(5))
print(f"From range: {set_from_range}")
```
**Output**
```
From list: {1, 2, 3, 4}
From tuple: {1, 2, 3}
From string: {'o', 'h', 'e', 'l'}
From range: {0, 1, 2, 3, 4}
```

---

## 4. Set Operations

### 4.1 Adding Elements
```python
fruits = {"apple", "banana"}

# add() - adds single element
fruits.add("cherry")
print(f"After add: {fruits}")

# Adding duplicate has no effect
fruits.add("apple")   # Won't add again
print(f"Adding duplicate: {fruits}")

# update() - adds multiple elements
fruits.update(["date", "elderberry", "fig"])
print(f"After update: {fruits}")

# Add from another set
more_fruits = {"grape", "honeydew"}
fruits.update(more_fruits)
print(f"After adding set: {fruits}")
```
**Output** *(order may vary — this is one possible run)*
```
After add: {'cherry', 'banana', 'apple'}
Adding duplicate: {'cherry', 'banana', 'apple'}
After update: {'cherry', 'date', 'elderberry', 'fig', 'banana', 'apple'}
After adding set: {'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'banana', 'apple'}
```

### 4.2 Removing Elements
```python
fruits = {"apple", "banana", "cherry", "date", "elderberry"}

# remove() - removes element (error if not found)
fruits.remove("banana")
print(f"After remove: {fruits}")

# discard() - removes if exists (no error if not found)
fruits.discard("grape")   # Won't give error
fruits.discard("cherry")
print(f"After discard: {fruits}")

# pop() - removes and returns arbitrary element
removed = fruits.pop()
print(f"Removed: {removed}, Remaining: {fruits}")

# clear() - removes all elements
fruits.clear()
print(f"After clear: {fruits}")
```
**Output** *(order may vary — `pop()` removes an arbitrary element)*
```
After remove: {'cherry', 'date', 'elderberry', 'apple'}
After discard: {'date', 'elderberry', 'apple'}
Removed: date, Remaining: {'elderberry', 'apple'}
After clear: set()
```
> ⚠️ `remove()` raises a `KeyError` if the element isn't in the set. `discard()` does the same job but stays silent if it's missing — use it when you're not sure the element exists.

### 4.3 Checking Membership
```python
fruits = {"apple", "banana", "cherry"}

# in operator
print(f"Is 'apple' in fruits? {'apple' in fruits}")
print(f"Is 'grape' in fruits? {'grape' in fruits}")

# not in operator
print(f"Is 'orange' not in fruits? {'orange' not in fruits}")

# Length of set
print(f"Number of fruits: {len(fruits)}")
```
**Output**
```
Is 'apple' in fruits? True
Is 'grape' in fruits? False
Is 'orange' not in fruits? True
Number of fruits: 3
```

### 4.4 Looping Through a Set
Since sets are unordered, you can still loop through them, but the order is not guaranteed.
```python
fruits = {"apple", "banana", "cherry", "date", "elderberry"}
print("Basic for loop:")
for fruit in fruits:
    print(fruit)
```
**Output** *(order may be different each time you run!)*
```
Basic for loop:
cherry
date
apple
elderberry
banana
```

---

## Quick Recap
- Sets hold **unique** elements only — duplicates are silently dropped.
- Sets are **unordered**, so never rely on the printed order or on indexing (`fruits[0]` doesn't work on a set).
- `{}` makes an empty **dictionary**, not a set — use `set()` for an empty set.
- `add()` inserts one item, `update()` merges in multiple items (from a list, tuple, or another set).
- `remove()` errors if the item is missing; `discard()` doesn't; `pop()` removes an arbitrary item; `clear()` empties the set.
- Great for membership checks (`in`) and removing duplicates fast, e.g. `set(my_list)`.
