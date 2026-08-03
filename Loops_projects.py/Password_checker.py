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
