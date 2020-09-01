# Calculate how much is needed for a down payment

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the portion you are saving as a decimal: '))
total_cost = float(input('Enter the cost of the house: '))

monthly_salary = annual_salary/12
portion_down_payment = 0.25*total_cost
current_savings = 0
annual_return = 0.04
months = 0

while current_savings < portion_down_payment:
    monthly_return = current_savings*annual_return/12
    current_savings += monthly_return
    current_savings += portion_saved*monthly_salary
    months += 1

print('Number of months:', months)