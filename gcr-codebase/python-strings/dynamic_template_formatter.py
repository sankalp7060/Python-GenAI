def format_template(template, data):
    return template.format(**data)

print(format_template("Hello {name}, welcome to {city}!", {"name": "Alex", "city": "Bengaluru"}))