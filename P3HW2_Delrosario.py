# CTI-110-004
# P3HW2 - Salary
# Brian M. Delrosario
# Sat 9/23/2023

"""
Create a program that:

1. Asks the user to enter name of employee

2. Ask user to enter number of hours the employee worked this week

3. Ask user to enter employee's pay rate

4. Evaluate if employee has worked overtime (more than 40 hours). If yes, calculate the amount owed to employee for overtime hours

5. Calculate amount employee should be paid for regular hours worked.

6. Display gross pay (total amount that should be paid to employee)

7. The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).

8. Once finished, submit the finished code file through the assignment link in this folder.

"""

# 1. Ask for employee's name

employee = input("Enter employee's name: ")

# 2. Ask for hours worked this week

hours_worked_week = float(input("Enter number of hours worked this week: "))

# 3. Ask user to enter employee's pay rate

pay_rate = float(input("Enter employee's pay rate: $"))

# 4. Overtime

if hours_worked_week > 40:
    overtime = (hours_worked_week - 40)
else:
    overtime = 0

if hours_worked_week > 40:
    overtime_pay = overtime * pay_rate
else:
    overtime_pay = 0

# 5. Amount of pay for regular hours worked

if hours_worked_week < 0:
    reg_hour_pay = 0 * pay_rate
elif hours_worked_week <= 40:
    reg_hour_pay = hours_worked_week * pay_rate
else:
    reg_hour_pay = 40 * pay_rate

# 6. Gross pay

gross_pay = reg_hour_pay + overtime_pay

# 7. Disply output

print('---- ---- ---- ---- ---- ---- ')

print('Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay')

print('---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ')

print(f'{hours_worked_week:.1f}\t\t${pay_rate:.2f}\t\t{overtime:.1f}\t\t${overtime_pay:.2f}\t\t${reg_hour_pay:.2f}\t\t${gross_pay:.2f}')

