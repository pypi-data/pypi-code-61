# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for efs service client

Usage::

    ```python
    import boto3
    from mypy_boto3_efs import EFSClient

    client: EFSClient = boto3.client("efs")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_efs.paginator import (
    DescribeFileSystemsPaginator,
    DescribeMountTargetsPaginator,
    DescribeTagsPaginator,
)
from mypy_boto3_efs.type_defs import (
    AccessPointDescriptionTypeDef,
    BackupPolicyDescriptionTypeDef,
    BackupPolicyTypeDef,
    DescribeAccessPointsResponseTypeDef,
    DescribeFileSystemsResponseTypeDef,
    DescribeMountTargetSecurityGroupsResponseTypeDef,
    DescribeMountTargetsResponseTypeDef,
    DescribeTagsResponseTypeDef,
    FileSystemDescriptionTypeDef,
    FileSystemPolicyDescriptionTypeDef,
    LifecycleConfigurationDescriptionTypeDef,
    LifecyclePolicyTypeDef,
    ListTagsForResourceResponseTypeDef,
    MountTargetDescriptionTypeDef,
    PosixUserTypeDef,
    RootDirectoryTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EFSClient",)


class Exceptions:
    AccessPointAlreadyExists: Type[Boto3ClientError]
    AccessPointLimitExceeded: Type[Boto3ClientError]
    AccessPointNotFound: Type[Boto3ClientError]
    BadRequest: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    DependencyTimeout: Type[Boto3ClientError]
    FileSystemAlreadyExists: Type[Boto3ClientError]
    FileSystemInUse: Type[Boto3ClientError]
    FileSystemLimitExceeded: Type[Boto3ClientError]
    FileSystemNotFound: Type[Boto3ClientError]
    IncorrectFileSystemLifeCycleState: Type[Boto3ClientError]
    IncorrectMountTargetState: Type[Boto3ClientError]
    InsufficientThroughputCapacity: Type[Boto3ClientError]
    InternalServerError: Type[Boto3ClientError]
    InvalidPolicyException: Type[Boto3ClientError]
    IpAddressInUse: Type[Boto3ClientError]
    MountTargetConflict: Type[Boto3ClientError]
    MountTargetNotFound: Type[Boto3ClientError]
    NetworkInterfaceLimitExceeded: Type[Boto3ClientError]
    NoFreeAddressesInSubnet: Type[Boto3ClientError]
    PolicyNotFound: Type[Boto3ClientError]
    SecurityGroupLimitExceeded: Type[Boto3ClientError]
    SecurityGroupNotFound: Type[Boto3ClientError]
    SubnetNotFound: Type[Boto3ClientError]
    ThroughputLimitExceeded: Type[Boto3ClientError]
    TooManyRequests: Type[Boto3ClientError]
    UnsupportedAvailabilityZone: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]


class EFSClient:
    """
    [EFS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.can_paginate)
        """

    def create_access_point(
        self,
        ClientToken: str,
        FileSystemId: str,
        Tags: List["TagTypeDef"] = None,
        PosixUser: "PosixUserTypeDef" = None,
        RootDirectory: "RootDirectoryTypeDef" = None,
    ) -> "AccessPointDescriptionTypeDef":
        """
        [Client.create_access_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.create_access_point)
        """

    def create_file_system(
        self,
        CreationToken: str,
        PerformanceMode: Literal["generalPurpose", "maxIO"] = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        ThroughputMode: Literal["bursting", "provisioned"] = None,
        ProvisionedThroughputInMibps: float = None,
        Tags: List["TagTypeDef"] = None,
    ) -> "FileSystemDescriptionTypeDef":
        """
        [Client.create_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.create_file_system)
        """

    def create_mount_target(
        self,
        FileSystemId: str,
        SubnetId: str,
        IpAddress: str = None,
        SecurityGroups: List[str] = None,
    ) -> "MountTargetDescriptionTypeDef":
        """
        [Client.create_mount_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.create_mount_target)
        """

    def create_tags(self, FileSystemId: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.create_tags)
        """

    def delete_access_point(self, AccessPointId: str) -> None:
        """
        [Client.delete_access_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.delete_access_point)
        """

    def delete_file_system(self, FileSystemId: str) -> None:
        """
        [Client.delete_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.delete_file_system)
        """

    def delete_file_system_policy(self, FileSystemId: str) -> None:
        """
        [Client.delete_file_system_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.delete_file_system_policy)
        """

    def delete_mount_target(self, MountTargetId: str) -> None:
        """
        [Client.delete_mount_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.delete_mount_target)
        """

    def delete_tags(self, FileSystemId: str, TagKeys: List[str]) -> None:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.delete_tags)
        """

    def describe_access_points(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        AccessPointId: str = None,
        FileSystemId: str = None,
    ) -> DescribeAccessPointsResponseTypeDef:
        """
        [Client.describe_access_points documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.describe_access_points)
        """

    def describe_backup_policy(self, FileSystemId: str) -> BackupPolicyDescriptionTypeDef:
        """
        [Client.describe_backup_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.describe_backup_policy)
        """

    def describe_file_system_policy(self, FileSystemId: str) -> FileSystemPolicyDescriptionTypeDef:
        """
        [Client.describe_file_system_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.describe_file_system_policy)
        """

    def describe_file_systems(
        self,
        MaxItems: int = None,
        Marker: str = None,
        CreationToken: str = None,
        FileSystemId: str = None,
    ) -> DescribeFileSystemsResponseTypeDef:
        """
        [Client.describe_file_systems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.describe_file_systems)
        """

    def describe_lifecycle_configuration(
        self, FileSystemId: str
    ) -> LifecycleConfigurationDescriptionTypeDef:
        """
        [Client.describe_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.describe_lifecycle_configuration)
        """

    def describe_mount_target_security_groups(
        self, MountTargetId: str
    ) -> DescribeMountTargetSecurityGroupsResponseTypeDef:
        """
        [Client.describe_mount_target_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.describe_mount_target_security_groups)
        """

    def describe_mount_targets(
        self,
        MaxItems: int = None,
        Marker: str = None,
        FileSystemId: str = None,
        MountTargetId: str = None,
        AccessPointId: str = None,
    ) -> DescribeMountTargetsResponseTypeDef:
        """
        [Client.describe_mount_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.describe_mount_targets)
        """

    def describe_tags(
        self, FileSystemId: str, MaxItems: int = None, Marker: str = None
    ) -> DescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.describe_tags)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.generate_presigned_url)
        """

    def list_tags_for_resource(
        self, ResourceId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.list_tags_for_resource)
        """

    def modify_mount_target_security_groups(
        self, MountTargetId: str, SecurityGroups: List[str] = None
    ) -> None:
        """
        [Client.modify_mount_target_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.modify_mount_target_security_groups)
        """

    def put_backup_policy(
        self, FileSystemId: str, BackupPolicy: "BackupPolicyTypeDef"
    ) -> BackupPolicyDescriptionTypeDef:
        """
        [Client.put_backup_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.put_backup_policy)
        """

    def put_file_system_policy(
        self, FileSystemId: str, Policy: str, BypassPolicyLockoutSafetyCheck: bool = None
    ) -> FileSystemPolicyDescriptionTypeDef:
        """
        [Client.put_file_system_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.put_file_system_policy)
        """

    def put_lifecycle_configuration(
        self, FileSystemId: str, LifecyclePolicies: List["LifecyclePolicyTypeDef"]
    ) -> LifecycleConfigurationDescriptionTypeDef:
        """
        [Client.put_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.put_lifecycle_configuration)
        """

    def tag_resource(self, ResourceId: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.tag_resource)
        """

    def untag_resource(self, ResourceId: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.untag_resource)
        """

    def update_file_system(
        self,
        FileSystemId: str,
        ThroughputMode: Literal["bursting", "provisioned"] = None,
        ProvisionedThroughputInMibps: float = None,
    ) -> "FileSystemDescriptionTypeDef":
        """
        [Client.update_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Client.update_file_system)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_file_systems"]
    ) -> DescribeFileSystemsPaginator:
        """
        [Paginator.DescribeFileSystems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Paginator.DescribeFileSystems)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_mount_targets"]
    ) -> DescribeMountTargetsPaginator:
        """
        [Paginator.DescribeMountTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Paginator.DescribeMountTargets)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_tags"]) -> DescribeTagsPaginator:
        """
        [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.38/reference/services/efs.html#EFS.Paginator.DescribeTags)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
