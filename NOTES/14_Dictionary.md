# Python Dictionaries

## What is a Dictionary?
A dictionary stores data in **key-value pairs**. Like a real dictionary - word (key) and its meaning (value).

```python
# Simple dictionary example
student = {
    "name": "John",
    "age": 15,
    "grade": "A"
}
print(student)
```
**Output**
```
{'name': 'John', 'age': 15, 'grade': 'A'}
```

---

## 1. Creating Dictionaries

### Empty Dictionary
```python
my_dict = {}
print(my_dict)
```
**Output**
```
{}
```

### Dictionary with Data
```python
# String keys
person = {"name": "Alice", "city": "New York", "job": "Engineer"}
print(person)

# Number keys
scores = {1: "Poor", 2: "Average", 3: "Good", 4: "Excellent"}
print(scores)

# Mixed keys (but keys must be unique)
mixed = {"name": "John", 10: "ten", 3.14: "pi"}
print(mixed)
```
**Output**
```
{'name': 'Alice', 'city': 'New York', 'job': 'Engineer'}
{1: 'Poor', 2: 'Average', 3: 'Good', 4: 'Excellent'}
{'name': 'John', 10: 'ten', 3.14: 'pi'}
```

---

## 2. Accessing Dictionary Values

### Using Square Brackets `[ ]`
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
```
**Output**
```
Name: Alice
Age: 25
City: New York
```

### Using `get()` Method (Safer)
```python
person = {"name": "Alice", "age": 25}

# Get existing key
print(person.get("name"))

# Get non-existing key (no error, returns None)
print(person.get("city"))

# Get with default value
print(person.get("city", "Unknown"))
```
**Output**
```
Alice
None
Unknown
```
> ⚠️ `person["city"]` raises a `KeyError` if the key doesn't exist. `person.get("city")` returns `None` instead (or a default you supply) — much safer when you're not sure the key is there.

---

## 3. Adding and Updating Values

### Add New Key-Value Pair
```python
person = {"name": "John", "age": 30}
person["city"] = "New York"
print(person)
```
**Output**
```
{'name': 'John', 'age': 30, 'city': 'New York'}
```

### Update Existing Value
```python
person = {"name": "John", "age": 30}
person["age"] = 31
print(person)
```
**Output**
```
{'name': 'John', 'age': 31}
```

### Update Multiple Values at Once
```python
person = {"name": "John", "age": 30}
person.update({"age": 31, "city": "NYC", "job": "Engineer"})
print(person)
```
**Output**
```
{'name': 'John', 'age': 31, 'city': 'NYC', 'job': 'Engineer'}
```

---

## 4. Removing Values

### Using `pop()` - Remove and Return
```python
person = {"name": "John", "age": 30, "city": "NYC"}
removed = person.pop("age")
print(f"Removed: {removed}")
print(f"After pop: {person}")
```
**Output**
```
Removed: 30
After pop: {'name': 'John', 'city': 'NYC'}
```

### Using `del` - Delete Key
```python
person = {"name": "John", "age": 30, "city": "NYC"}
del person["city"]
print(person)
```
**Output**
```
{'name': 'John', 'age': 30}
```

### Using `clear()` - Remove Everything
```python
person = {"name": "John", "age": 30, "city": "NYC"}
person.clear()
print(person)
```
**Output**
```
{}
```

---

## 5. Checking if Key Exists
```python
person = {"name": "John", "age": 30}

if "name" in person:
    print("Name exists!")

if "city" in person:
    print("City exists")
else:
    print("City does not exist")
```
**Output**
```
Name exists!
City does not exist
```

---

## 6. Getting All Keys, Values, and Items
```python
person = {"name": "John", "age": 30, "city": "NYC"}

# Get all keys
print(f"Keys: {person.keys()}")
print(f"Keys as list: {list(person.keys())}")

# Get all values
print(f"Values: {person.values()}")
print(f"Values as list: {list(person.values())}")

# Get all key-value pairs
print(f"Items: {person.items()}")
print(f"Items as list: {list(person.items())}")
```
**Output**
```
Keys: dict_keys(['name', 'age', 'city'])
Keys as list: ['name', 'age', 'city']
Values: dict_values(['John', 30, 'NYC'])
Values as list: ['John', 30, 'NYC']
Items: dict_items([('name', 'John'), ('age', 30), ('city', 'NYC')])
Items as list: [('name', 'John'), ('age', 30), ('city', 'NYC')]
```

---

## 7. Looping Through Dictionaries

### Loop Through Keys
```python
person = {"name": "John", "age": 30, "city": "NYC"}
print("All keys:")
for key in person:
    print(key)
```
**Output**
```
All keys:
name
age
city
```

### Loop Through Values
```python
person = {"name": "John", "age": 30, "city": "NYC"}
print("All values:")
for value in person.values():
    print(value)
```
**Output**
```
All values:
John
30
NYC
```

### Loop Through Key-Value Pairs (Most Common)
```python
person = {"name": "John", "age": 30, "city": "NYC"}
print("Key-Value pairs:")
for key, value in person.items():
    print(f"{key} = {value}")
```
**Output**
```
Key-Value pairs:
name = John
age = 30
city = NYC
```

---

## 8. Dictionary Length
```python
person = {"name": "John", "age": 30, "city": "NYC", "job": "Engineer"}
print(f"Number of items: {len(person)}")
```
**Output**
```
Number of items: 4
```

---

## 9. Common Mistakes to Avoid

### Mistake 1: Accessing Non-Existent Key
```python
person = {"name": "John", "age": 30}

# Wrong - causes error
# print(person["city"])   # KeyError!

# Correct - use get()
print(person.get("city", "Not found"))
```

### Mistake 2: Using Mutable Keys
```python
# Wrong - list can't be a key
# my_dict = {[1, 2]: "value"}   # TypeError!

# Correct - use a tuple instead (tuples are immutable)
my_dict = {(1, 2): "value"}
print(my_dict)
```

### Mistake 3: Forgetting Quotes Around String Keys
```python
# Wrong - name is treated as a variable
# person = {name: "John"}   # Error if `name` isn't already defined

# Correct
person = {"name": "John"}
```

---

## Quick Reference Card (Basics Only)

| Operation | Code | What it does |
|---|---|---|
| Create empty | `d = {}` | Empty dictionary |
| Create with data | `d = {"a":1, "b":2}` | Dictionary with 2 items |
| Access value | `d["key"]` | Get value (error if missing) |
| Safe access | `d.get("key")` | Get value or `None` |
| Add/Update | `d["key"] = value` | Add or change |
| Delete | `del d["key"]` | Remove key |
| Remove & return | `d.pop("key")` | Remove and get value |
| Clear all | `d.clear()` | Empty the dictionary |
| Check key | `"key" in d` | Returns `True`/`False` |
| Get length | `len(d)` | Number of items |
| Get all keys | `d.keys()` | All keys |
| Get all values | `d.values()` | All values |
| Get all pairs | `d.items()` | Key-value pairs |
| Loop keys | `for k in d:` | Iterate keys |
| Loop values | `for v in d.values():` | Iterate values |
| Loop pairs | `for k, v in d.items():` | Iterate both |

---

## Quick Recap
- Dictionaries map unique **keys** to **values** — order of insertion is preserved (Python 3.7+).
- Keys must be **immutable** (strings, numbers, tuples) — lists can't be keys.
- Use `.get()` instead of `[]` when a key might not exist, to avoid a `KeyError`.
- `.keys()`, `.values()`, `.items()` give you views you can loop over directly or convert to a `list`.
- `for key, value in d.items():` is the most common way to loop through a dictionary.
