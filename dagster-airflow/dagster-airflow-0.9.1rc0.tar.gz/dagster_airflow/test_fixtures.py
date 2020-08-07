import logging
import sys

import pytest
from airflow import DAG
from airflow.exceptions import AirflowSkipException
from airflow.models import TaskInstance
from airflow.settings import LOG_FORMAT
from airflow.utils import timezone

from dagster.core.utils import make_new_run_id
from dagster.utils import load_yaml_from_glob_list


def execute_tasks_in_dag(dag, tasks, run_id, execution_date):
    assert isinstance(dag, DAG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter(LOG_FORMAT))
    root = logging.getLogger('airflow.task.operators')
    root.setLevel(logging.DEBUG)
    root.addHandler(handler)

    dag_run = dag.create_dagrun(run_id=run_id, state='success', execution_date=execution_date)

    results = {}
    for task in tasks:
        ti = TaskInstance(task=task, execution_date=execution_date)
        context = ti.get_template_context()
        context['dag_run'] = dag_run

        try:
            results[ti] = task.execute(context)
        except AirflowSkipException as exc:
            results[ti] = exc

    return results


@pytest.fixture(scope='function')
def dagster_airflow_python_operator_pipeline():
    '''This is a test fixture for running Dagster pipelines as Airflow DAGs.

    Usage:
        from dagster_airflow.test_fixtures import dagster_airflow_python_operator_pipeline

        def test_airflow(dagster_airflow_python_operator_pipeline):
            results = dagster_airflow_python_operator_pipeline(
                pipeline_name='test_pipeline',
                recon_repo=reconstructable(define_pipeline),
                environment_yaml=['environments/test_*.yaml']
            )
            assert len(results) == 3
    '''
    from .factory import make_airflow_dag_for_recon_repo
    from .vendor.python_operator import PythonOperator

    def _pipeline_fn(
        recon_repo,
        pipeline_name,
        run_config=None,
        environment_yaml=None,
        op_kwargs=None,
        mode=None,
        execution_date=timezone.utcnow(),
    ):
        if run_config is None and environment_yaml is not None:
            run_config = load_yaml_from_glob_list(environment_yaml)

        dag, tasks = make_airflow_dag_for_recon_repo(
            recon_repo, pipeline_name, run_config, mode=mode, op_kwargs=op_kwargs
        )
        assert isinstance(dag, DAG)

        for task in tasks:
            assert isinstance(task, PythonOperator)

        return execute_tasks_in_dag(
            dag, tasks, run_id=make_new_run_id(), execution_date=execution_date
        )

    return _pipeline_fn


@pytest.fixture(scope='function')
def dagster_airflow_custom_operator_pipeline():
    '''This is a test fixture for running Dagster pipelines with custom operators as Airflow DAGs.

    Usage:
        from dagster_airflow.test_fixtures import dagster_airflow_custom_operator_pipeline

        def test_airflow(dagster_airflow_python_operator_pipeline):
            results = dagster_airflow_custom_operator_pipeline(
                pipeline_name='test_pipeline',
                recon_repo=reconstructable(define_pipeline),
                operator=MyCustomOperator,
                environment_yaml=['environments/test_*.yaml']
            )
            assert len(results) == 3
    '''
    from .factory import make_airflow_dag_for_operator
    from .vendor.python_operator import PythonOperator

    def _pipeline_fn(
        recon_repo,
        pipeline_name,
        operator,
        run_config=None,
        environment_yaml=None,
        op_kwargs=None,
        mode=None,
        execution_date=timezone.utcnow(),
    ):
        if run_config is None and environment_yaml is not None:
            run_config = load_yaml_from_glob_list(environment_yaml)

        dag, tasks = make_airflow_dag_for_operator(
            recon_repo, pipeline_name, operator, run_config, mode=mode, op_kwargs=op_kwargs
        )
        assert isinstance(dag, DAG)

        for task in tasks:
            assert isinstance(task, PythonOperator)

        return execute_tasks_in_dag(
            dag, tasks, run_id=make_new_run_id(), execution_date=execution_date
        )

    return _pipeline_fn


@pytest.fixture(scope='function')
def dagster_airflow_docker_operator_pipeline():
    '''This is a test fixture for running Dagster pipelines as containerized Airflow DAGs.

    Usage:
        from dagster_airflow.test_fixtures import dagster_airflow_docker_operator_pipeline

        def test_airflow(dagster_airflow_docker_operator_pipeline):
            results = dagster_airflow_docker_operator_pipeline(
                pipeline_name='test_pipeline',
                recon_repo=reconstructable(define_pipeline),
                environment_yaml=['environments/test_*.yaml'],
                image='myimage:latest'
            )
            assert len(results) == 3
    '''
    from .factory import make_airflow_dag_containerized_for_recon_repo
    from .operators.docker_operator import DagsterDockerOperator

    def _pipeline_fn(
        recon_repo,
        pipeline_name,
        image,
        run_config=None,
        environment_yaml=None,
        op_kwargs=None,
        mode=None,
        execution_date=timezone.utcnow(),
    ):
        if run_config is None and environment_yaml is not None:
            run_config = load_yaml_from_glob_list(environment_yaml)

        dag, tasks = make_airflow_dag_containerized_for_recon_repo(
            recon_repo=recon_repo,
            pipeline_name=pipeline_name,
            image=image,
            mode=mode,
            run_config=run_config,
            op_kwargs=op_kwargs,
        )
        assert isinstance(dag, DAG)

        for task in tasks:
            assert isinstance(task, DagsterDockerOperator)

        return execute_tasks_in_dag(
            dag, tasks, run_id=make_new_run_id(), execution_date=execution_date
        )

    return _pipeline_fn


@pytest.fixture(scope='function')
def dagster_airflow_k8s_operator_pipeline():
    '''This is a test fixture for running Dagster pipelines on Airflow + K8s.

    Usage:
        from dagster_airflow.test_fixtures import dagster_airflow_k8s_operator_pipeline

        def test_airflow(dagster_airflow_k8s_operator_pipeline):
            results = dagster_airflow_k8s_operator_pipeline(
                pipeline_name='test_pipeline',
                recon_repo=reconstructable(define_pipeline),
                environment_yaml=['environments/test_*.yaml'],
                image='myimage:latest'
            )
            assert len(results) == 3
    '''
    from .factory import make_airflow_dag_kubernetized_for_recon_repo
    from .operators.kubernetes_operator import DagsterKubernetesPodOperator

    def _pipeline_fn(
        recon_repo,
        pipeline_name,
        image,
        run_config=None,
        environment_yaml=None,
        op_kwargs=None,
        mode=None,
        namespace='default',
        execution_date=timezone.utcnow(),
    ):
        if run_config is None and environment_yaml is not None:
            run_config = load_yaml_from_glob_list(environment_yaml)

        op_kwargs = op_kwargs or {}

        # In this test, sometimes we are pulling the integration image for the first
        # time on a BK node, which can take a long time.
        op_kwargs['startup_timeout_seconds'] = 300

        dag, tasks = make_airflow_dag_kubernetized_for_recon_repo(
            recon_repo=recon_repo,
            pipeline_name=pipeline_name,
            image=image,
            mode=mode,
            namespace=namespace,
            run_config=run_config,
            op_kwargs=op_kwargs,
        )
        assert isinstance(dag, DAG)

        for task in tasks:
            assert isinstance(task, DagsterKubernetesPodOperator)
            # testing to make sure that kwargs shuffling works
            assert task.startup_timeout_seconds == 300

        return execute_tasks_in_dag(
            dag, tasks, run_id=make_new_run_id(), execution_date=execution_date
        )

    return _pipeline_fn
