monthly_income = int(input("Enter your monthly income:")) #currency units in usd $
monthly_expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) #assume 5% interest rate
print(f"Your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest is: {projected_savings}.")