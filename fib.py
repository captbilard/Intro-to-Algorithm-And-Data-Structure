import time


def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(time.process_time_ns())
print(fib(6))
print(time.process_time_ns())

print(time.process_time_ns())
print(fib(7))
print(time.process_time_ns())



print(time.process_time_ns())
print(fib(50))
print(time.process_time_ns())