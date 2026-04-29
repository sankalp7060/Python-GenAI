def measure_time(func):
    start = time.time()
    func()
    end = time.time()
    print("Execution time:", (end - start) * 1000, "ms")

measure_time(lambda: sum(range(100000)))