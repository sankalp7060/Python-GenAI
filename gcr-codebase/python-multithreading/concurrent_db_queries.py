import threading
import time

def query(db):
    print(f"Querying {db}...")
    time.sleep(1)

threads = []
dbs = ["DB1", "DB2", "DB3"]

for db in dbs:
    t = threading.Thread(target=query, args=(db,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All queries completed.")