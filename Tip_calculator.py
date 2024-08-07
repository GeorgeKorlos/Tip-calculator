print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = tip_percent / 100
perc_bill = bill * tip 
final_bill = bill + perc_bill
final_amount = final_bill / people

print(f"Each person should pay: ${final_amount}")
