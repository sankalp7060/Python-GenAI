from collections import deque

times = [0, 2, 4]  # minutes representation
dq = deque()

for t in times:
    dq.append(t)
    while dq and t - dq[0] > 5:
        dq.popleft()
    if len(dq) >= 3:
        print("Alert: Multiple login attempts detected")
        break