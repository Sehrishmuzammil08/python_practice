# Lecture Notes: The 'for' Loop in Python 

## 1. Introduction to the for Loop 

**A loop is used to repeat a block of code multiple times. 
The for loop is mainly used when: 
- The number of repetitions is known. 
- We want to repeat something a fixed number of times. 
- We want to go through characters of a string. 
- We want to generate numbers using range().**
  
Unlike while loops, the for loop is usually cleaner and easier when the number of iterations 
is predictable. 

## 2. Basic Syntax of for Loop 
for variable in sequence: 
statement(s) 
Part 
for 
variable 
in 
sequence 
: 
Indentation 

## 3. Using range() with for Loop 
Meaning 
Python keyword that starts the loop 
Stores value during each iteration 
Connects variable with sequence 
Something that produces values (like range 
or string) 
Colon is mandatory 
Required in Python to define loop body 
The most common way to use a for loop is with the range() function. 
range() generates numbers automatically. 
Example 1: Basic range(stop) 
# Print numbers from 0 to 4 
for i in range(5): 
    print(i) 
Output: 
0 
1 
2 
3 
4 
Explanation: 
• range(5) generates numbers starting from 0. 
• It stops before 5. 
• So it generates: 0, 1, 2, 3, 4. 
• Loop runs 5 times. 
 
Important: The stop value is excluded. 
4. range(start, stop) 
# Print numbers from 1 to 5 
 
for num in range(1, 6): 
    print(num) 
Output: 
1 
2 
3 
4 
5 
Explanation: 
• Start = 1 
• Stop = 6 (excluded) 
• So it prints 1 to 5. 
5. range(start, stop, step) 
# Print even numbers from 0 to 10 
 
for even in range(0, 11, 2): 
    print(even) 
Output: 
0 
2 
4 
6 
8 
10 
Explanation: 
• Start at 0 
• Stop before 11 
• Increase by 2 each time 
 
So sequence becomes: 0 → 2 → 4 → 6 → 8 → 10 
6. Looping Through a String 
# Print each character of a string 
 
for letter in "Python": 
    print(letter) 
Output: 
P 
y 
t 
h 
o 
n 
Explanation: 
• Loop takes each character one by one. 
• First iteration → P 
• Second iteration → y 
• And so on. 
 
No index is required. 
7. The break Statement 
for i in range(10): 
    if i == 4: 
        break 
    print(i) 
Output: 
0 
1 
2 
3 
Explanation: 
• Loop starts normally. 
• When i == 4, break executes. 
• Loop ends immediately. 
• 4 is not printed. 
8. The continue Statement 
for i in range(5): 
    if i == 2: 
        continue 
    print(i) 
Output: 
0 
1 
3 
4 
Explanation: 
• When i == 2, continue runs. 
• That iteration is skipped. 
• Loop continues with next value. 
9. for Loop Flow (Step-by-Step) 
for i in range(3): 
    print(i) 
Execution Steps: 
1. range(3) creates: 0, 1, 2 
2. i = 0 → print(0) 
3. i = 1 → print(1) 
4. i = 2 → print(2) 
5. Loop ends (no more values) 
10. Important Rules 
• Colon ':' is required 
• Indentation is mandatory 
• Stop value in range() is excluded 
• break stops loop 
• continue skips one iteration 
11. Common Student Mistakes 
• Forgetting colon 
• Wrong indentation 
• Thinking range(5) includes 5 
• Using '=' instead of '==' 
• Confusing break and continue 
12. When Should You Use for Loop? 
Use for loop when: 
• Number of repetitions is known 
• Using range() 
• Iterating through a string 
• Cleaner and shorter code is needed 
Final Summary 
Concept 
for loop 
range() 
range(5) 
break 
continue 
Stop value 
Meaning 
Repeats code fixed number of times 
Generates numbers 
0 to 4 
Stops loop completely 
Skips current iteration 
Always excluded 
