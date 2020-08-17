import multiprocessing
import time
from abc import abstractmethod, ABC
from multiprocessing import Queue

from simses.commons.console_printer import ConsolePrinter
from simses.commons.utils.utils import format_float
from simses.processing.batch_simulation import BatchSimulation


class BatchProcessing(ABC):

    UPDATE: int = 1  # s

    def __init__(self, do_simulation: bool = True, do_analysis: bool = True):
        self.__do_simulation: bool = do_simulation
        self.__do_analysis: bool = do_analysis
        self.__max_parallel_processes: int = multiprocessing.cpu_count()

    @abstractmethod
    def _setup_config(self) -> dict:
        pass

    @abstractmethod
    def clean_up(self) -> None:
        pass

    def run(self):
        config_set: dict = self._setup_config()
        printer_queue: Queue = Queue(maxsize=len(config_set) * 2)
        printer: ConsolePrinter = ConsolePrinter(printer_queue)
        jobs: [BatchSimulation] = list()
        for key, value in config_set.items():
            jobs.append(BatchSimulation(config_set={key: value}, printer_queue=printer_queue,
                                        do_simulation=self.__do_simulation, do_analysis=self.__do_analysis))
        printer.start()
        started: [BatchSimulation] = list()
        start = time.time()
        for job in jobs:
            job.start()
            started.append(job)
            self.__check_running_process(started)
        for job in jobs:
            job.join()
        duration: float = (time.time() - start) / 60.0
        job_count: int = len(jobs)
        print('\nMultiprocessing finished ' + str(job_count) + ' simulations in ' + format_float(duration) + ' min '
              '(' + format_float(duration / job_count) + ' min per simulation)')
        printer.stop_immediately()

    def __check_running_process(self, processes: [multiprocessing.Process]) -> None:
        while True:
            running_jobs: int = 0
            for process in processes:
                if process.is_alive():
                    running_jobs += 1
            if running_jobs < self.__max_parallel_processes:
                break
            time.sleep(self.UPDATE)
