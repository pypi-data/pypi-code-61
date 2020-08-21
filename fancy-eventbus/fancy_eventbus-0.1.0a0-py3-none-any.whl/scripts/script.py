import fancy.eventbus as fe


class TestEvent:
    value: int

    def __init__(self, value: int):
        self.value = value


class MyListeners:
    i: int

    def __init__(self):
        fe.register(self)
        self.i = 0

    @fe.SubscribeEvent()
    def on_start(self, event: fe.StartEvent):
        print("start", event.event_loop)
        fe.post(TestEvent(-1))

    @fe.SubscribeEvent()
    def test_event(self, event: TestEvent):
        print("recv:", event.value)
        if self.i < 10:
            print("post:", self.i)
            fe.post(TestEvent(self.i))
            self.i += 1
        else:
            raise TypeError("error")

    @fe.SubscribeEvent(priority=fe.EventPriority.LOWEST)
    def test_event_2(self, event: TestEvent):
        print("recv2:", event.value)

    @fe.SubscribeEvent()
    def error(self, e: Exception):
        print("H", e)
        fe.post(self)
        return False

    @fe.SubscribeEvent(priority=fe.EventPriority.LOW)
    def error2(self, e: TypeError):
        print("L", e)

    @fe.SubscribeEvent()
    def self_forward(self, e: "MyListeners"):
        print("self", e is self)


def main():
    loop = fe.EventLoop()
    MyListeners()

    loop.start()


if __name__ == '__main__':
    main()
