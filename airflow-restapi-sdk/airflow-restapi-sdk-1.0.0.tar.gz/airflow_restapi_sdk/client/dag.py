import time
from ..http import MyHttp
from ..exceptions import DagRunTimeOutError


class State(object):
    """
    Static class with task instance states constants and color method to
    avoid hardcoding.
    """

    # scheduler
    NONE = None
    REMOVED = "removed"
    SCHEDULED = "scheduled"

    # set by the executor (t.b.d.)
    # LAUNCHED = "launched"

    # set by a task
    QUEUED = "queued"
    RUNNING = "running"
    SUCCESS = "success"
    SHUTDOWN = "shutdown"  # External request to shut down
    FAILED = "failed"
    UP_FOR_RETRY = "up_for_retry"
    UP_FOR_RESCHEDULE = "up_for_reschedule"
    UPSTREAM_FAILED = "upstream_failed"
    SKIPPED = "skipped"


class DagRun:
    def __init__(self, _http: MyHttp) -> None:
        self._http = _http

    def trigger(self, dag_id, conf=None):
        return self._http.post('/api/experimental/dags/{}/dag_runs'.format(dag_id), json={'conf': conf})

    def state(self, dag_id, execution_date):
        return self._http.get('/api/experimental/dags/{}/dag_runs/{}'.format(dag_id, execution_date))

    def trigger_join(self, dag_id, conf=None, timeout=600, step=10):
        data = self.trigger(dag_id, conf=conf)
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                raise DagRunTimeOutError('timeout {}s'.format(timeout))

            result = self.state(dag_id, data['execution_date'])
            if result['state'] in [State.FAILED, State.SUCCESS]:
                return result['state']
            time.sleep(step)
