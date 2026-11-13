# Problem 2: Simple Shopping Cart

# customer 
customer_name = input("Enter customer name: ")

subTotal = 0
discount = 0
final_total = 0
count = 0

# product 
for p in range(3):
    product_name = input("this is product name:")
    product_price = int(input("this is product price:"))

    subTotal = subTotal + product_price
    count = count + 1

    print("")
    print(f"Product {count}: {product_name}")
    print(f"Price: {product_price}")


if subTotal >= 5000:
    discount = (subTotal * 20) / 100
    final_total = round(subTotal - discount) 
    print("20% discount")
elif subTotal >=3000:
    discount = (subTotal * 10) / 100
    final_total = round(subTotal - discount) 
    print("10% discount")
elif subTotal >= 1000:
    discount = (subTotal * 5) / 100
    final_total = round(subTotal - discount) 
    print("5% discount")
else:
    final_total = subTotal
    print("No discount")
    

# calculation 
print("======================")
print(f"SubTotal: {subTotal}")
print(f"Discount: {round(discount)}")
print(f"Final_total: {final_total}")
