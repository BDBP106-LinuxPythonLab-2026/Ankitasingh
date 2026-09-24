principal=int(input("Enter your principal: "))
rate_per_annum=int(input("Enter your rate: "))
time_years=int(input("Enter your time period: "))

simple_interest=principal*rate_per_annum*time_years
total_amount=principal+simple_interest

print(f"Simple interest: {simple_interest:,.2f}")
print(f"Total amount:{total_amount:,.2f}")