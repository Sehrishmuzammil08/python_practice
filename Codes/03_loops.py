# Print even numbers from 1 to 20
 num = 1
 print("Even numbers from 1 to 20:")
 while num <= 20:
  if num % 2 == 0: 
     print(num, end=" ") 
     num += 1
 print() 


 # Calculate average of positive numbers
 sum_numbers = 0
 count = 0
 print("Enter numbers (enter negative number to stop):")
 while True:
     num = int(input("Enter number: "))
     if num < 0:
         break 
     sum_numbers += num  
     count += 1
 if count > 0:
     average = sum_numbers / count
     print(f"\nSum of numbers: {sum_numbers}")
     print(f"Count of numbers: {count}")
     print(f"Average: {average:.2f}")
 else:
     print("No positive numbers were entered!")



# Find factors of a number
num = int(input("Enter a positive number: "))
i = 1
print(f"Factors of {num} are:")

while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1
print()



# Simple password checker with 3 attempts
correct_password = "python123"
attempts = 1
max_attempts = 3
print("Welcome! Please enter your password.")

while attempts <= max_attempts:
    password = input(f"Attempt {attempts}/{max_attempts}: ")

    if password == correct_password:
        print("Access Granted! Welcome to the system.")
        break
    else:
        print("Incorrect password!")
        attempts += 1

        if attempts > max_attempts:
            print("Sorry, you've used all attempts. Account locked!")
