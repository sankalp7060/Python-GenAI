data = "23,45,67,12"
numbers = list(map(int, data.split(",")))

mean = sum(numbers) / len(numbers)
maximum = max(numbers)

print("Mean:", mean)
print("Maximum:", maximum)