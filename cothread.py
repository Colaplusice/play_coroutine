from play_coroutine.utils import coroutine
from queue import Queue
from threading import Thread
from play_coroutine.parse_xml_buses import (
    EventHandler,
    buses_to_dict,
    filter_on_field,
    bus_locations,
)

import xml


@coroutine
def threaded(target):
    messages = Queue()

    def run_target():
        while True:
            item = messages.get()
            if item is GeneratorExit:
                target.close()
                return
            else:
                target.send(item)

    Thread(target=run_target).start()
    try:
        # 接受值然后存在队列中
        while True:
            item = yield
            messages.put(item)
    except GeneratorExit:
        messages.put(GeneratorExit)


# 解析并添加事件监听
xml.sax.parse(
    "a.xml",
    EventHandler(
        # 时间监听发送消息到bus_to_dict函数
        buses_to_dict(
            # 通过线程来传输data
            threaded(
                # 继续向下发送过滤22路公交车
                filter_on_field(
                    # 向下发送过滤目的地为North Bus的站牌
                    "route",
                    "22",
                    filter_on_field("direction", "North bus", bus_locations),
                )
            )
        )
    ),
)
