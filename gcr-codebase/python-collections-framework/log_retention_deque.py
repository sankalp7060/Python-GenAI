from collections import deque

logs = [f"Log{i}" for i in range(1, 1002)]
dq = deque(logs, maxlen=1000)

print("Stored Logs:", list(dq))