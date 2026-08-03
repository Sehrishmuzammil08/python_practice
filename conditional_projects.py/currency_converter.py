print("=" * 50)
print("        CURRENCY CONVERTER")
print("=" * 50)

inr = float(input("Enter amount in INR(indian rupee): "))

print("-" * 50)
print("Select target currency:")
print("1. USD (US Dollar)")
print("2. EUR (Euro)")
print("3. GBP (British Pound)")
print("4. JPY (Japanese Yen)")
print("-" * 50)

choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    converted = inr / 83.50
    print(f"INR{inr:.2f} = {converted:.2f} USD")
    print("Exchange Rate: 1 USD = 83.50 INR")

elif choice == 2:
    converted = inr / 90.20
    print(f"INR{inr:.2f} = {converted:.2f} EUR")
    print("Exchange Rate: 1 EUR = 90.20 INR")

elif choice == 3:
    converted = inr / 105.30
    print(f"INR{inr:.2f} = {converted:.2f} GBP")
    print("Exchange Rate: 1 GBP = 105.30 INR")

elif choice == 4:
    converted = inr / 0.56
    print(f"INR{inr:.2f} = {converted:.2f} JPY")
    print("Exchange Rate: 1 JPY = 0.56INR")

else:
    print("Invalid choice!")
