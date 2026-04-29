def merge_configs(*configs):
    result = {}
    for c in configs:
        result.update(c)
    return result

print(merge_configs({"timeout": 10}, {"timeout": 20, "debug": True}))