import re

text = "Na#me: A$le%x"

try:
    cleaned = re.sub('[^a-zA-Z0-9: ]', '', text)
    print("Cleaned Data:", cleaned)
except Exception:
    print("Error cleaning data")