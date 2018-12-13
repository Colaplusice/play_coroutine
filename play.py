import time


def a():
    print('12')

    time.sleep(2)
    for i in range(10):
        print(
            '123'
        )
        yield i


result = a()
# next(result)