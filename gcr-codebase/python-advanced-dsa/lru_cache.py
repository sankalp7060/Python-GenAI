from collections import OrderedDict

cache = OrderedDict()
capacity = 3

operations = ["A", "B", "C", "A", "D"]

for op in operations:
    if op in cache:
        cache.move_to_end(op)
    else:
        if len(cache) >= capacity:
            cache.popitem(last=False)
        cache[op] = True

print("Cache:", list(cache.keys()))