from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThreadPool

from worker import CASWorker

import time
from pyperclip import copy

class TesterClass(QWidget):
    # There's probably a better way to do this but hey, it works
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.passed_tests = 0
        self.failed_tests = 0
        self.counter_threads = 0

        self.test_scientific_notation()
        self.thread_is_running()
        self.test_prev_deriv()

    def thread_is_running(self):
        # Only change theses four variables from test to test
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

    def test_scientific_notation(self):
        self.test_to_scientific_notation()
        self.test_to_scientific_notation_negative_number()
        self.test_to_scientific_notation_large_number()
        self.test_to_scientific_notation_small_number()
        self.test_to_scientific_notation_accuracy()
        self.test_to_scientific_notation_invalid_accuracy()
        self.test_to_scientific_notation_non_complex_number()
        self.test_to_scientific_notation_complex()

    def test_prev_deriv(self):
        self.test_deriv_prev()
        self.test_deriv_prev_latex()
        self.test_deriv_prev_normal()
        self.test_deriv_prev_order()
        self.test_deriv_prev_point()
        self.test_deriv_prev_var()
        self.test_deriv_prev_unicode()

    def test_calc_deriv(self):
        pass

    def test_prev_integ(self):
        pass

    def test_calc_integ(self):
        pass

    def test_prev_limit(self):
        pass

    def test_calc_limit(self):
        pass

    def test_prev_normal_eq(self):
        pass

    def test_prev_diff_eq(self):
        pass

    def test_prev_system_eq(self):
        pass

    def test_calc_normal_eq(self):
        pass

    def test_calc_diff_eq(self):
        pass

    def test_calc_system_eq(self):
        pass

    def test_parse_diff_text(self):
        pass

    def test_prev_simp_exp(self):
        pass

    def test_simp_exp(self):
        pass

    def test_prev_expand_exp(self):
        pass

    def test_expand_exp(self):
        pass

    def test_prev_eval_exp(self):
        pass

    def test_eval_exp(self):
        pass

    def test_calc_pf(self):
        pass

    def test_execute_code(self):
        pass

    def test_prev_formula(self):
        pass

    def test_calc_formula(self):
        pass

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

    def test_deriv_prev(self):
        command = "prev_deriv"
        params = ["x**x", "x", 1, None, 1, False, False]
        solution = {'deriv': ['d / x\\\n--\\x /\ndx    ', 0], 'latex': '\\frac{d}{d x} x^{x}'}
        test_name = "test_deriv_prev"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_deriv_prev_latex(self):
        command = "prev_deriv"
        params = ["x**x", "x", 1, None, 2, False, False]
        solution = {'deriv': ['\\frac{d}{d x} x^{x}', 0], 'latex': '\\frac{d}{d x} x^{x}'}
        test_name = "test_deriv_prev_latex"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_deriv_prev_normal(self):
        command = "prev_deriv"
        params = ["x**x", "x", 1, None, 3, False, False]
        solution = {'deriv': ['Derivative(x**x, x)', 0], 'latex': '\\frac{d}{d x} x^{x}'}
        test_name = "test_deriv_prev_normal"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_deriv_prev_order(self):
        command = "prev_deriv"
        params = ["x**x", "x", 4, None, 1, False, False]
        solution = {'deriv': ['  4    \n d / x\\\n---\\x /\n  4    \ndx     ', 0], 'latex': '\\frac{d^{4}}{d x^{4}} x^{x}'}
        test_name = "test_deriv_prev_order"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_deriv_prev_point(self):
        command = "prev_deriv"
        params = ["x**x", "x", 1, "sqrt(pi)/5.3", 1, False, False]
        solution = {'deriv': ['At x = sqrt(pi)/5.3\nd / x\\\n--\\x /\ndx    ', 0], 'latex': '\\frac{d}{d x} x^{x}'}
        test_name = "test_deriv_prev_point"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_deriv_prev_var(self):
        command = "prev_deriv"
        params = ["hi**hi", "hi", 1, None, 1, False, False]
        solution = {'deriv': [' d /  hi\\\n---\\hi  /\ndhi      ', 0], 'latex': '\\frac{d}{d hi} hi^{hi}'}
        test_name = "test_deriv_prev_var"

        self.current_time = time.time()
        self.counter_threads += 1
        self.qworker = CASWorker(command, params)
        self.qworker.signals.output.connect(lambda output: self.test_output(output, solution, [command, params], test_name))
        self.qworker.signals.finished.connect(self.stop_thread)
        self.threadpool.start(self.qworker)

    def test_deriv_prev_unicode(self):
        command = "prev_deriv"
        params = ["x**x", "x", 1, None, 1, True, False]
        solution = {'deriv': ['d ⎛ x⎞\n──⎝x ⎠\ndx    ', 0], 'latex': '\\frac{d}{d x} x^{x}'}
        test_name = "test_deriv_prev_unicode"

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