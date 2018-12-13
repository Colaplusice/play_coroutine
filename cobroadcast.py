from play_coroutine.utils import coroutine
from play_coroutine.coroutine_pipeline import follow, grep_filter, printer


# 多重协程管道，一对多广播
@coroutine
def broadcast(targets):
    while True:
        item = yield
        for target in targets:
            target.send(item)


f = open("mongodb.log")
follow(f, broadcast([grep_filter("python", printer()), grep_filter("ruby"), printer()]))
