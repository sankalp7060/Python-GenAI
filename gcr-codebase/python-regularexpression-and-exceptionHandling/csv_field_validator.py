import re

emails = ["alex@corp.com", "wrong.email@"]

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

for email in emails:
    try:
        if re.match(pattern, email):
            print("Valid:", email)
        else:
            print("Invalid:", email)
    except Exception:
        print("Error processing:", email)