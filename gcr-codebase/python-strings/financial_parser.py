import re

def parse_finance(text):
    matches = re.findall(r'([₹$€])(\d+)', text)
    return [(symbol, int(amount)) for symbol, amount in matches]

print(parse_finance("Q1 Revenue: $1200, Q2 Revenue: €1500, Q3: ₹95000"))