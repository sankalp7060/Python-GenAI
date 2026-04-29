from multiprocessing import Process, Queue

def worker(q):
    while not q.empty():
        order = q.get()
        print(f"Processed {order}")

q = Queue()
orders = ["Order1", "Order2", "Order3"]

for o in orders:
    q.put(o)

processes = []
for _ in range(2):
    p = Process(target=worker, args=(q,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()