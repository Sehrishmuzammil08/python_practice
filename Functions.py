#Question: Write a function called say_hello that prints "Hello, World!" when called. 

def say_hello(): 
    print("Hello, World!") 
say_hello()



#Write a function called greet that takes a name as a parameter and prints "Hello, [name]!". 

def greet(name): 
    print(f"Hello, {name}!") 
greet("Ali")



#Question: Write a function called double that takes a number and returns its double (multiply by 2). 

def double(num): 
    return num * 2 
result = double(5) 
print(f"Double of 5 is {result}")



#Question: Write a function called add that takes two numbers and returns their sum. :

def add(a, b): 
    return a + b 
result = add(3, 5)
print(f"addition  = {result }") 



#Question: Write a function called rectangle_area that takes length and width and returns the area. Also print "Calculating area..." inside the function. 

def rectangle_area(length, width): 
    print("Calculating area...") 
    area = length * width 
    return area 
result = rectangle_area(5, 3) 
print(f"Area of rectangle: {result}")



#Question: Write a function called is_even that takes a number and returns True if it's even, False if it's odd. 

def is_even(num): 
    if num % 2 == 0: 
        return True 
    else: 
        return False 
print(f"Is 4 even? {is_even(4)}") 
print(f"Is 7 even? {is_even(7)}") 
    


#Question: Write a function that asks the user for two numbers, adds them, and returns the result. Then use it in a program. 

def get_and_add(): 
    num_1 = float(input("Enter first number: ")) 
    num_2 = float(input("Enter second number: ")) 
    return num_1 + num_2 
print("Let's add two numbers!") 
result = get_and_add()
print(f"The sum is: {result}")
    
