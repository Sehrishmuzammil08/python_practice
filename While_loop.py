#Problem 1: Print numbers from 1 to 1
num = 1
while num <= 10:
 print(num, end=" ") 
 num += 1
print() 



#Problem 2: Sum of first N natural numbers
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
 sum += i
 i += 1
print(f"Sum of first {n} natural numbers is: {sum}")


# Problem 3: Multiplication table
num = int(input("Enter a number: "))
i = 1
print(f"Multiplication Table of {num}:")
while i <= 10:
 print(f"{num} x {i} = {num * i}")
 i += 1



# Problem 4: Factorial of a number
num = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= num:
 factorial *= i
 i += 1
print(f"Factorial of {num} is: {factorial}")



# Problem 5: Count digits in a number
num = int(input("Enter a number: "))
original_num = num
count = 0
if num == 0:
 count = 1
else:
	while num > 0:
		num = num // 10
		count += 1
print(f"Number of digits in {original_num} is: {count}")
