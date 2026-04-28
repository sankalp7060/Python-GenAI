def generate_email(template, data):
    return template.format(**data)

template = "Hello {name}, your order {order_id} is confirmed."
data = {"name": "Alice", "order_id": "12345"}

print(generate_email(template, data))