product_name = input("Enter product name: ")
price = float(input("Enter price: "))
discount = float(input("Enter discount rate (%): "))

final_price = price - (price * discount / 100)

print(f"Final price of {product_name} is: {final_price}")