def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2

for number in even_range(0,10):
    print(number)


ranger = even_range(1,4)
next(ranger)
next(ranger)
next(ranger)
