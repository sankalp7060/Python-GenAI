d1 = {"A": 5, "B": 10}
d2 = {"A": 3, "C": 8}

result = {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)}

print(result)