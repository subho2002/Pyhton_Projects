menu = {
    "Dosa" : 120,
    "Tea" : 20,
    "Coffee" : 40,
    "Idli" : 50,
    "Frence Fries" : 80
}
bill = 0
bill_details = {}

print("Welcome to PoorResturent \n")
for key in menu:
    print(key.ljust(20),"-",menu[key])


while True :
    order = input("Enter the oder you want or write done to exit : ")
    if order == "done" or order == "DONE":
        break
    elif order in menu:
        quantity = int(input("Enter the quantity you want for that dish : "))
        bill_details[order] = quantity
    else:
        print("please enter the correct dish")

for item in bill_details:
    item_cost = bill_details[item]*menu[item]
    bill = bill + item_cost
    print(f"{item.ljust(10)}{bill_details[item]}\t{item_cost}")
print(f"Bill :- {bill}")
print(f"Bil with the GST is : {bill+(18/100)*bill}")