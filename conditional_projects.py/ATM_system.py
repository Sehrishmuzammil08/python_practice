# Program 4: ATM Withdrawal System

balance = int(input("Enter your balance: "))
withdrawal_amount = int(input("Enter withdrawal amount: "))
daily_limit = int(input("Enter daily limit: "))
daily_withdrawn = int(input("Enter already withdrawn today: "))

if withdrawal_amount <= balance:
    if withdrawal_amount <= (daily_limit - daily_withdrawn):
        if withdrawal_amount % 100 == 0:
            print("Transaction Successful!")
            print(f"Withdrawn: ${withdrawal_amount}")
            print(f"Remaining Balance: ${balance - withdrawal_amount}")
        else:
            print("Please enter amount in multiples of 100")
    else:
        print("Daily limit exceeded!")
else:
    print("Insufficient balance!")
