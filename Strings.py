#Strings in Python are immutable sequences of Unicode characters. Once created, they 
cannot be modified.

# Basic string characteristics
text = "Hello, World!"
print(f"Type: {type(text)}")       # <class 'str'>
print(f"Length: {len(text)}")      # 13 

# Concatenation 
# Using + operator 
first_name = "John" 
last_name = "Smith" 
full_name = first_name + " " + last_name 
print(f"Concatenation: {full_name}")       # Concatenation: John Smith


#Repetition 
# Using * operator 
separator = "-" * 50 
print(separator)


# Slicing (Indexing) 
text = "Python Programming" 

# Basic indexing 
print(f"First character: {text[0]}")      # P 
print(f"Last character: {text[-1]}")      # g 
print(f"Second last: {text[-2]}")         # n

# Slicing syntax: [start:stop:step] 
print(f"Every 2nd char between 1-9: {text[1:9:2]}") 
print(f"First 6 chars: {text[:6]}")       # Python 
print(f"From index 7: {text[7:]}")        # Programming 
print(f"Chars 7-18: {text[7:18]}")        # Programming 
print(f"Every 2nd char: {text[::2]}")     # Pto rgamn 
print(f"Reverse string: {text[::-1]}")    # gnimmargorP nohtyP


# Case Conversion Methods 
text = "Python Is AWESOME!" 
 
print(f"Lower: {text.lower()}")           # "  python is awesome!  " 
print(f"Upper: {text.upper()}")           # "  PYTHON IS AWESOME!  " 
print(f"Title: {text.title()}")           # "  Python Is Awesome!  " 
print(f"Capitalize: {text.capitalize()}") # "Python is awesome!" 
print(f"Swap case: {text.swapcase()}")    # "  pYTHON iS awesome!  "


# Strip Methods ( Removing characters )
messy_string = "***Hello***World***" 

print(f"Strip '*': {messy_string.strip('*')}")      # Hello***World 
print(f"Lstrip '*': {messy_string.lstrip('*')}")    # Hello***World*** 
print(f"Rstrip '*': {messy_string.rstrip('*')}")    # ***Hello***World


#Replace Methods 
text = "The cat sat on the mat" 

# Simple replace 
print(f"Replace 'cat' with 'dog': {text.replace('cat', 'dog')}")      # The dog sat on the mat 

# Replace with count limit 
print(f"Replace first 2 spaces: {text.replace(' ', '_', 2)}")         # The_cat_sat on the mat 

# Chain replacements 
cleaned = text.replace('cat', 'dog').replace('mat', 'rug') 
print(f"Chained replace: {cleaned}") 
