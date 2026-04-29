def calculate_net_salary(gross, tax_rate):
    return gross - (gross * tax_rate / 100)

print(calculate_net_salary(50000, 10))