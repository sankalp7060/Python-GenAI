principal = float(input("Enter principal: "))
rate = float(input("Enter rate (%): "))
years = int(input("Enter number of years: "))

year = 1

while year <= years:
    principal *= (1 + rate / 100)
    print(f"Year {year}: {round(principal, 2)}")
    year += 1