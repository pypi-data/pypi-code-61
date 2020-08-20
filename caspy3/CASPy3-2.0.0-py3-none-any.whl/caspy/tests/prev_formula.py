import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThreadPool

from pyperclip import copy
import time

from worker import CASWorker

class TesterClass(QWidget):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.passed_tests = 0
        self.failed_tests = 0
        self.counter_threads = 0

        self.thread_is_running()

    def thread_is_running(self):
        command = "is_running"
        params = ["does_run"]
        solution = {'running': 'does_run'}
        test_name = "thread_is_running"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def stop_thread(self):
        pass

    def test_output(self, input_dict, solution, input_list, test_name):
        """
        Compares input_dict with solution and prints info if it fails
        :param input_dict: dict
            Dictionary returned by the worker thread
        :param solution: dict
            Expected solution
        :param input_list: list
            Contains called command and params. First element = command (str), second element = list of params
        :param test_name: str
            Name of current test. Gets printed if it Passes
        :param current_time: float
            Time before worker executes command
        """
        self.counter_threads -= 1
        if input_dict == solution:
            execution_time = str(time.time() - self.current_time)[0:5]
            print(f"Test '{test_name}' passed in {execution_time}s")
            self.passed_tests += 1
        else:
            copy(str(input_dict))
            print(f"\033[91m\n Test '{test_name}' failed with command '{input_list[0]}' and with params '{input_list[1]}'\n Output         : {input_dict}\n Expected output: {solution}\n\033[0m")
            self.failed_tests += 1

        if self.counter_threads == 0:
            print("-" * 30)
            print(f"Testing finished\nFailed tests: {self.failed_tests}\nPassed tests: {self.passed_tests}\nNumber of tests: {self.failed_tests + self.passed_tests}")
            QApplication.quit()

if __name__ == "__main__":
    import sys

    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook

    app = QApplication(sys.argv)
    caspy = TesterClass()
    sys.exit(app.exec_())