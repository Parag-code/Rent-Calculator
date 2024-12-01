rent =int(input("Enter your hostel/flat rent: "))
food=int(input("Enter the amount of food ordered: "))
electricity_spend=int(input("Enter the total electrcity spend: "))
charge_per_unit=int(input("Enter the charge per unit: "))
persons=int(input("Enter the number of persons living in flat/hostel: "))


total_bill=(electricity_spend*charge_per_unit)

total_expenditure= (rent+food+total_bill)/persons

print("Each person will pay:",total_expenditure)
