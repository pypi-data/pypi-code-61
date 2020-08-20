from hyperfoil.clients import RunClient, BenchmarkClient
from hyperfoil.resources import Run, Benchmark


def test_create(benchmark, benchmark_yaml):
    assert benchmark.create(params=benchmark_yaml)
    mark = benchmark.read(benchmark_yaml['name'])
    assert mark.entity == benchmark_yaml
    assert isinstance(mark, Benchmark)
    assert isinstance(mark.client, BenchmarkClient)


def test_all(benchmark, benchmark_yaml):
    assert benchmark.create(params=benchmark_yaml)
    all_benchmarks = benchmark.list()
    filtered = list(filter(lambda x: x.get('name') == benchmark_yaml['name'], all_benchmarks))
    assert len(filtered) == 1
    assert filtered[0].entity == benchmark_yaml


def test_start(benchmark, benchmark_yaml):
    assert benchmark.create(params=benchmark_yaml)
    run = benchmark.start(benchmark_yaml['name'])
    assert run
    assert run['id']
    assert isinstance(run, Run)
    assert isinstance(run.client, RunClient)
