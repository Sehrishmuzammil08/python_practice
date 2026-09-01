# Searching Algorithms in Python

# ==================================================

# 1. Linear Search

# ==================================================

# Find position of an element in a list by checking each item in order.

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

# Output: 70 found at index 3

# ==================================================

# 2. Find Maximum in List

# ==================================================

numbers = [23, 45, 12, 67, 34, 89, 21]
max_num = numbers[0]

for num in numbers:
if num > max_num:
max_num = num

print(f"Numbers: {numbers}")
print(f"Maximum: {max_num}")

# Output:

# Numbers: [23, 45, 12, 67, 34, 89, 21]

# Maximum: 89

# ==================================================

# 3. Binary Search

# ==================================================

# Find element in a SORTED list by repeatedly halving the search range.

def binary_search(arr, target):
low = 0
high = len(arr) - 1

```
while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid              # Found at index mid
    elif arr[mid] < target:
        low = mid + 1           # Search right half
    else:
        high = mid - 1          # Search left half

return -1   # Not found - returned after the while loop ends
```

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

# Output:

# List: [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]

# Searching for: 23

# Found at index 5

# ==================================================

# Bonus: Binary Search - "Not Found" Case

# ==================================================

numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
target = 100

print(f"\nList: {numbers}")
print(f"Searching for: {target}")

result = binary_search(numbers, target)

if result != -1:
print(f"Found at index {result}")
else:
print(f"Not found")

# Output:

# List: [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]

# Searching for: 100

# Not found
