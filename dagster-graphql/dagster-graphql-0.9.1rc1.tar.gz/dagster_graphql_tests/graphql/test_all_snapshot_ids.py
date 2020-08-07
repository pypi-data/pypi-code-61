from dagster.serdes import serialize_pp

from .setup import get_main_external_repo


def test_all_snapshot_ids(snapshot):
    # This ensures that pipeline snapshots remain stable
    # If you 1) change any pipelines in dagster_graphql_test or 2) change the
    # schema of PipelineSnapshots you are free to rerecord
    repo = get_main_external_repo()
    for pipeline in sorted(repo.get_all_external_pipelines(), key=lambda p: p.name):
        snapshot.assert_match(serialize_pp(pipeline.pipeline_snapshot))
        snapshot.assert_match(pipeline.computed_pipeline_snapshot_id)
