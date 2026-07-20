#                               project 2#

print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("how meny people split the bill? "))

tip_prec = tip / 100
tip_amount = bill * tip_prec
total_bill = tip_amount + bill
bill_per_person = total_bill / people
final = round(bill_per_person, 2)
print(f"each person should pay: {final}")



