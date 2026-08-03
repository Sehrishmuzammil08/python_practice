# Question 1: String Concatenation (Combine first_name and last_name with a space in between)
first_name = "Jane"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)        # Output: Jane Smith


# Question 2: String Length (Find and print the length of this string)
message = "Hello Python"
print(len(message))     # Output: 12


# Question 3: Accessing Characters (Print the first and last character of the string)
text = "Programming"
print(f"First: {text[0]}, Last: {text[-1]}")   # Output: First: P, Last: g


# Question 4: String Slicing (Extract "Python" from this string)
text = "I love Python programming"
print(text[7:13])       # Output: Python


# Question 5: Removing Whitespace (Remove the extra spaces from the beginning and end)
text = "   Hello World   "
print(text.strip())     # Output: Hello World


# Question 6: Find Substring (Check if "World" exists in the string)
text = "Hello World"
print("World" in text)  # Output: True


#Question 7: Check String End ( Check if filename ends with .py) 
filename = "script.py" 
print(filename.endswith(".py"))       #Output: True 



#Question 8: Count Characters (Count how many times 'l' appears in the string )
text = "Hello World" 
print(text.count("l"))       #Output: 3 



#Question 9: String Formatting with f-strings (Create a sentence using variables)
name = "Alice" 
age = 25 
city = "New York" 
print(f"{name} is {age} years old and lives in {city}")    #Output: Alice is 25 years old and lives in New York 



#Question 10: Extract Domain from Email (Get everything after/before @ symbol)
email = "user@example.com" 
print(email.split("@")[1])    #Output: example.com 



#Question 11: Check Palindrome ( Check if string reads the same backwards )
word = "radar" 
print(word == word[::-1])      #Output: True 



#Question 12: Remove Vowels (Remove all vowels (a, e, i, o, u) from the string )
text = "Hello World"
vowels = "aeiouAEIOU"
result = ""
for word in text:
    if word not in vowels:
        result = result + word
print(result)
        
        
        
#Question 13: Count Words (Count the number of words in the sentence )
sentence = "Python is a powerful language" 
print(len(sentence.split()))     #Output: 5 



#Question 14: Check Empty String (Check if string is empty )
text1 = "" 
text2 = "Hello" 
print(len(text1) == 0) 
print(len(text2) == 0) 
print(not text1) 
print(not text2)      #Output: True ,False , True , False
