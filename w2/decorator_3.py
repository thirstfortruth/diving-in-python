def first_decorator(func):
    def wrapped():
        print('the first decorator')
        return func()
    return wrapped

def second_decorator(func):
    def wrapped():
        print('Second decorator')
        return func()
    return wrapped
    
@first_decorator
@second_decorator

def decorated():
    print('Finally called...')


decorated()




