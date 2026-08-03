print("=" * 50)
print("      EMPLOYEE SALARY SLIP")
print("=" * 50)

E_name = input("Employee Name: ")
E_id = input("Employee ID: ")
month = input("Month: ")
B_salary = float(input("Basic Salary: "))

DA = B_salary * 40 / 100
HRA = B_salary * 20 / 100
PF = B_salary * 12 / 100

if B_salary > 25000:
    tax = B_salary * 10 / 100
else:
    tax = 0
G_salary = B_salary + DA + HRA
total_deduction = PF + tax
N_salary = G_salary - total_deduction

print("=" * 50)
print("Employee Name:", E_name)
print("Employee ID:", E_id)
print("Month:", month)
print("=" * 50)

print("EARNINGS")
print("Basic Salary:", B_salary)
print("Dearness Allowance 40%:", DA)
print("House Rent Allowance 20%:", HRA)
print("Gross Salary:", G_salary)

print("=" * 50)
print("DEDUCTIONS")
print("Provident Fund 12%:", PF)
print("Income Tax 10%:", tax)
print("Total Deductions:", total_deduction)
print("=" * 50)
print("NET SALARY:", N_salary)
print("=" * 50)
