customer = str(input("Enter the customer name: "))
contact = str(input("Enter the contact Number: "))
address = str(input("Enter the address: "))

product1 = str(input("Enter the product_1_name: "))
price1 = float(input("Enter the price 1: "))
quantity1 = int(input("Enter quantity 1: "))
amount1 = price1 * quantity1

product2 = str(input("Enter the product_2_name: "))
price2 = float(input("Enter the price 2: "))
quantity2 = int(input("Enter quantity 2: "))
amount2 = price2 * quantity2

product3 = str(input("Enter the product_3_name: "))
price3 = float(input("Enter the price 3: "))
quantity3 = int(input("Enter quantity 3: "))
amount3 = price3 * quantity3

discount = float(input("Enter Discount (%): "))
subtotal = amount1 + amount2 + amount3
discount_amount = subtotal * (discount / 100)
total = subtotal - discount_amount

print("\n==========================================")
print("              STORE RECEIPT")
print("==========================================")

print("Customer :", customer)
print("Contact No.   :", contact)
print("address       :", address)


print("==========================================")

print("product   :", product1)
print("Price     :", price1)
print("Quantity  :", quantity1)

print("Amount    :", amount1)

print("==========================================")


print("product2  :", product2)
print("Price     :", price2)
print("Quantity   :", quantity2)

print("Amount     :", amount2)

print("==========================================")

print("product3   :", product3)
print("Price      :", price3)
print("Quantity  :", quantity3)

print("Amount    :", amount3)

print("==========================================") 


print("Subtotal    :", subtotal)
print("Discount    :", discount_amount)
print("Total       :", total)
