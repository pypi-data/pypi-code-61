class FancyEventBusException(Exception):
    def should_shutdown_immediately(self) -> bool:
        return False
