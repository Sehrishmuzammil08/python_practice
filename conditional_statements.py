#problem 1: Voting and ID Verification
age = int(input("Enter age: "))
if age >= 18:
 print("Eligible by age")
 has_id = input("Do you have ID? (yes/no): ")
 if has_id == "yes":
 print("You can vote")
 else:
 print("ID required to vote")
else:
 print("Not eligible to vote")


# problem 2: Student Result and Grade System
marks = int(input("Enter marks: "))
if marks >= 40:
 print("You passed")
 if marks >= 80:
 print("Grade A")
 elif marks >= 60:
 print("Grade B")
 else:
 print("Grade C")
else:
 print("You failed")



#problem 3: Login System
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
 if password == "1234":
 print("Login successful")
 else:
 print("Wrong password")
else:
 print("Invalid username")
