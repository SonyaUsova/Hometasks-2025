def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def fib_with_file(n, filename="text.txt"):
    with open(filename, "w") as file:
        for number in fib(n):
            file.write(str(number) + "\n")

fib_with_file(200)


fib_gen = fib(200)
fib_numbers = list(fib_gen)
print(fib_numbers[-1])
