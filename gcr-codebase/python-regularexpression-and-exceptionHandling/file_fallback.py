try:
    with open("config.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Creating a new file...")
    with open("config.txt", "w") as f:
        f.write("")