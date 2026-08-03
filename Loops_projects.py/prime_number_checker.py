# Prime Number Checker

num = 97

if num <= 1:
    print(f"{num} is NOT prime")

elif num == 2:
    print(f"{num} is a PRIME!")

else:
    is_prime = True

    """
    We only need to check divisibility up to the square root of the number.
    So, we start the loop from 2 and continue up to
    int(num ** 0.5) + 1.
    """

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            print(f"{num} is divisible by {i}")
            break

    if is_prime == True:
        print(f"{num} is PRIME!")
    else:
        print(f"{num} is NOT prime")
