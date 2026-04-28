production = [120, 95, 110, 80]
target = 100

for i in range(len(production)):
    if production[i] < target:
        print(f"Day {i+1}: {production[i]} units (below target)")