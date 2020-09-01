# Use bisection search to find required savings for down payment in 36 months

input_salary = float(input('Enter your annual salary: '))
annual_salary = input_salary

total_cost = 1000000
semi_annual_raise = 0.07
monthly_salary = annual_salary/12
portion_down_payment = 0.25*total_cost
current_savings = 0
annual_return = 0.04
months = 0
low = 0
high = 10000
portion_saved = (low + high)/2.0
steps = 0

if annual_salary < portion_down_payment:
    print('It is not possible to pay the down payment in three years.')

else:
    while abs(portion_down_payment - current_savings) > 100:
        for month in range(1, 37):
            monthly_return = current_savings*annual_return/12
            current_savings += monthly_return
            current_savings += .0001*portion_saved*monthly_salary
            if month % 6 == 0:
                annual_salary += annual_salary*semi_annual_raise
                monthly_salary = annual_salary/12
        if portion_down_payment - current_savings > 100:
            low = portion_saved
            current_savings = 0
            annual_salary = input_salary
        elif current_savings - portion_down_payment > 100:
            high = portion_saved
            current_savings = 0
            annual_salary = input_salary
        portion_saved = (low + high)/2.0
        steps += 1
            
    print('Best savings rate:', .0001*portion_saved)
    print('Steps in bisection search: ', steps)