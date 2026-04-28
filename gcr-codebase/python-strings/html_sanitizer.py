import re

def sanitize(html):
    return re.sub(r'</?(?!b|i|u)[^>]+>', '', html)

print(sanitize("<div><b>Bold</b><script>alert('X')</script></div>"))