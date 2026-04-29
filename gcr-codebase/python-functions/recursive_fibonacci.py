def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def generate_fibonacci(n):
    return [fib(i) for i in range(n)]

print(generate_fibonacci(6))