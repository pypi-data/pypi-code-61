from collections import deque
from typing import List, Deque, Optional, TypeVar

from fancy.eventbus.scheduler import SchedulerBase, Prioritiable

T = TypeVar("T", bound=Prioritiable)


class MultilevelFeedbackQueueScheduler(SchedulerBase[T]):  # TODO use max heap
    queues: List[Deque[T]]
    _length: int = 0
    max_queues: int = 5

    def __init__(self):
        self.queues = [deque() for _ in range(self.max_queues)]

    def has_next(self) -> bool:
        return self._length > 0

    def next(self) -> T:
        currently_highest_non_empty_queue = self._find_first_non_empty_queue()
        if currently_highest_non_empty_queue is None:
            raise StopIteration()

        item = currently_highest_non_empty_queue.popleft()
        self._length -= 1
        self._aging()
        return item

    def _find_first_non_empty_queue(self) -> Optional[Deque[T]]:
        for queue in reversed(self.queues):
            if len(queue) > 0:
                return queue
        return None

    def _aging(self):
        for i in range(self.max_queues - 2, -1, -1):
            self.queues[i + 1].extend(self.queues[i])
            self.queues[i].clear()

    def add(self, item: T) -> None:
        self.queues[item.get_priority()].append(item)
        self._length += 1

    def remove(self, item: T) -> None:
        for queue in self.queues:
            try:
                queue.remove(item)
                self._length -= 1
                return
            except ValueError as _:
                pass
        raise ValueError(f'{MultilevelFeedbackQueueScheduler.__name__}.remove(item): item not in queues.')
