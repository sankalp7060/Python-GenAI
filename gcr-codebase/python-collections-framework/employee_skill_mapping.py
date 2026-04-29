from collections import defaultdict

data = {"Alex": ["Python", "SQL"], "Neha": ["SQL"], "Sam": ["Python"]}
skill_map = defaultdict(list)

for emp, skills in data.items():
    for skill in skills:
        skill_map[skill].append(emp)

print(dict(skill_map))