# Take raise every 6 months into consideration

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the portion you are saving as a decimal: '))
total_cost = float(input('Enter the cost of the house: '))
semi_annual_raise = float(input('Enter semi-annual raise as a decimal: '))

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
    if months % 6 == 0:
        annual_salary += annual_salary*semi_annual_raise
        monthly_salary = annual_salary/12

print('Number of months:', months)