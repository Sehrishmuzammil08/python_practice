# Find factors of a number
num = int(input("Enter a positive number: "))

i = 1
print(f"Factors of {num} are:")

while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1

print()
