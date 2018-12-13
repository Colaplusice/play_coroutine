import time
from play_coroutine.utils import coroutine


def read():
    try:
        lines = yield
    except GeneratorExit:
        pass


def follow(the_file, target):
    the_file.seek(0, 2)  # to end of file
    while True:
        line = the_file.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


@coroutine
def printer():
    while True:
        line = yield
        print(line)


f = open('mongodb.log')
follow(f, printer())


# follow函数将读取到的内容send到printer函数中，printer函数接收值，然后打印出来。 形成协程到的管道

#   grep filter
def grep_filter(pattern, target):
    while True:
        line = yield
        if pattern in line:
            target.send(line)


f = open('mongodb.log')
follow(f, grep_filter('python', printer()))
