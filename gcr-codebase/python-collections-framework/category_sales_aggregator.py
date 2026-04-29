def aggregate(data):
    result = {}
    for cat, amt in data:
        result[cat] = result.get(cat, 0) + amt
    return result

print(aggregate([("Electronics", 1000), ("Furniture", 2000), ("Electronics", 1500)]))