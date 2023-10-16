# CTI-110-0004
# P4HW2 - Salary Calculator
# Brian M. Delrosario
# Sun 10/15/2023

'''

# Plan is to use P3HW2, sentinel loop, and append list



# See Fig. 10.2.1 (sentinel while loop) in textbook, simplified

  # Use this to loop, exit w/ 'Done', employee info entries

user_value = input("Enter a short word: ")

while user_value != 'Done':
    print(user_value)
    user_input = input("Enter a word (enter 'Done' to quit): ")
    user_value = user_input
print('Goodbye.\n')



# P4HW1, simplified, for reference, for employee totals

  # Use the append list, see also Participation Acitivity 8.2.4

numbers = int(input('How many number values do you want to enter:' ))
list =[]
print('Enter a number between 0 and 100 (inclusive).')

for i in range(1, numbers + 1, 1):

  valid = False
  while not valid:
    value = float(input(f'Enter #{i}: '))
    if 0 <= value <= 100:
      valid = True
    else:
      print('Invalid number. Try again.')
  list.append(value)

print(list)


'''
# 1. Create the empty lists
total_employees = []
total_overtime_pay = []
total_reg_hour_pay = []
total_gross_pay = []

# 2. While loop; first list append
employee = input("Enter employee's name or 'Done' to terminate: ")
total_employees.append(employee)

while employee != 'Done':

  # 3. Ask for hours worked this week  
  hours_worked_week = float(input("Enter number of hours worked this week: "))
  
  # 4. Ask user to enter employee's pay rate  
  pay_rate = float(input("Enter employee's pay rate: $"))
  
  # 5. Overtime, calculation; second list append
  overtime = hours_worked_week - 40 if hours_worked_week > 40 else 0  
  overtime_pay = overtime * pay_rate if hours_worked_week > 40 else 0  
  total_overtime_pay.append(overtime_pay)
  
  # 6. Regular hours worked, calculation; third list append
  if hours_worked_week < 0:
    reg_hour_pay = 0 * pay_rate
  elif hours_worked_week <= 40:
    reg_hour_pay = hours_worked_week * pay_rate
  else:
    reg_hour_pay = 40 * pay_rate
  total_reg_hour_pay.append(reg_hour_pay)
  
  # 7. Gross pay; fourth list append
  gross_pay = reg_hour_pay + overtime_pay
  total_gross_pay.append(gross_pay)
  
  # 8. Display output
  print('\n---- ---- ---- ---- ---- ---- ')
  print('Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay')
  print('---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --')
  print(f'{hours_worked_week:.1f}\t\t\t${pay_rate:.2f}\t\t{overtime:.1f}\t\t${overtime_pay:.2f}\t\t\t${reg_hour_pay:.2f}\t${gross_pay:.2f}''\n')

  # 9. Ask for employee's name or 'Done' to terminate (repeats the loop or quits)  
  employee = input("\nEnter employee's name or 'Done' to terminate: ")
  total_employees.append(employee) # This appends 'Done' as an employee


print('\nTotal employees: ', len(total_employees) - 1) # Subtract 1 for 'Done'
print(f'Total amount paid for overtime:  ${sum(total_overtime_pay):.2f}')
print(f'Total amount paid for regular hours:  ${sum(total_reg_hour_pay):.2f}')
print(f'Total amount paid in gross:  ${sum(total_gross_pay):.2f}')
