from collections import defaultdict

data = [("IT", 5000), ("HR", 3000), ("IT", 4000)]
dept_salary = defaultdict(int)

for dept, salary in data:
    dept_salary[dept] += salary

print(dict(dept_salary))