from collections import defaultdict

data = [("IT", "Alex"), ("HR", "Riya"), ("IT", "John")]
dept_map = defaultdict(list)

for dept, emp in data:
    dept_map[dept].append(emp)

print(dict(dept_map))