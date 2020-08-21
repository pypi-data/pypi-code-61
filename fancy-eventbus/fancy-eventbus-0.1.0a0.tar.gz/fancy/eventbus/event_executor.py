from fancy.eventbus.executor import MainExecutorBase
from fancy.eventbus.executor.thread_executor import ThreadExecutorBase


class EventExecutor:
    MAIN = MainExecutorBase()
    THREAD = ThreadExecutorBase()
