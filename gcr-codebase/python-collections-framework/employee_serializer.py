data = [("Alex", "IT"), ("Riya", "HR")]

result = [{"name": name, "department": dept} for name, dept in data]
print(result)