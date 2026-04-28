def flatten(d, parent_key='', result=None):
    if result is None:
        result = []
    
    for k, v in d.items():
        new_key = f"{parent_key}.{k}" if parent_key else k
        if isinstance(v, dict):
            flatten(v, new_key, result)
        else:
            result.append(f"{new_key}={v}")
    
    return ", ".join(result)

data = {'user': {'name': 'Alex', 'contact': {'email': 'alex@corp.com'}}}
print(flatten(data))