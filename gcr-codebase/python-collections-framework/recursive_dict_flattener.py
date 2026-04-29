def flatten(d, parent=""):
    result = {}
    for k, v in d.items():
        key = f"{parent}.{k}" if parent else k
        if isinstance(v, dict):
            result.update(flatten(v, key))
        else:
            result[key] = v
    return result

print(flatten({"a": {"b": {"c": 1}}}))