user_income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = user_income - expenses
interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)
print(f"your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest is: {projected_savings}.")