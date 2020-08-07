import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from .._jsii import *

from .. import (
    Construct as _Construct_f50a3f53,
    IResolvable as _IResolvable_9ceae33e,
    CfnResource as _CfnResource_7760e8e4,
    FromCloudFormationOptions as _FromCloudFormationOptions_5f49f6f1,
    ICfnFinder as _ICfnFinder_3b168f30,
    TreeInspector as _TreeInspector_154f5999,
    IInspectable as _IInspectable_051e6ed8,
    CfnTag as _CfnTag_b4661f1a,
    TagManager as _TagManager_2508893f,
)
from ..aws_cognito import IUserPool as _IUserPool_e9547b0f
from ..aws_dynamodb import ITable as _ITable_e6850701
from ..aws_iam import (
    IPrincipal as _IPrincipal_97126874,
    IGrantable as _IGrantable_0fcfc53a,
    IRole as _IRole_e69bbae4,
    Grant as _Grant_96af6d2d,
)
from ..aws_lambda import IFunction as _IFunction_1c1de0bc


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.ApiKeyConfig",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "expires": "expires", "name": "name"},
)
class ApiKeyConfig:
    def __init__(
        self,
        *,
        description: typing.Optional[str] = None,
        expires: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
    ) -> None:
        """Configuration for API Key authorization in AppSync.

        :param description: Description of API key. Default: - 'Default API Key created by CDK'
        :param expires: The time from creation time after which the API key expires, using RFC3339 representation. It must be a minimum of 1 day and a maximum of 365 days from date of creation. Rounded down to the nearest hour. Default: - 7 days from creation time
        :param name: Unique name of the API Key. Default: - 'DefaultAPIKey'

        stability
        :stability: experimental
        """
        self._values = {}
        if description is not None:
            self._values["description"] = description
        if expires is not None:
            self._values["expires"] = expires
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """Description of API key.

        default
        :default: - 'Default API Key created by CDK'

        stability
        :stability: experimental
        """
        return self._values.get("description")

    @builtins.property
    def expires(self) -> typing.Optional[str]:
        """The time from creation time after which the API key expires, using RFC3339 representation.

        It must be a minimum of 1 day and a maximum of 365 days from date of creation.
        Rounded down to the nearest hour.

        default
        :default: - 7 days from creation time

        stability
        :stability: experimental
        """
        return self._values.get("expires")

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """Unique name of the API Key.

        default
        :default: - 'DefaultAPIKey'

        stability
        :stability: experimental
        """
        return self._values.get("name")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiKeyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Assign(
    metaclass=jsii.JSIIMeta, jsii_type="monocdk-experiment.aws_appsync.Assign"
):
    """Utility class representing the assigment of a value to an attribute.

    stability
    :stability: experimental
    """

    def __init__(self, attr: str, arg: str) -> None:
        """
        :param attr: -
        :param arg: -

        stability
        :stability: experimental
        """
        jsii.create(Assign, self, [attr, arg])

    @jsii.member(jsii_name="putInMap")
    def put_in_map(self, map: str) -> str:
        """Renders the assignment as a map element.

        :param map: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "putInMap", [map])

    @jsii.member(jsii_name="renderAsAssignment")
    def render_as_assignment(self) -> str:
        """Renders the assignment as a VTL string.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderAsAssignment", [])


class AttributeValues(
    metaclass=jsii.JSIIMeta, jsii_type="monocdk-experiment.aws_appsync.AttributeValues"
):
    """Specifies the attribute value assignments.

    stability
    :stability: experimental
    """

    def __init__(
        self, container: str, assignments: typing.Optional[typing.List["Assign"]] = None
    ) -> None:
        """
        :param container: -
        :param assignments: -

        stability
        :stability: experimental
        """
        jsii.create(AttributeValues, self, [container, assignments])

    @jsii.member(jsii_name="attribute")
    def attribute(self, attr: str) -> "AttributeValuesStep":
        """Allows assigning a value to the specified attribute.

        :param attr: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "attribute", [attr])

    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> str:
        """Renders the attribute value assingments to a VTL string.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderTemplate", [])

    @jsii.member(jsii_name="renderVariables")
    def render_variables(self) -> str:
        """Renders the variables required for ``renderTemplate``.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderVariables", [])


class AttributeValuesStep(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.AttributeValuesStep",
):
    """Utility class to allow assigning a value to an attribute.

    stability
    :stability: experimental
    """

    def __init__(
        self, attr: str, container: str, assignments: typing.List["Assign"]
    ) -> None:
        """
        :param attr: -
        :param container: -
        :param assignments: -

        stability
        :stability: experimental
        """
        jsii.create(AttributeValuesStep, self, [attr, container, assignments])

    @jsii.member(jsii_name="is")
    def is_(self, val: str) -> "AttributeValues":
        """Assign the value to the current attribute.

        :param val: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "is", [val])


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.AuthorizationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "additional_authorization_modes": "additionalAuthorizationModes",
        "default_authorization": "defaultAuthorization",
    },
)
class AuthorizationConfig:
    def __init__(
        self,
        *,
        additional_authorization_modes: typing.Optional[
            typing.List["AuthorizationMode"]
        ] = None,
        default_authorization: typing.Optional["AuthorizationMode"] = None,
    ) -> None:
        """Configuration of the API authorization modes.

        :param additional_authorization_modes: Additional authorization modes. Default: - No other modes
        :param default_authorization: Optional authorization configuration. Default: - API Key authorization

        stability
        :stability: experimental
        """
        if isinstance(default_authorization, dict):
            default_authorization = AuthorizationMode(**default_authorization)
        self._values = {}
        if additional_authorization_modes is not None:
            self._values[
                "additional_authorization_modes"
            ] = additional_authorization_modes
        if default_authorization is not None:
            self._values["default_authorization"] = default_authorization

    @builtins.property
    def additional_authorization_modes(
        self,
    ) -> typing.Optional[typing.List["AuthorizationMode"]]:
        """Additional authorization modes.

        default
        :default: - No other modes

        stability
        :stability: experimental
        """
        return self._values.get("additional_authorization_modes")

    @builtins.property
    def default_authorization(self) -> typing.Optional["AuthorizationMode"]:
        """Optional authorization configuration.

        default
        :default: - API Key authorization

        stability
        :stability: experimental
        """
        return self._values.get("default_authorization")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.AuthorizationMode",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_type": "authorizationType",
        "api_key_config": "apiKeyConfig",
        "open_id_connect_config": "openIdConnectConfig",
        "user_pool_config": "userPoolConfig",
    },
)
class AuthorizationMode:
    def __init__(
        self,
        *,
        authorization_type: "AuthorizationType",
        api_key_config: typing.Optional["ApiKeyConfig"] = None,
        open_id_connect_config: typing.Optional["OpenIdConnectConfig"] = None,
        user_pool_config: typing.Optional["UserPoolConfig"] = None,
    ) -> None:
        """Interface to specify default or additional authorization(s).

        :param authorization_type: One of possible four values AppSync supports. Default: - ``AuthorizationType.API_KEY``
        :param api_key_config: If authorizationType is ``AuthorizationType.API_KEY``, this option can be configured. Default: - name: 'DefaultAPIKey' | description: 'Default API Key created by CDK'
        :param open_id_connect_config: If authorizationType is ``AuthorizationType.OIDC``, this option is required. Default: - none
        :param user_pool_config: If authorizationType is ``AuthorizationType.USER_POOL``, this option is required. Default: - none

        stability
        :stability: experimental
        """
        if isinstance(api_key_config, dict):
            api_key_config = ApiKeyConfig(**api_key_config)
        if isinstance(open_id_connect_config, dict):
            open_id_connect_config = OpenIdConnectConfig(**open_id_connect_config)
        if isinstance(user_pool_config, dict):
            user_pool_config = UserPoolConfig(**user_pool_config)
        self._values = {
            "authorization_type": authorization_type,
        }
        if api_key_config is not None:
            self._values["api_key_config"] = api_key_config
        if open_id_connect_config is not None:
            self._values["open_id_connect_config"] = open_id_connect_config
        if user_pool_config is not None:
            self._values["user_pool_config"] = user_pool_config

    @builtins.property
    def authorization_type(self) -> "AuthorizationType":
        """One of possible four values AppSync supports.

        default
        :default: - ``AuthorizationType.API_KEY``

        see
        :see: https://docs.aws.amazon.com/appsync/latest/devguide/security.html
        stability
        :stability: experimental
        """
        return self._values.get("authorization_type")

    @builtins.property
    def api_key_config(self) -> typing.Optional["ApiKeyConfig"]:
        """If authorizationType is ``AuthorizationType.API_KEY``, this option can be configured.

        default
        :default: - name: 'DefaultAPIKey' | description: 'Default API Key created by CDK'

        stability
        :stability: experimental
        """
        return self._values.get("api_key_config")

    @builtins.property
    def open_id_connect_config(self) -> typing.Optional["OpenIdConnectConfig"]:
        """If authorizationType is ``AuthorizationType.OIDC``, this option is required.

        default
        :default: - none

        stability
        :stability: experimental
        """
        return self._values.get("open_id_connect_config")

    @builtins.property
    def user_pool_config(self) -> typing.Optional["UserPoolConfig"]:
        """If authorizationType is ``AuthorizationType.USER_POOL``, this option is required.

        default
        :default: - none

        stability
        :stability: experimental
        """
        return self._values.get("user_pool_config")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationMode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk-experiment.aws_appsync.AuthorizationType")
class AuthorizationType(enum.Enum):
    """enum with all possible values for AppSync authorization type.

    stability
    :stability: experimental
    """

    API_KEY = "API_KEY"
    """API Key authorization type.

    stability
    :stability: experimental
    """
    IAM = "IAM"
    """AWS IAM authorization type.

    Can be used with Cognito Identity Pool federated credentials

    stability
    :stability: experimental
    """
    USER_POOL = "USER_POOL"
    """Cognito User Pool authorization type.

    stability
    :stability: experimental
    """
    OIDC = "OIDC"
    """OpenID Connect authorization type.

    stability
    :stability: experimental
    """


class BaseDataSource(
    _Construct_f50a3f53,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk-experiment.aws_appsync.BaseDataSource",
):
    """Abstract AppSync datasource implementation.

    Do not use directly but use subclasses for concrete datasources

    stability
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _BaseDataSourceProxy

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        props: "BackedDataSourceProps",
        *,
        type: str,
        dynamo_db_config: typing.Optional[
            typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        elasticsearch_config: typing.Optional[
            typing.Union[
                "CfnDataSource.ElasticsearchConfigProperty", _IResolvable_9ceae33e
            ]
        ] = None,
        http_config: typing.Optional[
            typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        lambda_config: typing.Optional[
            typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        relational_database_config: typing.Optional[
            typing.Union[
                "CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_9ceae33e
            ]
        ] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param type: the type of the AppSync datasource.
        :param dynamo_db_config: configuration for DynamoDB Datasource. Default: - No config
        :param elasticsearch_config: configuration for Elasticsearch Datasource. Default: - No config
        :param http_config: configuration for HTTP Datasource. Default: - No config
        :param lambda_config: configuration for Lambda Datasource. Default: - No config
        :param relational_database_config: configuration for RDS Datasource. Default: - No config

        stability
        :stability: experimental
        """
        extended = ExtendedDataSourceProps(
            type=type,
            dynamo_db_config=dynamo_db_config,
            elasticsearch_config=elasticsearch_config,
            http_config=http_config,
            lambda_config=lambda_config,
            relational_database_config=relational_database_config,
        )

        jsii.create(BaseDataSource, self, [scope, id, props, extended])

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        *,
        field_name: str,
        type_name: str,
        pipeline_config: typing.Optional[typing.List[str]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> "Resolver":
        """creates a new resolver for this datasource and API using the given properties.

        :param field_name: name of the GraphQL fiel din the given type this resolver is attached to.
        :param type_name: name of the GraphQL type this resolver is attached to.
        :param pipeline_config: configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: The response mapping template for this resolver. Default: - No mapping template

        stability
        :stability: experimental
        """
        props = BaseResolverProps(
            field_name=field_name,
            type_name=type_name,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        return jsii.invoke(self, "createResolver", [props])

    @builtins.property
    @jsii.member(jsii_name="ds")
    def ds(self) -> "CfnDataSource":
        """the underlying CFN data source resource.

        stability
        :stability: experimental
        """
        return jsii.get(self, "ds")

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """the name of the data source.

        stability
        :stability: experimental
        """
        return jsii.get(self, "name")

    @builtins.property
    @jsii.member(jsii_name="api")
    def _api(self) -> "GraphQLApi":
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "api")

    @_api.setter
    def _api(self, value: "GraphQLApi") -> None:
        jsii.set(self, "api", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def _service_role(self) -> typing.Optional[_IRole_e69bbae4]:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "serviceRole")

    @_service_role.setter
    def _service_role(self, value: typing.Optional[_IRole_e69bbae4]) -> None:
        jsii.set(self, "serviceRole", value)


class _BaseDataSourceProxy(BaseDataSource):
    pass


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.BaseDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={"api": "api", "name": "name", "description": "description"},
)
class BaseDataSourceProps:
    def __init__(
        self, *, api: "GraphQLApi", name: str, description: typing.Optional[str] = None
    ) -> None:
        """Base properties for an AppSync datasource.

        :param api: The API to attach this data source to.
        :param name: The name of the data source.
        :param description: the description of the data source. Default: - None

        stability
        :stability: experimental
        """
        self._values = {
            "api": api,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def api(self) -> "GraphQLApi":
        """The API to attach this data source to.

        stability
        :stability: experimental
        """
        return self._values.get("api")

    @builtins.property
    def name(self) -> str:
        """The name of the data source.

        stability
        :stability: experimental
        """
        return self._values.get("name")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """the description of the data source.

        default
        :default: - None

        stability
        :stability: experimental
        """
        return self._values.get("description")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.BaseResolverProps",
    jsii_struct_bases=[],
    name_mapping={
        "field_name": "fieldName",
        "type_name": "typeName",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
    },
)
class BaseResolverProps:
    def __init__(
        self,
        *,
        field_name: str,
        type_name: str,
        pipeline_config: typing.Optional[typing.List[str]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> None:
        """Basic properties for an AppSync resolver.

        :param field_name: name of the GraphQL fiel din the given type this resolver is attached to.
        :param type_name: name of the GraphQL type this resolver is attached to.
        :param pipeline_config: configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: The response mapping template for this resolver. Default: - No mapping template

        stability
        :stability: experimental
        """
        self._values = {
            "field_name": field_name,
            "type_name": type_name,
        }
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template

    @builtins.property
    def field_name(self) -> str:
        """name of the GraphQL fiel din the given type this resolver is attached to.

        stability
        :stability: experimental
        """
        return self._values.get("field_name")

    @builtins.property
    def type_name(self) -> str:
        """name of the GraphQL type this resolver is attached to.

        stability
        :stability: experimental
        """
        return self._values.get("type_name")

    @builtins.property
    def pipeline_config(self) -> typing.Optional[typing.List[str]]:
        """configuration of the pipeline resolver.

        default
        :default:

        - no pipeline resolver configuration
          An empty array | undefined sets resolver to be of kind, unit

        stability
        :stability: experimental
        """
        return self._values.get("pipeline_config")

    @builtins.property
    def request_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        """The request mapping template for this resolver.

        default
        :default: - No mapping template

        stability
        :stability: experimental
        """
        return self._values.get("request_mapping_template")

    @builtins.property
    def response_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        """The response mapping template for this resolver.

        default
        :default: - No mapping template

        stability
        :stability: experimental
        """
        return self._values.get("response_mapping_template")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_051e6ed8)
class CfnApiCache(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.CfnApiCache",
):
    """A CloudFormation ``AWS::AppSync::ApiCache``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html
    cloudformationResource:
    :cloudformationResource:: AWS::AppSync::ApiCache
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        api_caching_behavior: str,
        api_id: str,
        ttl: jsii.Number,
        type: str,
        at_rest_encryption_enabled: typing.Optional[
            typing.Union[bool, _IResolvable_9ceae33e]
        ] = None,
        transit_encryption_enabled: typing.Optional[
            typing.Union[bool, _IResolvable_9ceae33e]
        ] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::ApiCache``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_caching_behavior: ``AWS::AppSync::ApiCache.ApiCachingBehavior``.
        :param api_id: ``AWS::AppSync::ApiCache.ApiId``.
        :param ttl: ``AWS::AppSync::ApiCache.Ttl``.
        :param type: ``AWS::AppSync::ApiCache.Type``.
        :param at_rest_encryption_enabled: ``AWS::AppSync::ApiCache.AtRestEncryptionEnabled``.
        :param transit_encryption_enabled: ``AWS::AppSync::ApiCache.TransitEncryptionEnabled``.
        """
        props = CfnApiCacheProps(
            api_caching_behavior=api_caching_behavior,
            api_id=api_id,
            ttl=ttl,
            type=type,
            at_rest_encryption_enabled=at_rest_encryption_enabled,
            transit_encryption_enabled=transit_encryption_enabled,
        )

        jsii.create(CfnApiCache, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnApiCache":
        """A factory method that creates a new instance of this class from an object containing the CloudFormation properties of this resource.

        Used in the @aws-cdk/cloudformation-include module.

        :param scope: -
        :param id: -
        :param resource_attributes: -
        :param finder: The finder interface used to resolve references across the template.

        stability
        :stability: experimental
        """
        options = _FromCloudFormationOptions_5f49f6f1(finder=finder)

        return jsii.sinvoke(
            cls, "fromCloudFormation", [scope, id, resource_attributes, options]
        )

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_154f5999) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self, props: typing.Mapping[str, typing.Any]
    ) -> typing.Mapping[str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiCachingBehavior")
    def api_caching_behavior(self) -> str:
        """``AWS::AppSync::ApiCache.ApiCachingBehavior``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apicachingbehavior
        """
        return jsii.get(self, "apiCachingBehavior")

    @api_caching_behavior.setter
    def api_caching_behavior(self, value: str) -> None:
        jsii.set(self, "apiCachingBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::AppSync::ApiCache.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str) -> None:
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        """``AWS::AppSync::ApiCache.Ttl``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-ttl
        """
        return jsii.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> str:
        """``AWS::AppSync::ApiCache.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-type
        """
        return jsii.get(self, "type")

    @type.setter
    def type(self, value: str) -> None:
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
        """``AWS::AppSync::ApiCache.AtRestEncryptionEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-atrestencryptionenabled
        """
        return jsii.get(self, "atRestEncryptionEnabled")

    @at_rest_encryption_enabled.setter
    def at_rest_encryption_enabled(
        self, value: typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]
    ) -> None:
        jsii.set(self, "atRestEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionEnabled")
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
        """``AWS::AppSync::ApiCache.TransitEncryptionEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-transitencryptionenabled
        """
        return jsii.get(self, "transitEncryptionEnabled")

    @transit_encryption_enabled.setter
    def transit_encryption_enabled(
        self, value: typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]
    ) -> None:
        jsii.set(self, "transitEncryptionEnabled", value)


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.CfnApiCacheProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_caching_behavior": "apiCachingBehavior",
        "api_id": "apiId",
        "ttl": "ttl",
        "type": "type",
        "at_rest_encryption_enabled": "atRestEncryptionEnabled",
        "transit_encryption_enabled": "transitEncryptionEnabled",
    },
)
class CfnApiCacheProps:
    def __init__(
        self,
        *,
        api_caching_behavior: str,
        api_id: str,
        ttl: jsii.Number,
        type: str,
        at_rest_encryption_enabled: typing.Optional[
            typing.Union[bool, _IResolvable_9ceae33e]
        ] = None,
        transit_encryption_enabled: typing.Optional[
            typing.Union[bool, _IResolvable_9ceae33e]
        ] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::ApiCache``.

        :param api_caching_behavior: ``AWS::AppSync::ApiCache.ApiCachingBehavior``.
        :param api_id: ``AWS::AppSync::ApiCache.ApiId``.
        :param ttl: ``AWS::AppSync::ApiCache.Ttl``.
        :param type: ``AWS::AppSync::ApiCache.Type``.
        :param at_rest_encryption_enabled: ``AWS::AppSync::ApiCache.AtRestEncryptionEnabled``.
        :param transit_encryption_enabled: ``AWS::AppSync::ApiCache.TransitEncryptionEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html
        """
        self._values = {
            "api_caching_behavior": api_caching_behavior,
            "api_id": api_id,
            "ttl": ttl,
            "type": type,
        }
        if at_rest_encryption_enabled is not None:
            self._values["at_rest_encryption_enabled"] = at_rest_encryption_enabled
        if transit_encryption_enabled is not None:
            self._values["transit_encryption_enabled"] = transit_encryption_enabled

    @builtins.property
    def api_caching_behavior(self) -> str:
        """``AWS::AppSync::ApiCache.ApiCachingBehavior``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apicachingbehavior
        """
        return self._values.get("api_caching_behavior")

    @builtins.property
    def api_id(self) -> str:
        """``AWS::AppSync::ApiCache.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apiid
        """
        return self._values.get("api_id")

    @builtins.property
    def ttl(self) -> jsii.Number:
        """``AWS::AppSync::ApiCache.Ttl``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-ttl
        """
        return self._values.get("ttl")

    @builtins.property
    def type(self) -> str:
        """``AWS::AppSync::ApiCache.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-type
        """
        return self._values.get("type")

    @builtins.property
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
        """``AWS::AppSync::ApiCache.AtRestEncryptionEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-atrestencryptionenabled
        """
        return self._values.get("at_rest_encryption_enabled")

    @builtins.property
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
        """``AWS::AppSync::ApiCache.TransitEncryptionEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-transitencryptionenabled
        """
        return self._values.get("transit_encryption_enabled")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiCacheProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_051e6ed8)
class CfnApiKey(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.CfnApiKey",
):
    """A CloudFormation ``AWS::AppSync::ApiKey``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html
    cloudformationResource:
    :cloudformationResource:: AWS::AppSync::ApiKey
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        api_id: str,
        description: typing.Optional[str] = None,
        expires: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::ApiKey``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::AppSync::ApiKey.ApiId``.
        :param description: ``AWS::AppSync::ApiKey.Description``.
        :param expires: ``AWS::AppSync::ApiKey.Expires``.
        """
        props = CfnApiKeyProps(api_id=api_id, description=description, expires=expires)

        jsii.create(CfnApiKey, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnApiKey":
        """A factory method that creates a new instance of this class from an object containing the CloudFormation properties of this resource.

        Used in the @aws-cdk/cloudformation-include module.

        :param scope: -
        :param id: -
        :param resource_attributes: -
        :param finder: The finder interface used to resolve references across the template.

        stability
        :stability: experimental
        """
        options = _FromCloudFormationOptions_5f49f6f1(finder=finder)

        return jsii.sinvoke(
            cls, "fromCloudFormation", [scope, id, resource_attributes, options]
        )

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_154f5999) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self, props: typing.Mapping[str, typing.Any]
    ) -> typing.Mapping[str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="attrApiKey")
    def attr_api_key(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ApiKey
        """
        return jsii.get(self, "attrApiKey")

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Arn
        """
        return jsii.get(self, "attrArn")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::AppSync::ApiKey.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str) -> None:
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::AppSync::ApiKey.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expires")
    def expires(self) -> typing.Optional[jsii.Number]:
        """``AWS::AppSync::ApiKey.Expires``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-expires
        """
        return jsii.get(self, "expires")

    @expires.setter
    def expires(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "expires", value)


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.CfnApiKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "description": "description",
        "expires": "expires",
    },
)
class CfnApiKeyProps:
    def __init__(
        self,
        *,
        api_id: str,
        description: typing.Optional[str] = None,
        expires: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::ApiKey``.

        :param api_id: ``AWS::AppSync::ApiKey.ApiId``.
        :param description: ``AWS::AppSync::ApiKey.Description``.
        :param expires: ``AWS::AppSync::ApiKey.Expires``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html
        """
        self._values = {
            "api_id": api_id,
        }
        if description is not None:
            self._values["description"] = description
        if expires is not None:
            self._values["expires"] = expires

    @builtins.property
    def api_id(self) -> str:
        """``AWS::AppSync::ApiKey.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apiid
        """
        return self._values.get("api_id")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::AppSync::ApiKey.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-description
        """
        return self._values.get("description")

    @builtins.property
    def expires(self) -> typing.Optional[jsii.Number]:
        """``AWS::AppSync::ApiKey.Expires``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-expires
        """
        return self._values.get("expires")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_051e6ed8)
class CfnDataSource(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.CfnDataSource",
):
    """A CloudFormation ``AWS::AppSync::DataSource``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html
    cloudformationResource:
    :cloudformationResource:: AWS::AppSync::DataSource
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        api_id: str,
        name: str,
        type: str,
        description: typing.Optional[str] = None,
        dynamo_db_config: typing.Optional[
            typing.Union["DynamoDBConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        elasticsearch_config: typing.Optional[
            typing.Union["ElasticsearchConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        http_config: typing.Optional[
            typing.Union["HttpConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        lambda_config: typing.Optional[
            typing.Union["LambdaConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        relational_database_config: typing.Optional[
            typing.Union["RelationalDatabaseConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        service_role_arn: typing.Optional[str] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::DataSource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::AppSync::DataSource.ApiId``.
        :param name: ``AWS::AppSync::DataSource.Name``.
        :param type: ``AWS::AppSync::DataSource.Type``.
        :param description: ``AWS::AppSync::DataSource.Description``.
        :param dynamo_db_config: ``AWS::AppSync::DataSource.DynamoDBConfig``.
        :param elasticsearch_config: ``AWS::AppSync::DataSource.ElasticsearchConfig``.
        :param http_config: ``AWS::AppSync::DataSource.HttpConfig``.
        :param lambda_config: ``AWS::AppSync::DataSource.LambdaConfig``.
        :param relational_database_config: ``AWS::AppSync::DataSource.RelationalDatabaseConfig``.
        :param service_role_arn: ``AWS::AppSync::DataSource.ServiceRoleArn``.
        """
        props = CfnDataSourceProps(
            api_id=api_id,
            name=name,
            type=type,
            description=description,
            dynamo_db_config=dynamo_db_config,
            elasticsearch_config=elasticsearch_config,
            http_config=http_config,
            lambda_config=lambda_config,
            relational_database_config=relational_database_config,
            service_role_arn=service_role_arn,
        )

        jsii.create(CfnDataSource, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnDataSource":
        """A factory method that creates a new instance of this class from an object containing the CloudFormation properties of this resource.

        Used in the @aws-cdk/cloudformation-include module.

        :param scope: -
        :param id: -
        :param resource_attributes: -
        :param finder: The finder interface used to resolve references across the template.

        stability
        :stability: experimental
        """
        options = _FromCloudFormationOptions_5f49f6f1(finder=finder)

        return jsii.sinvoke(
            cls, "fromCloudFormation", [scope, id, resource_attributes, options]
        )

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_154f5999) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self, props: typing.Mapping[str, typing.Any]
    ) -> typing.Mapping[str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="attrDataSourceArn")
    def attr_data_source_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DataSourceArn
        """
        return jsii.get(self, "attrDataSourceArn")

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::AppSync::DataSource.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str) -> None:
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::AppSync::DataSource.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str) -> None:
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> str:
        """``AWS::AppSync::DataSource.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-type
        """
        return jsii.get(self, "type")

    @type.setter
    def type(self, value: str) -> None:
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::AppSync::DataSource.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="dynamoDbConfig")
    def dynamo_db_config(
        self,
    ) -> typing.Optional[typing.Union["DynamoDBConfigProperty", _IResolvable_9ceae33e]]:
        """``AWS::AppSync::DataSource.DynamoDBConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-dynamodbconfig
        """
        return jsii.get(self, "dynamoDbConfig")

    @dynamo_db_config.setter
    def dynamo_db_config(
        self,
        value: typing.Optional[
            typing.Union["DynamoDBConfigProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "dynamoDbConfig", value)

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfig")
    def elasticsearch_config(
        self,
    ) -> typing.Optional[
        typing.Union["ElasticsearchConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::DataSource.ElasticsearchConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-elasticsearchconfig
        """
        return jsii.get(self, "elasticsearchConfig")

    @elasticsearch_config.setter
    def elasticsearch_config(
        self,
        value: typing.Optional[
            typing.Union["ElasticsearchConfigProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "elasticsearchConfig", value)

    @builtins.property
    @jsii.member(jsii_name="httpConfig")
    def http_config(
        self,
    ) -> typing.Optional[typing.Union["HttpConfigProperty", _IResolvable_9ceae33e]]:
        """``AWS::AppSync::DataSource.HttpConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-httpconfig
        """
        return jsii.get(self, "httpConfig")

    @http_config.setter
    def http_config(
        self,
        value: typing.Optional[
            typing.Union["HttpConfigProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "httpConfig", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaConfig")
    def lambda_config(
        self,
    ) -> typing.Optional[typing.Union["LambdaConfigProperty", _IResolvable_9ceae33e]]:
        """``AWS::AppSync::DataSource.LambdaConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-lambdaconfig
        """
        return jsii.get(self, "lambdaConfig")

    @lambda_config.setter
    def lambda_config(
        self,
        value: typing.Optional[
            typing.Union["LambdaConfigProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "lambdaConfig", value)

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseConfig")
    def relational_database_config(
        self,
    ) -> typing.Optional[
        typing.Union["RelationalDatabaseConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::DataSource.RelationalDatabaseConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-relationaldatabaseconfig
        """
        return jsii.get(self, "relationalDatabaseConfig")

    @relational_database_config.setter
    def relational_database_config(
        self,
        value: typing.Optional[
            typing.Union["RelationalDatabaseConfigProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "relationalDatabaseConfig", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> typing.Optional[str]:
        """``AWS::AppSync::DataSource.ServiceRoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-servicerolearn
        """
        return jsii.get(self, "serviceRoleArn")

    @service_role_arn.setter
    def service_role_arn(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "serviceRoleArn", value)

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnDataSource.AuthorizationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_type": "authorizationType",
            "aws_iam_config": "awsIamConfig",
        },
    )
    class AuthorizationConfigProperty:
        def __init__(
            self,
            *,
            authorization_type: str,
            aws_iam_config: typing.Optional[
                typing.Union[
                    "CfnDataSource.AwsIamConfigProperty", _IResolvable_9ceae33e
                ]
            ] = None,
        ) -> None:
            """
            :param authorization_type: ``CfnDataSource.AuthorizationConfigProperty.AuthorizationType``.
            :param aws_iam_config: ``CfnDataSource.AuthorizationConfigProperty.AwsIamConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html
            """
            self._values = {
                "authorization_type": authorization_type,
            }
            if aws_iam_config is not None:
                self._values["aws_iam_config"] = aws_iam_config

        @builtins.property
        def authorization_type(self) -> str:
            """``CfnDataSource.AuthorizationConfigProperty.AuthorizationType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html#cfn-appsync-datasource-authorizationconfig-authorizationtype
            """
            return self._values.get("authorization_type")

        @builtins.property
        def aws_iam_config(
            self,
        ) -> typing.Optional[
            typing.Union["CfnDataSource.AwsIamConfigProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnDataSource.AuthorizationConfigProperty.AwsIamConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html#cfn-appsync-datasource-authorizationconfig-awsiamconfig
            """
            return self._values.get("aws_iam_config")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnDataSource.AwsIamConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "signing_region": "signingRegion",
            "signing_service_name": "signingServiceName",
        },
    )
    class AwsIamConfigProperty:
        def __init__(
            self,
            *,
            signing_region: typing.Optional[str] = None,
            signing_service_name: typing.Optional[str] = None,
        ) -> None:
            """
            :param signing_region: ``CfnDataSource.AwsIamConfigProperty.SigningRegion``.
            :param signing_service_name: ``CfnDataSource.AwsIamConfigProperty.SigningServiceName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html
            """
            self._values = {}
            if signing_region is not None:
                self._values["signing_region"] = signing_region
            if signing_service_name is not None:
                self._values["signing_service_name"] = signing_service_name

        @builtins.property
        def signing_region(self) -> typing.Optional[str]:
            """``CfnDataSource.AwsIamConfigProperty.SigningRegion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html#cfn-appsync-datasource-awsiamconfig-signingregion
            """
            return self._values.get("signing_region")

        @builtins.property
        def signing_service_name(self) -> typing.Optional[str]:
            """``CfnDataSource.AwsIamConfigProperty.SigningServiceName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html#cfn-appsync-datasource-awsiamconfig-signingservicename
            """
            return self._values.get("signing_service_name")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsIamConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnDataSource.DeltaSyncConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "base_table_ttl": "baseTableTtl",
            "delta_sync_table_name": "deltaSyncTableName",
            "delta_sync_table_ttl": "deltaSyncTableTtl",
        },
    )
    class DeltaSyncConfigProperty:
        def __init__(
            self,
            *,
            base_table_ttl: str,
            delta_sync_table_name: str,
            delta_sync_table_ttl: str,
        ) -> None:
            """
            :param base_table_ttl: ``CfnDataSource.DeltaSyncConfigProperty.BaseTableTTL``.
            :param delta_sync_table_name: ``CfnDataSource.DeltaSyncConfigProperty.DeltaSyncTableName``.
            :param delta_sync_table_ttl: ``CfnDataSource.DeltaSyncConfigProperty.DeltaSyncTableTTL``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html
            """
            self._values = {
                "base_table_ttl": base_table_ttl,
                "delta_sync_table_name": delta_sync_table_name,
                "delta_sync_table_ttl": delta_sync_table_ttl,
            }

        @builtins.property
        def base_table_ttl(self) -> str:
            """``CfnDataSource.DeltaSyncConfigProperty.BaseTableTTL``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-basetablettl
            """
            return self._values.get("base_table_ttl")

        @builtins.property
        def delta_sync_table_name(self) -> str:
            """``CfnDataSource.DeltaSyncConfigProperty.DeltaSyncTableName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-deltasynctablename
            """
            return self._values.get("delta_sync_table_name")

        @builtins.property
        def delta_sync_table_ttl(self) -> str:
            """``CfnDataSource.DeltaSyncConfigProperty.DeltaSyncTableTTL``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-deltasynctablettl
            """
            return self._values.get("delta_sync_table_ttl")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeltaSyncConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnDataSource.DynamoDBConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_region": "awsRegion",
            "table_name": "tableName",
            "delta_sync_config": "deltaSyncConfig",
            "use_caller_credentials": "useCallerCredentials",
            "versioned": "versioned",
        },
    )
    class DynamoDBConfigProperty:
        def __init__(
            self,
            *,
            aws_region: str,
            table_name: str,
            delta_sync_config: typing.Optional[
                typing.Union[
                    "CfnDataSource.DeltaSyncConfigProperty", _IResolvable_9ceae33e
                ]
            ] = None,
            use_caller_credentials: typing.Optional[
                typing.Union[bool, _IResolvable_9ceae33e]
            ] = None,
            versioned: typing.Optional[
                typing.Union[bool, _IResolvable_9ceae33e]
            ] = None,
        ) -> None:
            """
            :param aws_region: ``CfnDataSource.DynamoDBConfigProperty.AwsRegion``.
            :param table_name: ``CfnDataSource.DynamoDBConfigProperty.TableName``.
            :param delta_sync_config: ``CfnDataSource.DynamoDBConfigProperty.DeltaSyncConfig``.
            :param use_caller_credentials: ``CfnDataSource.DynamoDBConfigProperty.UseCallerCredentials``.
            :param versioned: ``CfnDataSource.DynamoDBConfigProperty.Versioned``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html
            """
            self._values = {
                "aws_region": aws_region,
                "table_name": table_name,
            }
            if delta_sync_config is not None:
                self._values["delta_sync_config"] = delta_sync_config
            if use_caller_credentials is not None:
                self._values["use_caller_credentials"] = use_caller_credentials
            if versioned is not None:
                self._values["versioned"] = versioned

        @builtins.property
        def aws_region(self) -> str:
            """``CfnDataSource.DynamoDBConfigProperty.AwsRegion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-awsregion
            """
            return self._values.get("aws_region")

        @builtins.property
        def table_name(self) -> str:
            """``CfnDataSource.DynamoDBConfigProperty.TableName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-tablename
            """
            return self._values.get("table_name")

        @builtins.property
        def delta_sync_config(
            self,
        ) -> typing.Optional[
            typing.Union["CfnDataSource.DeltaSyncConfigProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnDataSource.DynamoDBConfigProperty.DeltaSyncConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-deltasyncconfig
            """
            return self._values.get("delta_sync_config")

        @builtins.property
        def use_caller_credentials(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnDataSource.DynamoDBConfigProperty.UseCallerCredentials``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-usecallercredentials
            """
            return self._values.get("use_caller_credentials")

        @builtins.property
        def versioned(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnDataSource.DynamoDBConfigProperty.Versioned``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-versioned
            """
            return self._values.get("versioned")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnDataSource.ElasticsearchConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"aws_region": "awsRegion", "endpoint": "endpoint"},
    )
    class ElasticsearchConfigProperty:
        def __init__(self, *, aws_region: str, endpoint: str) -> None:
            """
            :param aws_region: ``CfnDataSource.ElasticsearchConfigProperty.AwsRegion``.
            :param endpoint: ``CfnDataSource.ElasticsearchConfigProperty.Endpoint``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html
            """
            self._values = {
                "aws_region": aws_region,
                "endpoint": endpoint,
            }

        @builtins.property
        def aws_region(self) -> str:
            """``CfnDataSource.ElasticsearchConfigProperty.AwsRegion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html#cfn-appsync-datasource-elasticsearchconfig-awsregion
            """
            return self._values.get("aws_region")

        @builtins.property
        def endpoint(self) -> str:
            """``CfnDataSource.ElasticsearchConfigProperty.Endpoint``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html#cfn-appsync-datasource-elasticsearchconfig-endpoint
            """
            return self._values.get("endpoint")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnDataSource.HttpConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "authorization_config": "authorizationConfig",
        },
    )
    class HttpConfigProperty:
        def __init__(
            self,
            *,
            endpoint: str,
            authorization_config: typing.Optional[
                typing.Union[
                    "CfnDataSource.AuthorizationConfigProperty", _IResolvable_9ceae33e
                ]
            ] = None,
        ) -> None:
            """
            :param endpoint: ``CfnDataSource.HttpConfigProperty.Endpoint``.
            :param authorization_config: ``CfnDataSource.HttpConfigProperty.AuthorizationConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html
            """
            self._values = {
                "endpoint": endpoint,
            }
            if authorization_config is not None:
                self._values["authorization_config"] = authorization_config

        @builtins.property
        def endpoint(self) -> str:
            """``CfnDataSource.HttpConfigProperty.Endpoint``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html#cfn-appsync-datasource-httpconfig-endpoint
            """
            return self._values.get("endpoint")

        @builtins.property
        def authorization_config(
            self,
        ) -> typing.Optional[
            typing.Union[
                "CfnDataSource.AuthorizationConfigProperty", _IResolvable_9ceae33e
            ]
        ]:
            """``CfnDataSource.HttpConfigProperty.AuthorizationConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html#cfn-appsync-datasource-httpconfig-authorizationconfig
            """
            return self._values.get("authorization_config")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnDataSource.LambdaConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_function_arn": "lambdaFunctionArn"},
    )
    class LambdaConfigProperty:
        def __init__(self, *, lambda_function_arn: str) -> None:
            """
            :param lambda_function_arn: ``CfnDataSource.LambdaConfigProperty.LambdaFunctionArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html
            """
            self._values = {
                "lambda_function_arn": lambda_function_arn,
            }

        @builtins.property
        def lambda_function_arn(self) -> str:
            """``CfnDataSource.LambdaConfigProperty.LambdaFunctionArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html#cfn-appsync-datasource-lambdaconfig-lambdafunctionarn
            """
            return self._values.get("lambda_function_arn")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnDataSource.RdsHttpEndpointConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_region": "awsRegion",
            "aws_secret_store_arn": "awsSecretStoreArn",
            "db_cluster_identifier": "dbClusterIdentifier",
            "database_name": "databaseName",
            "schema": "schema",
        },
    )
    class RdsHttpEndpointConfigProperty:
        def __init__(
            self,
            *,
            aws_region: str,
            aws_secret_store_arn: str,
            db_cluster_identifier: str,
            database_name: typing.Optional[str] = None,
            schema: typing.Optional[str] = None,
        ) -> None:
            """
            :param aws_region: ``CfnDataSource.RdsHttpEndpointConfigProperty.AwsRegion``.
            :param aws_secret_store_arn: ``CfnDataSource.RdsHttpEndpointConfigProperty.AwsSecretStoreArn``.
            :param db_cluster_identifier: ``CfnDataSource.RdsHttpEndpointConfigProperty.DbClusterIdentifier``.
            :param database_name: ``CfnDataSource.RdsHttpEndpointConfigProperty.DatabaseName``.
            :param schema: ``CfnDataSource.RdsHttpEndpointConfigProperty.Schema``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html
            """
            self._values = {
                "aws_region": aws_region,
                "aws_secret_store_arn": aws_secret_store_arn,
                "db_cluster_identifier": db_cluster_identifier,
            }
            if database_name is not None:
                self._values["database_name"] = database_name
            if schema is not None:
                self._values["schema"] = schema

        @builtins.property
        def aws_region(self) -> str:
            """``CfnDataSource.RdsHttpEndpointConfigProperty.AwsRegion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-awsregion
            """
            return self._values.get("aws_region")

        @builtins.property
        def aws_secret_store_arn(self) -> str:
            """``CfnDataSource.RdsHttpEndpointConfigProperty.AwsSecretStoreArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-awssecretstorearn
            """
            return self._values.get("aws_secret_store_arn")

        @builtins.property
        def db_cluster_identifier(self) -> str:
            """``CfnDataSource.RdsHttpEndpointConfigProperty.DbClusterIdentifier``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-dbclusteridentifier
            """
            return self._values.get("db_cluster_identifier")

        @builtins.property
        def database_name(self) -> typing.Optional[str]:
            """``CfnDataSource.RdsHttpEndpointConfigProperty.DatabaseName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-databasename
            """
            return self._values.get("database_name")

        @builtins.property
        def schema(self) -> typing.Optional[str]:
            """``CfnDataSource.RdsHttpEndpointConfigProperty.Schema``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-schema
            """
            return self._values.get("schema")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RdsHttpEndpointConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnDataSource.RelationalDatabaseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "relational_database_source_type": "relationalDatabaseSourceType",
            "rds_http_endpoint_config": "rdsHttpEndpointConfig",
        },
    )
    class RelationalDatabaseConfigProperty:
        def __init__(
            self,
            *,
            relational_database_source_type: str,
            rds_http_endpoint_config: typing.Optional[
                typing.Union[
                    "CfnDataSource.RdsHttpEndpointConfigProperty", _IResolvable_9ceae33e
                ]
            ] = None,
        ) -> None:
            """
            :param relational_database_source_type: ``CfnDataSource.RelationalDatabaseConfigProperty.RelationalDatabaseSourceType``.
            :param rds_http_endpoint_config: ``CfnDataSource.RelationalDatabaseConfigProperty.RdsHttpEndpointConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html
            """
            self._values = {
                "relational_database_source_type": relational_database_source_type,
            }
            if rds_http_endpoint_config is not None:
                self._values["rds_http_endpoint_config"] = rds_http_endpoint_config

        @builtins.property
        def relational_database_source_type(self) -> str:
            """``CfnDataSource.RelationalDatabaseConfigProperty.RelationalDatabaseSourceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html#cfn-appsync-datasource-relationaldatabaseconfig-relationaldatabasesourcetype
            """
            return self._values.get("relational_database_source_type")

        @builtins.property
        def rds_http_endpoint_config(
            self,
        ) -> typing.Optional[
            typing.Union[
                "CfnDataSource.RdsHttpEndpointConfigProperty", _IResolvable_9ceae33e
            ]
        ]:
            """``CfnDataSource.RelationalDatabaseConfigProperty.RdsHttpEndpointConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html#cfn-appsync-datasource-relationaldatabaseconfig-rdshttpendpointconfig
            """
            return self._values.get("rds_http_endpoint_config")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelationalDatabaseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.CfnDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "name": "name",
        "type": "type",
        "description": "description",
        "dynamo_db_config": "dynamoDbConfig",
        "elasticsearch_config": "elasticsearchConfig",
        "http_config": "httpConfig",
        "lambda_config": "lambdaConfig",
        "relational_database_config": "relationalDatabaseConfig",
        "service_role_arn": "serviceRoleArn",
    },
)
class CfnDataSourceProps:
    def __init__(
        self,
        *,
        api_id: str,
        name: str,
        type: str,
        description: typing.Optional[str] = None,
        dynamo_db_config: typing.Optional[
            typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        elasticsearch_config: typing.Optional[
            typing.Union[
                "CfnDataSource.ElasticsearchConfigProperty", _IResolvable_9ceae33e
            ]
        ] = None,
        http_config: typing.Optional[
            typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        lambda_config: typing.Optional[
            typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        relational_database_config: typing.Optional[
            typing.Union[
                "CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_9ceae33e
            ]
        ] = None,
        service_role_arn: typing.Optional[str] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::DataSource``.

        :param api_id: ``AWS::AppSync::DataSource.ApiId``.
        :param name: ``AWS::AppSync::DataSource.Name``.
        :param type: ``AWS::AppSync::DataSource.Type``.
        :param description: ``AWS::AppSync::DataSource.Description``.
        :param dynamo_db_config: ``AWS::AppSync::DataSource.DynamoDBConfig``.
        :param elasticsearch_config: ``AWS::AppSync::DataSource.ElasticsearchConfig``.
        :param http_config: ``AWS::AppSync::DataSource.HttpConfig``.
        :param lambda_config: ``AWS::AppSync::DataSource.LambdaConfig``.
        :param relational_database_config: ``AWS::AppSync::DataSource.RelationalDatabaseConfig``.
        :param service_role_arn: ``AWS::AppSync::DataSource.ServiceRoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html
        """
        self._values = {
            "api_id": api_id,
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if dynamo_db_config is not None:
            self._values["dynamo_db_config"] = dynamo_db_config
        if elasticsearch_config is not None:
            self._values["elasticsearch_config"] = elasticsearch_config
        if http_config is not None:
            self._values["http_config"] = http_config
        if lambda_config is not None:
            self._values["lambda_config"] = lambda_config
        if relational_database_config is not None:
            self._values["relational_database_config"] = relational_database_config
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn

    @builtins.property
    def api_id(self) -> str:
        """``AWS::AppSync::DataSource.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-apiid
        """
        return self._values.get("api_id")

    @builtins.property
    def name(self) -> str:
        """``AWS::AppSync::DataSource.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-name
        """
        return self._values.get("name")

    @builtins.property
    def type(self) -> str:
        """``AWS::AppSync::DataSource.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-type
        """
        return self._values.get("type")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::AppSync::DataSource.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-description
        """
        return self._values.get("description")

    @builtins.property
    def dynamo_db_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::DataSource.DynamoDBConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-dynamodbconfig
        """
        return self._values.get("dynamo_db_config")

    @builtins.property
    def elasticsearch_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnDataSource.ElasticsearchConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::DataSource.ElasticsearchConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-elasticsearchconfig
        """
        return self._values.get("elasticsearch_config")

    @builtins.property
    def http_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::DataSource.HttpConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-httpconfig
        """
        return self._values.get("http_config")

    @builtins.property
    def lambda_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::DataSource.LambdaConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-lambdaconfig
        """
        return self._values.get("lambda_config")

    @builtins.property
    def relational_database_config(
        self,
    ) -> typing.Optional[
        typing.Union[
            "CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_9ceae33e
        ]
    ]:
        """``AWS::AppSync::DataSource.RelationalDatabaseConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-relationaldatabaseconfig
        """
        return self._values.get("relational_database_config")

    @builtins.property
    def service_role_arn(self) -> typing.Optional[str]:
        """``AWS::AppSync::DataSource.ServiceRoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-servicerolearn
        """
        return self._values.get("service_role_arn")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_051e6ed8)
class CfnFunctionConfiguration(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.CfnFunctionConfiguration",
):
    """A CloudFormation ``AWS::AppSync::FunctionConfiguration``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html
    cloudformationResource:
    :cloudformationResource:: AWS::AppSync::FunctionConfiguration
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        api_id: str,
        data_source_name: str,
        function_version: str,
        name: str,
        description: typing.Optional[str] = None,
        request_mapping_template: typing.Optional[str] = None,
        request_mapping_template_s3_location: typing.Optional[str] = None,
        response_mapping_template: typing.Optional[str] = None,
        response_mapping_template_s3_location: typing.Optional[str] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::FunctionConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::AppSync::FunctionConfiguration.ApiId``.
        :param data_source_name: ``AWS::AppSync::FunctionConfiguration.DataSourceName``.
        :param function_version: ``AWS::AppSync::FunctionConfiguration.FunctionVersion``.
        :param name: ``AWS::AppSync::FunctionConfiguration.Name``.
        :param description: ``AWS::AppSync::FunctionConfiguration.Description``.
        :param request_mapping_template: ``AWS::AppSync::FunctionConfiguration.RequestMappingTemplate``.
        :param request_mapping_template_s3_location: ``AWS::AppSync::FunctionConfiguration.RequestMappingTemplateS3Location``.
        :param response_mapping_template: ``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplate``.
        :param response_mapping_template_s3_location: ``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplateS3Location``.
        """
        props = CfnFunctionConfigurationProps(
            api_id=api_id,
            data_source_name=data_source_name,
            function_version=function_version,
            name=name,
            description=description,
            request_mapping_template=request_mapping_template,
            request_mapping_template_s3_location=request_mapping_template_s3_location,
            response_mapping_template=response_mapping_template,
            response_mapping_template_s3_location=response_mapping_template_s3_location,
        )

        jsii.create(CfnFunctionConfiguration, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnFunctionConfiguration":
        """A factory method that creates a new instance of this class from an object containing the CloudFormation properties of this resource.

        Used in the @aws-cdk/cloudformation-include module.

        :param scope: -
        :param id: -
        :param resource_attributes: -
        :param finder: The finder interface used to resolve references across the template.

        stability
        :stability: experimental
        """
        options = _FromCloudFormationOptions_5f49f6f1(finder=finder)

        return jsii.sinvoke(
            cls, "fromCloudFormation", [scope, id, resource_attributes, options]
        )

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_154f5999) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self, props: typing.Mapping[str, typing.Any]
    ) -> typing.Mapping[str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="attrDataSourceName")
    def attr_data_source_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DataSourceName
        """
        return jsii.get(self, "attrDataSourceName")

    @builtins.property
    @jsii.member(jsii_name="attrFunctionArn")
    def attr_function_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: FunctionArn
        """
        return jsii.get(self, "attrFunctionArn")

    @builtins.property
    @jsii.member(jsii_name="attrFunctionId")
    def attr_function_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: FunctionId
        """
        return jsii.get(self, "attrFunctionId")

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::AppSync::FunctionConfiguration.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str) -> None:
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceName")
    def data_source_name(self) -> str:
        """``AWS::AppSync::FunctionConfiguration.DataSourceName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-datasourcename
        """
        return jsii.get(self, "dataSourceName")

    @data_source_name.setter
    def data_source_name(self, value: str) -> None:
        jsii.set(self, "dataSourceName", value)

    @builtins.property
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> str:
        """``AWS::AppSync::FunctionConfiguration.FunctionVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-functionversion
        """
        return jsii.get(self, "functionVersion")

    @function_version.setter
    def function_version(self, value: str) -> None:
        jsii.set(self, "functionVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::AppSync::FunctionConfiguration.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str) -> None:
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::AppSync::FunctionConfiguration.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplate")
    def request_mapping_template(self) -> typing.Optional[str]:
        """``AWS::AppSync::FunctionConfiguration.RequestMappingTemplate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplate
        """
        return jsii.get(self, "requestMappingTemplate")

    @request_mapping_template.setter
    def request_mapping_template(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "requestMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplateS3Location")
    def request_mapping_template_s3_location(self) -> typing.Optional[str]:
        """``AWS::AppSync::FunctionConfiguration.RequestMappingTemplateS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplates3location
        """
        return jsii.get(self, "requestMappingTemplateS3Location")

    @request_mapping_template_s3_location.setter
    def request_mapping_template_s3_location(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "requestMappingTemplateS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplate")
    def response_mapping_template(self) -> typing.Optional[str]:
        """``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplate
        """
        return jsii.get(self, "responseMappingTemplate")

    @response_mapping_template.setter
    def response_mapping_template(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "responseMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplateS3Location")
    def response_mapping_template_s3_location(self) -> typing.Optional[str]:
        """``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplateS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplates3location
        """
        return jsii.get(self, "responseMappingTemplateS3Location")

    @response_mapping_template_s3_location.setter
    def response_mapping_template_s3_location(
        self, value: typing.Optional[str]
    ) -> None:
        jsii.set(self, "responseMappingTemplateS3Location", value)


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.CfnFunctionConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "data_source_name": "dataSourceName",
        "function_version": "functionVersion",
        "name": "name",
        "description": "description",
        "request_mapping_template": "requestMappingTemplate",
        "request_mapping_template_s3_location": "requestMappingTemplateS3Location",
        "response_mapping_template": "responseMappingTemplate",
        "response_mapping_template_s3_location": "responseMappingTemplateS3Location",
    },
)
class CfnFunctionConfigurationProps:
    def __init__(
        self,
        *,
        api_id: str,
        data_source_name: str,
        function_version: str,
        name: str,
        description: typing.Optional[str] = None,
        request_mapping_template: typing.Optional[str] = None,
        request_mapping_template_s3_location: typing.Optional[str] = None,
        response_mapping_template: typing.Optional[str] = None,
        response_mapping_template_s3_location: typing.Optional[str] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::FunctionConfiguration``.

        :param api_id: ``AWS::AppSync::FunctionConfiguration.ApiId``.
        :param data_source_name: ``AWS::AppSync::FunctionConfiguration.DataSourceName``.
        :param function_version: ``AWS::AppSync::FunctionConfiguration.FunctionVersion``.
        :param name: ``AWS::AppSync::FunctionConfiguration.Name``.
        :param description: ``AWS::AppSync::FunctionConfiguration.Description``.
        :param request_mapping_template: ``AWS::AppSync::FunctionConfiguration.RequestMappingTemplate``.
        :param request_mapping_template_s3_location: ``AWS::AppSync::FunctionConfiguration.RequestMappingTemplateS3Location``.
        :param response_mapping_template: ``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplate``.
        :param response_mapping_template_s3_location: ``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplateS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html
        """
        self._values = {
            "api_id": api_id,
            "data_source_name": data_source_name,
            "function_version": function_version,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if request_mapping_template_s3_location is not None:
            self._values[
                "request_mapping_template_s3_location"
            ] = request_mapping_template_s3_location
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if response_mapping_template_s3_location is not None:
            self._values[
                "response_mapping_template_s3_location"
            ] = response_mapping_template_s3_location

    @builtins.property
    def api_id(self) -> str:
        """``AWS::AppSync::FunctionConfiguration.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-apiid
        """
        return self._values.get("api_id")

    @builtins.property
    def data_source_name(self) -> str:
        """``AWS::AppSync::FunctionConfiguration.DataSourceName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-datasourcename
        """
        return self._values.get("data_source_name")

    @builtins.property
    def function_version(self) -> str:
        """``AWS::AppSync::FunctionConfiguration.FunctionVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-functionversion
        """
        return self._values.get("function_version")

    @builtins.property
    def name(self) -> str:
        """``AWS::AppSync::FunctionConfiguration.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-name
        """
        return self._values.get("name")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::AppSync::FunctionConfiguration.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-description
        """
        return self._values.get("description")

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[str]:
        """``AWS::AppSync::FunctionConfiguration.RequestMappingTemplate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplate
        """
        return self._values.get("request_mapping_template")

    @builtins.property
    def request_mapping_template_s3_location(self) -> typing.Optional[str]:
        """``AWS::AppSync::FunctionConfiguration.RequestMappingTemplateS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplates3location
        """
        return self._values.get("request_mapping_template_s3_location")

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[str]:
        """``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplate
        """
        return self._values.get("response_mapping_template")

    @builtins.property
    def response_mapping_template_s3_location(self) -> typing.Optional[str]:
        """``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplateS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplates3location
        """
        return self._values.get("response_mapping_template_s3_location")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFunctionConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_051e6ed8)
class CfnGraphQLApi(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.CfnGraphQLApi",
):
    """A CloudFormation ``AWS::AppSync::GraphQLApi``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html
    cloudformationResource:
    :cloudformationResource:: AWS::AppSync::GraphQLApi
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        authentication_type: str,
        name: str,
        additional_authentication_providers: typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union[
                        "AdditionalAuthenticationProviderProperty",
                        _IResolvable_9ceae33e,
                    ]
                ],
            ]
        ] = None,
        log_config: typing.Optional[
            typing.Union["LogConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        open_id_connect_config: typing.Optional[
            typing.Union["OpenIDConnectConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        tags: typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[typing.Union[_IResolvable_9ceae33e, _CfnTag_b4661f1a]],
            ]
        ] = None,
        user_pool_config: typing.Optional[
            typing.Union["UserPoolConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        xray_enabled: typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::GraphQLApi``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param authentication_type: ``AWS::AppSync::GraphQLApi.AuthenticationType``.
        :param name: ``AWS::AppSync::GraphQLApi.Name``.
        :param additional_authentication_providers: ``AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders``.
        :param log_config: ``AWS::AppSync::GraphQLApi.LogConfig``.
        :param open_id_connect_config: ``AWS::AppSync::GraphQLApi.OpenIDConnectConfig``.
        :param tags: ``AWS::AppSync::GraphQLApi.Tags``.
        :param user_pool_config: ``AWS::AppSync::GraphQLApi.UserPoolConfig``.
        :param xray_enabled: ``AWS::AppSync::GraphQLApi.XrayEnabled``.
        """
        props = CfnGraphQLApiProps(
            authentication_type=authentication_type,
            name=name,
            additional_authentication_providers=additional_authentication_providers,
            log_config=log_config,
            open_id_connect_config=open_id_connect_config,
            tags=tags,
            user_pool_config=user_pool_config,
            xray_enabled=xray_enabled,
        )

        jsii.create(CfnGraphQLApi, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnGraphQLApi":
        """A factory method that creates a new instance of this class from an object containing the CloudFormation properties of this resource.

        Used in the @aws-cdk/cloudformation-include module.

        :param scope: -
        :param id: -
        :param resource_attributes: -
        :param finder: The finder interface used to resolve references across the template.

        stability
        :stability: experimental
        """
        options = _FromCloudFormationOptions_5f49f6f1(finder=finder)

        return jsii.sinvoke(
            cls, "fromCloudFormation", [scope, id, resource_attributes, options]
        )

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_154f5999) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self, props: typing.Mapping[str, typing.Any]
    ) -> typing.Mapping[str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="attrApiId")
    def attr_api_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ApiId
        """
        return jsii.get(self, "attrApiId")

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Arn
        """
        return jsii.get(self, "attrArn")

    @builtins.property
    @jsii.member(jsii_name="attrGraphQlUrl")
    def attr_graph_ql_url(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: GraphQLUrl
        """
        return jsii.get(self, "attrGraphQlUrl")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_2508893f:
        """``AWS::AppSync::GraphQLApi.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> str:
        """``AWS::AppSync::GraphQLApi.AuthenticationType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-authenticationtype
        """
        return jsii.get(self, "authenticationType")

    @authentication_type.setter
    def authentication_type(self, value: str) -> None:
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::AppSync::GraphQLApi.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str) -> None:
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="additionalAuthenticationProviders")
    def additional_authentication_providers(
        self,
    ) -> typing.Optional[
        typing.Union[
            _IResolvable_9ceae33e,
            typing.List[
                typing.Union[
                    "AdditionalAuthenticationProviderProperty", _IResolvable_9ceae33e
                ]
            ],
        ]
    ]:
        """``AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-additionalauthenticationproviders
        """
        return jsii.get(self, "additionalAuthenticationProviders")

    @additional_authentication_providers.setter
    def additional_authentication_providers(
        self,
        value: typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union[
                        "AdditionalAuthenticationProviderProperty",
                        _IResolvable_9ceae33e,
                    ]
                ],
            ]
        ],
    ) -> None:
        jsii.set(self, "additionalAuthenticationProviders", value)

    @builtins.property
    @jsii.member(jsii_name="logConfig")
    def log_config(
        self,
    ) -> typing.Optional[typing.Union["LogConfigProperty", _IResolvable_9ceae33e]]:
        """``AWS::AppSync::GraphQLApi.LogConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-logconfig
        """
        return jsii.get(self, "logConfig")

    @log_config.setter
    def log_config(
        self,
        value: typing.Optional[
            typing.Union["LogConfigProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "logConfig", value)

    @builtins.property
    @jsii.member(jsii_name="openIdConnectConfig")
    def open_id_connect_config(
        self,
    ) -> typing.Optional[
        typing.Union["OpenIDConnectConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::GraphQLApi.OpenIDConnectConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-openidconnectconfig
        """
        return jsii.get(self, "openIdConnectConfig")

    @open_id_connect_config.setter
    def open_id_connect_config(
        self,
        value: typing.Optional[
            typing.Union["OpenIDConnectConfigProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "openIdConnectConfig", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolConfig")
    def user_pool_config(
        self,
    ) -> typing.Optional[typing.Union["UserPoolConfigProperty", _IResolvable_9ceae33e]]:
        """``AWS::AppSync::GraphQLApi.UserPoolConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-userpoolconfig
        """
        return jsii.get(self, "userPoolConfig")

    @user_pool_config.setter
    def user_pool_config(
        self,
        value: typing.Optional[
            typing.Union["UserPoolConfigProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "userPoolConfig", value)

    @builtins.property
    @jsii.member(jsii_name="xrayEnabled")
    def xray_enabled(
        self,
    ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
        """``AWS::AppSync::GraphQLApi.XrayEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-xrayenabled
        """
        return jsii.get(self, "xrayEnabled")

    @xray_enabled.setter
    def xray_enabled(
        self, value: typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]
    ) -> None:
        jsii.set(self, "xrayEnabled", value)

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnGraphQLApi.AdditionalAuthenticationProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_type": "authenticationType",
            "open_id_connect_config": "openIdConnectConfig",
            "user_pool_config": "userPoolConfig",
        },
    )
    class AdditionalAuthenticationProviderProperty:
        def __init__(
            self,
            *,
            authentication_type: str,
            open_id_connect_config: typing.Optional[
                typing.Union[
                    "CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_9ceae33e
                ]
            ] = None,
            user_pool_config: typing.Optional[
                typing.Union[
                    "CfnGraphQLApi.CognitoUserPoolConfigProperty", _IResolvable_9ceae33e
                ]
            ] = None,
        ) -> None:
            """
            :param authentication_type: ``CfnGraphQLApi.AdditionalAuthenticationProviderProperty.AuthenticationType``.
            :param open_id_connect_config: ``CfnGraphQLApi.AdditionalAuthenticationProviderProperty.OpenIDConnectConfig``.
            :param user_pool_config: ``CfnGraphQLApi.AdditionalAuthenticationProviderProperty.UserPoolConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html
            """
            self._values = {
                "authentication_type": authentication_type,
            }
            if open_id_connect_config is not None:
                self._values["open_id_connect_config"] = open_id_connect_config
            if user_pool_config is not None:
                self._values["user_pool_config"] = user_pool_config

        @builtins.property
        def authentication_type(self) -> str:
            """``CfnGraphQLApi.AdditionalAuthenticationProviderProperty.AuthenticationType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-authenticationtype
            """
            return self._values.get("authentication_type")

        @builtins.property
        def open_id_connect_config(
            self,
        ) -> typing.Optional[
            typing.Union[
                "CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_9ceae33e
            ]
        ]:
            """``CfnGraphQLApi.AdditionalAuthenticationProviderProperty.OpenIDConnectConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-openidconnectconfig
            """
            return self._values.get("open_id_connect_config")

        @builtins.property
        def user_pool_config(
            self,
        ) -> typing.Optional[
            typing.Union[
                "CfnGraphQLApi.CognitoUserPoolConfigProperty", _IResolvable_9ceae33e
            ]
        ]:
            """``CfnGraphQLApi.AdditionalAuthenticationProviderProperty.UserPoolConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-userpoolconfig
            """
            return self._values.get("user_pool_config")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdditionalAuthenticationProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnGraphQLApi.CognitoUserPoolConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_id_client_regex": "appIdClientRegex",
            "aws_region": "awsRegion",
            "user_pool_id": "userPoolId",
        },
    )
    class CognitoUserPoolConfigProperty:
        def __init__(
            self,
            *,
            app_id_client_regex: typing.Optional[str] = None,
            aws_region: typing.Optional[str] = None,
            user_pool_id: typing.Optional[str] = None,
        ) -> None:
            """
            :param app_id_client_regex: ``CfnGraphQLApi.CognitoUserPoolConfigProperty.AppIdClientRegex``.
            :param aws_region: ``CfnGraphQLApi.CognitoUserPoolConfigProperty.AwsRegion``.
            :param user_pool_id: ``CfnGraphQLApi.CognitoUserPoolConfigProperty.UserPoolId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html
            """
            self._values = {}
            if app_id_client_regex is not None:
                self._values["app_id_client_regex"] = app_id_client_regex
            if aws_region is not None:
                self._values["aws_region"] = aws_region
            if user_pool_id is not None:
                self._values["user_pool_id"] = user_pool_id

        @builtins.property
        def app_id_client_regex(self) -> typing.Optional[str]:
            """``CfnGraphQLApi.CognitoUserPoolConfigProperty.AppIdClientRegex``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-appidclientregex
            """
            return self._values.get("app_id_client_regex")

        @builtins.property
        def aws_region(self) -> typing.Optional[str]:
            """``CfnGraphQLApi.CognitoUserPoolConfigProperty.AwsRegion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-awsregion
            """
            return self._values.get("aws_region")

        @builtins.property
        def user_pool_id(self) -> typing.Optional[str]:
            """``CfnGraphQLApi.CognitoUserPoolConfigProperty.UserPoolId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-userpoolid
            """
            return self._values.get("user_pool_id")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CognitoUserPoolConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnGraphQLApi.LogConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs_role_arn": "cloudWatchLogsRoleArn",
            "exclude_verbose_content": "excludeVerboseContent",
            "field_log_level": "fieldLogLevel",
        },
    )
    class LogConfigProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs_role_arn: typing.Optional[str] = None,
            exclude_verbose_content: typing.Optional[
                typing.Union[bool, _IResolvable_9ceae33e]
            ] = None,
            field_log_level: typing.Optional[str] = None,
        ) -> None:
            """
            :param cloud_watch_logs_role_arn: ``CfnGraphQLApi.LogConfigProperty.CloudWatchLogsRoleArn``.
            :param exclude_verbose_content: ``CfnGraphQLApi.LogConfigProperty.ExcludeVerboseContent``.
            :param field_log_level: ``CfnGraphQLApi.LogConfigProperty.FieldLogLevel``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html
            """
            self._values = {}
            if cloud_watch_logs_role_arn is not None:
                self._values["cloud_watch_logs_role_arn"] = cloud_watch_logs_role_arn
            if exclude_verbose_content is not None:
                self._values["exclude_verbose_content"] = exclude_verbose_content
            if field_log_level is not None:
                self._values["field_log_level"] = field_log_level

        @builtins.property
        def cloud_watch_logs_role_arn(self) -> typing.Optional[str]:
            """``CfnGraphQLApi.LogConfigProperty.CloudWatchLogsRoleArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-cloudwatchlogsrolearn
            """
            return self._values.get("cloud_watch_logs_role_arn")

        @builtins.property
        def exclude_verbose_content(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnGraphQLApi.LogConfigProperty.ExcludeVerboseContent``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-excludeverbosecontent
            """
            return self._values.get("exclude_verbose_content")

        @builtins.property
        def field_log_level(self) -> typing.Optional[str]:
            """``CfnGraphQLApi.LogConfigProperty.FieldLogLevel``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-fieldloglevel
            """
            return self._values.get("field_log_level")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnGraphQLApi.OpenIDConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auth_ttl": "authTtl",
            "client_id": "clientId",
            "iat_ttl": "iatTtl",
            "issuer": "issuer",
        },
    )
    class OpenIDConnectConfigProperty:
        def __init__(
            self,
            *,
            auth_ttl: typing.Optional[jsii.Number] = None,
            client_id: typing.Optional[str] = None,
            iat_ttl: typing.Optional[jsii.Number] = None,
            issuer: typing.Optional[str] = None,
        ) -> None:
            """
            :param auth_ttl: ``CfnGraphQLApi.OpenIDConnectConfigProperty.AuthTTL``.
            :param client_id: ``CfnGraphQLApi.OpenIDConnectConfigProperty.ClientId``.
            :param iat_ttl: ``CfnGraphQLApi.OpenIDConnectConfigProperty.IatTTL``.
            :param issuer: ``CfnGraphQLApi.OpenIDConnectConfigProperty.Issuer``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html
            """
            self._values = {}
            if auth_ttl is not None:
                self._values["auth_ttl"] = auth_ttl
            if client_id is not None:
                self._values["client_id"] = client_id
            if iat_ttl is not None:
                self._values["iat_ttl"] = iat_ttl
            if issuer is not None:
                self._values["issuer"] = issuer

        @builtins.property
        def auth_ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnGraphQLApi.OpenIDConnectConfigProperty.AuthTTL``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-authttl
            """
            return self._values.get("auth_ttl")

        @builtins.property
        def client_id(self) -> typing.Optional[str]:
            """``CfnGraphQLApi.OpenIDConnectConfigProperty.ClientId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-clientid
            """
            return self._values.get("client_id")

        @builtins.property
        def iat_ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnGraphQLApi.OpenIDConnectConfigProperty.IatTTL``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-iatttl
            """
            return self._values.get("iat_ttl")

        @builtins.property
        def issuer(self) -> typing.Optional[str]:
            """``CfnGraphQLApi.OpenIDConnectConfigProperty.Issuer``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-issuer
            """
            return self._values.get("issuer")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenIDConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnGraphQLApi.UserPoolConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_id_client_regex": "appIdClientRegex",
            "aws_region": "awsRegion",
            "default_action": "defaultAction",
            "user_pool_id": "userPoolId",
        },
    )
    class UserPoolConfigProperty:
        def __init__(
            self,
            *,
            app_id_client_regex: typing.Optional[str] = None,
            aws_region: typing.Optional[str] = None,
            default_action: typing.Optional[str] = None,
            user_pool_id: typing.Optional[str] = None,
        ) -> None:
            """
            :param app_id_client_regex: ``CfnGraphQLApi.UserPoolConfigProperty.AppIdClientRegex``.
            :param aws_region: ``CfnGraphQLApi.UserPoolConfigProperty.AwsRegion``.
            :param default_action: ``CfnGraphQLApi.UserPoolConfigProperty.DefaultAction``.
            :param user_pool_id: ``CfnGraphQLApi.UserPoolConfigProperty.UserPoolId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html
            """
            self._values = {}
            if app_id_client_regex is not None:
                self._values["app_id_client_regex"] = app_id_client_regex
            if aws_region is not None:
                self._values["aws_region"] = aws_region
            if default_action is not None:
                self._values["default_action"] = default_action
            if user_pool_id is not None:
                self._values["user_pool_id"] = user_pool_id

        @builtins.property
        def app_id_client_regex(self) -> typing.Optional[str]:
            """``CfnGraphQLApi.UserPoolConfigProperty.AppIdClientRegex``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-appidclientregex
            """
            return self._values.get("app_id_client_regex")

        @builtins.property
        def aws_region(self) -> typing.Optional[str]:
            """``CfnGraphQLApi.UserPoolConfigProperty.AwsRegion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-awsregion
            """
            return self._values.get("aws_region")

        @builtins.property
        def default_action(self) -> typing.Optional[str]:
            """``CfnGraphQLApi.UserPoolConfigProperty.DefaultAction``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-defaultaction
            """
            return self._values.get("default_action")

        @builtins.property
        def user_pool_id(self) -> typing.Optional[str]:
            """``CfnGraphQLApi.UserPoolConfigProperty.UserPoolId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-userpoolid
            """
            return self._values.get("user_pool_id")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPoolConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.CfnGraphQLApiProps",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_type": "authenticationType",
        "name": "name",
        "additional_authentication_providers": "additionalAuthenticationProviders",
        "log_config": "logConfig",
        "open_id_connect_config": "openIdConnectConfig",
        "tags": "tags",
        "user_pool_config": "userPoolConfig",
        "xray_enabled": "xrayEnabled",
    },
)
class CfnGraphQLApiProps:
    def __init__(
        self,
        *,
        authentication_type: str,
        name: str,
        additional_authentication_providers: typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union[
                        "CfnGraphQLApi.AdditionalAuthenticationProviderProperty",
                        _IResolvable_9ceae33e,
                    ]
                ],
            ]
        ] = None,
        log_config: typing.Optional[
            typing.Union["CfnGraphQLApi.LogConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        open_id_connect_config: typing.Optional[
            typing.Union[
                "CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_9ceae33e
            ]
        ] = None,
        tags: typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[typing.Union[_IResolvable_9ceae33e, _CfnTag_b4661f1a]],
            ]
        ] = None,
        user_pool_config: typing.Optional[
            typing.Union["CfnGraphQLApi.UserPoolConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        xray_enabled: typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::GraphQLApi``.

        :param authentication_type: ``AWS::AppSync::GraphQLApi.AuthenticationType``.
        :param name: ``AWS::AppSync::GraphQLApi.Name``.
        :param additional_authentication_providers: ``AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders``.
        :param log_config: ``AWS::AppSync::GraphQLApi.LogConfig``.
        :param open_id_connect_config: ``AWS::AppSync::GraphQLApi.OpenIDConnectConfig``.
        :param tags: ``AWS::AppSync::GraphQLApi.Tags``.
        :param user_pool_config: ``AWS::AppSync::GraphQLApi.UserPoolConfig``.
        :param xray_enabled: ``AWS::AppSync::GraphQLApi.XrayEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html
        """
        self._values = {
            "authentication_type": authentication_type,
            "name": name,
        }
        if additional_authentication_providers is not None:
            self._values[
                "additional_authentication_providers"
            ] = additional_authentication_providers
        if log_config is not None:
            self._values["log_config"] = log_config
        if open_id_connect_config is not None:
            self._values["open_id_connect_config"] = open_id_connect_config
        if tags is not None:
            self._values["tags"] = tags
        if user_pool_config is not None:
            self._values["user_pool_config"] = user_pool_config
        if xray_enabled is not None:
            self._values["xray_enabled"] = xray_enabled

    @builtins.property
    def authentication_type(self) -> str:
        """``AWS::AppSync::GraphQLApi.AuthenticationType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-authenticationtype
        """
        return self._values.get("authentication_type")

    @builtins.property
    def name(self) -> str:
        """``AWS::AppSync::GraphQLApi.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-name
        """
        return self._values.get("name")

    @builtins.property
    def additional_authentication_providers(
        self,
    ) -> typing.Optional[
        typing.Union[
            _IResolvable_9ceae33e,
            typing.List[
                typing.Union[
                    "CfnGraphQLApi.AdditionalAuthenticationProviderProperty",
                    _IResolvable_9ceae33e,
                ]
            ],
        ]
    ]:
        """``AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-additionalauthenticationproviders
        """
        return self._values.get("additional_authentication_providers")

    @builtins.property
    def log_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnGraphQLApi.LogConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::GraphQLApi.LogConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-logconfig
        """
        return self._values.get("log_config")

    @builtins.property
    def open_id_connect_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::GraphQLApi.OpenIDConnectConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-openidconnectconfig
        """
        return self._values.get("open_id_connect_config")

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[
        typing.Union[
            _IResolvable_9ceae33e,
            typing.List[typing.Union[_IResolvable_9ceae33e, _CfnTag_b4661f1a]],
        ]
    ]:
        """``AWS::AppSync::GraphQLApi.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-tags
        """
        return self._values.get("tags")

    @builtins.property
    def user_pool_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnGraphQLApi.UserPoolConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::GraphQLApi.UserPoolConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-userpoolconfig
        """
        return self._values.get("user_pool_config")

    @builtins.property
    def xray_enabled(
        self,
    ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
        """``AWS::AppSync::GraphQLApi.XrayEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-xrayenabled
        """
        return self._values.get("xray_enabled")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphQLApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_051e6ed8)
class CfnGraphQLSchema(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.CfnGraphQLSchema",
):
    """A CloudFormation ``AWS::AppSync::GraphQLSchema``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html
    cloudformationResource:
    :cloudformationResource:: AWS::AppSync::GraphQLSchema
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        api_id: str,
        definition: typing.Optional[str] = None,
        definition_s3_location: typing.Optional[str] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::GraphQLSchema``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::AppSync::GraphQLSchema.ApiId``.
        :param definition: ``AWS::AppSync::GraphQLSchema.Definition``.
        :param definition_s3_location: ``AWS::AppSync::GraphQLSchema.DefinitionS3Location``.
        """
        props = CfnGraphQLSchemaProps(
            api_id=api_id,
            definition=definition,
            definition_s3_location=definition_s3_location,
        )

        jsii.create(CfnGraphQLSchema, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnGraphQLSchema":
        """A factory method that creates a new instance of this class from an object containing the CloudFormation properties of this resource.

        Used in the @aws-cdk/cloudformation-include module.

        :param scope: -
        :param id: -
        :param resource_attributes: -
        :param finder: The finder interface used to resolve references across the template.

        stability
        :stability: experimental
        """
        options = _FromCloudFormationOptions_5f49f6f1(finder=finder)

        return jsii.sinvoke(
            cls, "fromCloudFormation", [scope, id, resource_attributes, options]
        )

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_154f5999) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self, props: typing.Mapping[str, typing.Any]
    ) -> typing.Mapping[str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::AppSync::GraphQLSchema.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str) -> None:
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Optional[str]:
        """``AWS::AppSync::GraphQLSchema.Definition``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definition
        """
        return jsii.get(self, "definition")

    @definition.setter
    def definition(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "definition", value)

    @builtins.property
    @jsii.member(jsii_name="definitionS3Location")
    def definition_s3_location(self) -> typing.Optional[str]:
        """``AWS::AppSync::GraphQLSchema.DefinitionS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definitions3location
        """
        return jsii.get(self, "definitionS3Location")

    @definition_s3_location.setter
    def definition_s3_location(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "definitionS3Location", value)


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.CfnGraphQLSchemaProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "definition": "definition",
        "definition_s3_location": "definitionS3Location",
    },
)
class CfnGraphQLSchemaProps:
    def __init__(
        self,
        *,
        api_id: str,
        definition: typing.Optional[str] = None,
        definition_s3_location: typing.Optional[str] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::GraphQLSchema``.

        :param api_id: ``AWS::AppSync::GraphQLSchema.ApiId``.
        :param definition: ``AWS::AppSync::GraphQLSchema.Definition``.
        :param definition_s3_location: ``AWS::AppSync::GraphQLSchema.DefinitionS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html
        """
        self._values = {
            "api_id": api_id,
        }
        if definition is not None:
            self._values["definition"] = definition
        if definition_s3_location is not None:
            self._values["definition_s3_location"] = definition_s3_location

    @builtins.property
    def api_id(self) -> str:
        """``AWS::AppSync::GraphQLSchema.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-apiid
        """
        return self._values.get("api_id")

    @builtins.property
    def definition(self) -> typing.Optional[str]:
        """``AWS::AppSync::GraphQLSchema.Definition``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definition
        """
        return self._values.get("definition")

    @builtins.property
    def definition_s3_location(self) -> typing.Optional[str]:
        """``AWS::AppSync::GraphQLSchema.DefinitionS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definitions3location
        """
        return self._values.get("definition_s3_location")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphQLSchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_051e6ed8)
class CfnResolver(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.CfnResolver",
):
    """A CloudFormation ``AWS::AppSync::Resolver``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html
    cloudformationResource:
    :cloudformationResource:: AWS::AppSync::Resolver
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        api_id: str,
        field_name: str,
        type_name: str,
        caching_config: typing.Optional[
            typing.Union["CachingConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        data_source_name: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
        pipeline_config: typing.Optional[
            typing.Union["PipelineConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        request_mapping_template: typing.Optional[str] = None,
        request_mapping_template_s3_location: typing.Optional[str] = None,
        response_mapping_template: typing.Optional[str] = None,
        response_mapping_template_s3_location: typing.Optional[str] = None,
        sync_config: typing.Optional[
            typing.Union["SyncConfigProperty", _IResolvable_9ceae33e]
        ] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::Resolver``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::AppSync::Resolver.ApiId``.
        :param field_name: ``AWS::AppSync::Resolver.FieldName``.
        :param type_name: ``AWS::AppSync::Resolver.TypeName``.
        :param caching_config: ``AWS::AppSync::Resolver.CachingConfig``.
        :param data_source_name: ``AWS::AppSync::Resolver.DataSourceName``.
        :param kind: ``AWS::AppSync::Resolver.Kind``.
        :param pipeline_config: ``AWS::AppSync::Resolver.PipelineConfig``.
        :param request_mapping_template: ``AWS::AppSync::Resolver.RequestMappingTemplate``.
        :param request_mapping_template_s3_location: ``AWS::AppSync::Resolver.RequestMappingTemplateS3Location``.
        :param response_mapping_template: ``AWS::AppSync::Resolver.ResponseMappingTemplate``.
        :param response_mapping_template_s3_location: ``AWS::AppSync::Resolver.ResponseMappingTemplateS3Location``.
        :param sync_config: ``AWS::AppSync::Resolver.SyncConfig``.
        """
        props = CfnResolverProps(
            api_id=api_id,
            field_name=field_name,
            type_name=type_name,
            caching_config=caching_config,
            data_source_name=data_source_name,
            kind=kind,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            request_mapping_template_s3_location=request_mapping_template_s3_location,
            response_mapping_template=response_mapping_template,
            response_mapping_template_s3_location=response_mapping_template_s3_location,
            sync_config=sync_config,
        )

        jsii.create(CfnResolver, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnResolver":
        """A factory method that creates a new instance of this class from an object containing the CloudFormation properties of this resource.

        Used in the @aws-cdk/cloudformation-include module.

        :param scope: -
        :param id: -
        :param resource_attributes: -
        :param finder: The finder interface used to resolve references across the template.

        stability
        :stability: experimental
        """
        options = _FromCloudFormationOptions_5f49f6f1(finder=finder)

        return jsii.sinvoke(
            cls, "fromCloudFormation", [scope, id, resource_attributes, options]
        )

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_154f5999) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self, props: typing.Mapping[str, typing.Any]
    ) -> typing.Mapping[str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="attrFieldName")
    def attr_field_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: FieldName
        """
        return jsii.get(self, "attrFieldName")

    @builtins.property
    @jsii.member(jsii_name="attrResolverArn")
    def attr_resolver_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ResolverArn
        """
        return jsii.get(self, "attrResolverArn")

    @builtins.property
    @jsii.member(jsii_name="attrTypeName")
    def attr_type_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: TypeName
        """
        return jsii.get(self, "attrTypeName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::AppSync::Resolver.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str) -> None:
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="fieldName")
    def field_name(self) -> str:
        """``AWS::AppSync::Resolver.FieldName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-fieldname
        """
        return jsii.get(self, "fieldName")

    @field_name.setter
    def field_name(self, value: str) -> None:
        jsii.set(self, "fieldName", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> str:
        """``AWS::AppSync::Resolver.TypeName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-typename
        """
        return jsii.get(self, "typeName")

    @type_name.setter
    def type_name(self, value: str) -> None:
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="cachingConfig")
    def caching_config(
        self,
    ) -> typing.Optional[typing.Union["CachingConfigProperty", _IResolvable_9ceae33e]]:
        """``AWS::AppSync::Resolver.CachingConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-cachingconfig
        """
        return jsii.get(self, "cachingConfig")

    @caching_config.setter
    def caching_config(
        self,
        value: typing.Optional[
            typing.Union["CachingConfigProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "cachingConfig", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceName")
    def data_source_name(self) -> typing.Optional[str]:
        """``AWS::AppSync::Resolver.DataSourceName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-datasourcename
        """
        return jsii.get(self, "dataSourceName")

    @data_source_name.setter
    def data_source_name(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "dataSourceName", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> typing.Optional[str]:
        """``AWS::AppSync::Resolver.Kind``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-kind
        """
        return jsii.get(self, "kind")

    @kind.setter
    def kind(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineConfig")
    def pipeline_config(
        self,
    ) -> typing.Optional[typing.Union["PipelineConfigProperty", _IResolvable_9ceae33e]]:
        """``AWS::AppSync::Resolver.PipelineConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-pipelineconfig
        """
        return jsii.get(self, "pipelineConfig")

    @pipeline_config.setter
    def pipeline_config(
        self,
        value: typing.Optional[
            typing.Union["PipelineConfigProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "pipelineConfig", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplate")
    def request_mapping_template(self) -> typing.Optional[str]:
        """``AWS::AppSync::Resolver.RequestMappingTemplate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplate
        """
        return jsii.get(self, "requestMappingTemplate")

    @request_mapping_template.setter
    def request_mapping_template(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "requestMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="requestMappingTemplateS3Location")
    def request_mapping_template_s3_location(self) -> typing.Optional[str]:
        """``AWS::AppSync::Resolver.RequestMappingTemplateS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplates3location
        """
        return jsii.get(self, "requestMappingTemplateS3Location")

    @request_mapping_template_s3_location.setter
    def request_mapping_template_s3_location(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "requestMappingTemplateS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplate")
    def response_mapping_template(self) -> typing.Optional[str]:
        """``AWS::AppSync::Resolver.ResponseMappingTemplate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplate
        """
        return jsii.get(self, "responseMappingTemplate")

    @response_mapping_template.setter
    def response_mapping_template(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "responseMappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="responseMappingTemplateS3Location")
    def response_mapping_template_s3_location(self) -> typing.Optional[str]:
        """``AWS::AppSync::Resolver.ResponseMappingTemplateS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplates3location
        """
        return jsii.get(self, "responseMappingTemplateS3Location")

    @response_mapping_template_s3_location.setter
    def response_mapping_template_s3_location(
        self, value: typing.Optional[str]
    ) -> None:
        jsii.set(self, "responseMappingTemplateS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="syncConfig")
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union["SyncConfigProperty", _IResolvable_9ceae33e]]:
        """``AWS::AppSync::Resolver.SyncConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-syncconfig
        """
        return jsii.get(self, "syncConfig")

    @sync_config.setter
    def sync_config(
        self,
        value: typing.Optional[
            typing.Union["SyncConfigProperty", _IResolvable_9ceae33e]
        ],
    ) -> None:
        jsii.set(self, "syncConfig", value)

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnResolver.CachingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"caching_keys": "cachingKeys", "ttl": "ttl"},
    )
    class CachingConfigProperty:
        def __init__(
            self,
            *,
            caching_keys: typing.Optional[typing.List[str]] = None,
            ttl: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param caching_keys: ``CfnResolver.CachingConfigProperty.CachingKeys``.
            :param ttl: ``CfnResolver.CachingConfigProperty.Ttl``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html
            """
            self._values = {}
            if caching_keys is not None:
                self._values["caching_keys"] = caching_keys
            if ttl is not None:
                self._values["ttl"] = ttl

        @builtins.property
        def caching_keys(self) -> typing.Optional[typing.List[str]]:
            """``CfnResolver.CachingConfigProperty.CachingKeys``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html#cfn-appsync-resolver-cachingconfig-cachingkeys
            """
            return self._values.get("caching_keys")

        @builtins.property
        def ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnResolver.CachingConfigProperty.Ttl``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html#cfn-appsync-resolver-cachingconfig-ttl
            """
            return self._values.get("ttl")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CachingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnResolver.LambdaConflictHandlerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_conflict_handler_arn": "lambdaConflictHandlerArn"},
    )
    class LambdaConflictHandlerConfigProperty:
        def __init__(
            self, *, lambda_conflict_handler_arn: typing.Optional[str] = None
        ) -> None:
            """
            :param lambda_conflict_handler_arn: ``CfnResolver.LambdaConflictHandlerConfigProperty.LambdaConflictHandlerArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html
            """
            self._values = {}
            if lambda_conflict_handler_arn is not None:
                self._values[
                    "lambda_conflict_handler_arn"
                ] = lambda_conflict_handler_arn

        @builtins.property
        def lambda_conflict_handler_arn(self) -> typing.Optional[str]:
            """``CfnResolver.LambdaConflictHandlerConfigProperty.LambdaConflictHandlerArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html#cfn-appsync-resolver-lambdaconflicthandlerconfig-lambdaconflicthandlerarn
            """
            return self._values.get("lambda_conflict_handler_arn")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConflictHandlerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnResolver.PipelineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"functions": "functions"},
    )
    class PipelineConfigProperty:
        def __init__(
            self, *, functions: typing.Optional[typing.List[str]] = None
        ) -> None:
            """
            :param functions: ``CfnResolver.PipelineConfigProperty.Functions``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html
            """
            self._values = {}
            if functions is not None:
                self._values["functions"] = functions

        @builtins.property
        def functions(self) -> typing.Optional[typing.List[str]]:
            """``CfnResolver.PipelineConfigProperty.Functions``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html#cfn-appsync-resolver-pipelineconfig-functions
            """
            return self._values.get("functions")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipelineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_appsync.CfnResolver.SyncConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "conflict_detection": "conflictDetection",
            "conflict_handler": "conflictHandler",
            "lambda_conflict_handler_config": "lambdaConflictHandlerConfig",
        },
    )
    class SyncConfigProperty:
        def __init__(
            self,
            *,
            conflict_detection: str,
            conflict_handler: typing.Optional[str] = None,
            lambda_conflict_handler_config: typing.Optional[
                typing.Union[
                    "CfnResolver.LambdaConflictHandlerConfigProperty",
                    _IResolvable_9ceae33e,
                ]
            ] = None,
        ) -> None:
            """
            :param conflict_detection: ``CfnResolver.SyncConfigProperty.ConflictDetection``.
            :param conflict_handler: ``CfnResolver.SyncConfigProperty.ConflictHandler``.
            :param lambda_conflict_handler_config: ``CfnResolver.SyncConfigProperty.LambdaConflictHandlerConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html
            """
            self._values = {
                "conflict_detection": conflict_detection,
            }
            if conflict_handler is not None:
                self._values["conflict_handler"] = conflict_handler
            if lambda_conflict_handler_config is not None:
                self._values[
                    "lambda_conflict_handler_config"
                ] = lambda_conflict_handler_config

        @builtins.property
        def conflict_detection(self) -> str:
            """``CfnResolver.SyncConfigProperty.ConflictDetection``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-conflictdetection
            """
            return self._values.get("conflict_detection")

        @builtins.property
        def conflict_handler(self) -> typing.Optional[str]:
            """``CfnResolver.SyncConfigProperty.ConflictHandler``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-conflicthandler
            """
            return self._values.get("conflict_handler")

        @builtins.property
        def lambda_conflict_handler_config(
            self,
        ) -> typing.Optional[
            typing.Union[
                "CfnResolver.LambdaConflictHandlerConfigProperty", _IResolvable_9ceae33e
            ]
        ]:
            """``CfnResolver.SyncConfigProperty.LambdaConflictHandlerConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-lambdaconflicthandlerconfig
            """
            return self._values.get("lambda_conflict_handler_config")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SyncConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.CfnResolverProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "field_name": "fieldName",
        "type_name": "typeName",
        "caching_config": "cachingConfig",
        "data_source_name": "dataSourceName",
        "kind": "kind",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "request_mapping_template_s3_location": "requestMappingTemplateS3Location",
        "response_mapping_template": "responseMappingTemplate",
        "response_mapping_template_s3_location": "responseMappingTemplateS3Location",
        "sync_config": "syncConfig",
    },
)
class CfnResolverProps:
    def __init__(
        self,
        *,
        api_id: str,
        field_name: str,
        type_name: str,
        caching_config: typing.Optional[
            typing.Union["CfnResolver.CachingConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        data_source_name: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
        pipeline_config: typing.Optional[
            typing.Union["CfnResolver.PipelineConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        request_mapping_template: typing.Optional[str] = None,
        request_mapping_template_s3_location: typing.Optional[str] = None,
        response_mapping_template: typing.Optional[str] = None,
        response_mapping_template_s3_location: typing.Optional[str] = None,
        sync_config: typing.Optional[
            typing.Union["CfnResolver.SyncConfigProperty", _IResolvable_9ceae33e]
        ] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::Resolver``.

        :param api_id: ``AWS::AppSync::Resolver.ApiId``.
        :param field_name: ``AWS::AppSync::Resolver.FieldName``.
        :param type_name: ``AWS::AppSync::Resolver.TypeName``.
        :param caching_config: ``AWS::AppSync::Resolver.CachingConfig``.
        :param data_source_name: ``AWS::AppSync::Resolver.DataSourceName``.
        :param kind: ``AWS::AppSync::Resolver.Kind``.
        :param pipeline_config: ``AWS::AppSync::Resolver.PipelineConfig``.
        :param request_mapping_template: ``AWS::AppSync::Resolver.RequestMappingTemplate``.
        :param request_mapping_template_s3_location: ``AWS::AppSync::Resolver.RequestMappingTemplateS3Location``.
        :param response_mapping_template: ``AWS::AppSync::Resolver.ResponseMappingTemplate``.
        :param response_mapping_template_s3_location: ``AWS::AppSync::Resolver.ResponseMappingTemplateS3Location``.
        :param sync_config: ``AWS::AppSync::Resolver.SyncConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html
        """
        self._values = {
            "api_id": api_id,
            "field_name": field_name,
            "type_name": type_name,
        }
        if caching_config is not None:
            self._values["caching_config"] = caching_config
        if data_source_name is not None:
            self._values["data_source_name"] = data_source_name
        if kind is not None:
            self._values["kind"] = kind
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if request_mapping_template_s3_location is not None:
            self._values[
                "request_mapping_template_s3_location"
            ] = request_mapping_template_s3_location
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if response_mapping_template_s3_location is not None:
            self._values[
                "response_mapping_template_s3_location"
            ] = response_mapping_template_s3_location
        if sync_config is not None:
            self._values["sync_config"] = sync_config

    @builtins.property
    def api_id(self) -> str:
        """``AWS::AppSync::Resolver.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-apiid
        """
        return self._values.get("api_id")

    @builtins.property
    def field_name(self) -> str:
        """``AWS::AppSync::Resolver.FieldName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-fieldname
        """
        return self._values.get("field_name")

    @builtins.property
    def type_name(self) -> str:
        """``AWS::AppSync::Resolver.TypeName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-typename
        """
        return self._values.get("type_name")

    @builtins.property
    def caching_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnResolver.CachingConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::Resolver.CachingConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-cachingconfig
        """
        return self._values.get("caching_config")

    @builtins.property
    def data_source_name(self) -> typing.Optional[str]:
        """``AWS::AppSync::Resolver.DataSourceName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-datasourcename
        """
        return self._values.get("data_source_name")

    @builtins.property
    def kind(self) -> typing.Optional[str]:
        """``AWS::AppSync::Resolver.Kind``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-kind
        """
        return self._values.get("kind")

    @builtins.property
    def pipeline_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnResolver.PipelineConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::Resolver.PipelineConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-pipelineconfig
        """
        return self._values.get("pipeline_config")

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[str]:
        """``AWS::AppSync::Resolver.RequestMappingTemplate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplate
        """
        return self._values.get("request_mapping_template")

    @builtins.property
    def request_mapping_template_s3_location(self) -> typing.Optional[str]:
        """``AWS::AppSync::Resolver.RequestMappingTemplateS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplates3location
        """
        return self._values.get("request_mapping_template_s3_location")

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[str]:
        """``AWS::AppSync::Resolver.ResponseMappingTemplate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplate
        """
        return self._values.get("response_mapping_template")

    @builtins.property
    def response_mapping_template_s3_location(self) -> typing.Optional[str]:
        """``AWS::AppSync::Resolver.ResponseMappingTemplateS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplates3location
        """
        return self._values.get("response_mapping_template_s3_location")

    @builtins.property
    def sync_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnResolver.SyncConfigProperty", _IResolvable_9ceae33e]
    ]:
        """``AWS::AppSync::Resolver.SyncConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-syncconfig
        """
        return self._values.get("sync_config")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.ExtendedDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "dynamo_db_config": "dynamoDbConfig",
        "elasticsearch_config": "elasticsearchConfig",
        "http_config": "httpConfig",
        "lambda_config": "lambdaConfig",
        "relational_database_config": "relationalDatabaseConfig",
    },
)
class ExtendedDataSourceProps:
    def __init__(
        self,
        *,
        type: str,
        dynamo_db_config: typing.Optional[
            typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        elasticsearch_config: typing.Optional[
            typing.Union[
                "CfnDataSource.ElasticsearchConfigProperty", _IResolvable_9ceae33e
            ]
        ] = None,
        http_config: typing.Optional[
            typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        lambda_config: typing.Optional[
            typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        relational_database_config: typing.Optional[
            typing.Union[
                "CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_9ceae33e
            ]
        ] = None,
    ) -> None:
        """props used by implementations of BaseDataSource to provide configuration.

        Should not be used directly.

        :param type: the type of the AppSync datasource.
        :param dynamo_db_config: configuration for DynamoDB Datasource. Default: - No config
        :param elasticsearch_config: configuration for Elasticsearch Datasource. Default: - No config
        :param http_config: configuration for HTTP Datasource. Default: - No config
        :param lambda_config: configuration for Lambda Datasource. Default: - No config
        :param relational_database_config: configuration for RDS Datasource. Default: - No config

        stability
        :stability: experimental
        """
        self._values = {
            "type": type,
        }
        if dynamo_db_config is not None:
            self._values["dynamo_db_config"] = dynamo_db_config
        if elasticsearch_config is not None:
            self._values["elasticsearch_config"] = elasticsearch_config
        if http_config is not None:
            self._values["http_config"] = http_config
        if lambda_config is not None:
            self._values["lambda_config"] = lambda_config
        if relational_database_config is not None:
            self._values["relational_database_config"] = relational_database_config

    @builtins.property
    def type(self) -> str:
        """the type of the AppSync datasource.

        stability
        :stability: experimental
        """
        return self._values.get("type")

    @builtins.property
    def dynamo_db_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_9ceae33e]
    ]:
        """configuration for DynamoDB Datasource.

        default
        :default: - No config

        stability
        :stability: experimental
        """
        return self._values.get("dynamo_db_config")

    @builtins.property
    def elasticsearch_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnDataSource.ElasticsearchConfigProperty", _IResolvable_9ceae33e]
    ]:
        """configuration for Elasticsearch Datasource.

        default
        :default: - No config

        stability
        :stability: experimental
        """
        return self._values.get("elasticsearch_config")

    @builtins.property
    def http_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_9ceae33e]
    ]:
        """configuration for HTTP Datasource.

        default
        :default: - No config

        stability
        :stability: experimental
        """
        return self._values.get("http_config")

    @builtins.property
    def lambda_config(
        self,
    ) -> typing.Optional[
        typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_9ceae33e]
    ]:
        """configuration for Lambda Datasource.

        default
        :default: - No config

        stability
        :stability: experimental
        """
        return self._values.get("lambda_config")

    @builtins.property
    def relational_database_config(
        self,
    ) -> typing.Optional[
        typing.Union[
            "CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_9ceae33e
        ]
    ]:
        """configuration for RDS Datasource.

        default
        :default: - No config

        stability
        :stability: experimental
        """
        return self._values.get("relational_database_config")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtendedDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk-experiment.aws_appsync.FieldLogLevel")
class FieldLogLevel(enum.Enum):
    """log-level for fields in AppSync.

    stability
    :stability: experimental
    """

    NONE = "NONE"
    """No logging.

    stability
    :stability: experimental
    """
    ERROR = "ERROR"
    """Error logging.

    stability
    :stability: experimental
    """
    ALL = "ALL"
    """All logging.

    stability
    :stability: experimental
    """


class GraphQLApi(
    _Construct_f50a3f53,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.GraphQLApi",
):
    """An AppSync GraphQL API.

    stability
    :stability: experimental
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        name: str,
        schema_definition: "SchemaDefinition",
        authorization_config: typing.Optional["AuthorizationConfig"] = None,
        log_config: typing.Optional["LogConfig"] = None,
        schema_definition_file: typing.Optional[str] = None,
        xray_enabled: typing.Optional[bool] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param name: the name of the GraphQL API.
        :param schema_definition: GraphQL schema definition. Specify how you want to define your schema. SchemaDefinition.CODE allows schema definition through CDK SchemaDefinition.FILE allows schema definition through schema.graphql file
        :param authorization_config: Optional authorization configuration. Default: - API Key authorization
        :param log_config: Logging configuration for this api. Default: - None
        :param schema_definition_file: File containing the GraphQL schema definition. You have to specify a definition or a file containing one. Default: - Use schemaDefinition
        :param xray_enabled: A flag indicating whether or not X-Ray tracing is enabled for the GraphQL API. Default: - false

        stability
        :stability: experimental
        """
        props = GraphQLApiProps(
            name=name,
            schema_definition=schema_definition,
            authorization_config=authorization_config,
            log_config=log_config,
            schema_definition_file=schema_definition_file,
            xray_enabled=xray_enabled,
        )

        jsii.create(GraphQLApi, self, [scope, id, props])

    @jsii.member(jsii_name="addDynamoDbDataSource")
    def add_dynamo_db_data_source(
        self, name: str, description: str, table: _ITable_e6850701
    ) -> "DynamoDbDataSource":
        """add a new DynamoDB data source to this API.

        :param name: The name of the data source.
        :param description: The description of the data source.
        :param table: The DynamoDB table backing this data source [disable-awslint:ref-via-interface].

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addDynamoDbDataSource", [name, description, table])

    @jsii.member(jsii_name="addHttpDataSource")
    def add_http_data_source(
        self, name: str, description: str, endpoint: str
    ) -> "HttpDataSource":
        """add a new http data source to this API.

        :param name: The name of the data source.
        :param description: The description of the data source.
        :param endpoint: The http endpoint.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addHttpDataSource", [name, description, endpoint])

    @jsii.member(jsii_name="addLambdaDataSource")
    def add_lambda_data_source(
        self, name: str, description: str, lambda_function: _IFunction_1c1de0bc
    ) -> "LambdaDataSource":
        """add a new Lambda data source to this API.

        :param name: The name of the data source.
        :param description: The description of the data source.
        :param lambda_function: The Lambda function to call to interact with this data source.

        stability
        :stability: experimental
        """
        return jsii.invoke(
            self, "addLambdaDataSource", [name, description, lambda_function]
        )

    @jsii.member(jsii_name="addNoneDataSource")
    def add_none_data_source(self, name: str, description: str) -> "NoneDataSource":
        """add a new dummy data source to this API.

        :param name: The name of the data source.
        :param description: The description of the data source.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addNoneDataSource", [name, description])

    @jsii.member(jsii_name="grant")
    def grant(
        self, grantee: _IGrantable_0fcfc53a, resources: "IamResource", *actions: str
    ) -> _Grant_96af6d2d:
        """Adds an IAM policy statement associated with this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param resources: The set of resources to allow (i.e. ...:[region]:[accountId]:apis/GraphQLId/...).
        :param actions: The actions that should be granted to the principal (i.e. appsync:graphql ).

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grant", [grantee, resources, *actions])

    @jsii.member(jsii_name="grantMutation")
    def grant_mutation(
        self, grantee: _IGrantable_0fcfc53a, *fields: str
    ) -> _Grant_96af6d2d:
        """Adds an IAM policy statement for Mutation access to this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param fields: The fields to grant access to that are Mutations (leave blank for all).

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantMutation", [grantee, *fields])

    @jsii.member(jsii_name="grantQuery")
    def grant_query(
        self, grantee: _IGrantable_0fcfc53a, *fields: str
    ) -> _Grant_96af6d2d:
        """Adds an IAM policy statement for Query access to this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param fields: The fields to grant access to that are Queries (leave blank for all).

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantQuery", [grantee, *fields])

    @jsii.member(jsii_name="grantSubscription")
    def grant_subscription(
        self, grantee: _IGrantable_0fcfc53a, *fields: str
    ) -> _Grant_96af6d2d:
        """Adds an IAM policy statement for Subscription access to this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param fields: The fields to grant access to that are Subscriptions (leave blank for all).

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantSubscription", [grantee, *fields])

    @jsii.member(jsii_name="updateDefinition")
    def update_definition(self, definition: str) -> None:
        """Sets schema defintiion to input if schema mode is configured with SchemaDefinition.CODE.

        :param definition: string that is the graphql representation of schema.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "updateDefinition", [definition])

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """the id of the GraphQL API.

        stability
        :stability: experimental
        """
        return jsii.get(self, "apiId")

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> str:
        """the ARN of the API.

        stability
        :stability: experimental
        """
        return jsii.get(self, "arn")

    @builtins.property
    @jsii.member(jsii_name="graphQlUrl")
    def graph_ql_url(self) -> str:
        """the URL of the endpoint created by AppSync.

        stability
        :stability: experimental
        """
        return jsii.get(self, "graphQlUrl")

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """the name of the API.

        stability
        :stability: experimental
        """
        return jsii.get(self, "name")

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> "CfnGraphQLSchema":
        """underlying CFN schema resource.

        stability
        :stability: experimental
        """
        return jsii.get(self, "schema")

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> typing.Optional[str]:
        """the configured API key, if present.

        stability
        :stability: experimental
        """
        return jsii.get(self, "apiKey")


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.GraphQLApiProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "schema_definition": "schemaDefinition",
        "authorization_config": "authorizationConfig",
        "log_config": "logConfig",
        "schema_definition_file": "schemaDefinitionFile",
        "xray_enabled": "xrayEnabled",
    },
)
class GraphQLApiProps:
    def __init__(
        self,
        *,
        name: str,
        schema_definition: "SchemaDefinition",
        authorization_config: typing.Optional["AuthorizationConfig"] = None,
        log_config: typing.Optional["LogConfig"] = None,
        schema_definition_file: typing.Optional[str] = None,
        xray_enabled: typing.Optional[bool] = None,
    ) -> None:
        """Properties for an AppSync GraphQL API.

        :param name: the name of the GraphQL API.
        :param schema_definition: GraphQL schema definition. Specify how you want to define your schema. SchemaDefinition.CODE allows schema definition through CDK SchemaDefinition.FILE allows schema definition through schema.graphql file
        :param authorization_config: Optional authorization configuration. Default: - API Key authorization
        :param log_config: Logging configuration for this api. Default: - None
        :param schema_definition_file: File containing the GraphQL schema definition. You have to specify a definition or a file containing one. Default: - Use schemaDefinition
        :param xray_enabled: A flag indicating whether or not X-Ray tracing is enabled for the GraphQL API. Default: - false

        stability
        :stability: experimental
        """
        if isinstance(authorization_config, dict):
            authorization_config = AuthorizationConfig(**authorization_config)
        if isinstance(log_config, dict):
            log_config = LogConfig(**log_config)
        self._values = {
            "name": name,
            "schema_definition": schema_definition,
        }
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config
        if log_config is not None:
            self._values["log_config"] = log_config
        if schema_definition_file is not None:
            self._values["schema_definition_file"] = schema_definition_file
        if xray_enabled is not None:
            self._values["xray_enabled"] = xray_enabled

    @builtins.property
    def name(self) -> str:
        """the name of the GraphQL API.

        stability
        :stability: experimental
        """
        return self._values.get("name")

    @builtins.property
    def schema_definition(self) -> "SchemaDefinition":
        """GraphQL schema definition. Specify how you want to define your schema.

        SchemaDefinition.CODE allows schema definition through CDK
        SchemaDefinition.FILE allows schema definition through schema.graphql file

        stability
        :stability: experimental
        """
        return self._values.get("schema_definition")

    @builtins.property
    def authorization_config(self) -> typing.Optional["AuthorizationConfig"]:
        """Optional authorization configuration.

        default
        :default: - API Key authorization

        stability
        :stability: experimental
        """
        return self._values.get("authorization_config")

    @builtins.property
    def log_config(self) -> typing.Optional["LogConfig"]:
        """Logging configuration for this api.

        default
        :default: - None

        stability
        :stability: experimental
        """
        return self._values.get("log_config")

    @builtins.property
    def schema_definition_file(self) -> typing.Optional[str]:
        """File containing the GraphQL schema definition.

        You have to specify a definition or a file containing one.

        default
        :default: - Use schemaDefinition

        stability
        :stability: experimental
        """
        return self._values.get("schema_definition_file")

    @builtins.property
    def xray_enabled(self) -> typing.Optional[bool]:
        """A flag indicating whether or not X-Ray tracing is enabled for the GraphQL API.

        default
        :default: - false

        stability
        :stability: experimental
        """
        return self._values.get("xray_enabled")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphQLApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HttpDataSource(
    BaseDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.HttpDataSource",
):
    """An AppSync datasource backed by a http endpoint.

    stability
    :stability: experimental
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        endpoint: str,
        api: "GraphQLApi",
        name: str,
        description: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param endpoint: The http endpoint.
        :param api: The API to attach this data source to.
        :param name: The name of the data source.
        :param description: the description of the data source. Default: - None

        stability
        :stability: experimental
        """
        props = HttpDataSourceProps(
            endpoint=endpoint, api=api, name=name, description=description
        )

        jsii.create(HttpDataSource, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.HttpDataSourceProps",
    jsii_struct_bases=[BaseDataSourceProps],
    name_mapping={
        "api": "api",
        "name": "name",
        "description": "description",
        "endpoint": "endpoint",
    },
)
class HttpDataSourceProps(BaseDataSourceProps):
    def __init__(
        self,
        *,
        api: "GraphQLApi",
        name: str,
        description: typing.Optional[str] = None,
        endpoint: str,
    ) -> None:
        """Properties for an AppSync http datasource.

        :param api: The API to attach this data source to.
        :param name: The name of the data source.
        :param description: the description of the data source. Default: - None
        :param endpoint: The http endpoint.

        stability
        :stability: experimental
        """
        self._values = {
            "api": api,
            "name": name,
            "endpoint": endpoint,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def api(self) -> "GraphQLApi":
        """The API to attach this data source to.

        stability
        :stability: experimental
        """
        return self._values.get("api")

    @builtins.property
    def name(self) -> str:
        """The name of the data source.

        stability
        :stability: experimental
        """
        return self._values.get("name")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """the description of the data source.

        default
        :default: - None

        stability
        :stability: experimental
        """
        return self._values.get("description")

    @builtins.property
    def endpoint(self) -> str:
        """The http endpoint.

        stability
        :stability: experimental
        """
        return self._values.get("endpoint")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IamResource(
    metaclass=jsii.JSIIMeta, jsii_type="monocdk-experiment.aws_appsync.IamResource"
):
    """A class used to generate resource arns for AppSync.

    stability
    :stability: experimental
    """

    @jsii.member(jsii_name="all")
    @builtins.classmethod
    def all(cls) -> "IamResource":
        """Generate the resource names that accepts all types: ``*``.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "all", [])

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(cls, *arns: str) -> "IamResource":
        """Generate the resource names given custom arns.

        :param arns: The custom arns that need to be permissioned. Example: custom('/types/Query/fields/getExample')

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "custom", [*arns])

    @jsii.member(jsii_name="ofType")
    @builtins.classmethod
    def of_type(cls, type: str, *fields: str) -> "IamResource":
        """Generate the resource names given a type and fields.

        :param type: The type that needs to be allowed.
        :param fields: The fields that need to be allowed, if empty grant permissions to ALL fields. Example: ofType('Query', 'GetExample')

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "ofType", [type, *fields])

    @jsii.member(jsii_name="resourceArns")
    def resource_arns(self, api: "GraphQLApi") -> typing.List[str]:
        """Return the Resource ARN.

        :param api: The GraphQL API to give permissions.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "resourceArns", [api])


class KeyCondition(
    metaclass=jsii.JSIIMeta, jsii_type="monocdk-experiment.aws_appsync.KeyCondition"
):
    """Factory class for DynamoDB key conditions.

    stability
    :stability: experimental
    """

    @jsii.member(jsii_name="beginsWith")
    @builtins.classmethod
    def begins_with(cls, key_name: str, arg: str) -> "KeyCondition":
        """Condition (k, arg).

        True if the key attribute k begins with the Query argument.

        :param key_name: -
        :param arg: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "beginsWith", [key_name, arg])

    @jsii.member(jsii_name="between")
    @builtins.classmethod
    def between(cls, key_name: str, arg1: str, arg2: str) -> "KeyCondition":
        """Condition k BETWEEN arg1 AND arg2, true if k >= arg1 and k <= arg2.

        :param key_name: -
        :param arg1: -
        :param arg2: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "between", [key_name, arg1, arg2])

    @jsii.member(jsii_name="eq")
    @builtins.classmethod
    def eq(cls, key_name: str, arg: str) -> "KeyCondition":
        """Condition k = arg, true if the key attribute k is equal to the Query argument.

        :param key_name: -
        :param arg: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "eq", [key_name, arg])

    @jsii.member(jsii_name="ge")
    @builtins.classmethod
    def ge(cls, key_name: str, arg: str) -> "KeyCondition":
        """Condition k >= arg, true if the key attribute k is greater or equal to the Query argument.

        :param key_name: -
        :param arg: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "ge", [key_name, arg])

    @jsii.member(jsii_name="gt")
    @builtins.classmethod
    def gt(cls, key_name: str, arg: str) -> "KeyCondition":
        """Condition k > arg, true if the key attribute k is greater than the the Query argument.

        :param key_name: -
        :param arg: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "gt", [key_name, arg])

    @jsii.member(jsii_name="le")
    @builtins.classmethod
    def le(cls, key_name: str, arg: str) -> "KeyCondition":
        """Condition k <= arg, true if the key attribute k is less than or equal to the Query argument.

        :param key_name: -
        :param arg: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "le", [key_name, arg])

    @jsii.member(jsii_name="lt")
    @builtins.classmethod
    def lt(cls, key_name: str, arg: str) -> "KeyCondition":
        """Condition k < arg, true if the key attribute k is less than the Query argument.

        :param key_name: -
        :param arg: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "lt", [key_name, arg])

    @jsii.member(jsii_name="and")
    def and_(self, key_cond: "KeyCondition") -> "KeyCondition":
        """Conjunction between two conditions.

        :param key_cond: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "and", [key_cond])

    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> str:
        """Renders the key condition to a VTL string.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderTemplate", [])


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.LogConfig",
    jsii_struct_bases=[],
    name_mapping={
        "exclude_verbose_content": "excludeVerboseContent",
        "field_log_level": "fieldLogLevel",
    },
)
class LogConfig:
    def __init__(
        self,
        *,
        exclude_verbose_content: typing.Optional[
            typing.Union[bool, _IResolvable_9ceae33e]
        ] = None,
        field_log_level: typing.Optional["FieldLogLevel"] = None,
    ) -> None:
        """Logging configuration for AppSync.

        :param exclude_verbose_content: exclude verbose content. Default: false
        :param field_log_level: log level for fields. Default: - Use AppSync default

        stability
        :stability: experimental
        """
        self._values = {}
        if exclude_verbose_content is not None:
            self._values["exclude_verbose_content"] = exclude_verbose_content
        if field_log_level is not None:
            self._values["field_log_level"] = field_log_level

    @builtins.property
    def exclude_verbose_content(
        self,
    ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
        """exclude verbose content.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get("exclude_verbose_content")

    @builtins.property
    def field_log_level(self) -> typing.Optional["FieldLogLevel"]:
        """log level for fields.

        default
        :default: - Use AppSync default

        stability
        :stability: experimental
        """
        return self._values.get("field_log_level")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MappingTemplate(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk-experiment.aws_appsync.MappingTemplate",
):
    """MappingTemplates for AppSync resolvers.

    stability
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _MappingTemplateProxy

    def __init__(self) -> None:
        jsii.create(MappingTemplate, self, [])

    @jsii.member(jsii_name="dynamoDbDeleteItem")
    @builtins.classmethod
    def dynamo_db_delete_item(cls, key_name: str, id_arg: str) -> "MappingTemplate":
        """Mapping template to delete a single item from a DynamoDB table.

        :param key_name: the name of the hash key field.
        :param id_arg: the name of the Mutation argument.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbDeleteItem", [key_name, id_arg])

    @jsii.member(jsii_name="dynamoDbGetItem")
    @builtins.classmethod
    def dynamo_db_get_item(cls, key_name: str, id_arg: str) -> "MappingTemplate":
        """Mapping template to get a single item from a DynamoDB table.

        :param key_name: the name of the hash key field.
        :param id_arg: the name of the Query argument.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbGetItem", [key_name, id_arg])

    @jsii.member(jsii_name="dynamoDbPutItem")
    @builtins.classmethod
    def dynamo_db_put_item(
        cls, key: "PrimaryKey", values: "AttributeValues"
    ) -> "MappingTemplate":
        """Mapping template to save a single item to a DynamoDB table.

        :param key: the assigment of Mutation values to the primary key.
        :param values: the assignment of Mutation values to the table attributes.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbPutItem", [key, values])

    @jsii.member(jsii_name="dynamoDbQuery")
    @builtins.classmethod
    def dynamo_db_query(cls, cond: "KeyCondition") -> "MappingTemplate":
        """Mapping template to query a set of items from a DynamoDB table.

        :param cond: the key condition for the query.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbQuery", [cond])

    @jsii.member(jsii_name="dynamoDbResultItem")
    @builtins.classmethod
    def dynamo_db_result_item(cls) -> "MappingTemplate":
        """Mapping template for a single result item from DynamoDB.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbResultItem", [])

    @jsii.member(jsii_name="dynamoDbResultList")
    @builtins.classmethod
    def dynamo_db_result_list(cls) -> "MappingTemplate":
        """Mapping template for a result list from DynamoDB.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbResultList", [])

    @jsii.member(jsii_name="dynamoDbScanTable")
    @builtins.classmethod
    def dynamo_db_scan_table(cls) -> "MappingTemplate":
        """Mapping template to scan a DynamoDB table to fetch all entries.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbScanTable", [])

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(cls, file_name: str) -> "MappingTemplate":
        """Create a mapping template from the given file.

        :param file_name: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromFile", [file_name])

    @jsii.member(jsii_name="fromString")
    @builtins.classmethod
    def from_string(cls, template: str) -> "MappingTemplate":
        """Create a mapping template from the given string.

        :param template: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromString", [template])

    @jsii.member(jsii_name="lambdaRequest")
    @builtins.classmethod
    def lambda_request(cls, payload: typing.Optional[str] = None) -> "MappingTemplate":
        """Mapping template to invoke a Lambda function.

        :param payload: the VTL template snippet of the payload to send to the lambda. If no payload is provided all available context fields are sent to the Lambda function

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "lambdaRequest", [payload])

    @jsii.member(jsii_name="lambdaResult")
    @builtins.classmethod
    def lambda_result(cls) -> "MappingTemplate":
        """Mapping template to return the Lambda result to the caller.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "lambdaResult", [])

    @jsii.member(jsii_name="renderTemplate")
    @abc.abstractmethod
    def render_template(self) -> str:
        """this is called to render the mapping template to a VTL string.

        stability
        :stability: experimental
        """
        ...


class _MappingTemplateProxy(MappingTemplate):
    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> str:
        """this is called to render the mapping template to a VTL string.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderTemplate", [])


class NoneDataSource(
    BaseDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.NoneDataSource",
):
    """An AppSync dummy datasource.

    stability
    :stability: experimental
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        api: "GraphQLApi",
        name: str,
        description: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param api: The API to attach this data source to.
        :param name: The name of the data source.
        :param description: the description of the data source. Default: - None

        stability
        :stability: experimental
        """
        props = NoneDataSourceProps(api=api, name=name, description=description)

        jsii.create(NoneDataSource, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.NoneDataSourceProps",
    jsii_struct_bases=[BaseDataSourceProps],
    name_mapping={"api": "api", "name": "name", "description": "description"},
)
class NoneDataSourceProps(BaseDataSourceProps):
    def __init__(
        self, *, api: "GraphQLApi", name: str, description: typing.Optional[str] = None
    ) -> None:
        """Properties for an AppSync dummy datasource.

        :param api: The API to attach this data source to.
        :param name: The name of the data source.
        :param description: the description of the data source. Default: - None

        stability
        :stability: experimental
        """
        self._values = {
            "api": api,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def api(self) -> "GraphQLApi":
        """The API to attach this data source to.

        stability
        :stability: experimental
        """
        return self._values.get("api")

    @builtins.property
    def name(self) -> str:
        """The name of the data source.

        stability
        :stability: experimental
        """
        return self._values.get("name")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """the description of the data source.

        default
        :default: - None

        stability
        :stability: experimental
        """
        return self._values.get("description")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NoneDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.OpenIdConnectConfig",
    jsii_struct_bases=[],
    name_mapping={
        "oidc_provider": "oidcProvider",
        "client_id": "clientId",
        "token_expiry_from_auth": "tokenExpiryFromAuth",
        "token_expiry_from_issue": "tokenExpiryFromIssue",
    },
)
class OpenIdConnectConfig:
    def __init__(
        self,
        *,
        oidc_provider: str,
        client_id: typing.Optional[str] = None,
        token_expiry_from_auth: typing.Optional[jsii.Number] = None,
        token_expiry_from_issue: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Configuration for OpenID Connect authorization in AppSync.

        :param oidc_provider: The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of ``iss`` in the OIDC token.
        :param client_id: The client identifier of the Relying party at the OpenID identity provider. A regular expression can be specified so AppSync can validate against multiple client identifiers at a time. Default: - - (All)
        :param token_expiry_from_auth: The number of milliseconds an OIDC token is valid after being authenticated by OIDC provider. ``auth_time`` claim in OIDC token is required for this validation to work. Default: - no validation
        :param token_expiry_from_issue: The number of milliseconds an OIDC token is valid after being issued to a user. This validation uses ``iat`` claim of OIDC token. Default: - no validation

        stability
        :stability: experimental
        """
        self._values = {
            "oidc_provider": oidc_provider,
        }
        if client_id is not None:
            self._values["client_id"] = client_id
        if token_expiry_from_auth is not None:
            self._values["token_expiry_from_auth"] = token_expiry_from_auth
        if token_expiry_from_issue is not None:
            self._values["token_expiry_from_issue"] = token_expiry_from_issue

    @builtins.property
    def oidc_provider(self) -> str:
        """The issuer for the OIDC configuration.

        The issuer returned by discovery must exactly match the value of ``iss`` in the OIDC token.

        stability
        :stability: experimental
        """
        return self._values.get("oidc_provider")

    @builtins.property
    def client_id(self) -> typing.Optional[str]:
        """The client identifier of the Relying party at the OpenID identity provider.

        A regular expression can be specified so AppSync can validate against multiple client identifiers at a time.

        default
        :default:

        -
          - (All)

        stability
        :stability: experimental

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            -"ABCD|CDEF"whereABCDandCDEFaretwodifferentclient_id
        """
        return self._values.get("client_id")

    @builtins.property
    def token_expiry_from_auth(self) -> typing.Optional[jsii.Number]:
        """The number of milliseconds an OIDC token is valid after being authenticated by OIDC provider.

        ``auth_time`` claim in OIDC token is required for this validation to work.

        default
        :default: - no validation

        stability
        :stability: experimental
        """
        return self._values.get("token_expiry_from_auth")

    @builtins.property
    def token_expiry_from_issue(self) -> typing.Optional[jsii.Number]:
        """The number of milliseconds an OIDC token is valid after being issued to a user.

        This validation uses ``iat`` claim of OIDC token.

        default
        :default: - no validation

        stability
        :stability: experimental
        """
        return self._values.get("token_expiry_from_issue")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenIdConnectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PartitionKeyStep(
    metaclass=jsii.JSIIMeta, jsii_type="monocdk-experiment.aws_appsync.PartitionKeyStep"
):
    """Utility class to allow assigning a value or an auto-generated id to a partition key.

    stability
    :stability: experimental
    """

    def __init__(self, key: str) -> None:
        """
        :param key: -

        stability
        :stability: experimental
        """
        jsii.create(PartitionKeyStep, self, [key])

    @jsii.member(jsii_name="auto")
    def auto(self) -> "PartitionKey":
        """Assign an auto-generated value to the partition key.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "auto", [])

    @jsii.member(jsii_name="is")
    def is_(self, val: str) -> "PartitionKey":
        """Assign an auto-generated value to the partition key.

        :param val: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "is", [val])


class PrimaryKey(
    metaclass=jsii.JSIIMeta, jsii_type="monocdk-experiment.aws_appsync.PrimaryKey"
):
    """Specifies the assignment to the primary key.

    It either
    contains the full primary key or only the partition key.

    stability
    :stability: experimental
    """

    def __init__(self, pkey: "Assign", skey: typing.Optional["Assign"] = None) -> None:
        """
        :param pkey: -
        :param skey: -

        stability
        :stability: experimental
        """
        jsii.create(PrimaryKey, self, [pkey, skey])

    @jsii.member(jsii_name="partition")
    @builtins.classmethod
    def partition(cls, key: str) -> "PartitionKeyStep":
        """Allows assigning a value to the partition key.

        :param key: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "partition", [key])

    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> str:
        """Renders the key assignment to a VTL string.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderTemplate", [])

    @builtins.property
    @jsii.member(jsii_name="pkey")
    def _pkey(self) -> "Assign":
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "pkey")


class Resolver(
    _Construct_f50a3f53,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.Resolver",
):
    """An AppSync resolver.

    stability
    :stability: experimental
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        api: "GraphQLApi",
        data_source: typing.Optional["BaseDataSource"] = None,
        field_name: str,
        type_name: str,
        pipeline_config: typing.Optional[typing.List[str]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param api: The API this resolver is attached to.
        :param data_source: The data source this resolver is using. Default: - No datasource
        :param field_name: name of the GraphQL fiel din the given type this resolver is attached to.
        :param type_name: name of the GraphQL type this resolver is attached to.
        :param pipeline_config: configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: The response mapping template for this resolver. Default: - No mapping template

        stability
        :stability: experimental
        """
        props = ResolverProps(
            api=api,
            data_source=data_source,
            field_name=field_name,
            type_name=type_name,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        jsii.create(Resolver, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> str:
        """the ARN of the resolver.

        stability
        :stability: experimental
        """
        return jsii.get(self, "arn")


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.ResolverProps",
    jsii_struct_bases=[BaseResolverProps],
    name_mapping={
        "field_name": "fieldName",
        "type_name": "typeName",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "api": "api",
        "data_source": "dataSource",
    },
)
class ResolverProps(BaseResolverProps):
    def __init__(
        self,
        *,
        field_name: str,
        type_name: str,
        pipeline_config: typing.Optional[typing.List[str]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
        api: "GraphQLApi",
        data_source: typing.Optional["BaseDataSource"] = None,
    ) -> None:
        """Additional properties for an AppSync resolver like GraphQL API reference and datasource.

        :param field_name: name of the GraphQL fiel din the given type this resolver is attached to.
        :param type_name: name of the GraphQL type this resolver is attached to.
        :param pipeline_config: configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: The response mapping template for this resolver. Default: - No mapping template
        :param api: The API this resolver is attached to.
        :param data_source: The data source this resolver is using. Default: - No datasource

        stability
        :stability: experimental
        """
        self._values = {
            "field_name": field_name,
            "type_name": type_name,
            "api": api,
        }
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if data_source is not None:
            self._values["data_source"] = data_source

    @builtins.property
    def field_name(self) -> str:
        """name of the GraphQL fiel din the given type this resolver is attached to.

        stability
        :stability: experimental
        """
        return self._values.get("field_name")

    @builtins.property
    def type_name(self) -> str:
        """name of the GraphQL type this resolver is attached to.

        stability
        :stability: experimental
        """
        return self._values.get("type_name")

    @builtins.property
    def pipeline_config(self) -> typing.Optional[typing.List[str]]:
        """configuration of the pipeline resolver.

        default
        :default:

        - no pipeline resolver configuration
          An empty array | undefined sets resolver to be of kind, unit

        stability
        :stability: experimental
        """
        return self._values.get("pipeline_config")

    @builtins.property
    def request_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        """The request mapping template for this resolver.

        default
        :default: - No mapping template

        stability
        :stability: experimental
        """
        return self._values.get("request_mapping_template")

    @builtins.property
    def response_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        """The response mapping template for this resolver.

        default
        :default: - No mapping template

        stability
        :stability: experimental
        """
        return self._values.get("response_mapping_template")

    @builtins.property
    def api(self) -> "GraphQLApi":
        """The API this resolver is attached to.

        stability
        :stability: experimental
        """
        return self._values.get("api")

    @builtins.property
    def data_source(self) -> typing.Optional["BaseDataSource"]:
        """The data source this resolver is using.

        default
        :default: - No datasource

        stability
        :stability: experimental
        """
        return self._values.get("data_source")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk-experiment.aws_appsync.SchemaDefinition")
class SchemaDefinition(enum.Enum):
    """Enum containing the different modes of schema definition.

    stability
    :stability: experimental
    """

    CODE = "CODE"
    """Define schema through functions like addType, addQuery, etc.

    stability
    :stability: experimental
    """
    FILE = "FILE"
    """Define schema in a file, i.e. schema.graphql.

    stability
    :stability: experimental
    """


class SortKeyStep(
    metaclass=jsii.JSIIMeta, jsii_type="monocdk-experiment.aws_appsync.SortKeyStep"
):
    """Utility class to allow assigning a value or an auto-generated id to a sort key.

    stability
    :stability: experimental
    """

    def __init__(self, pkey: "Assign", skey: str) -> None:
        """
        :param pkey: -
        :param skey: -

        stability
        :stability: experimental
        """
        jsii.create(SortKeyStep, self, [pkey, skey])

    @jsii.member(jsii_name="auto")
    def auto(self) -> "PrimaryKey":
        """Assign an auto-generated value to the sort key.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "auto", [])

    @jsii.member(jsii_name="is")
    def is_(self, val: str) -> "PrimaryKey":
        """Assign an auto-generated value to the sort key.

        :param val: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "is", [val])


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.UserPoolConfig",
    jsii_struct_bases=[],
    name_mapping={
        "user_pool": "userPool",
        "app_id_client_regex": "appIdClientRegex",
        "default_action": "defaultAction",
    },
)
class UserPoolConfig:
    def __init__(
        self,
        *,
        user_pool: _IUserPool_e9547b0f,
        app_id_client_regex: typing.Optional[str] = None,
        default_action: typing.Optional["UserPoolDefaultAction"] = None,
    ) -> None:
        """Configuration for Cognito user-pools in AppSync.

        :param user_pool: The Cognito user pool to use as identity source.
        :param app_id_client_regex: the optional app id regex. Default: - None
        :param default_action: Default auth action. Default: ALLOW

        stability
        :stability: experimental
        """
        self._values = {
            "user_pool": user_pool,
        }
        if app_id_client_regex is not None:
            self._values["app_id_client_regex"] = app_id_client_regex
        if default_action is not None:
            self._values["default_action"] = default_action

    @builtins.property
    def user_pool(self) -> _IUserPool_e9547b0f:
        """The Cognito user pool to use as identity source.

        stability
        :stability: experimental
        """
        return self._values.get("user_pool")

    @builtins.property
    def app_id_client_regex(self) -> typing.Optional[str]:
        """the optional app id regex.

        default
        :default: - None

        stability
        :stability: experimental
        """
        return self._values.get("app_id_client_regex")

    @builtins.property
    def default_action(self) -> typing.Optional["UserPoolDefaultAction"]:
        """Default auth action.

        default
        :default: ALLOW

        stability
        :stability: experimental
        """
        return self._values.get("default_action")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk-experiment.aws_appsync.UserPoolDefaultAction")
class UserPoolDefaultAction(enum.Enum):
    """enum with all possible values for Cognito user-pool default actions.

    stability
    :stability: experimental
    """

    ALLOW = "ALLOW"
    """ALLOW access to API.

    stability
    :stability: experimental
    """
    DENY = "DENY"
    """DENY access to API.

    stability
    :stability: experimental
    """


class Values(
    metaclass=jsii.JSIIMeta, jsii_type="monocdk-experiment.aws_appsync.Values"
):
    """Factory class for attribute value assignments.

    stability
    :stability: experimental
    """

    def __init__(self) -> None:
        jsii.create(Values, self, [])

    @jsii.member(jsii_name="attribute")
    @builtins.classmethod
    def attribute(cls, attr: str) -> "AttributeValuesStep":
        """Allows assigning a value to the specified attribute.

        :param attr: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "attribute", [attr])

    @jsii.member(jsii_name="projecting")
    @builtins.classmethod
    def projecting(cls, arg: typing.Optional[str] = None) -> "AttributeValues":
        """Treats the specified object as a map of assignments, where the property names represent attribute names.

        It’s opinionated about how it represents
        some of the nested objects: e.g., it will use lists (“L”) rather than sets
        (“SS”, “NS”, “BS”). By default it projects the argument container ("$ctx.args").

        :param arg: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "projecting", [arg])


@jsii.implements(_IGrantable_0fcfc53a)
class BackedDataSource(
    BaseDataSource,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk-experiment.aws_appsync.BackedDataSource",
):
    """Abstract AppSync datasource implementation.

    Do not use directly but use subclasses for resource backed datasources

    stability
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _BackedDataSourceProxy

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        props: "BackedDataSourceProps",
        *,
        type: str,
        dynamo_db_config: typing.Optional[
            typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        elasticsearch_config: typing.Optional[
            typing.Union[
                "CfnDataSource.ElasticsearchConfigProperty", _IResolvable_9ceae33e
            ]
        ] = None,
        http_config: typing.Optional[
            typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        lambda_config: typing.Optional[
            typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_9ceae33e]
        ] = None,
        relational_database_config: typing.Optional[
            typing.Union[
                "CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_9ceae33e
            ]
        ] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param type: the type of the AppSync datasource.
        :param dynamo_db_config: configuration for DynamoDB Datasource. Default: - No config
        :param elasticsearch_config: configuration for Elasticsearch Datasource. Default: - No config
        :param http_config: configuration for HTTP Datasource. Default: - No config
        :param lambda_config: configuration for Lambda Datasource. Default: - No config
        :param relational_database_config: configuration for RDS Datasource. Default: - No config

        stability
        :stability: experimental
        """
        extended = ExtendedDataSourceProps(
            type=type,
            dynamo_db_config=dynamo_db_config,
            elasticsearch_config=elasticsearch_config,
            http_config=http_config,
            lambda_config=lambda_config,
            relational_database_config=relational_database_config,
        )

        jsii.create(BackedDataSource, self, [scope, id, props, extended])

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_97126874:
        """the principal of the data source to be IGrantable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")


class _BackedDataSourceProxy(BackedDataSource, jsii.proxy_for(BaseDataSource)):
    pass


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.BackedDataSourceProps",
    jsii_struct_bases=[BaseDataSourceProps],
    name_mapping={
        "api": "api",
        "name": "name",
        "description": "description",
        "service_role": "serviceRole",
    },
)
class BackedDataSourceProps(BaseDataSourceProps):
    def __init__(
        self,
        *,
        api: "GraphQLApi",
        name: str,
        description: typing.Optional[str] = None,
        service_role: typing.Optional[_IRole_e69bbae4] = None,
    ) -> None:
        """properties for an AppSync datasource backed by a resource.

        :param api: The API to attach this data source to.
        :param name: The name of the data source.
        :param description: the description of the data source. Default: - None
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role

        stability
        :stability: experimental
        """
        self._values = {
            "api": api,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> "GraphQLApi":
        """The API to attach this data source to.

        stability
        :stability: experimental
        """
        return self._values.get("api")

    @builtins.property
    def name(self) -> str:
        """The name of the data source.

        stability
        :stability: experimental
        """
        return self._values.get("name")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """the description of the data source.

        default
        :default: - None

        stability
        :stability: experimental
        """
        return self._values.get("description")

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_e69bbae4]:
        """The IAM service role to be assumed by AppSync to interact with the data source.

        default
        :default: - Create a new role

        stability
        :stability: experimental
        """
        return self._values.get("service_role")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackedDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamoDbDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.DynamoDbDataSource",
):
    """An AppSync datasource backed by a DynamoDB table.

    stability
    :stability: experimental
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        table: _ITable_e6850701,
        read_only_access: typing.Optional[bool] = None,
        use_caller_credentials: typing.Optional[bool] = None,
        service_role: typing.Optional[_IRole_e69bbae4] = None,
        api: "GraphQLApi",
        name: str,
        description: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param table: The DynamoDB table backing this data source [disable-awslint:ref-via-interface].
        :param read_only_access: Specify whether this DS is read only or has read and write permissions to the DynamoDB table. Default: false
        :param use_caller_credentials: use credentials of caller to access DynamoDB. Default: false
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: The API to attach this data source to.
        :param name: The name of the data source.
        :param description: the description of the data source. Default: - None

        stability
        :stability: experimental
        """
        props = DynamoDbDataSourceProps(
            table=table,
            read_only_access=read_only_access,
            use_caller_credentials=use_caller_credentials,
            service_role=service_role,
            api=api,
            name=name,
            description=description,
        )

        jsii.create(DynamoDbDataSource, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.DynamoDbDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "name": "name",
        "description": "description",
        "service_role": "serviceRole",
        "table": "table",
        "read_only_access": "readOnlyAccess",
        "use_caller_credentials": "useCallerCredentials",
    },
)
class DynamoDbDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: "GraphQLApi",
        name: str,
        description: typing.Optional[str] = None,
        service_role: typing.Optional[_IRole_e69bbae4] = None,
        table: _ITable_e6850701,
        read_only_access: typing.Optional[bool] = None,
        use_caller_credentials: typing.Optional[bool] = None,
    ) -> None:
        """Properties for an AppSync DynamoDB datasource.

        :param api: The API to attach this data source to.
        :param name: The name of the data source.
        :param description: the description of the data source. Default: - None
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param table: The DynamoDB table backing this data source [disable-awslint:ref-via-interface].
        :param read_only_access: Specify whether this DS is read only or has read and write permissions to the DynamoDB table. Default: false
        :param use_caller_credentials: use credentials of caller to access DynamoDB. Default: false

        stability
        :stability: experimental
        """
        self._values = {
            "api": api,
            "name": name,
            "table": table,
        }
        if description is not None:
            self._values["description"] = description
        if service_role is not None:
            self._values["service_role"] = service_role
        if read_only_access is not None:
            self._values["read_only_access"] = read_only_access
        if use_caller_credentials is not None:
            self._values["use_caller_credentials"] = use_caller_credentials

    @builtins.property
    def api(self) -> "GraphQLApi":
        """The API to attach this data source to.

        stability
        :stability: experimental
        """
        return self._values.get("api")

    @builtins.property
    def name(self) -> str:
        """The name of the data source.

        stability
        :stability: experimental
        """
        return self._values.get("name")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """the description of the data source.

        default
        :default: - None

        stability
        :stability: experimental
        """
        return self._values.get("description")

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_e69bbae4]:
        """The IAM service role to be assumed by AppSync to interact with the data source.

        default
        :default: - Create a new role

        stability
        :stability: experimental
        """
        return self._values.get("service_role")

    @builtins.property
    def table(self) -> _ITable_e6850701:
        """The DynamoDB table backing this data source [disable-awslint:ref-via-interface].

        stability
        :stability: experimental
        """
        return self._values.get("table")

    @builtins.property
    def read_only_access(self) -> typing.Optional[bool]:
        """Specify whether this DS is read only or has read and write permissions to the DynamoDB table.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get("read_only_access")

    @builtins.property
    def use_caller_credentials(self) -> typing.Optional[bool]:
        """use credentials of caller to access DynamoDB.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get("use_caller_credentials")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamoDbDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.LambdaDataSource",
):
    """An AppSync datasource backed by a Lambda function.

    stability
    :stability: experimental
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        lambda_function: _IFunction_1c1de0bc,
        service_role: typing.Optional[_IRole_e69bbae4] = None,
        api: "GraphQLApi",
        name: str,
        description: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param lambda_function: The Lambda function to call to interact with this data source.
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: The API to attach this data source to.
        :param name: The name of the data source.
        :param description: the description of the data source. Default: - None

        stability
        :stability: experimental
        """
        props = LambdaDataSourceProps(
            lambda_function=lambda_function,
            service_role=service_role,
            api=api,
            name=name,
            description=description,
        )

        jsii.create(LambdaDataSource, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_appsync.LambdaDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "name": "name",
        "description": "description",
        "service_role": "serviceRole",
        "lambda_function": "lambdaFunction",
    },
)
class LambdaDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: "GraphQLApi",
        name: str,
        description: typing.Optional[str] = None,
        service_role: typing.Optional[_IRole_e69bbae4] = None,
        lambda_function: _IFunction_1c1de0bc,
    ) -> None:
        """Properties for an AppSync Lambda datasource.

        :param api: The API to attach this data source to.
        :param name: The name of the data source.
        :param description: the description of the data source. Default: - None
        :param service_role: The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param lambda_function: The Lambda function to call to interact with this data source.

        stability
        :stability: experimental
        """
        self._values = {
            "api": api,
            "name": name,
            "lambda_function": lambda_function,
        }
        if description is not None:
            self._values["description"] = description
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> "GraphQLApi":
        """The API to attach this data source to.

        stability
        :stability: experimental
        """
        return self._values.get("api")

    @builtins.property
    def name(self) -> str:
        """The name of the data source.

        stability
        :stability: experimental
        """
        return self._values.get("name")

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """the description of the data source.

        default
        :default: - None

        stability
        :stability: experimental
        """
        return self._values.get("description")

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_e69bbae4]:
        """The IAM service role to be assumed by AppSync to interact with the data source.

        default
        :default: - Create a new role

        stability
        :stability: experimental
        """
        return self._values.get("service_role")

    @builtins.property
    def lambda_function(self) -> _IFunction_1c1de0bc:
        """The Lambda function to call to interact with this data source.

        stability
        :stability: experimental
        """
        return self._values.get("lambda_function")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PartitionKey(
    PrimaryKey,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_appsync.PartitionKey",
):
    """Specifies the assignment to the partition key.

    It can be
    enhanced with the assignment of the sort key.

    stability
    :stability: experimental
    """

    def __init__(self, pkey: "Assign") -> None:
        """
        :param pkey: -

        stability
        :stability: experimental
        """
        jsii.create(PartitionKey, self, [pkey])

    @jsii.member(jsii_name="sort")
    def sort(self, key: str) -> "SortKeyStep":
        """Allows assigning a value to the sort key.

        :param key: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "sort", [key])


__all__ = [
    "ApiKeyConfig",
    "Assign",
    "AttributeValues",
    "AttributeValuesStep",
    "AuthorizationConfig",
    "AuthorizationMode",
    "AuthorizationType",
    "BackedDataSource",
    "BackedDataSourceProps",
    "BaseDataSource",
    "BaseDataSourceProps",
    "BaseResolverProps",
    "CfnApiCache",
    "CfnApiCacheProps",
    "CfnApiKey",
    "CfnApiKeyProps",
    "CfnDataSource",
    "CfnDataSourceProps",
    "CfnFunctionConfiguration",
    "CfnFunctionConfigurationProps",
    "CfnGraphQLApi",
    "CfnGraphQLApiProps",
    "CfnGraphQLSchema",
    "CfnGraphQLSchemaProps",
    "CfnResolver",
    "CfnResolverProps",
    "DynamoDbDataSource",
    "DynamoDbDataSourceProps",
    "ExtendedDataSourceProps",
    "FieldLogLevel",
    "GraphQLApi",
    "GraphQLApiProps",
    "HttpDataSource",
    "HttpDataSourceProps",
    "IamResource",
    "KeyCondition",
    "LambdaDataSource",
    "LambdaDataSourceProps",
    "LogConfig",
    "MappingTemplate",
    "NoneDataSource",
    "NoneDataSourceProps",
    "OpenIdConnectConfig",
    "PartitionKey",
    "PartitionKeyStep",
    "PrimaryKey",
    "Resolver",
    "ResolverProps",
    "SchemaDefinition",
    "SortKeyStep",
    "UserPoolConfig",
    "UserPoolDefaultAction",
    "Values",
]

publication.publish()
