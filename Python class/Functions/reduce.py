# reduce() calls a function on an iterable and reduce the elements of the iterable it to a single
# value. functools will be imported to use reduce
import functools
letters = ["S", "T", "E", "V", "E"]
name = functools.reduce(lambda a, b: a + b, letters)
print(name)

factorial = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
result = functools.reduce(lambda a, b: a * b, factorial)
print(result)
