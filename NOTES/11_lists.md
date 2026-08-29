# 1. What is a List?
A list is a **mutable, ordered** collection of items that can hold different data types.

---

## 2. Creating a List
```python
# Empty list
my_list = []

# List with values
numbers = [1, 2, 3, 4, 5]

# Mixed data types
mixed = [10, "Python", 3.14, True]
```

---

## 3. Key Characteristics of Lists
```python
# 1. Ordered - items have a specific order
fruits = ["apple", "banana", "orange"]
print(f"Ordered: {fruits}")

# 2. Mutable - can be changed after creation
fruits[0] = "grape"
print(f"After change: {fruits}")

# 3. Allow duplicates
numbers = [1, 2, 2, 3, 3, 3]
print(f"Duplicates allowed: {numbers}")

# 4. Can hold mixed types
mixed = [1, "text", 3.14, True]
print(f"Mixed types: {mixed}")
```
**Output**
```
Ordered: ['apple', 'banana', 'orange']
After change: ['grape', 'banana', 'orange']
Duplicates allowed: [1, 2, 2, 3, 3, 3]
Mixed types: [1, 'text', 3.14, True]
```

---

## 4. Accessing Elements

### 4.1 Indexing (Positive and Negative)
```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

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

### 4.2 Length (`len()`)
```python
numbers = [1, 2, 3, 4, 5]
print(f"Length: {len(numbers)}")
```
**Output**
```
Length: 5
```

### 4.3 Accessing with Loops
```python
fruits = ["apple", "banana", "cherry"]

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

### 4.4 Membership (`in` / `not in`)
```python
fruits = ["apple", "banana", "cherry"]
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

---

## 5. List Methods

### 5.1 Adding Elements
```python
# append() - add to end
fruits = ["apple", "banana"]
fruits.append("cherry")
print(f"After append: {fruits}")

# insert() - add at specific position
fruits.insert(1, "blueberry")
print(f"After insert: {fruits}")

# extend() - add multiple elements
more_fruits = ["date", "elderberry"]
fruits.extend(more_fruits)
print(f"After extend: {fruits}")

# Using + operator
fruits = fruits + ["fig", "grape"]
print(f"After +: {fruits}")
```
**Output**
```
After append: ['apple', 'banana', 'cherry']
After insert: ['apple', 'blueberry', 'banana', 'cherry']
After extend: ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']
After +: ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
```

### 5.2 Removing Elements
```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

# remove() - removes first occurrence
fruits.remove("banana")
print(f"After remove: {fruits}")

# pop() - removes by index (default last)
removed = fruits.pop()
print(f"Removed: {removed}, List: {fruits}")

removed = fruits.pop(1)
print(f"Removed index 1: {removed}, List: {fruits}")

# clear() - removes all elements
fruits.clear()
print(f"After clear: {fruits}")
```
**Output**
```
After remove: ['apple', 'cherry', 'banana', 'date']
Removed: date, List: ['apple', 'cherry', 'banana']
Removed index 1: cherry, List: ['apple', 'banana']
After clear: []
```

### 5.3 Searching and Counting
```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# index() - find first occurrence
position = numbers.index(2)
print(f"First 2 at index: {position}")

# count() - count occurrences
count = numbers.count(2)
print(f"Number of 2's: {count}")

# in operator
print(f"Is 3 in list? {3 in numbers}")
print(f"Is 10 in list? {10 in numbers}")
```
**Output**
```
First 2 at index: 1
Number of 2's: 3
Is 3 in list? True
Is 10 in list? False
```

### 5.4 Sorting and Reversing
```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# sort() - modifies original (ascending)
numbers.sort()
print(f"Ascending sort: {numbers}")

# sort(reverse=True) - descending
numbers.sort(reverse=True)
print(f"Descending sort: {numbers}")

# reverse() - reverses order
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"Reversed: {numbers}")

# sorted() - returns new list (doesn't modify original)
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(f"Original: {original}")
print(f"Sorted (new): {sorted_list}")
```
**Output**
```
Ascending sort: [1, 1, 2, 3, 4, 5, 9]
Descending sort: [9, 5, 4, 3, 2, 1, 1]
Reversed: [5, 4, 3, 2, 1]
Original: [3, 1, 4, 1, 5]
Sorted (new): [1, 1, 3, 4, 5]
```

### 5.5 Copying Lists
```python
original = [1, 2, 3]

# Wrong way - just references same list
wrong_copy = original
wrong_copy.append(4)
print(f"Original: {original}")   # Changed! - not a real copy

# Method 1: slice copy
original = [1, 2, 3]
copy1 = original[:]
copy1.append(4)
print(f"Original: {original}, Copy: {copy1}")

# Method 2: list() constructor
original = [1, 2, 3]
copy2 = list(original)
copy2.append(4)
print(f"Original: {original}, Copy: {copy2}")

# Method 3: copy() method
original = [1, 2, 3]
copy3 = original.copy()
copy3.append(4)
print(f"Original: {original}, Copy: {copy3}")
```
**Output**
```
Original: [1, 2, 3, 4]
Original: [1, 2, 3], Copy: [1, 2, 3, 4]
Original: [1, 2, 3], Copy: [1, 2, 3, 4]
Original: [1, 2, 3], Copy: [1, 2, 3, 4]
```
>  `wrong_copy = original` does **not** create a new list — both names point to the same list in memory. Always use `[:]`, `list()`, or `.copy()` for a real copy.

---

## 6. List Slicing

### 6.1 Basic Slicing
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Syntax: [start:stop:step]
print(f"First 3: {numbers[:3]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Index 2 to 5: {numbers[2:6]}")
print(f"Every 2nd: {numbers[::2]}")
print(f"Reverse: {numbers[::-1]}")
```
**Output**
```
First 3: [0, 1, 2]
Last 3: [7, 8, 9]
Index 2 to 5: [2, 3, 4, 5]
Every 2nd: [0, 2, 4, 6, 8]
Reverse: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### 6.2 Modifying with Slicing
```python
numbers = [1, 2, 3, 4, 5]

# Replace slice
numbers[1:3] = [20, 30]
print(f"After replacement: {numbers}")

# Insert with slice
numbers[2:2] = [100, 200]
print(f"After insertion: {numbers}")

# Delete with slice
numbers[1:4] = []
print(f"After deletion: {numbers}")
```
**Output**
```
After replacement: [1, 20, 30, 4, 5]
After insertion: [1, 20, 100, 200, 30, 4, 5]
After deletion: [1, 4, 5]
```

---

## Quick Recap
- Lists are **ordered**, **mutable**, allow **duplicates**, and can hold **mixed types**.
- `append()` adds one item to the end; `extend()` merges another iterable in; `insert()` adds at a chosen position.
- `remove()` deletes by value (first match), `pop()` deletes by index (default last) and returns it, `clear()` empties the list.
- `sort()` / `reverse()` change the list in place; `sorted()` returns a **new** list and leaves the original untouched.
- `copy()`, `list(original)`, and `original[:]` all make a real copy — plain `=` just creates another name for the same list.
- Slicing `[start:stop:step]` can also be used on the left side of `=` to replace, insert, or delete a chunk of the list at once.
