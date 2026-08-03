# discount_calculator.py - Discount based on Age + Membership

age = int(input("Enter your age: "))
member_input = input("Are you a member? yes/no: ")
is_member = True if member_input == "yes" else False

if age < 18:
    print("Child: 20% discount")
    if is_member:
        print("Additional 5% for members")
        print("Total discount: 25%")
    else:
        print("Total discount: 20%")

elif age >= 60:
    print("Senior Citizen: 30% discount")
    if is_member:
        print("Additional 5% for members")
        print("Total discount: 35%")
    else:
        print("Total discount: 30%")

else:
    print("Adult: 10% discount")
    if is_member:
        print("Additional 5% for members")
        print("Total discount: 15%")
    else:
        print("Total discount: 10%")
