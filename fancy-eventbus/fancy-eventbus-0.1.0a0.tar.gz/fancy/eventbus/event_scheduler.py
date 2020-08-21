from fancy.eventbus import EventListener
from fancy.eventbus.scheduler import MultilevelFeedbackQueueScheduler, SchedulerBase


class EventScheduler:
    MULTILEVEL_FEEDBACK_QUEUE: SchedulerBase[EventListener] = MultilevelFeedbackQueueScheduler()
