def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

fib_gen = fib(200)
fib_numbers = list(fib_gen)
fib_200 = fib_numbers[-1]
print(fib_200)
