print("=" * 50)
print("      PROFIT & LOSS CALCULATOR")
print("=" * 50)

cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    profit = sp - cp
    profit_percent = (profit / cp) * 100
    print(f"PROFIT: {profit:.2f}")
    print(f"Profit Percentage: {profit_percent:.2f}%")

elif cp > sp:
    loss = cp - sp
    loss_percent = (loss / cp) * 100
    print(f"LOSS: {loss:.2f}")
    print(f"Loss Percentage: {loss_percent:.2f}%")

else:
    print("No profit, no loss")
