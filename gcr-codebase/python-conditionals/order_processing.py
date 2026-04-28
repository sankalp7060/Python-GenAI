orders = ["Pending", "Processing", "Delivered", "Failed", "Pending"]

for order in orders:
    if order == "Failed":
        print("Processing stopped due to Failed status.")
        break
    print(f"Processing order: {order}")