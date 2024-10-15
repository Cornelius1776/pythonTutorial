# fibonacci
def fib(num):
    if num <= 1:
        return num
    result = fib(num - 1) + fib(num - 2)
    return result


print(fib(4))
print(fib(8))
print(fib(10))


# print(fib(50))

# Optimized Using dynamic programming
# Memoization (Top-down)
def optimized_fib(num, cache=None):
    if cache is None:
        cache = {}
    if num <= 1:
        return num

    if num in cache:
        return cache[num]

    result = optimized_fib(num - 1) + optimized_fib(num - 2)
    cache[num] = result
    return result


print(optimized_fib(50))


# Tabulation (Bottom-up)
def tab_fib(num):
    if num <= 1:
        return num
    arr = [0] * (num + 1)
    arr[1] = 1

    for i in range(2, num + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[num]


print(tab_fib(4))
print(tab_fib(8))
print(tab_fib(10))
print(tab_fib(50))
