# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import _utilities, _tables


class DrsVmOverride(pulumi.CustomResource):
    compute_cluster_id: pulumi.Output[str]
    """
    The managed object reference
    ID of the cluster to put the override in.  Forces a new
    resource if changed.
    """
    drs_automation_level: pulumi.Output[str]
    """
    Overrides the automation level for this virtual
    machine in the cluster. Can be one of `manual`, `partiallyAutomated`, or
    `fullyAutomated`. Default: `manual`.
    """
    drs_enabled: pulumi.Output[bool]
    """
    Overrides the default DRS setting for this virtual
    machine. Can be either `true` or `false`. Default: `false`.
    """
    virtual_machine_id: pulumi.Output[str]
    """
    The UUID of the virtual machine to create
    the override for.  Forces a new resource if changed.
    """
    def __init__(__self__, resource_name, opts=None, compute_cluster_id=None, drs_automation_level=None, drs_enabled=None, virtual_machine_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a DrsVmOverride resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the override in.  Forces a new
               resource if changed.
        :param pulumi.Input[str] drs_automation_level: Overrides the automation level for this virtual
               machine in the cluster. Can be one of `manual`, `partiallyAutomated`, or
               `fullyAutomated`. Default: `manual`.
        :param pulumi.Input[bool] drs_enabled: Overrides the default DRS setting for this virtual
               machine. Can be either `true` or `false`. Default: `false`.
        :param pulumi.Input[str] virtual_machine_id: The UUID of the virtual machine to create
               the override for.  Forces a new resource if changed.
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
            __props__['drs_automation_level'] = drs_automation_level
            __props__['drs_enabled'] = drs_enabled
            if virtual_machine_id is None:
                raise TypeError("Missing required property 'virtual_machine_id'")
            __props__['virtual_machine_id'] = virtual_machine_id
        super(DrsVmOverride, __self__).__init__(
            'vsphere:index/drsVmOverride:DrsVmOverride',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, compute_cluster_id=None, drs_automation_level=None, drs_enabled=None, virtual_machine_id=None):
        """
        Get an existing DrsVmOverride resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the override in.  Forces a new
               resource if changed.
        :param pulumi.Input[str] drs_automation_level: Overrides the automation level for this virtual
               machine in the cluster. Can be one of `manual`, `partiallyAutomated`, or
               `fullyAutomated`. Default: `manual`.
        :param pulumi.Input[bool] drs_enabled: Overrides the default DRS setting for this virtual
               machine. Can be either `true` or `false`. Default: `false`.
        :param pulumi.Input[str] virtual_machine_id: The UUID of the virtual machine to create
               the override for.  Forces a new resource if changed.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["compute_cluster_id"] = compute_cluster_id
        __props__["drs_automation_level"] = drs_automation_level
        __props__["drs_enabled"] = drs_enabled
        __props__["virtual_machine_id"] = virtual_machine_id
        return DrsVmOverride(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
