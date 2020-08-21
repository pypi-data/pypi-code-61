from fancy.eventbus.execeptions import FancyEventBusException


class StopLoopingException(FancyEventBusException):
    def should_shutdown_immediately(self) -> bool:
        return True
