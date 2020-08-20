import time
import pytest
import uuid

from .context import Context, Parameter
from .base_listener import BaseZafiraListener
from .resource_constants import TestStatus


class PyTestZafiraListener(BaseZafiraListener):
    """
    Contains hook implementations
    """

    def __init__(self, state):
        super().__init__(state)

        self.state.CONFIG = "<config><arg unique='false'><key>env</key><value>API " \
                            + Context.get_gui_parameter(Parameter.BROWSER).upper() + "</value></arg></config>"

    @pytest.hookimpl
    def pytest_sessionstart(self, session):
        """
        Setup-class handler, signs in user, creates a testsuite,
        testcase, job and registers testrun in Zafira
        """
        if not self.initialized:
            return
        try:
            self.state.user = self.state.zc.get_user_profile().json()
            self.state.test_suite = self.state.zc.create_test_suite(
                self.state.user["id"], self.state.suite_name, 'filename'
            ).json()
            self.state.job = self.state.zc.create_job(
                self.state.user["id"],
                self.state.job_name,
                self.state.job_url,
                "jenkins_host"
            ).json()
            self.state.test_run = self.state.zc.start_test_run(
                self.state.job["id"],
                self.state.test_suite["id"],
                0,
                config=self.state.CONFIG
            ).json()
            self.state.ci_run_id = self.state.test_run.get('ciRunId')
        except Exception as e:
            self.state.is_enabled = False
            self.logger.error("Undefined error during test run registration! {}".format(e))

    @pytest.hookimpl
    def pytest_runtest_setup(self, item):
        """
        Setup handler, set up initial parameters for test,
        attaches to testsuite, registers and starts the test
        """
        if not self.state.is_enabled:
            return
        try:
            test_name = item.name
            class_name = item.nodeid.split('::')[1]
            self.state.ci_test_id = str(uuid.uuid4())

            full_path_to_file = item.nodeid.split('::')[0].split('/')
            package = self.compose_package_name(full_path_to_file) + '/'
            self.state.test_case = self.state.zc.create_test_case(
                class_name, test_name, self.state.test_suite["id"], self.state.user["id"]
            ).json()
            work_items = []
            if hasattr(item._evalxfail, 'reason'):
                work_items.append('xfail')
            self.state.test = self.state.zc.start_test(
                self.state.test_run["id"],
                self.state.test_case["id"],
                test_name,
                round(time.time() * 1000),
                self.state.ci_test_id,
                TestStatus.IN_PROGRESS.value,
                class_name,
                package,
                work_items
            ).json()
        except Exception as e:
            self.logger.error("Undefined error during test case/method start! {}".format(e))

    @pytest.hookimpl
    def pytest_runtest_teardown(self, item):
        """
        Teardown handler. Finishes test, adds workitems if needed
        """
        if not self.state.is_enabled:
            return
        try:
            if item._skipped_by_mark:
                test_name = item.name
                class_name = item.nodeid.split('::')[1]
                full_path_to_file = item.nodeid.split('::')[0].split('/')
                package = self.compose_package_name(full_path_to_file) + '/'
                self.state.test_case = self.state.zc.create_test_case(
                    class_name, test_name, self.state.test_suite["id"], self.state.user["id"]
                ).json()
                self.state.test = self.state.zc.start_test(
                    self.state.test_run["id"], self.state.test_case["id"], test_name,
                    round(time.time() * 1000), self.state.ci_test_id, test_class=class_name, test_group=package
                ).json()

                self.state.test['status'] = TestStatus.SKIPPED.value
                self.add_work_item_to_test(self.state.test['id'], self.state.skip_reason)

            self.state.zc.finish_test(self.state.test)
        except Exception as e:
            self.logger.error("Unable to finish test run correctly: {}".format(e))

    @pytest.hookimpl
    def pytest_runtest_logreport(self, report):
        """
        Set test status, stacktrace if needed
        :param report: info about test
        """
        if not self.state.is_enabled:
            return
        try:
            if report.when == 'setup':
                if report.skipped:
                    self.state.skip_reason = report.longrepr[2]
                if report.failed:
                    self.on_test_failure(report)
            if report.when == 'call':
                self.state.test["finishTime"] = round(time.time() * 1000)
                test_result = report.outcome
                if test_result is 'passed':
                    self.on_test_success()
                elif test_result is 'failed':
                    self.on_test_failure(report)
                else:
                    self.on_test_skipped(report)
                self.add_artifact_to_test(
                    self.state.test,
                    self.state.artifact_log_name,
                    'http://google.com',
                    self.state.artifact_expires_in_default_time
                )
        except Exception as e:
            self.logger.error("Unable to finish test correctly: {}".format(e))

    @pytest.hookimpl
    def pytest_sessionfinish(self, session, exitstatus):
        """
        Teardown-class handler, closes the testrun
        """
        if not self.state.is_enabled:
            return
        try:
            self.state.zc.finish_test_run(self.state.test_run["id"])
        except Exception as e:
            self.logger.error("Unable to finish test run correctly: {}".format(e))

    def on_test_success(self):
        self.state.test['status'] = TestStatus.PASSED.value

    def on_test_failure(self, message):
        self.state.test['status'] = TestStatus.FAILED.value
        self.state.test['message'] = message.longreprtext

    def on_test_skipped(self, message):
        self.state.test['message'] = message.longreprtext
        if not hasattr(message, 'wasxfail'):
            self.state.test['status'] = TestStatus.SKIPPED.value
        else:
            self.state.test['status'] = TestStatus.FAILED.value
