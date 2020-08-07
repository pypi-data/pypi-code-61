# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import _utilities, _tables


class ComputeClusterVmDependencyRule(pulumi.CustomResource):
    compute_cluster_id: pulumi.Output[str]
    """
    The managed object reference
    ID of the cluster to put the group in.  Forces a new
    resource if changed.
    """
    dependency_vm_group_name: pulumi.Output[str]
    """
    The name of the VM group that this
    rule depends on. The VMs defined in the group specified by
    `vm_group_name` will not be started until the VMs in this
    group are started.
    """
    enabled: pulumi.Output[bool]
    """
    Enable this rule in the cluster. Default: `true`.
    """
    mandatory: pulumi.Output[bool]
    """
    When this value is `true`, prevents any virtual
    machine operations that may violate this rule. Default: `false`.
    """
    name: pulumi.Output[str]
    """
    The name of the rule. This must be unique in the
    cluster.
    """
    vm_group_name: pulumi.Output[str]
    """
    The name of the VM group that is the subject of
    this rule. The VMs defined in this group will not be started until the VMs in
    the group specified by
    `dependency_vm_group_name` are started.
    """
    def __init__(__self__, resource_name, opts=None, compute_cluster_id=None, dependency_vm_group_name=None, enabled=None, mandatory=None, name=None, vm_group_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a ComputeClusterVmDependencyRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[str] dependency_vm_group_name: The name of the VM group that this
               rule depends on. The VMs defined in the group specified by
               `vm_group_name` will not be started until the VMs in this
               group are started.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the
               cluster.
        :param pulumi.Input[str] vm_group_name: The name of the VM group that is the subject of
               this rule. The VMs defined in this group will not be started until the VMs in
               the group specified by
               `dependency_vm_group_name` are started.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if compute_cluster_id is None:
                raise TypeError("Missing required property 'compute_cluster_id'")
            __props__['compute_cluster_id'] = compute_cluster_id
            if dependency_vm_group_name is None:
                raise TypeError("Missing required property 'dependency_vm_group_name'")
            __props__['dependency_vm_group_name'] = dependency_vm_group_name
            __props__['enabled'] = enabled
            __props__['mandatory'] = mandatory
            __props__['name'] = name
            if vm_group_name is None:
                raise TypeError("Missing required property 'vm_group_name'")
            __props__['vm_group_name'] = vm_group_name
        super(ComputeClusterVmDependencyRule, __self__).__init__(
            'vsphere:index/computeClusterVmDependencyRule:ComputeClusterVmDependencyRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, compute_cluster_id=None, dependency_vm_group_name=None, enabled=None, mandatory=None, name=None, vm_group_name=None):
        """
        Get an existing ComputeClusterVmDependencyRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[str] dependency_vm_group_name: The name of the VM group that this
               rule depends on. The VMs defined in the group specified by
               `vm_group_name` will not be started until the VMs in this
               group are started.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the
               cluster.
        :param pulumi.Input[str] vm_group_name: The name of the VM group that is the subject of
               this rule. The VMs defined in this group will not be started until the VMs in
               the group specified by
               `dependency_vm_group_name` are started.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["compute_cluster_id"] = compute_cluster_id
        __props__["dependency_vm_group_name"] = dependency_vm_group_name
        __props__["enabled"] = enabled
        __props__["mandatory"] = mandatory
        __props__["name"] = name
        __props__["vm_group_name"] = vm_group_name
        return ComputeClusterVmDependencyRule(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
