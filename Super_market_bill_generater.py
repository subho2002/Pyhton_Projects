# Write a program to enter the number of products, then enter product name, quantity, and price and
# create a list of tuples. At last Display the Bill and Total Bill.

n = int(input("Enter the number of products that you want : "))
product = []
total_Bill = 0

for i in range(n):
    name = input("Enter the name you the product you want :")
    quantity = float(input("Enter the quantity that you want : "))
    price = float(input("Enter the Price of that product : "))
    product.append((name,quantity,price))

print("\n\nWelcome to PrroSupermarket")

print("Item \t Qty \t Price \t Total")


# Displaying te bill 
for item in product:
    total = item[2]*item[1]
    print(f"{item[0][0:5]},\t{item[1]:3.2f},\t{item[2]:6.2f},\t{total:7.2f}")
    total_Bill = total_Bill + total

print(f"\n\nTotal Bill = {total_Bill}")
print("Thanks for visiting")