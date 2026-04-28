departments = {
    "IT": ["Alice", "Bob"],
    "HR": ["Charlie", "David"],
    "Finance": ["Eve", "Frank"]
}

dept = input("Enter department name: ")

if dept in departments:
    print("Employees:", departments[dept])
else:
    print("Department not found")