def clean_csv(text):
    text = text.replace("!!", "").replace(",,", ",")
    parts = [p.strip() for p in text.split(",") if p.strip()]
    return ", ".join(parts)

print(clean_csv("John,, Doe!!, New York "))