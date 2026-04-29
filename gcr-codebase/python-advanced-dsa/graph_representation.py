graph = {'Alex': ['Riya', 'John'], 'Riya': ['Alex']}

for node, neighbors in graph.items():
    print(f"{node} -> {', '.join(neighbors)}")