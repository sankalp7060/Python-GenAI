import queue
import threading
import time

q = queue.Queue()

for req in ["Req1", "Req2", "Req3"]:
    q.put(req)

def process():
    while not q.empty():
        req = q.get()
        print("Processed:", req)
        time.sleep(1)
        q.task_done()

t = threading.Thread(target=process)
t.start()
t.join()