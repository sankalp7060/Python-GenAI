back_stack = []
forward_stack = []

# visiting pages
current = "A"
back_stack.append(current)

current = "B"
back_stack.append(current)

current = "C"
back_stack.append(current)

# back
forward_stack.append(back_stack.pop())
current = back_stack[-1]

# forward
back_stack.append(forward_stack.pop())
current = back_stack[-1]

print("Current Page:", current)