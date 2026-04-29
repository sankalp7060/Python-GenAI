import threading
import time

def timer():
    for _ in range(3):
        print("System alive...")
        time.sleep(2)

t = threading.Thread(target=timer)
t.start()
t.join()