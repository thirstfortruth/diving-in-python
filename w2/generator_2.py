def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b

print(fibonacci(10))

