import heapq

queue = []

heapq.heappush(queue, (3, "Regular"))
heapq.heappush(queue, (1, "VIP"))

priority, customer = heapq.heappop(queue)
print("Processing", customer)