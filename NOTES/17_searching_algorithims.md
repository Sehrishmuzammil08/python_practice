# Searching Algorithms - Notes

## 1. Linear Search

**Problem:** Find the position of an element in a list.

### Algorithm
```
Start
    Set list
    Take target
    Set position = -1
    For i from 0 to n-1:
        If list[i] == target then
            position = i
            break
    END FOR
    If position != -1 then
        Display "Found at index", position
    Else
        print "Not found"
End
```

### Code
```python
# Linear search
numbers = [10, 23, 45, 70, 11, 15, 89]
target = 70
position = -1
for i in range(len(numbers)):
    if numbers[i] == target:
        position = i
        break
if position != -1:
    print(f"{target} found at index {position}")
else:
    print(f"{target} not found")
```
**Output**
```
70 found at index 3
```

> Linear search checks each element **one by one**, in order, until it finds a match (or reaches the end). It works on **any** list — sorted or not — but is `O(n)`, so it can be slow on large lists.

---

## 2. Find Maximum in List

**Problem:** Find the largest number in a list.

### Algorithm
```
Start
    Take list of numbers
    Set max = first number
    For each number in list:
        If number > max then
            max = number
    END FOR
    Display max
End
```

### Code
```python
# Find maximum in list
numbers = [23, 45, 12, 67, 34, 89, 21]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Numbers: {numbers}")
print(f"Maximum: {max_num}")
```
**Output**
```
Numbers: [23, 45, 12, 67, 34, 89, 21]
Maximum: 89
```

---

## 3. Binary Search

### What is Binary Search?
Binary Search is an efficient algorithm to find an element in a **sorted** list by repeatedly dividing the search interval in half.

### Real-Life Analogy
Searching for a word in a dictionary:
- Open the dictionary at the middle page
- If the word comes before, search the left half
- If the word comes after, search the right half
- Repeat until found

### How Binary Search Works
**Key Rule: the list MUST be sorted**

```
Sorted List: [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
Search for: 23

Step 1: Find middle element (16)
        16 < 23 → Search right half
Step 2: Search in [23, 38, 45, 56, 72]
        Middle = 45
        45 > 23 → Search left half
Step 3: Search in [23, 38]
        Middle = 23
        23 == 23 → Found!
```

### Binary Search Algorithm (Step by Step)
```
Start
FUNCTION BinarySearch(arr, target):
    Set low = 0 (first index)
    Set high = len(arr) - 1 (last index)
    While low <= high:
        mid = (low + high) // 2
        If arr[mid] == target:
            Return mid (found)
        Else if arr[mid] < target:
            low = mid + 1 (search right)
        Else:
            high = mid - 1 (search left)
    END WHILE
    Return -1 (not found)
END FUNCTION
End
```

### Binary Search Code
```python
# Binary Search - Find element in sorted list
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid              # Found at index mid
        elif arr[mid] < target:
            low = mid + 1           # Search right half
        else:
            high = mid - 1          # Search left half

    return -1   # Not found - function returns -1 after the while loop ends

# Test the function
numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
target = 23
print(f"List: {numbers}")
print(f"Searching for: {target}")
result = binary_search(numbers, target)
if result != -1:
    print(f"Found at index {result}")
else:
    print(f"Not found")
```
**Output**
```
List: [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
Searching for: 23
Found at index 5
```

---

## Quick Recap
- **Linear search** checks every element in order — works on unsorted data, but is `O(n)`.
- **Binary search** repeatedly halves the search range — much faster (`O(log n)`), but the list **must be sorted first**.
- "Find maximum" follows the same pattern as linear search: start with an assumption (first element), then loop and update it whenever you find something better.
- Binary search's core loop: compute `mid`, compare to `target`, then narrow to the left half (`high = mid - 1`) or right half (`low = mid + 1`) — repeat until `low > high`.
