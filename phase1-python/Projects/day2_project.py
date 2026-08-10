#Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the totsl bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
bill_split = float(input("How many people to split the bill? "))

#CALCULATIONS
tip_amount = (bill * tip)/100
total_bill = tip_amount + bill
total_bill_split = round( total_bill / bill_split, 2)


print("Each person shouls pay: " + str(total_bill_split))