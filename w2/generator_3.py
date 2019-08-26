def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value: break
        total += value

generator = accumulator()
next(generator)
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(2)))
next(generator)
print('Accumulated: {}'.format(generator.send(1)))
next(generator)
