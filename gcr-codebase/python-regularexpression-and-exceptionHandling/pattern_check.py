import re

text = "Python"

if re.match(r'^[A-Z]', text):
    print("Starts with a capital letter.")
else:
    print("Does not start with a capital letter.")