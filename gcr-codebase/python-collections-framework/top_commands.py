from collections import Counter

commands = ["init", "push", "push", "commit", "push", "init"]
result = Counter(commands).most_common(3)

print(result)