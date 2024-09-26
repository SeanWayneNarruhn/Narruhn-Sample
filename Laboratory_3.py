def loan():
    try:
        monthly_salary = float(input("What is your monthly salary? "))
        loan_amount_requested = float(input("Enter the loan amount you are requesting: "))
    except:
        print("Please enter valid numerical values for salary and loan amount.")
    if monthly_salary>=30000:
        if loan_amount_requested<=10*monthly_salary:
            months_to_pay=float(input("How many months do you want to pay the loan over? "))
            interest_increase=loan_amount_requested*0.10 
            total_amount_due=loan_amount_requested+interest_increase
            monthly_payment=total_amount_due/months_to_pay
            print(f"\nCongrats! You are eligible for the loan.")
            print(f"Total amount due after interest: {total_amount_due:.1f}")
            print(f"Monthly payment over {months_to_pay}months: {monthly_payment:.1f}")
        else:
            print("\nYou are not approved for the loan because the requested amount exceeds 10 times your salary.")
    else:
        print("\nYou are not approved for the loan because your monthly salary is less than 30,000.00.")
loan()