revenue = {
    "Delhi": [1000, 2000, 3000],
    "Mumbai": [1500, 2500, 3500],
    "Bangalore": [2000, 3000, 4000]
}

max_branch = ""
max_revenue = 0

for branch, values in revenue.items():
    total = sum(values)
    if total > max_revenue:
        max_revenue = total
        max_branch = branch

print(f"Highest revenue branch: {max_branch} with revenue {max_revenue}")