#Program 1: Basic Number Match
#Display text based on a number.
num = int(input("Enter a number (1-3): "))
match num:
 case 1:
 print("You entered ONE")
 case 2:
 print("You entered TWO")
 case 3:
 print("You entered THREE")
 case _:
 print("Invalid number")



#Program 2: Calculator using match-case
#Perform operations using match-case.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")
match op:
 case "+":
 print("Result =", num1 + num2)
 case "-":
 print("Result =", num1 - num2)
 case "*":
 print("Result =", num1 * num2)
 case "/":
 print("Result =", num1 / num2)
 case _:
 print("Invalid operator")


  
#Program 3: Grade using Guards
#Use conditional guards inside match-case.
marks = int(input("Enter marks: "))
match marks:
 case m if m >= 80:
 print("Grade A")
 case m if m >= 60:
 print("Grade B")
 case m if m >= 40:
 print("Pass")
 case _:
 print("Fail")
     
