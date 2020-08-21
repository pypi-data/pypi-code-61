from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fancy.eventbus import EventLoop


class StartEvent:
    _event_loop: 'EventLoop'

    def __init__(self, event_loop: 'EventLoop'):
        self._event_loop = event_loop

    @property
    def event_loop(self) -> 'EventLoop':
        return self._event_loop
