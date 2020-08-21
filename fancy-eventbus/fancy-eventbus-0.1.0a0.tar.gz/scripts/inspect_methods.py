import fancy.eventbus as fe


class MyEvent:
    value: int

    def __init__(self, value):
        self.value = value


class MyEvent2:
    pass


class Target:
    def __init__(self):
        fe.register(self)

    @fe.SubscribeEvent()
    def on_start(self, event: fe.StartEvent):
        print("start!")
        fe.post(MyEvent(1))

    @fe.SubscribeEvent()
    def my_event(self, event: MyEvent):
        print("my_event", event.value)
        fe.post(MyEvent2())
        fe.post(self)

    @fe.SubscribeEvent()
    def my_event2(self, event: MyEvent2):
        print("my_event2")
        raise RuntimeError("an error")

    @fe.SubscribeEvent(priority=fe.EventPriority.HIGHEST)  # execute before my_event2
    def self_as_event(self, event: "Target"):  # forwarding ref
        print("self_as_event", event is self)

    @fe.SubscribeEvent()
    def error_handler(self, e: RuntimeError):
        print("handle by runtime error", e)

    @fe.SubscribeEvent(priority=fe.EventPriority.LOW)  # method name should different
    def error_handler2(self, e: Exception):
        print("handle by exception", e)
        return False  # returned false will cancel the event

    @fe.SubscribeEvent(priority=fe.EventPriority.LOWEST)
    def error_handler3(self, e: BaseException):
        print("this should be canceled.", e)


loop = fe.EventLoop()
# registers
Target()

loop.start()
