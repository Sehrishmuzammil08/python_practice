#Program 1:
#Check if a number is divisible by both 3 and 5
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is NOT divisible by both 3 and 5")




#Program 2:
#Create a password validation program
password = input("Enter password: ")

if len(password) >= 8 :
    print("Password is Valid ")
else:
    print("Invalid Password ")
    print("Rule: Min 8 charactres are musts")



#Program 3:
#Determine the largest among three numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is: {largest}")
