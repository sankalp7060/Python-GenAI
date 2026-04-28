def extract_keywords(text, keywords):
    words = text.lower().replace(",", "").replace(".", "").split()
    found = []
    
    for k in keywords:
        if k.lower() in words:
            found.append(k)
    
    return found

text = "John has experience in Python, Django, and React."
print(extract_keywords(text, ["Python", "Django"]))