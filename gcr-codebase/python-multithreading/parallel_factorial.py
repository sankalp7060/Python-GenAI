from multiprocessing import Pool
import math

nums = [5, 7, 10]

with Pool() as p:
    results = p.map(math.factorial, nums)

print(*results)