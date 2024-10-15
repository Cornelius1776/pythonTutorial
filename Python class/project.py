no_of_item = int(input("How many items do you want? "))
total_amount = 0
item_price: int = 0

print(item_price)
if no_of_item < 10:
    item_price = 1200
elif 10 <= no_of_item < 100:
    item_price = 1000
else:
    item_price = 700

total_amount = no_of_item * item_price
print(f"The total amount is {total_amount}")