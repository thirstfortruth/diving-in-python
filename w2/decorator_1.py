import functools


def logger(func):
#    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt','a') as f:
            f.write(str(result))

        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


summator([1,3,6,8])

with open('log.txt', 'r') as f:
    print(f.read())

print(summator.__name__)
