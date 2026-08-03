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
