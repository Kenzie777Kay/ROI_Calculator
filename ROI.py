def rental(monthly_incomes, monthly_expenses, investments, goal_roi):
    total_monthly_income = sum(monthly_incomes)
    print(f"\ntotal monthly income is ${total_monthly_income}")
    
    total_monthly_expenses = sum(monthly_expenses)
    print(f"\nexpected monthly expenses ${total_monthly_expenses}")
    
    cash_flow = total_monthly_income - total_monthly_expenses
    print(f"\nexpected monthly cash flow ${cash_flow}")
    
    total_investment = sum(investments)
    print(f"\ntotal investment is {total_investment}")
    
    annual_cash_flow = cash_flow * 12
    roi = annual_cash_flow / total_investment
    
    print(f'\estimated ROI {roi * 100}%')
    
    if roi >= goal_roi:
        print("\nThis property is a great deal.")
        return True
    print('\nThis property is a bust.')
    return False


    # Test Property one
incomes1 = [1600, 200]
expenses1 = [100, 50, 50, 50, 100, 760]
investments1 = [30000, 2000, 6000]
goal1 = 0.05

rental(incomes1, expenses1, investments1, goal1)



# Test Property two
incomes2 = [1500]
expenses2 = [300, 400, 1000]
investments2 = [80000, 6000]
goal2 = 0.5

rental(incomes2, expenses2, investments2, goal2)