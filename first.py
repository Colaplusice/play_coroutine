import time
from play_coroutine.utils import coroutine


def follow(the_file):
    the_file.seek(0)  # Go to the end of the file
    while True:
        line = the_file.readline()
        if not line:
            time.sleep(1)
            continue
        yield line


@coroutine
def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


logfile = open("mongodb.log")
loglines = follow(logfile)
pylines = grep("python", loglines)

for line in pylines:
    print(line)


# yield 接受数据
def grep(pattern):
    print("looking for %s" % pattern)
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)

    except GeneratorExit:
        print("going away goodbye")
