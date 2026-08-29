# ========================================
# Program 1: Create a list and print it.
# ========================================
# Write a program to create a list of fruits and print the list.
fruits = ["apple", "banana", "cherry"]
print(fruits)
# Output: ['apple', 'banana', 'cherry']


# ========================================
# Program 2: Access list item by index.
# ========================================
# Write a program to access the second fruit from the list and print it.
fruits = ["apple", "banana", "cherry"]
print("Second fruit is:", fruits[1])
# Output: Second fruit is: banana


# ========================================
# Program 3: Change list item.
# ========================================
# Write a program to change the second item in the list to 'mango'.
fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)
# Output: ['apple', 'mango', 'cherry']


# ========================================
# Program 4: Add item using append().
# ========================================
# Write a program to add 'cherry' at the end of the list using append().
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)
# Output: ['apple', 'banana', 'cherry']


# ========================================
# Program 5: Add item at specific index using insert().
# ========================================
# Write a program to insert 'mango' at index 1 in the list.
fruits = ["apple", "banana"]
fruits.insert(1, "mango")
print(fruits)
# Output: ['apple', 'mango', 'banana']


# ========================================
# Program 6: Remove item using remove().
# ========================================
# Write a program to remove 'banana' from the list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
# Output: ['apple', 'cherry']


# ========================================
# Program 7: Remove item using pop(index).
# ========================================
# Write a program to remove the item at index 1 using pop().
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)
# Output: ['apple', 'cherry']


# ========================================
# Program 8: Remove last item using pop().
# ========================================
# Write a program to remove the last item from the list using pop().
fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)
# Output: ['apple', 'banana']


# ========================================
# Program 9: Loop through list using for loop.
# ========================================
# Write a program to print each fruit in the list using a for loop.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


# ========================================
# Program 10: Loop through list using index.
# ========================================
# Write a program to print each fruit with its index.
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])
# Output:
# 0 apple
# 1 banana
# 2 cherry


# ========================================
# Program 11: Check if item exists in list.
# ========================================
# Write a program to check if 'banana' exists in the list.
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is in the list.")
# Output: Banana is in the list.


# ========================================
# Program 12: Sort list in ascending order.
# ========================================
# Write a program to sort the list of numbers in ascending order.
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)
# Output: [1, 2, 3, 4]


# ========================================
# Program 13: Sort list in descending order.
# ========================================
# Write a program to sort the list of numbers in descending order.
numbers = [3, 1, 4, 2]
numbers.sort(reverse=True)
print(numbers)
# Output: [4, 3, 2, 1]


# ========================================
# Program 14: Copy list using copy().
# ========================================
# Write a program to create a copy of a list using copy().
fruits = ["apple", "banana"]
new_list = fruits.copy()
print(new_list)
# Output: ['apple', 'banana']


# ========================================
# Program 15: Join two lists.
# ========================================
# Write a program to join two lists into one.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)
# Output: [1, 2, 3, 4, 5, 6]


# ========================================
# Program 16: Count occurrences of an item.
# ========================================
# Write a program to count how many times 'red' appears in the list.
colors = ["red", "blue", "red", "green"]
print("Red appears", colors.count("red"), "times.")
# Output: Red appears 2 times.


# ========================================
# Program 17: Find index of an item.
# ========================================
# Write a program to find the index of 'green' in the list.
colors = ["red", "blue", "green"]
index = colors.index("green")
print("Green is at index", index)
# Output: Green is at index 2


# ========================================
# Program 18: Clear all list items.
# ========================================
# Write a program to remove all items from the list.
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
# Output: []


# ========================================
# Program 19: Separate even and odd numbers.
# ========================================
# Write a program to create a list of numbers and separate even
# and odd numbers into two lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)
# Output:
# Even numbers: [2, 4, 6, 8]
# Odd numbers: [1, 3, 5, 7, 9]


# ========================================
# MORE EXAMPLES
# ========================================


# ========================================
# Example 1: Separate Even and Odd Numbers
# ========================================
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(f"Original list: {numbers}")
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
# Output:
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers: [2, 4, 6, 8, 10]
# Odd numbers: [1, 3, 5, 7, 9]


# ========================================
# Example 2: Separate Positive and Negative Numbers
# ========================================
numbers = [5, -3, 8, -1, 0, 12, -7, 4, -2, 9]

positive = []
negative = []
zero = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

print(f"Original: {numbers}")
print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Zeros: {zero}")
# Output:
# Original: [5, -3, 8, -1, 0, 12, -7, 4, -2, 9]
# Positive: [5, 8, 12, 4, 9]
# Negative: [-3, -1, -7, -2]
# Zeros: [0]


# ========================================
# Example 3: Separate Prime and Composite Numbers
# ========================================
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 19, 20]

prime = []
composite = []

for num in numbers:
    if is_prime(num):
        prime.append(num)
    else:
        composite.append(num)

print(f"Numbers: {numbers}")
print(f"Prime numbers: {prime}")
print(f"Composite numbers: {composite}")
# Output:
# Numbers: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 19, 20]
# Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19]
# Composite numbers: [4, 6, 8, 9, 10, 12, 20]


# ========================================
# Example 4: Separate Numbers Greater Than and Less Than Average
# ========================================
numbers = [15, 22, 8, 19, 31, 12, 25, 18, 30, 14]

# Calculate sum using loop
total = 0

for num in numbers:
    total = total + num

# Calculate average
average = total / len(numbers)

print(f"Numbers: {numbers}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")

# Separate
above_average = []
below_average = []
equal_to_average = []

for num in numbers:
    if num > average:
        above_average.append(num)
    elif num < average:
        below_average.append(num)
    else:
        equal_to_average.append(num)

print(f"\nAbove average: {above_average}")
print(f"Below average: {below_average}")
print(f"Equal to average: {equal_to_average}")
# Output:
# Numbers: [15, 22, 8, 19, 31, 12, 25, 18, 30, 14]
# Sum: 194
# Average: 19.40
#
# Above average: [22, 31, 25, 30]
# Below average: [15, 8, 19, 12, 18, 14]
# Equal to average: []


# ========================================
# Example 5: Separate String Lists by Length
# ========================================
words = ["cat", "elephant", "dog", "butterfly", "bird", "hippopotamus", "ant"]

short_words = []    # length <= 3
medium_words = []   # length 4-6
long_words = []     # length >= 7

for word in words:
    if len(word) <= 3:
        short_words.append(word)
    elif len(word) <= 6:
        medium_words.append(word)
    else:
        long_words.append(word)

print(f"All words: {words}")
print(f"\nShort words (<=3 letters): {short_words}")
print(f"Medium words (4-6 letters): {medium_words}")
print(f"Long words (>=7 letters): {long_words}")
# Output:
# All words: ['cat', 'elephant', 'dog', 'butterfly', 'bird', 'hippopotamus', 'ant']
#
# Short words (<=3 letters): ['cat', 'dog', 'ant']
# Medium words (4-6 letters): ['bird']
# Long words (>=7 letters): ['elephant', 'butterfly', 'hippopotamus']
