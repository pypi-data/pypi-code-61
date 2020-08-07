from dagster_graphql import dauphin
from dagster_graphql.implementation.fetch_partition_sets import (
    get_partition_by_name,
    get_partition_config,
    get_partition_tags,
    get_partitions,
)
from dagster_graphql.implementation.fetch_runs import get_runs
from dagster_graphql.schema.errors import (
    DauphinPartitionSetNotFoundError,
    DauphinPipelineNotFoundError,
    DauphinPythonError,
)

from dagster import check
from dagster.core.host_representation import ExternalPartitionSet, RepositoryHandle
from dagster.core.storage.pipeline_run import PipelineRunsFilter


class DauphinPartition(dauphin.ObjectType):
    class Meta(object):
        name = 'Partition'

    name = dauphin.NonNull(dauphin.String)
    partition_set_name = dauphin.NonNull(dauphin.String)
    solid_selection = dauphin.List(dauphin.NonNull(dauphin.String))
    mode = dauphin.NonNull(dauphin.String)
    runConfigOrError = dauphin.NonNull('PartitionRunConfigOrError')
    tagsOrError = dauphin.NonNull('PartitionTagsOrError')
    runs = dauphin.non_null_list('PipelineRun')

    def __init__(self, external_repository_handle, external_partition_set, partition_name):
        self._external_repository_handle = check.inst_param(
            external_repository_handle, 'external_respository_handle', RepositoryHandle
        )
        self._external_partition_set = check.inst_param(
            external_partition_set, 'external_partition_set', ExternalPartitionSet
        )
        self._partition_name = check.str_param(partition_name, 'partition_name')

        super(DauphinPartition, self).__init__(
            name=partition_name,
            partition_set_name=external_partition_set.name,
            solid_selection=external_partition_set.solid_selection,
            mode=external_partition_set.mode,
        )

    def resolve_runConfigOrError(self, graphene_info):
        return get_partition_config(
            graphene_info,
            self._external_repository_handle,
            self._external_partition_set.name,
            self._partition_name,
        )

    def resolve_tagsOrError(self, graphene_info):
        return get_partition_tags(
            graphene_info,
            self._external_repository_handle,
            self._external_partition_set.name,
            self._partition_name,
        )

    def resolve_runs(self, graphene_info):
        runs_filter = PipelineRunsFilter(
            tags={
                'dagster/partition_set': self._external_partition_set.name,
                'dagster/partition': self._partition_name,
            }
        )
        return get_runs(graphene_info, runs_filter)


class DauphinPartitions(dauphin.ObjectType):
    class Meta(object):
        name = 'Partitions'

    results = dauphin.non_null_list('Partition')


class DauphinPartitionSet(dauphin.ObjectType):
    class Meta(object):
        name = 'PartitionSet'

    name = dauphin.NonNull(dauphin.String)
    pipeline_name = dauphin.NonNull(dauphin.String)
    solid_selection = dauphin.List(dauphin.NonNull(dauphin.String))
    mode = dauphin.NonNull(dauphin.String)
    partitionsOrError = dauphin.Field(
        dauphin.NonNull('PartitionsOrError'),
        cursor=dauphin.String(),
        limit=dauphin.Int(),
        reverse=dauphin.Boolean(),
    )
    partition = dauphin.Field('Partition', partition_name=dauphin.NonNull(dauphin.String))

    def __init__(self, external_repository_handle, external_partition_set):
        self._external_repository_handle = check.inst_param(
            external_repository_handle, 'external_respository_handle', RepositoryHandle
        )
        self._external_partition_set = check.inst_param(
            external_partition_set, 'external_partition_set', ExternalPartitionSet
        )

        super(DauphinPartitionSet, self).__init__(
            name=external_partition_set.name,
            pipeline_name=external_partition_set.pipeline_name,
            solid_selection=external_partition_set.solid_selection,
            mode=external_partition_set.mode,
        )

    def resolve_partitionsOrError(self, graphene_info, **kwargs):
        return get_partitions(
            graphene_info,
            self._external_repository_handle,
            self._external_partition_set,
            cursor=kwargs.get("cursor"),
            limit=kwargs.get("limit"),
            reverse=kwargs.get('reverse'),
        )

    def resolve_partition(self, graphene_info, partition_name):
        return get_partition_by_name(
            graphene_info,
            self._external_repository_handle,
            self._external_partition_set,
            partition_name,
        )


class DapuphinPartitionSetOrError(dauphin.Union):
    class Meta(object):
        name = 'PartitionSetOrError'
        types = ('PartitionSet', DauphinPartitionSetNotFoundError, DauphinPythonError)


class DauphinPartitionSets(dauphin.ObjectType):
    class Meta(object):
        name = 'PartitionSets'

    results = dauphin.non_null_list('PartitionSet')


class DauphinPartitionTags(dauphin.ObjectType):
    class Meta(object):
        name = 'PartitionTags'

    results = dauphin.non_null_list('PipelineTag')


class DauphinPartitionRunConfig(dauphin.ObjectType):
    class Meta(object):
        name = 'PartitionRunConfig'

    yaml = dauphin.NonNull(dauphin.String)


class DauphinPartitionSetsOrError(dauphin.Union):
    class Meta(object):
        name = 'PartitionSetsOrError'
        types = (DauphinPartitionSets, DauphinPipelineNotFoundError, DauphinPythonError)


class DauphinPartitionsOrError(dauphin.Union):
    class Meta(object):
        name = 'PartitionsOrError'
        types = (DauphinPartitions, DauphinPythonError)


class DauphinPartitionTagsOrError(dauphin.Union):
    class Meta(object):
        name = 'PartitionTagsOrError'
        types = (DauphinPartitionTags, DauphinPythonError)


class DauphinPartitionRunConfigOrError(dauphin.Union):
    class Meta(object):
        name = 'PartitionRunConfigOrError'
        types = (DauphinPartitionRunConfig, DauphinPythonError)
