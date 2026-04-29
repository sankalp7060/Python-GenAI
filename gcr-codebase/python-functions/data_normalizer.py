def normalize_names(name_list):
    return [name.strip().lower() for name in name_list]

print(normalize_names([" John ", "MARY", " Alex "]))