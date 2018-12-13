import xml.sax
from play_coroutine.utils import coroutine


class EventHandler(xml.sax.ContentHandler):
    def __init__(self, target):
        self.target = target

    # override
    def startElement(self, name, attrs):
        self.target.send(("start", (name, attrs._attrs)))

    # override
    def characters(self, text):
        self.target.send(("text", text))

    def endElement(self, name):
        self.target.send(("end", name))


@coroutine
def buses_to_dict(target):
    # 发送数据格式  (start,bus('bus',*))   ('end','bus')
    while True:
        event, value = yield
        # start
        if event == "start" and value[0] == "bus":
            bus_dict = {}
            fragments = []
            # receive value
            while True:
                event, value = yield
                if event == "start":
                    fragments = []
                elif event == "text":
                    fragments.append(value)
                # if end send_value
                elif event == "end":
                    if value != "bus":
                        bus_dict[value] = ".".join(fragments)
                    else:
                        target.send(bus_dict)
                        break


@coroutine
def filter_on_field(field_name, value, target):
    while True:
        d = yield
        if d.get(field_name) == value:
            target.send(d)


# 寻找第22路公交车
# filter_on_field("route", "22", target="")
# 寻找到徐庄软件园的站
# filter_on_field("direction", "徐庄软件园", target="")


@coroutine
def bus_locations():
    while True:
        bus = yield
        print('%(route)s,%(id)s,"%(direction)s",' "%(latitude)s,%(latitude)s" % bus)


# 由外向内， 先解析xml， 将data转换为dict发送到 filter_field 找147路公交车
# ，找到后将dict继续向下发送，找目的地为 North Bound 的站牌，如果找到了,send到bus_locations打印出来。
a = xml.sax.parse(
    "a.xml",
    EventHandler(
        buses_to_dict(
            filter_on_field(
                "route",
                "147",
                filter_on_field("direction", "North Bound", bus_locations()),
            )
        )
    ),
)
