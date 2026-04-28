def normalize_ids(ids):
    result = []
    for i in ids:
        i = i.replace("_", "-").upper()
        result.append(i)
    return result

print(normalize_ids(["prod-001", "PROD_002", "prod-003"]))