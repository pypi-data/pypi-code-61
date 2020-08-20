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

        self.test_scientific_notation()

    def test_scientific_notation(self):
        self.test_to_scientific_notation()
        self.test_to_scientific_notation_negative_number()
        self.test_to_scientific_notation_large_number()
        self.test_to_scientific_notation_small_number()
        self.test_to_scientific_notation_accuracy()
        self.test_to_scientific_notation_invalid_accuracy()
        self.test_to_scientific_notation_non_complex_number()
        self.test_to_scientific_notation_complex()

    def test_to_scientific_notation(self):
        command = "to_scientific_notation"
        params = ["12345"]
        solution = {'answer': '1.2345*10**4'}
        test_name = "test_to_scientific_notation"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_to_scientific_notation_negative_number(self):
        command = "to_scientific_notation"
        params = ["-4345"]
        solution = {'answer': '-4.3450*10**3'}
        test_name = "test_to_scientific_notation_negative_number"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(
            lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_to_scientific_notation_large_number(self):
        command = "to_scientific_notation"
        params = ["18446744073709551616"]
        solution = {'answer': '1.8447*10**19'}
        test_name = "test_to_scientific_notation_large_number"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_to_scientific_notation_small_number(self):
        command = "to_scientific_notation"
        params = ["0.00000005747"]
        solution = {'answer': '5.7470*10**(-8)'}
        test_name = "test_to_scientific_notation_small_number"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_to_scientific_notation_accuracy(self):
        command = "to_scientific_notation"
        params = ["18446744073709551616", 15]
        solution = {'answer': '1.84467440737096*10**19'}
        test_name = "test_to_scientific_notation_accuracy"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_to_scientific_notation_invalid_accuracy(self):
        command = "to_scientific_notation"
        params = ["18446744073709551616", "15"]
        solution = {'answer': '1.8447*10**19'}
        test_name = "test_to_scientific_notation_invalid_accuracy"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_to_scientific_notation_non_complex_number(self):
        command = "to_scientific_notation"
        params = ["-oo"]
        solution = {'answer': '-oo'}
        test_name = "test_to_scientific_notation_non_complex_number"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_to_scientific_notation_complex(self):
        command = "to_scientific_notation"
        params = ["-0.109021273701475854840359048696 - 0.500507948960587890643366835011*I", 10]
        solution = {'answer': '-1.090212737*10**(-1) - 5.005079490*10**(-1)*I'}
        test_name = "test_to_scientific_notation_complex"

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