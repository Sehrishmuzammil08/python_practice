# Python Practice Formulas

## Average:

- Average = Sum of values / Number of values

## Percentage

- Percentage = (Obtained Value / Total Value) × 100


## Simple Interest

- SI = (P × R × T) / 100

- Total Amount = P + SI

Where:
- P = Principal
- R = Rate
- T = Time


## Minutes to Hours

- Hours = Minutes // 60

- Remaining Minutes = Minutes % 60


## Circle

- Area = π × radius × radius

- Circumference = 2 × π × radius

- where r is radius

## Temperature unit Conversion  

**Celsius → Fahrenheit**

- F = (C × 9/5) + 32

**Fahrenheit → Celsius**

- C = (F - 32) × 5/9


## Power

- a² = a × a
- a³ = a × a × a
  
Python:
- a ** 2
- a ** 3
  
---

## Even and Odd

- Even Number → Number % 2 == 0
- Odd Number → Number % 2 != 0
  

## Range Checking

- Number is between two values → lower <= number <= upper

Example:
- 1 <= num <= 10

## Profit and Loss

- Profit = Selling Price - Cost Price
- Profit Percentage = (Profit / Cost Price) × 100

- Loss = Cost Price - Selling Price
- Loss Percentage = (Loss / Cost Price) × 100

## Salary
- as used in my program not fixed values
- Dearness Allowance (DA) = Basic Salary × 40 / 100
- House Rent Allowance (HRA) = Basic Salary × 20 / 100
- Provident Fund (PF) = Basic Salary × 12 / 100

- Gross Salary = Basic Salary + Dearness Allowance (DA) +  House Rent Allowance (HRA) 
- Total Deduction = Provident Fund (PF) + Tax
- Net Salary = Gross Salary - Total Deduction

## Tax

- Tax = Salary × Tax Rate / 100

Example:
- If salary > 25000:
  Tax = Basic Salary × 10 / 100
- Otherwise:
  Tax = 0

## Time Conversion

- Hours = Total Seconds // 3600
- Remaining Seconds = Total Seconds % 3600
- Minutes = Remaining Seconds // 60
- Seconds = Total Seconds % 60

## Currency Conversion

- Converted Amount = Amount in Base Currency / Exchange Rate

Example:
- USD = INR / 83.50
- EUR = INR / 90.20
- GBP = INR / 105.30
- JPY = INR / 0.56

## Triangle

### Triangle Validity
- side1 + side2 > side3
- side2 + side3 > side1
- side1 + side3 > side2

All three conditions must be true for a valid triangle.

### Triangle Types
- Equilateral → side1 == side2 == side3
- Isosceles → Any two sides are equal
- Scalene → All sides are different

## Leap Year

A year is a leap year if:

- year % 4 == 0
- AND year % 100 != 0
- OR year % 400 == 0

Python:
- (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

## Largest of Three Numbers

Compare three numbers:

- Largest = max(num1, num2, num3)

Python:
- max(num1, num2, num3)


## Discount

- Discount Amount = Original Price × Discount Rate / 100
- Final Price = Original Price - Discount Amount

## Remaining Balance

- Remaining Balance = Original Balance - Withdrawn Amount

## ATM Daily Limit

- Remaining Daily Limit = Daily Limit - Amount Already Withdrawn
