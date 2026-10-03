rent = int(input("plz enter the rent of the hostel/apartment: "))
num_people = int(input("plz enter the number of people living: "))  
food_bill = int(input("plz enter the food bill of the month: "))        
electricity_units = int(input("plz enter the number of units consumed: "))
cost_per_unit = int(input("plz enter the cost per unit of electricity: "))

total_electricity_bill = electricity_units * cost_per_unit
total_monthly_cost = rent + food_bill + total_electricity_bill
amount_per_person = total_monthly_cost / num_people

print(f"Each person will pay: {amount_per_person}")

input("press Enter to exit.........")
