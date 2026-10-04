employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
transport_allowance = float(input("Enter transport allowance: "))
food_allowance = float(input("Enter food allowance: "))

gross_salary = basic_salary + transport_allowance + food_allowance

print("========================================")
print("             EMPLOYEE PAYSLIP           ")
print("========================================")
print()
print(f"Employee: {employee_name}")
print()
print(f"Basic Salary:            {basic_salary} ETB")
print(f"Transport Allowance:     {transport_allowance} ETB")
print(f"Food Allowance:          {food_allowance} ETB")
print("----------------------------------------")
print(f"Gross Salary:            {gross_salary} ETB")
print("========================================")

"""
Display a professional payslip.
Example
========================================
             EMPLOYEE PAYSLIP
========================================

Employee: Ahmed Ali

Basic Salary:          12,000 ETB
Transport Allowance:    2,000 ETB
Food Allowance:         1,500 ETB
----------------------------------------
Gross Salary:          15,500 ETB
========================================


"""