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
    Duration as _Duration_5170c158,
    CfnResource as _CfnResource_7760e8e4,
    Construct as _Construct_f50a3f53,
    IResolvable as _IResolvable_9ceae33e,
    FromCloudFormationOptions as _FromCloudFormationOptions_5f49f6f1,
    ICfnFinder as _ICfnFinder_3b168f30,
    TreeInspector as _TreeInspector_154f5999,
    IInspectable as _IInspectable_051e6ed8,
    CfnTag as _CfnTag_b4661f1a,
    TagManager as _TagManager_2508893f,
    Resource as _Resource_884d0774,
    IResource as _IResource_72f7ee7e,
)
from ..aws_certificatemanager import ICertificate as _ICertificate_8f3d4c96
from ..aws_iam import (
    IGrantable as _IGrantable_0fcfc53a,
    IPrincipal as _IPrincipal_97126874,
)
from ..aws_lambda import IVersion as _IVersion_1dc10564
from ..aws_s3 import IBucket as _IBucket_25bad983


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.AddBehaviorOptions",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_methods": "allowedMethods",
        "cached_methods": "cachedMethods",
        "compress": "compress",
        "edge_lambdas": "edgeLambdas",
        "forward_query_string": "forwardQueryString",
        "forward_query_string_cache_keys": "forwardQueryStringCacheKeys",
        "smooth_streaming": "smoothStreaming",
        "viewer_protocol_policy": "viewerProtocolPolicy",
    },
)
class AddBehaviorOptions:
    def __init__(
        self,
        *,
        allowed_methods: typing.Optional["AllowedMethods"] = None,
        cached_methods: typing.Optional["CachedMethods"] = None,
        compress: typing.Optional[bool] = None,
        edge_lambdas: typing.Optional[typing.List["EdgeLambda"]] = None,
        forward_query_string: typing.Optional[bool] = None,
        forward_query_string_cache_keys: typing.Optional[typing.List[str]] = None,
        smooth_streaming: typing.Optional[bool] = None,
        viewer_protocol_policy: typing.Optional["ViewerProtocolPolicy"] = None,
    ) -> None:
        """Options for adding a new behavior to a Distribution.

        :param allowed_methods: HTTP methods to allow for this behavior. Default: AllowedMethods.ALLOW_GET_HEAD
        :param cached_methods: HTTP methods to cache for this behavior. Default: CachedMethods.CACHE_GET_HEAD
        :param compress: Whether you want CloudFront to automatically compress certain files for this cache behavior. See https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-cloudfront-file-types for file types CloudFront will compress. Default: false
        :param edge_lambdas: The Lambda@Edge functions to invoke before serving the contents. Default: - no Lambda functions will be invoked
        :param forward_query_string: Whether CloudFront will forward query strings to the origin. If this is set to true, CloudFront will forward all query parameters to the origin, and cache based on all parameters. See ``forwardQueryStringCacheKeys`` for a way to limit the query parameters CloudFront caches on. Default: false
        :param forward_query_string_cache_keys: A set of query string parameter names to use for caching if ``forwardQueryString`` is set to true. Default: []
        :param smooth_streaming: Set this to true to indicate you want to distribute media files in the Microsoft Smooth Streaming format using this behavior. Default: false
        :param viewer_protocol_policy: The protocol that viewers can use to access the files controlled by this behavior. Default: ViewerProtocolPolicy.ALLOW_ALL

        stability
        :stability: experimental
        """
        self._values = {}
        if allowed_methods is not None:
            self._values["allowed_methods"] = allowed_methods
        if cached_methods is not None:
            self._values["cached_methods"] = cached_methods
        if compress is not None:
            self._values["compress"] = compress
        if edge_lambdas is not None:
            self._values["edge_lambdas"] = edge_lambdas
        if forward_query_string is not None:
            self._values["forward_query_string"] = forward_query_string
        if forward_query_string_cache_keys is not None:
            self._values[
                "forward_query_string_cache_keys"
            ] = forward_query_string_cache_keys
        if smooth_streaming is not None:
            self._values["smooth_streaming"] = smooth_streaming
        if viewer_protocol_policy is not None:
            self._values["viewer_protocol_policy"] = viewer_protocol_policy

    @builtins.property
    def allowed_methods(self) -> typing.Optional["AllowedMethods"]:
        """HTTP methods to allow for this behavior.

        default
        :default: AllowedMethods.ALLOW_GET_HEAD

        stability
        :stability: experimental
        """
        return self._values.get("allowed_methods")

    @builtins.property
    def cached_methods(self) -> typing.Optional["CachedMethods"]:
        """HTTP methods to cache for this behavior.

        default
        :default: CachedMethods.CACHE_GET_HEAD

        stability
        :stability: experimental
        """
        return self._values.get("cached_methods")

    @builtins.property
    def compress(self) -> typing.Optional[bool]:
        """Whether you want CloudFront to automatically compress certain files for this cache behavior.

        See https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-cloudfront-file-types
        for file types CloudFront will compress.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get("compress")

    @builtins.property
    def edge_lambdas(self) -> typing.Optional[typing.List["EdgeLambda"]]:
        """The Lambda@Edge functions to invoke before serving the contents.

        default
        :default: - no Lambda functions will be invoked

        see
        :see: https://aws.amazon.com/lambda/edge
        stability
        :stability: experimental
        """
        return self._values.get("edge_lambdas")

    @builtins.property
    def forward_query_string(self) -> typing.Optional[bool]:
        """Whether CloudFront will forward query strings to the origin.

        If this is set to true, CloudFront will forward all query parameters to the origin, and cache
        based on all parameters. See ``forwardQueryStringCacheKeys`` for a way to limit the query parameters
        CloudFront caches on.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get("forward_query_string")

    @builtins.property
    def forward_query_string_cache_keys(self) -> typing.Optional[typing.List[str]]:
        """A set of query string parameter names to use for caching if ``forwardQueryString`` is set to true.

        default
        :default: []

        stability
        :stability: experimental
        """
        return self._values.get("forward_query_string_cache_keys")

    @builtins.property
    def smooth_streaming(self) -> typing.Optional[bool]:
        """Set this to true to indicate you want to distribute media files in the Microsoft Smooth Streaming format using this behavior.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get("smooth_streaming")

    @builtins.property
    def viewer_protocol_policy(self) -> typing.Optional["ViewerProtocolPolicy"]:
        """The protocol that viewers can use to access the files controlled by this behavior.

        default
        :default: ViewerProtocolPolicy.ALLOW_ALL

        stability
        :stability: experimental
        """
        return self._values.get("viewer_protocol_policy")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddBehaviorOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.AliasConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "acm_cert_ref": "acmCertRef",
        "names": "names",
        "security_policy": "securityPolicy",
        "ssl_method": "sslMethod",
    },
)
class AliasConfiguration:
    def __init__(
        self,
        *,
        acm_cert_ref: str,
        names: typing.List[str],
        security_policy: typing.Optional["SecurityPolicyProtocol"] = None,
        ssl_method: typing.Optional["SSLMethod"] = None,
    ) -> None:
        """Configuration for custom domain names.

        CloudFront can use a custom domain that you provide instead of a
        "cloudfront.net" domain. To use this feature you must provide the list of
        additional domains, and the ACM Certificate that CloudFront should use for
        these additional domains.

        :param acm_cert_ref: ARN of an AWS Certificate Manager (ACM) certificate.
        :param names: Domain names on the certificate. Both main domain name and Subject Alternative Names.
        :param security_policy: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: - SSLv3 if sslMethod VIP, TLSv1 if sslMethod SNI
        :param ssl_method: How CloudFront should serve HTTPS requests. See the notes on SSLMethod if you wish to use other SSL termination types. Default: SSLMethod.SNI

        stability
        :stability: experimental
        """
        self._values = {
            "acm_cert_ref": acm_cert_ref,
            "names": names,
        }
        if security_policy is not None:
            self._values["security_policy"] = security_policy
        if ssl_method is not None:
            self._values["ssl_method"] = ssl_method

    @builtins.property
    def acm_cert_ref(self) -> str:
        """ARN of an AWS Certificate Manager (ACM) certificate.

        stability
        :stability: experimental
        """
        return self._values.get("acm_cert_ref")

    @builtins.property
    def names(self) -> typing.List[str]:
        """Domain names on the certificate.

        Both main domain name and Subject Alternative Names.

        stability
        :stability: experimental
        """
        return self._values.get("names")

    @builtins.property
    def security_policy(self) -> typing.Optional["SecurityPolicyProtocol"]:
        """The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections.

        CloudFront serves your objects only to browsers or devices that support at
        least the SSL version that you specify.

        default
        :default: - SSLv3 if sslMethod VIP, TLSv1 if sslMethod SNI

        stability
        :stability: experimental
        """
        return self._values.get("security_policy")

    @builtins.property
    def ssl_method(self) -> typing.Optional["SSLMethod"]:
        """How CloudFront should serve HTTPS requests.

        See the notes on SSLMethod if you wish to use other SSL termination types.

        default
        :default: SSLMethod.SNI

        see
        :see: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ViewerCertificate.html
        stability
        :stability: experimental
        """
        return self._values.get("ssl_method")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AllowedMethods(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_cloudfront.AllowedMethods",
):
    """The HTTP methods that the Behavior will accept requests on.

    stability
    :stability: experimental
    """

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALLOW_ALL")
    def ALLOW_ALL(cls) -> "AllowedMethods":
        """All supported HTTP methods.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "ALLOW_ALL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALLOW_GET_HEAD")
    def ALLOW_GET_HEAD(cls) -> "AllowedMethods":
        """HEAD and GET.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "ALLOW_GET_HEAD")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALLOW_GET_HEAD_OPTIONS")
    def ALLOW_GET_HEAD_OPTIONS(cls) -> "AllowedMethods":
        """HEAD, GET, and OPTIONS.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "ALLOW_GET_HEAD_OPTIONS")

    @builtins.property
    @jsii.member(jsii_name="methods")
    def methods(self) -> typing.List[str]:
        """HTTP methods supported.

        stability
        :stability: experimental
        """
        return jsii.get(self, "methods")


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.Behavior",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_methods": "allowedMethods",
        "cached_methods": "cachedMethods",
        "compress": "compress",
        "default_ttl": "defaultTtl",
        "forwarded_values": "forwardedValues",
        "is_default_behavior": "isDefaultBehavior",
        "lambda_function_associations": "lambdaFunctionAssociations",
        "max_ttl": "maxTtl",
        "min_ttl": "minTtl",
        "path_pattern": "pathPattern",
        "trusted_signers": "trustedSigners",
    },
)
class Behavior:
    def __init__(
        self,
        *,
        allowed_methods: typing.Optional["CloudFrontAllowedMethods"] = None,
        cached_methods: typing.Optional["CloudFrontAllowedCachedMethods"] = None,
        compress: typing.Optional[bool] = None,
        default_ttl: typing.Optional[_Duration_5170c158] = None,
        forwarded_values: typing.Optional[
            "CfnDistribution.ForwardedValuesProperty"
        ] = None,
        is_default_behavior: typing.Optional[bool] = None,
        lambda_function_associations: typing.Optional[
            typing.List["LambdaFunctionAssociation"]
        ] = None,
        max_ttl: typing.Optional[_Duration_5170c158] = None,
        min_ttl: typing.Optional[_Duration_5170c158] = None,
        path_pattern: typing.Optional[str] = None,
        trusted_signers: typing.Optional[typing.List[str]] = None,
    ) -> None:
        """A CloudFront behavior wrapper.

        :param allowed_methods: The method this CloudFront distribution responds do. Default: GET_HEAD
        :param cached_methods: Which methods are cached by CloudFront by default. Default: GET_HEAD
        :param compress: If CloudFront should automatically compress some content types. Default: true
        :param default_ttl: The default amount of time CloudFront will cache an object. This value applies only when your custom origin does not add HTTP headers, such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects. Default: 86400 (1 day)
        :param forwarded_values: The values CloudFront will forward to the origin when making a request. Default: none (no cookies - no headers)
        :param is_default_behavior: If this behavior is the default behavior for the distribution. You must specify exactly one default distribution per CloudFront distribution. The default behavior is allowed to omit the "path" property.
        :param lambda_function_associations: Declares associated lambda@edge functions for this distribution behaviour. Default: No lambda function associated
        :param max_ttl: The max amount of time you want objects to stay in the cache before CloudFront queries your origin. Default: Duration.seconds(31536000) (one year)
        :param min_ttl: The minimum amount of time that you want objects to stay in the cache before CloudFront queries your origin.
        :param path_pattern: The path this behavior responds to. Required for all non-default behaviors. (The default behavior implicitly has "*" as the path pattern. )
        :param trusted_signers: Trusted signers is how CloudFront allows you to serve private content. The signers are the account IDs that are allowed to sign cookies/presigned URLs for this distribution. If you pass a non empty value, all requests for this behavior must be signed (no public access will be allowed)

        stability
        :stability: experimental
        """
        if isinstance(forwarded_values, dict):
            forwarded_values = CfnDistribution.ForwardedValuesProperty(
                **forwarded_values
            )
        self._values = {}
        if allowed_methods is not None:
            self._values["allowed_methods"] = allowed_methods
        if cached_methods is not None:
            self._values["cached_methods"] = cached_methods
        if compress is not None:
            self._values["compress"] = compress
        if default_ttl is not None:
            self._values["default_ttl"] = default_ttl
        if forwarded_values is not None:
            self._values["forwarded_values"] = forwarded_values
        if is_default_behavior is not None:
            self._values["is_default_behavior"] = is_default_behavior
        if lambda_function_associations is not None:
            self._values["lambda_function_associations"] = lambda_function_associations
        if max_ttl is not None:
            self._values["max_ttl"] = max_ttl
        if min_ttl is not None:
            self._values["min_ttl"] = min_ttl
        if path_pattern is not None:
            self._values["path_pattern"] = path_pattern
        if trusted_signers is not None:
            self._values["trusted_signers"] = trusted_signers

    @builtins.property
    def allowed_methods(self) -> typing.Optional["CloudFrontAllowedMethods"]:
        """The method this CloudFront distribution responds do.

        default
        :default: GET_HEAD

        stability
        :stability: experimental
        """
        return self._values.get("allowed_methods")

    @builtins.property
    def cached_methods(self) -> typing.Optional["CloudFrontAllowedCachedMethods"]:
        """Which methods are cached by CloudFront by default.

        default
        :default: GET_HEAD

        stability
        :stability: experimental
        """
        return self._values.get("cached_methods")

    @builtins.property
    def compress(self) -> typing.Optional[bool]:
        """If CloudFront should automatically compress some content types.

        default
        :default: true

        stability
        :stability: experimental
        """
        return self._values.get("compress")

    @builtins.property
    def default_ttl(self) -> typing.Optional[_Duration_5170c158]:
        """The default amount of time CloudFront will cache an object.

        This value applies only when your custom origin does not add HTTP headers,
        such as Cache-Control max-age, Cache-Control s-maxage, and Expires to objects.

        default
        :default: 86400 (1 day)

        stability
        :stability: experimental
        """
        return self._values.get("default_ttl")

    @builtins.property
    def forwarded_values(
        self,
    ) -> typing.Optional["CfnDistribution.ForwardedValuesProperty"]:
        """The values CloudFront will forward to the origin when making a request.

        default
        :default: none (no cookies - no headers)

        stability
        :stability: experimental
        """
        return self._values.get("forwarded_values")

    @builtins.property
    def is_default_behavior(self) -> typing.Optional[bool]:
        """If this behavior is the default behavior for the distribution.

        You must specify exactly one default distribution per CloudFront distribution.
        The default behavior is allowed to omit the "path" property.

        stability
        :stability: experimental
        """
        return self._values.get("is_default_behavior")

    @builtins.property
    def lambda_function_associations(
        self,
    ) -> typing.Optional[typing.List["LambdaFunctionAssociation"]]:
        """Declares associated lambda@edge functions for this distribution behaviour.

        default
        :default: No lambda function associated

        stability
        :stability: experimental
        """
        return self._values.get("lambda_function_associations")

    @builtins.property
    def max_ttl(self) -> typing.Optional[_Duration_5170c158]:
        """The max amount of time you want objects to stay in the cache before CloudFront queries your origin.

        default
        :default: Duration.seconds(31536000) (one year)

        stability
        :stability: experimental
        """
        return self._values.get("max_ttl")

    @builtins.property
    def min_ttl(self) -> typing.Optional[_Duration_5170c158]:
        """The minimum amount of time that you want objects to stay in the cache before CloudFront queries your origin.

        stability
        :stability: experimental
        """
        return self._values.get("min_ttl")

    @builtins.property
    def path_pattern(self) -> typing.Optional[str]:
        """The path this behavior responds to.

        Required for all non-default behaviors. (The default behavior implicitly has "*" as the path pattern. )

        stability
        :stability: experimental
        """
        return self._values.get("path_pattern")

    @builtins.property
    def trusted_signers(self) -> typing.Optional[typing.List[str]]:
        """Trusted signers is how CloudFront allows you to serve private content.

        The signers are the account IDs that are allowed to sign cookies/presigned URLs for this distribution.

        If you pass a non empty value, all requests for this behavior must be signed (no public access will be allowed)

        stability
        :stability: experimental
        """
        return self._values.get("trusted_signers")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Behavior(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.BehaviorOptions",
    jsii_struct_bases=[AddBehaviorOptions],
    name_mapping={
        "allowed_methods": "allowedMethods",
        "cached_methods": "cachedMethods",
        "compress": "compress",
        "edge_lambdas": "edgeLambdas",
        "forward_query_string": "forwardQueryString",
        "forward_query_string_cache_keys": "forwardQueryStringCacheKeys",
        "smooth_streaming": "smoothStreaming",
        "viewer_protocol_policy": "viewerProtocolPolicy",
        "origin": "origin",
    },
)
class BehaviorOptions(AddBehaviorOptions):
    def __init__(
        self,
        *,
        allowed_methods: typing.Optional["AllowedMethods"] = None,
        cached_methods: typing.Optional["CachedMethods"] = None,
        compress: typing.Optional[bool] = None,
        edge_lambdas: typing.Optional[typing.List["EdgeLambda"]] = None,
        forward_query_string: typing.Optional[bool] = None,
        forward_query_string_cache_keys: typing.Optional[typing.List[str]] = None,
        smooth_streaming: typing.Optional[bool] = None,
        viewer_protocol_policy: typing.Optional["ViewerProtocolPolicy"] = None,
        origin: "IOrigin",
    ) -> None:
        """Options for creating a new behavior.

        :param allowed_methods: HTTP methods to allow for this behavior. Default: AllowedMethods.ALLOW_GET_HEAD
        :param cached_methods: HTTP methods to cache for this behavior. Default: CachedMethods.CACHE_GET_HEAD
        :param compress: Whether you want CloudFront to automatically compress certain files for this cache behavior. See https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-cloudfront-file-types for file types CloudFront will compress. Default: false
        :param edge_lambdas: The Lambda@Edge functions to invoke before serving the contents. Default: - no Lambda functions will be invoked
        :param forward_query_string: Whether CloudFront will forward query strings to the origin. If this is set to true, CloudFront will forward all query parameters to the origin, and cache based on all parameters. See ``forwardQueryStringCacheKeys`` for a way to limit the query parameters CloudFront caches on. Default: false
        :param forward_query_string_cache_keys: A set of query string parameter names to use for caching if ``forwardQueryString`` is set to true. Default: []
        :param smooth_streaming: Set this to true to indicate you want to distribute media files in the Microsoft Smooth Streaming format using this behavior. Default: false
        :param viewer_protocol_policy: The protocol that viewers can use to access the files controlled by this behavior. Default: ViewerProtocolPolicy.ALLOW_ALL
        :param origin: The origin that you want CloudFront to route requests to when they match this behavior.

        stability
        :stability: experimental
        """
        self._values = {
            "origin": origin,
        }
        if allowed_methods is not None:
            self._values["allowed_methods"] = allowed_methods
        if cached_methods is not None:
            self._values["cached_methods"] = cached_methods
        if compress is not None:
            self._values["compress"] = compress
        if edge_lambdas is not None:
            self._values["edge_lambdas"] = edge_lambdas
        if forward_query_string is not None:
            self._values["forward_query_string"] = forward_query_string
        if forward_query_string_cache_keys is not None:
            self._values[
                "forward_query_string_cache_keys"
            ] = forward_query_string_cache_keys
        if smooth_streaming is not None:
            self._values["smooth_streaming"] = smooth_streaming
        if viewer_protocol_policy is not None:
            self._values["viewer_protocol_policy"] = viewer_protocol_policy

    @builtins.property
    def allowed_methods(self) -> typing.Optional["AllowedMethods"]:
        """HTTP methods to allow for this behavior.

        default
        :default: AllowedMethods.ALLOW_GET_HEAD

        stability
        :stability: experimental
        """
        return self._values.get("allowed_methods")

    @builtins.property
    def cached_methods(self) -> typing.Optional["CachedMethods"]:
        """HTTP methods to cache for this behavior.

        default
        :default: CachedMethods.CACHE_GET_HEAD

        stability
        :stability: experimental
        """
        return self._values.get("cached_methods")

    @builtins.property
    def compress(self) -> typing.Optional[bool]:
        """Whether you want CloudFront to automatically compress certain files for this cache behavior.

        See https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-cloudfront-file-types
        for file types CloudFront will compress.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get("compress")

    @builtins.property
    def edge_lambdas(self) -> typing.Optional[typing.List["EdgeLambda"]]:
        """The Lambda@Edge functions to invoke before serving the contents.

        default
        :default: - no Lambda functions will be invoked

        see
        :see: https://aws.amazon.com/lambda/edge
        stability
        :stability: experimental
        """
        return self._values.get("edge_lambdas")

    @builtins.property
    def forward_query_string(self) -> typing.Optional[bool]:
        """Whether CloudFront will forward query strings to the origin.

        If this is set to true, CloudFront will forward all query parameters to the origin, and cache
        based on all parameters. See ``forwardQueryStringCacheKeys`` for a way to limit the query parameters
        CloudFront caches on.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get("forward_query_string")

    @builtins.property
    def forward_query_string_cache_keys(self) -> typing.Optional[typing.List[str]]:
        """A set of query string parameter names to use for caching if ``forwardQueryString`` is set to true.

        default
        :default: []

        stability
        :stability: experimental
        """
        return self._values.get("forward_query_string_cache_keys")

    @builtins.property
    def smooth_streaming(self) -> typing.Optional[bool]:
        """Set this to true to indicate you want to distribute media files in the Microsoft Smooth Streaming format using this behavior.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get("smooth_streaming")

    @builtins.property
    def viewer_protocol_policy(self) -> typing.Optional["ViewerProtocolPolicy"]:
        """The protocol that viewers can use to access the files controlled by this behavior.

        default
        :default: ViewerProtocolPolicy.ALLOW_ALL

        stability
        :stability: experimental
        """
        return self._values.get("viewer_protocol_policy")

    @builtins.property
    def origin(self) -> "IOrigin":
        """The origin that you want CloudFront to route requests to when they match this behavior.

        stability
        :stability: experimental
        """
        return self._values.get("origin")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BehaviorOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CachedMethods(
    metaclass=jsii.JSIIMeta, jsii_type="monocdk-experiment.aws_cloudfront.CachedMethods"
):
    """The HTTP methods that the Behavior will cache requests on.

    stability
    :stability: experimental
    """

    @jsii.python.classproperty
    @jsii.member(jsii_name="CACHE_GET_HEAD")
    def CACHE_GET_HEAD(cls) -> "CachedMethods":
        """HEAD and GET.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "CACHE_GET_HEAD")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CACHE_GET_HEAD_OPTIONS")
    def CACHE_GET_HEAD_OPTIONS(cls) -> "CachedMethods":
        """HEAD, GET, and OPTIONS.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "CACHE_GET_HEAD_OPTIONS")

    @builtins.property
    @jsii.member(jsii_name="methods")
    def methods(self) -> typing.List[str]:
        """HTTP methods supported.

        stability
        :stability: experimental
        """
        return jsii.get(self, "methods")


@jsii.implements(_IInspectable_051e6ed8)
class CfnCloudFrontOriginAccessIdentity(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_cloudfront.CfnCloudFrontOriginAccessIdentity",
):
    """A CloudFormation ``AWS::CloudFront::CloudFrontOriginAccessIdentity``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html
    cloudformationResource:
    :cloudformationResource:: AWS::CloudFront::CloudFrontOriginAccessIdentity
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        cloud_front_origin_access_identity_config: typing.Union[
            "CloudFrontOriginAccessIdentityConfigProperty", _IResolvable_9ceae33e
        ],
    ) -> None:
        """Create a new ``AWS::CloudFront::CloudFrontOriginAccessIdentity``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cloud_front_origin_access_identity_config: ``AWS::CloudFront::CloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfig``.
        """
        props = CfnCloudFrontOriginAccessIdentityProps(
            cloud_front_origin_access_identity_config=cloud_front_origin_access_identity_config
        )

        jsii.create(CfnCloudFrontOriginAccessIdentity, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnCloudFrontOriginAccessIdentity":
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
    @jsii.member(jsii_name="attrS3CanonicalUserId")
    def attr_s3_canonical_user_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: S3CanonicalUserId
        """
        return jsii.get(self, "attrS3CanonicalUserId")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="cloudFrontOriginAccessIdentityConfig")
    def cloud_front_origin_access_identity_config(
        self,
    ) -> typing.Union[
        "CloudFrontOriginAccessIdentityConfigProperty", _IResolvable_9ceae33e
    ]:
        """``AWS::CloudFront::CloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html#cfn-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig
        """
        return jsii.get(self, "cloudFrontOriginAccessIdentityConfig")

    @cloud_front_origin_access_identity_config.setter
    def cloud_front_origin_access_identity_config(
        self,
        value: typing.Union[
            "CloudFrontOriginAccessIdentityConfigProperty", _IResolvable_9ceae33e
        ],
    ) -> None:
        jsii.set(self, "cloudFrontOriginAccessIdentityConfig", value)

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnCloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"comment": "comment"},
    )
    class CloudFrontOriginAccessIdentityConfigProperty:
        def __init__(self, *, comment: str) -> None:
            """
            :param comment: ``CfnCloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfigProperty.Comment``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig.html
            """
            self._values = {
                "comment": comment,
            }

        @builtins.property
        def comment(self) -> str:
            """``CfnCloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfigProperty.Comment``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig.html#cfn-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig-comment
            """
            return self._values.get("comment")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudFrontOriginAccessIdentityConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.CfnCloudFrontOriginAccessIdentityProps",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_front_origin_access_identity_config": "cloudFrontOriginAccessIdentityConfig"
    },
)
class CfnCloudFrontOriginAccessIdentityProps:
    def __init__(
        self,
        *,
        cloud_front_origin_access_identity_config: typing.Union[
            "CfnCloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfigProperty",
            _IResolvable_9ceae33e,
        ],
    ) -> None:
        """Properties for defining a ``AWS::CloudFront::CloudFrontOriginAccessIdentity``.

        :param cloud_front_origin_access_identity_config: ``AWS::CloudFront::CloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html
        """
        self._values = {
            "cloud_front_origin_access_identity_config": cloud_front_origin_access_identity_config,
        }

    @builtins.property
    def cloud_front_origin_access_identity_config(
        self,
    ) -> typing.Union[
        "CfnCloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfigProperty",
        _IResolvable_9ceae33e,
    ]:
        """``AWS::CloudFront::CloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html#cfn-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig
        """
        return self._values.get("cloud_front_origin_access_identity_config")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFrontOriginAccessIdentityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_051e6ed8)
class CfnDistribution(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution",
):
    """A CloudFormation ``AWS::CloudFront::Distribution``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html
    cloudformationResource:
    :cloudformationResource:: AWS::CloudFront::Distribution
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        distribution_config: typing.Union[
            "DistributionConfigProperty", _IResolvable_9ceae33e
        ],
        tags: typing.Optional[typing.List[_CfnTag_b4661f1a]] = None,
    ) -> None:
        """Create a new ``AWS::CloudFront::Distribution``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param distribution_config: ``AWS::CloudFront::Distribution.DistributionConfig``.
        :param tags: ``AWS::CloudFront::Distribution.Tags``.
        """
        props = CfnDistributionProps(distribution_config=distribution_config, tags=tags)

        jsii.create(CfnDistribution, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnDistribution":
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
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DomainName
        """
        return jsii.get(self, "attrDomainName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_2508893f:
        """``AWS::CloudFront::Distribution.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html#cfn-cloudfront-distribution-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="distributionConfig")
    def distribution_config(
        self,
    ) -> typing.Union["DistributionConfigProperty", _IResolvable_9ceae33e]:
        """``AWS::CloudFront::Distribution.DistributionConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html#cfn-cloudfront-distribution-distributionconfig
        """
        return jsii.get(self, "distributionConfig")

    @distribution_config.setter
    def distribution_config(
        self, value: typing.Union["DistributionConfigProperty", _IResolvable_9ceae33e]
    ) -> None:
        jsii.set(self, "distributionConfig", value)

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.CacheBehaviorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "forwarded_values": "forwardedValues",
            "path_pattern": "pathPattern",
            "target_origin_id": "targetOriginId",
            "viewer_protocol_policy": "viewerProtocolPolicy",
            "allowed_methods": "allowedMethods",
            "cached_methods": "cachedMethods",
            "compress": "compress",
            "default_ttl": "defaultTtl",
            "field_level_encryption_id": "fieldLevelEncryptionId",
            "lambda_function_associations": "lambdaFunctionAssociations",
            "max_ttl": "maxTtl",
            "min_ttl": "minTtl",
            "smooth_streaming": "smoothStreaming",
            "trusted_signers": "trustedSigners",
        },
    )
    class CacheBehaviorProperty:
        def __init__(
            self,
            *,
            forwarded_values: typing.Union[
                "CfnDistribution.ForwardedValuesProperty", _IResolvable_9ceae33e
            ],
            path_pattern: str,
            target_origin_id: str,
            viewer_protocol_policy: str,
            allowed_methods: typing.Optional[typing.List[str]] = None,
            cached_methods: typing.Optional[typing.List[str]] = None,
            compress: typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]] = None,
            default_ttl: typing.Optional[jsii.Number] = None,
            field_level_encryption_id: typing.Optional[str] = None,
            lambda_function_associations: typing.Optional[
                typing.Union[
                    _IResolvable_9ceae33e,
                    typing.List[
                        typing.Union[
                            "CfnDistribution.LambdaFunctionAssociationProperty",
                            _IResolvable_9ceae33e,
                        ]
                    ],
                ]
            ] = None,
            max_ttl: typing.Optional[jsii.Number] = None,
            min_ttl: typing.Optional[jsii.Number] = None,
            smooth_streaming: typing.Optional[
                typing.Union[bool, _IResolvable_9ceae33e]
            ] = None,
            trusted_signers: typing.Optional[typing.List[str]] = None,
        ) -> None:
            """
            :param forwarded_values: ``CfnDistribution.CacheBehaviorProperty.ForwardedValues``.
            :param path_pattern: ``CfnDistribution.CacheBehaviorProperty.PathPattern``.
            :param target_origin_id: ``CfnDistribution.CacheBehaviorProperty.TargetOriginId``.
            :param viewer_protocol_policy: ``CfnDistribution.CacheBehaviorProperty.ViewerProtocolPolicy``.
            :param allowed_methods: ``CfnDistribution.CacheBehaviorProperty.AllowedMethods``.
            :param cached_methods: ``CfnDistribution.CacheBehaviorProperty.CachedMethods``.
            :param compress: ``CfnDistribution.CacheBehaviorProperty.Compress``.
            :param default_ttl: ``CfnDistribution.CacheBehaviorProperty.DefaultTTL``.
            :param field_level_encryption_id: ``CfnDistribution.CacheBehaviorProperty.FieldLevelEncryptionId``.
            :param lambda_function_associations: ``CfnDistribution.CacheBehaviorProperty.LambdaFunctionAssociations``.
            :param max_ttl: ``CfnDistribution.CacheBehaviorProperty.MaxTTL``.
            :param min_ttl: ``CfnDistribution.CacheBehaviorProperty.MinTTL``.
            :param smooth_streaming: ``CfnDistribution.CacheBehaviorProperty.SmoothStreaming``.
            :param trusted_signers: ``CfnDistribution.CacheBehaviorProperty.TrustedSigners``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html
            """
            self._values = {
                "forwarded_values": forwarded_values,
                "path_pattern": path_pattern,
                "target_origin_id": target_origin_id,
                "viewer_protocol_policy": viewer_protocol_policy,
            }
            if allowed_methods is not None:
                self._values["allowed_methods"] = allowed_methods
            if cached_methods is not None:
                self._values["cached_methods"] = cached_methods
            if compress is not None:
                self._values["compress"] = compress
            if default_ttl is not None:
                self._values["default_ttl"] = default_ttl
            if field_level_encryption_id is not None:
                self._values["field_level_encryption_id"] = field_level_encryption_id
            if lambda_function_associations is not None:
                self._values[
                    "lambda_function_associations"
                ] = lambda_function_associations
            if max_ttl is not None:
                self._values["max_ttl"] = max_ttl
            if min_ttl is not None:
                self._values["min_ttl"] = min_ttl
            if smooth_streaming is not None:
                self._values["smooth_streaming"] = smooth_streaming
            if trusted_signers is not None:
                self._values["trusted_signers"] = trusted_signers

        @builtins.property
        def forwarded_values(
            self,
        ) -> typing.Union[
            "CfnDistribution.ForwardedValuesProperty", _IResolvable_9ceae33e
        ]:
            """``CfnDistribution.CacheBehaviorProperty.ForwardedValues``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-forwardedvalues
            """
            return self._values.get("forwarded_values")

        @builtins.property
        def path_pattern(self) -> str:
            """``CfnDistribution.CacheBehaviorProperty.PathPattern``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-pathpattern
            """
            return self._values.get("path_pattern")

        @builtins.property
        def target_origin_id(self) -> str:
            """``CfnDistribution.CacheBehaviorProperty.TargetOriginId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-targetoriginid
            """
            return self._values.get("target_origin_id")

        @builtins.property
        def viewer_protocol_policy(self) -> str:
            """``CfnDistribution.CacheBehaviorProperty.ViewerProtocolPolicy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-viewerprotocolpolicy
            """
            return self._values.get("viewer_protocol_policy")

        @builtins.property
        def allowed_methods(self) -> typing.Optional[typing.List[str]]:
            """``CfnDistribution.CacheBehaviorProperty.AllowedMethods``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-allowedmethods
            """
            return self._values.get("allowed_methods")

        @builtins.property
        def cached_methods(self) -> typing.Optional[typing.List[str]]:
            """``CfnDistribution.CacheBehaviorProperty.CachedMethods``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-cachedmethods
            """
            return self._values.get("cached_methods")

        @builtins.property
        def compress(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnDistribution.CacheBehaviorProperty.Compress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-compress
            """
            return self._values.get("compress")

        @builtins.property
        def default_ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.CacheBehaviorProperty.DefaultTTL``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-defaultttl
            """
            return self._values.get("default_ttl")

        @builtins.property
        def field_level_encryption_id(self) -> typing.Optional[str]:
            """``CfnDistribution.CacheBehaviorProperty.FieldLevelEncryptionId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-fieldlevelencryptionid
            """
            return self._values.get("field_level_encryption_id")

        @builtins.property
        def lambda_function_associations(
            self,
        ) -> typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union[
                        "CfnDistribution.LambdaFunctionAssociationProperty",
                        _IResolvable_9ceae33e,
                    ]
                ],
            ]
        ]:
            """``CfnDistribution.CacheBehaviorProperty.LambdaFunctionAssociations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-lambdafunctionassociations
            """
            return self._values.get("lambda_function_associations")

        @builtins.property
        def max_ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.CacheBehaviorProperty.MaxTTL``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-maxttl
            """
            return self._values.get("max_ttl")

        @builtins.property
        def min_ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.CacheBehaviorProperty.MinTTL``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-minttl
            """
            return self._values.get("min_ttl")

        @builtins.property
        def smooth_streaming(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnDistribution.CacheBehaviorProperty.SmoothStreaming``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-smoothstreaming
            """
            return self._values.get("smooth_streaming")

        @builtins.property
        def trusted_signers(self) -> typing.Optional[typing.List[str]]:
            """``CfnDistribution.CacheBehaviorProperty.TrustedSigners``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-trustedsigners
            """
            return self._values.get("trusted_signers")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CacheBehaviorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.CookiesProperty",
        jsii_struct_bases=[],
        name_mapping={"forward": "forward", "whitelisted_names": "whitelistedNames"},
    )
    class CookiesProperty:
        def __init__(
            self,
            *,
            forward: str,
            whitelisted_names: typing.Optional[typing.List[str]] = None,
        ) -> None:
            """
            :param forward: ``CfnDistribution.CookiesProperty.Forward``.
            :param whitelisted_names: ``CfnDistribution.CookiesProperty.WhitelistedNames``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html
            """
            self._values = {
                "forward": forward,
            }
            if whitelisted_names is not None:
                self._values["whitelisted_names"] = whitelisted_names

        @builtins.property
        def forward(self) -> str:
            """``CfnDistribution.CookiesProperty.Forward``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html#cfn-cloudfront-distribution-cookies-forward
            """
            return self._values.get("forward")

        @builtins.property
        def whitelisted_names(self) -> typing.Optional[typing.List[str]]:
            """``CfnDistribution.CookiesProperty.WhitelistedNames``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html#cfn-cloudfront-distribution-cookies-whitelistednames
            """
            return self._values.get("whitelisted_names")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CookiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.CustomErrorResponseProperty",
        jsii_struct_bases=[],
        name_mapping={
            "error_code": "errorCode",
            "error_caching_min_ttl": "errorCachingMinTtl",
            "response_code": "responseCode",
            "response_page_path": "responsePagePath",
        },
    )
    class CustomErrorResponseProperty:
        def __init__(
            self,
            *,
            error_code: jsii.Number,
            error_caching_min_ttl: typing.Optional[jsii.Number] = None,
            response_code: typing.Optional[jsii.Number] = None,
            response_page_path: typing.Optional[str] = None,
        ) -> None:
            """
            :param error_code: ``CfnDistribution.CustomErrorResponseProperty.ErrorCode``.
            :param error_caching_min_ttl: ``CfnDistribution.CustomErrorResponseProperty.ErrorCachingMinTTL``.
            :param response_code: ``CfnDistribution.CustomErrorResponseProperty.ResponseCode``.
            :param response_page_path: ``CfnDistribution.CustomErrorResponseProperty.ResponsePagePath``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html
            """
            self._values = {
                "error_code": error_code,
            }
            if error_caching_min_ttl is not None:
                self._values["error_caching_min_ttl"] = error_caching_min_ttl
            if response_code is not None:
                self._values["response_code"] = response_code
            if response_page_path is not None:
                self._values["response_page_path"] = response_page_path

        @builtins.property
        def error_code(self) -> jsii.Number:
            """``CfnDistribution.CustomErrorResponseProperty.ErrorCode``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-errorcode
            """
            return self._values.get("error_code")

        @builtins.property
        def error_caching_min_ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.CustomErrorResponseProperty.ErrorCachingMinTTL``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-errorcachingminttl
            """
            return self._values.get("error_caching_min_ttl")

        @builtins.property
        def response_code(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.CustomErrorResponseProperty.ResponseCode``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-responsecode
            """
            return self._values.get("response_code")

        @builtins.property
        def response_page_path(self) -> typing.Optional[str]:
            """``CfnDistribution.CustomErrorResponseProperty.ResponsePagePath``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-responsepagepath
            """
            return self._values.get("response_page_path")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomErrorResponseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.CustomOriginConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "origin_protocol_policy": "originProtocolPolicy",
            "http_port": "httpPort",
            "https_port": "httpsPort",
            "origin_keepalive_timeout": "originKeepaliveTimeout",
            "origin_read_timeout": "originReadTimeout",
            "origin_ssl_protocols": "originSslProtocols",
        },
    )
    class CustomOriginConfigProperty:
        def __init__(
            self,
            *,
            origin_protocol_policy: str,
            http_port: typing.Optional[jsii.Number] = None,
            https_port: typing.Optional[jsii.Number] = None,
            origin_keepalive_timeout: typing.Optional[jsii.Number] = None,
            origin_read_timeout: typing.Optional[jsii.Number] = None,
            origin_ssl_protocols: typing.Optional[typing.List[str]] = None,
        ) -> None:
            """
            :param origin_protocol_policy: ``CfnDistribution.CustomOriginConfigProperty.OriginProtocolPolicy``.
            :param http_port: ``CfnDistribution.CustomOriginConfigProperty.HTTPPort``.
            :param https_port: ``CfnDistribution.CustomOriginConfigProperty.HTTPSPort``.
            :param origin_keepalive_timeout: ``CfnDistribution.CustomOriginConfigProperty.OriginKeepaliveTimeout``.
            :param origin_read_timeout: ``CfnDistribution.CustomOriginConfigProperty.OriginReadTimeout``.
            :param origin_ssl_protocols: ``CfnDistribution.CustomOriginConfigProperty.OriginSSLProtocols``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html
            """
            self._values = {
                "origin_protocol_policy": origin_protocol_policy,
            }
            if http_port is not None:
                self._values["http_port"] = http_port
            if https_port is not None:
                self._values["https_port"] = https_port
            if origin_keepalive_timeout is not None:
                self._values["origin_keepalive_timeout"] = origin_keepalive_timeout
            if origin_read_timeout is not None:
                self._values["origin_read_timeout"] = origin_read_timeout
            if origin_ssl_protocols is not None:
                self._values["origin_ssl_protocols"] = origin_ssl_protocols

        @builtins.property
        def origin_protocol_policy(self) -> str:
            """``CfnDistribution.CustomOriginConfigProperty.OriginProtocolPolicy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originprotocolpolicy
            """
            return self._values.get("origin_protocol_policy")

        @builtins.property
        def http_port(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.CustomOriginConfigProperty.HTTPPort``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-httpport
            """
            return self._values.get("http_port")

        @builtins.property
        def https_port(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.CustomOriginConfigProperty.HTTPSPort``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-httpsport
            """
            return self._values.get("https_port")

        @builtins.property
        def origin_keepalive_timeout(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.CustomOriginConfigProperty.OriginKeepaliveTimeout``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originkeepalivetimeout
            """
            return self._values.get("origin_keepalive_timeout")

        @builtins.property
        def origin_read_timeout(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.CustomOriginConfigProperty.OriginReadTimeout``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originreadtimeout
            """
            return self._values.get("origin_read_timeout")

        @builtins.property
        def origin_ssl_protocols(self) -> typing.Optional[typing.List[str]]:
            """``CfnDistribution.CustomOriginConfigProperty.OriginSSLProtocols``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originsslprotocols
            """
            return self._values.get("origin_ssl_protocols")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomOriginConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.DefaultCacheBehaviorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "forwarded_values": "forwardedValues",
            "target_origin_id": "targetOriginId",
            "viewer_protocol_policy": "viewerProtocolPolicy",
            "allowed_methods": "allowedMethods",
            "cached_methods": "cachedMethods",
            "compress": "compress",
            "default_ttl": "defaultTtl",
            "field_level_encryption_id": "fieldLevelEncryptionId",
            "lambda_function_associations": "lambdaFunctionAssociations",
            "max_ttl": "maxTtl",
            "min_ttl": "minTtl",
            "smooth_streaming": "smoothStreaming",
            "trusted_signers": "trustedSigners",
        },
    )
    class DefaultCacheBehaviorProperty:
        def __init__(
            self,
            *,
            forwarded_values: typing.Union[
                "CfnDistribution.ForwardedValuesProperty", _IResolvable_9ceae33e
            ],
            target_origin_id: str,
            viewer_protocol_policy: str,
            allowed_methods: typing.Optional[typing.List[str]] = None,
            cached_methods: typing.Optional[typing.List[str]] = None,
            compress: typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]] = None,
            default_ttl: typing.Optional[jsii.Number] = None,
            field_level_encryption_id: typing.Optional[str] = None,
            lambda_function_associations: typing.Optional[
                typing.Union[
                    _IResolvable_9ceae33e,
                    typing.List[
                        typing.Union[
                            "CfnDistribution.LambdaFunctionAssociationProperty",
                            _IResolvable_9ceae33e,
                        ]
                    ],
                ]
            ] = None,
            max_ttl: typing.Optional[jsii.Number] = None,
            min_ttl: typing.Optional[jsii.Number] = None,
            smooth_streaming: typing.Optional[
                typing.Union[bool, _IResolvable_9ceae33e]
            ] = None,
            trusted_signers: typing.Optional[typing.List[str]] = None,
        ) -> None:
            """
            :param forwarded_values: ``CfnDistribution.DefaultCacheBehaviorProperty.ForwardedValues``.
            :param target_origin_id: ``CfnDistribution.DefaultCacheBehaviorProperty.TargetOriginId``.
            :param viewer_protocol_policy: ``CfnDistribution.DefaultCacheBehaviorProperty.ViewerProtocolPolicy``.
            :param allowed_methods: ``CfnDistribution.DefaultCacheBehaviorProperty.AllowedMethods``.
            :param cached_methods: ``CfnDistribution.DefaultCacheBehaviorProperty.CachedMethods``.
            :param compress: ``CfnDistribution.DefaultCacheBehaviorProperty.Compress``.
            :param default_ttl: ``CfnDistribution.DefaultCacheBehaviorProperty.DefaultTTL``.
            :param field_level_encryption_id: ``CfnDistribution.DefaultCacheBehaviorProperty.FieldLevelEncryptionId``.
            :param lambda_function_associations: ``CfnDistribution.DefaultCacheBehaviorProperty.LambdaFunctionAssociations``.
            :param max_ttl: ``CfnDistribution.DefaultCacheBehaviorProperty.MaxTTL``.
            :param min_ttl: ``CfnDistribution.DefaultCacheBehaviorProperty.MinTTL``.
            :param smooth_streaming: ``CfnDistribution.DefaultCacheBehaviorProperty.SmoothStreaming``.
            :param trusted_signers: ``CfnDistribution.DefaultCacheBehaviorProperty.TrustedSigners``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html
            """
            self._values = {
                "forwarded_values": forwarded_values,
                "target_origin_id": target_origin_id,
                "viewer_protocol_policy": viewer_protocol_policy,
            }
            if allowed_methods is not None:
                self._values["allowed_methods"] = allowed_methods
            if cached_methods is not None:
                self._values["cached_methods"] = cached_methods
            if compress is not None:
                self._values["compress"] = compress
            if default_ttl is not None:
                self._values["default_ttl"] = default_ttl
            if field_level_encryption_id is not None:
                self._values["field_level_encryption_id"] = field_level_encryption_id
            if lambda_function_associations is not None:
                self._values[
                    "lambda_function_associations"
                ] = lambda_function_associations
            if max_ttl is not None:
                self._values["max_ttl"] = max_ttl
            if min_ttl is not None:
                self._values["min_ttl"] = min_ttl
            if smooth_streaming is not None:
                self._values["smooth_streaming"] = smooth_streaming
            if trusted_signers is not None:
                self._values["trusted_signers"] = trusted_signers

        @builtins.property
        def forwarded_values(
            self,
        ) -> typing.Union[
            "CfnDistribution.ForwardedValuesProperty", _IResolvable_9ceae33e
        ]:
            """``CfnDistribution.DefaultCacheBehaviorProperty.ForwardedValues``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-forwardedvalues
            """
            return self._values.get("forwarded_values")

        @builtins.property
        def target_origin_id(self) -> str:
            """``CfnDistribution.DefaultCacheBehaviorProperty.TargetOriginId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-targetoriginid
            """
            return self._values.get("target_origin_id")

        @builtins.property
        def viewer_protocol_policy(self) -> str:
            """``CfnDistribution.DefaultCacheBehaviorProperty.ViewerProtocolPolicy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-viewerprotocolpolicy
            """
            return self._values.get("viewer_protocol_policy")

        @builtins.property
        def allowed_methods(self) -> typing.Optional[typing.List[str]]:
            """``CfnDistribution.DefaultCacheBehaviorProperty.AllowedMethods``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-allowedmethods
            """
            return self._values.get("allowed_methods")

        @builtins.property
        def cached_methods(self) -> typing.Optional[typing.List[str]]:
            """``CfnDistribution.DefaultCacheBehaviorProperty.CachedMethods``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-cachedmethods
            """
            return self._values.get("cached_methods")

        @builtins.property
        def compress(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnDistribution.DefaultCacheBehaviorProperty.Compress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-compress
            """
            return self._values.get("compress")

        @builtins.property
        def default_ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.DefaultCacheBehaviorProperty.DefaultTTL``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-defaultttl
            """
            return self._values.get("default_ttl")

        @builtins.property
        def field_level_encryption_id(self) -> typing.Optional[str]:
            """``CfnDistribution.DefaultCacheBehaviorProperty.FieldLevelEncryptionId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-fieldlevelencryptionid
            """
            return self._values.get("field_level_encryption_id")

        @builtins.property
        def lambda_function_associations(
            self,
        ) -> typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union[
                        "CfnDistribution.LambdaFunctionAssociationProperty",
                        _IResolvable_9ceae33e,
                    ]
                ],
            ]
        ]:
            """``CfnDistribution.DefaultCacheBehaviorProperty.LambdaFunctionAssociations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-lambdafunctionassociations
            """
            return self._values.get("lambda_function_associations")

        @builtins.property
        def max_ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.DefaultCacheBehaviorProperty.MaxTTL``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-maxttl
            """
            return self._values.get("max_ttl")

        @builtins.property
        def min_ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.DefaultCacheBehaviorProperty.MinTTL``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-minttl
            """
            return self._values.get("min_ttl")

        @builtins.property
        def smooth_streaming(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnDistribution.DefaultCacheBehaviorProperty.SmoothStreaming``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-smoothstreaming
            """
            return self._values.get("smooth_streaming")

        @builtins.property
        def trusted_signers(self) -> typing.Optional[typing.List[str]]:
            """``CfnDistribution.DefaultCacheBehaviorProperty.TrustedSigners``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-trustedsigners
            """
            return self._values.get("trusted_signers")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultCacheBehaviorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.DistributionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "aliases": "aliases",
            "cache_behaviors": "cacheBehaviors",
            "comment": "comment",
            "custom_error_responses": "customErrorResponses",
            "default_cache_behavior": "defaultCacheBehavior",
            "default_root_object": "defaultRootObject",
            "http_version": "httpVersion",
            "ipv6_enabled": "ipv6Enabled",
            "logging": "logging",
            "origin_groups": "originGroups",
            "origins": "origins",
            "price_class": "priceClass",
            "restrictions": "restrictions",
            "viewer_certificate": "viewerCertificate",
            "web_acl_id": "webAclId",
        },
    )
    class DistributionConfigProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[bool, _IResolvable_9ceae33e],
            aliases: typing.Optional[typing.List[str]] = None,
            cache_behaviors: typing.Optional[
                typing.Union[
                    _IResolvable_9ceae33e,
                    typing.List[
                        typing.Union[
                            "CfnDistribution.CacheBehaviorProperty",
                            _IResolvable_9ceae33e,
                        ]
                    ],
                ]
            ] = None,
            comment: typing.Optional[str] = None,
            custom_error_responses: typing.Optional[
                typing.Union[
                    _IResolvable_9ceae33e,
                    typing.List[
                        typing.Union[
                            "CfnDistribution.CustomErrorResponseProperty",
                            _IResolvable_9ceae33e,
                        ]
                    ],
                ]
            ] = None,
            default_cache_behavior: typing.Optional[
                typing.Union[
                    "CfnDistribution.DefaultCacheBehaviorProperty",
                    _IResolvable_9ceae33e,
                ]
            ] = None,
            default_root_object: typing.Optional[str] = None,
            http_version: typing.Optional[str] = None,
            ipv6_enabled: typing.Optional[
                typing.Union[bool, _IResolvable_9ceae33e]
            ] = None,
            logging: typing.Optional[
                typing.Union["CfnDistribution.LoggingProperty", _IResolvable_9ceae33e]
            ] = None,
            origin_groups: typing.Optional[
                typing.Union[
                    "CfnDistribution.OriginGroupsProperty", _IResolvable_9ceae33e
                ]
            ] = None,
            origins: typing.Optional[
                typing.Union[
                    _IResolvable_9ceae33e,
                    typing.List[
                        typing.Union[
                            "CfnDistribution.OriginProperty", _IResolvable_9ceae33e
                        ]
                    ],
                ]
            ] = None,
            price_class: typing.Optional[str] = None,
            restrictions: typing.Optional[
                typing.Union[
                    "CfnDistribution.RestrictionsProperty", _IResolvable_9ceae33e
                ]
            ] = None,
            viewer_certificate: typing.Optional[
                typing.Union[
                    "CfnDistribution.ViewerCertificateProperty", _IResolvable_9ceae33e
                ]
            ] = None,
            web_acl_id: typing.Optional[str] = None,
        ) -> None:
            """
            :param enabled: ``CfnDistribution.DistributionConfigProperty.Enabled``.
            :param aliases: ``CfnDistribution.DistributionConfigProperty.Aliases``.
            :param cache_behaviors: ``CfnDistribution.DistributionConfigProperty.CacheBehaviors``.
            :param comment: ``CfnDistribution.DistributionConfigProperty.Comment``.
            :param custom_error_responses: ``CfnDistribution.DistributionConfigProperty.CustomErrorResponses``.
            :param default_cache_behavior: ``CfnDistribution.DistributionConfigProperty.DefaultCacheBehavior``.
            :param default_root_object: ``CfnDistribution.DistributionConfigProperty.DefaultRootObject``.
            :param http_version: ``CfnDistribution.DistributionConfigProperty.HttpVersion``.
            :param ipv6_enabled: ``CfnDistribution.DistributionConfigProperty.IPV6Enabled``.
            :param logging: ``CfnDistribution.DistributionConfigProperty.Logging``.
            :param origin_groups: ``CfnDistribution.DistributionConfigProperty.OriginGroups``.
            :param origins: ``CfnDistribution.DistributionConfigProperty.Origins``.
            :param price_class: ``CfnDistribution.DistributionConfigProperty.PriceClass``.
            :param restrictions: ``CfnDistribution.DistributionConfigProperty.Restrictions``.
            :param viewer_certificate: ``CfnDistribution.DistributionConfigProperty.ViewerCertificate``.
            :param web_acl_id: ``CfnDistribution.DistributionConfigProperty.WebACLId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html
            """
            self._values = {
                "enabled": enabled,
            }
            if aliases is not None:
                self._values["aliases"] = aliases
            if cache_behaviors is not None:
                self._values["cache_behaviors"] = cache_behaviors
            if comment is not None:
                self._values["comment"] = comment
            if custom_error_responses is not None:
                self._values["custom_error_responses"] = custom_error_responses
            if default_cache_behavior is not None:
                self._values["default_cache_behavior"] = default_cache_behavior
            if default_root_object is not None:
                self._values["default_root_object"] = default_root_object
            if http_version is not None:
                self._values["http_version"] = http_version
            if ipv6_enabled is not None:
                self._values["ipv6_enabled"] = ipv6_enabled
            if logging is not None:
                self._values["logging"] = logging
            if origin_groups is not None:
                self._values["origin_groups"] = origin_groups
            if origins is not None:
                self._values["origins"] = origins
            if price_class is not None:
                self._values["price_class"] = price_class
            if restrictions is not None:
                self._values["restrictions"] = restrictions
            if viewer_certificate is not None:
                self._values["viewer_certificate"] = viewer_certificate
            if web_acl_id is not None:
                self._values["web_acl_id"] = web_acl_id

        @builtins.property
        def enabled(self) -> typing.Union[bool, _IResolvable_9ceae33e]:
            """``CfnDistribution.DistributionConfigProperty.Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-enabled
            """
            return self._values.get("enabled")

        @builtins.property
        def aliases(self) -> typing.Optional[typing.List[str]]:
            """``CfnDistribution.DistributionConfigProperty.Aliases``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-aliases
            """
            return self._values.get("aliases")

        @builtins.property
        def cache_behaviors(
            self,
        ) -> typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union[
                        "CfnDistribution.CacheBehaviorProperty", _IResolvable_9ceae33e
                    ]
                ],
            ]
        ]:
            """``CfnDistribution.DistributionConfigProperty.CacheBehaviors``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-cachebehaviors
            """
            return self._values.get("cache_behaviors")

        @builtins.property
        def comment(self) -> typing.Optional[str]:
            """``CfnDistribution.DistributionConfigProperty.Comment``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-comment
            """
            return self._values.get("comment")

        @builtins.property
        def custom_error_responses(
            self,
        ) -> typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union[
                        "CfnDistribution.CustomErrorResponseProperty",
                        _IResolvable_9ceae33e,
                    ]
                ],
            ]
        ]:
            """``CfnDistribution.DistributionConfigProperty.CustomErrorResponses``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-customerrorresponses
            """
            return self._values.get("custom_error_responses")

        @builtins.property
        def default_cache_behavior(
            self,
        ) -> typing.Optional[
            typing.Union[
                "CfnDistribution.DefaultCacheBehaviorProperty", _IResolvable_9ceae33e
            ]
        ]:
            """``CfnDistribution.DistributionConfigProperty.DefaultCacheBehavior``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-defaultcachebehavior
            """
            return self._values.get("default_cache_behavior")

        @builtins.property
        def default_root_object(self) -> typing.Optional[str]:
            """``CfnDistribution.DistributionConfigProperty.DefaultRootObject``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-defaultrootobject
            """
            return self._values.get("default_root_object")

        @builtins.property
        def http_version(self) -> typing.Optional[str]:
            """``CfnDistribution.DistributionConfigProperty.HttpVersion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-httpversion
            """
            return self._values.get("http_version")

        @builtins.property
        def ipv6_enabled(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnDistribution.DistributionConfigProperty.IPV6Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-ipv6enabled
            """
            return self._values.get("ipv6_enabled")

        @builtins.property
        def logging(
            self,
        ) -> typing.Optional[
            typing.Union["CfnDistribution.LoggingProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnDistribution.DistributionConfigProperty.Logging``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-logging
            """
            return self._values.get("logging")

        @builtins.property
        def origin_groups(
            self,
        ) -> typing.Optional[
            typing.Union["CfnDistribution.OriginGroupsProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnDistribution.DistributionConfigProperty.OriginGroups``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-origingroups
            """
            return self._values.get("origin_groups")

        @builtins.property
        def origins(
            self,
        ) -> typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union[
                        "CfnDistribution.OriginProperty", _IResolvable_9ceae33e
                    ]
                ],
            ]
        ]:
            """``CfnDistribution.DistributionConfigProperty.Origins``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-origins
            """
            return self._values.get("origins")

        @builtins.property
        def price_class(self) -> typing.Optional[str]:
            """``CfnDistribution.DistributionConfigProperty.PriceClass``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-priceclass
            """
            return self._values.get("price_class")

        @builtins.property
        def restrictions(
            self,
        ) -> typing.Optional[
            typing.Union["CfnDistribution.RestrictionsProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnDistribution.DistributionConfigProperty.Restrictions``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-restrictions
            """
            return self._values.get("restrictions")

        @builtins.property
        def viewer_certificate(
            self,
        ) -> typing.Optional[
            typing.Union[
                "CfnDistribution.ViewerCertificateProperty", _IResolvable_9ceae33e
            ]
        ]:
            """``CfnDistribution.DistributionConfigProperty.ViewerCertificate``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-viewercertificate
            """
            return self._values.get("viewer_certificate")

        @builtins.property
        def web_acl_id(self) -> typing.Optional[str]:
            """``CfnDistribution.DistributionConfigProperty.WebACLId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-webaclid
            """
            return self._values.get("web_acl_id")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DistributionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.ForwardedValuesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "query_string": "queryString",
            "cookies": "cookies",
            "headers": "headers",
            "query_string_cache_keys": "queryStringCacheKeys",
        },
    )
    class ForwardedValuesProperty:
        def __init__(
            self,
            *,
            query_string: typing.Union[bool, _IResolvable_9ceae33e],
            cookies: typing.Optional[
                typing.Union["CfnDistribution.CookiesProperty", _IResolvable_9ceae33e]
            ] = None,
            headers: typing.Optional[typing.List[str]] = None,
            query_string_cache_keys: typing.Optional[typing.List[str]] = None,
        ) -> None:
            """
            :param query_string: ``CfnDistribution.ForwardedValuesProperty.QueryString``.
            :param cookies: ``CfnDistribution.ForwardedValuesProperty.Cookies``.
            :param headers: ``CfnDistribution.ForwardedValuesProperty.Headers``.
            :param query_string_cache_keys: ``CfnDistribution.ForwardedValuesProperty.QueryStringCacheKeys``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html
            """
            self._values = {
                "query_string": query_string,
            }
            if cookies is not None:
                self._values["cookies"] = cookies
            if headers is not None:
                self._values["headers"] = headers
            if query_string_cache_keys is not None:
                self._values["query_string_cache_keys"] = query_string_cache_keys

        @builtins.property
        def query_string(self) -> typing.Union[bool, _IResolvable_9ceae33e]:
            """``CfnDistribution.ForwardedValuesProperty.QueryString``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-querystring
            """
            return self._values.get("query_string")

        @builtins.property
        def cookies(
            self,
        ) -> typing.Optional[
            typing.Union["CfnDistribution.CookiesProperty", _IResolvable_9ceae33e]
        ]:
            """``CfnDistribution.ForwardedValuesProperty.Cookies``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-cookies
            """
            return self._values.get("cookies")

        @builtins.property
        def headers(self) -> typing.Optional[typing.List[str]]:
            """``CfnDistribution.ForwardedValuesProperty.Headers``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-headers
            """
            return self._values.get("headers")

        @builtins.property
        def query_string_cache_keys(self) -> typing.Optional[typing.List[str]]:
            """``CfnDistribution.ForwardedValuesProperty.QueryStringCacheKeys``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-querystringcachekeys
            """
            return self._values.get("query_string_cache_keys")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ForwardedValuesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.GeoRestrictionProperty",
        jsii_struct_bases=[],
        name_mapping={"restriction_type": "restrictionType", "locations": "locations"},
    )
    class GeoRestrictionProperty:
        def __init__(
            self,
            *,
            restriction_type: str,
            locations: typing.Optional[typing.List[str]] = None,
        ) -> None:
            """
            :param restriction_type: ``CfnDistribution.GeoRestrictionProperty.RestrictionType``.
            :param locations: ``CfnDistribution.GeoRestrictionProperty.Locations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html
            """
            self._values = {
                "restriction_type": restriction_type,
            }
            if locations is not None:
                self._values["locations"] = locations

        @builtins.property
        def restriction_type(self) -> str:
            """``CfnDistribution.GeoRestrictionProperty.RestrictionType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html#cfn-cloudfront-distribution-georestriction-restrictiontype
            """
            return self._values.get("restriction_type")

        @builtins.property
        def locations(self) -> typing.Optional[typing.List[str]]:
            """``CfnDistribution.GeoRestrictionProperty.Locations``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html#cfn-cloudfront-distribution-georestriction-locations
            """
            return self._values.get("locations")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeoRestrictionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.LambdaFunctionAssociationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_type": "eventType",
            "include_body": "includeBody",
            "lambda_function_arn": "lambdaFunctionArn",
        },
    )
    class LambdaFunctionAssociationProperty:
        def __init__(
            self,
            *,
            event_type: typing.Optional[str] = None,
            include_body: typing.Optional[
                typing.Union[bool, _IResolvable_9ceae33e]
            ] = None,
            lambda_function_arn: typing.Optional[str] = None,
        ) -> None:
            """
            :param event_type: ``CfnDistribution.LambdaFunctionAssociationProperty.EventType``.
            :param include_body: ``CfnDistribution.LambdaFunctionAssociationProperty.IncludeBody``.
            :param lambda_function_arn: ``CfnDistribution.LambdaFunctionAssociationProperty.LambdaFunctionARN``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html
            """
            self._values = {}
            if event_type is not None:
                self._values["event_type"] = event_type
            if include_body is not None:
                self._values["include_body"] = include_body
            if lambda_function_arn is not None:
                self._values["lambda_function_arn"] = lambda_function_arn

        @builtins.property
        def event_type(self) -> typing.Optional[str]:
            """``CfnDistribution.LambdaFunctionAssociationProperty.EventType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html#cfn-cloudfront-distribution-lambdafunctionassociation-eventtype
            """
            return self._values.get("event_type")

        @builtins.property
        def include_body(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnDistribution.LambdaFunctionAssociationProperty.IncludeBody``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html#cfn-cloudfront-distribution-lambdafunctionassociation-includebody
            """
            return self._values.get("include_body")

        @builtins.property
        def lambda_function_arn(self) -> typing.Optional[str]:
            """``CfnDistribution.LambdaFunctionAssociationProperty.LambdaFunctionARN``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html#cfn-cloudfront-distribution-lambdafunctionassociation-lambdafunctionarn
            """
            return self._values.get("lambda_function_arn")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaFunctionAssociationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.LoggingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "include_cookies": "includeCookies",
            "prefix": "prefix",
        },
    )
    class LoggingProperty:
        def __init__(
            self,
            *,
            bucket: str,
            include_cookies: typing.Optional[
                typing.Union[bool, _IResolvable_9ceae33e]
            ] = None,
            prefix: typing.Optional[str] = None,
        ) -> None:
            """
            :param bucket: ``CfnDistribution.LoggingProperty.Bucket``.
            :param include_cookies: ``CfnDistribution.LoggingProperty.IncludeCookies``.
            :param prefix: ``CfnDistribution.LoggingProperty.Prefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html
            """
            self._values = {
                "bucket": bucket,
            }
            if include_cookies is not None:
                self._values["include_cookies"] = include_cookies
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def bucket(self) -> str:
            """``CfnDistribution.LoggingProperty.Bucket``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html#cfn-cloudfront-distribution-logging-bucket
            """
            return self._values.get("bucket")

        @builtins.property
        def include_cookies(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnDistribution.LoggingProperty.IncludeCookies``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html#cfn-cloudfront-distribution-logging-includecookies
            """
            return self._values.get("include_cookies")

        @builtins.property
        def prefix(self) -> typing.Optional[str]:
            """``CfnDistribution.LoggingProperty.Prefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html#cfn-cloudfront-distribution-logging-prefix
            """
            return self._values.get("prefix")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.OriginCustomHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={"header_name": "headerName", "header_value": "headerValue"},
    )
    class OriginCustomHeaderProperty:
        def __init__(self, *, header_name: str, header_value: str) -> None:
            """
            :param header_name: ``CfnDistribution.OriginCustomHeaderProperty.HeaderName``.
            :param header_value: ``CfnDistribution.OriginCustomHeaderProperty.HeaderValue``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html
            """
            self._values = {
                "header_name": header_name,
                "header_value": header_value,
            }

        @builtins.property
        def header_name(self) -> str:
            """``CfnDistribution.OriginCustomHeaderProperty.HeaderName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html#cfn-cloudfront-distribution-origincustomheader-headername
            """
            return self._values.get("header_name")

        @builtins.property
        def header_value(self) -> str:
            """``CfnDistribution.OriginCustomHeaderProperty.HeaderValue``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html#cfn-cloudfront-distribution-origincustomheader-headervalue
            """
            return self._values.get("header_value")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OriginCustomHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.OriginGroupFailoverCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"status_codes": "statusCodes"},
    )
    class OriginGroupFailoverCriteriaProperty:
        def __init__(
            self,
            *,
            status_codes: typing.Union[
                "CfnDistribution.StatusCodesProperty", _IResolvable_9ceae33e
            ],
        ) -> None:
            """
            :param status_codes: ``CfnDistribution.OriginGroupFailoverCriteriaProperty.StatusCodes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html
            """
            self._values = {
                "status_codes": status_codes,
            }

        @builtins.property
        def status_codes(
            self,
        ) -> typing.Union["CfnDistribution.StatusCodesProperty", _IResolvable_9ceae33e]:
            """``CfnDistribution.OriginGroupFailoverCriteriaProperty.StatusCodes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html#cfn-cloudfront-distribution-origingroupfailovercriteria-statuscodes
            """
            return self._values.get("status_codes")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OriginGroupFailoverCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.OriginGroupMemberProperty",
        jsii_struct_bases=[],
        name_mapping={"origin_id": "originId"},
    )
    class OriginGroupMemberProperty:
        def __init__(self, *, origin_id: str) -> None:
            """
            :param origin_id: ``CfnDistribution.OriginGroupMemberProperty.OriginId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html
            """
            self._values = {
                "origin_id": origin_id,
            }

        @builtins.property
        def origin_id(self) -> str:
            """``CfnDistribution.OriginGroupMemberProperty.OriginId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html#cfn-cloudfront-distribution-origingroupmember-originid
            """
            return self._values.get("origin_id")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OriginGroupMemberProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.OriginGroupMembersProperty",
        jsii_struct_bases=[],
        name_mapping={"items": "items", "quantity": "quantity"},
    )
    class OriginGroupMembersProperty:
        def __init__(
            self,
            *,
            items: typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union[
                        "CfnDistribution.OriginGroupMemberProperty",
                        _IResolvable_9ceae33e,
                    ]
                ],
            ],
            quantity: jsii.Number,
        ) -> None:
            """
            :param items: ``CfnDistribution.OriginGroupMembersProperty.Items``.
            :param quantity: ``CfnDistribution.OriginGroupMembersProperty.Quantity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html
            """
            self._values = {
                "items": items,
                "quantity": quantity,
            }

        @builtins.property
        def items(
            self,
        ) -> typing.Union[
            _IResolvable_9ceae33e,
            typing.List[
                typing.Union[
                    "CfnDistribution.OriginGroupMemberProperty", _IResolvable_9ceae33e
                ]
            ],
        ]:
            """``CfnDistribution.OriginGroupMembersProperty.Items``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html#cfn-cloudfront-distribution-origingroupmembers-items
            """
            return self._values.get("items")

        @builtins.property
        def quantity(self) -> jsii.Number:
            """``CfnDistribution.OriginGroupMembersProperty.Quantity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html#cfn-cloudfront-distribution-origingroupmembers-quantity
            """
            return self._values.get("quantity")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OriginGroupMembersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.OriginGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "failover_criteria": "failoverCriteria",
            "id": "id",
            "members": "members",
        },
    )
    class OriginGroupProperty:
        def __init__(
            self,
            *,
            failover_criteria: typing.Union[
                "CfnDistribution.OriginGroupFailoverCriteriaProperty",
                _IResolvable_9ceae33e,
            ],
            id: str,
            members: typing.Union[
                "CfnDistribution.OriginGroupMembersProperty", _IResolvable_9ceae33e
            ],
        ) -> None:
            """
            :param failover_criteria: ``CfnDistribution.OriginGroupProperty.FailoverCriteria``.
            :param id: ``CfnDistribution.OriginGroupProperty.Id``.
            :param members: ``CfnDistribution.OriginGroupProperty.Members``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html
            """
            self._values = {
                "failover_criteria": failover_criteria,
                "id": id,
                "members": members,
            }

        @builtins.property
        def failover_criteria(
            self,
        ) -> typing.Union[
            "CfnDistribution.OriginGroupFailoverCriteriaProperty", _IResolvable_9ceae33e
        ]:
            """``CfnDistribution.OriginGroupProperty.FailoverCriteria``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html#cfn-cloudfront-distribution-origingroup-failovercriteria
            """
            return self._values.get("failover_criteria")

        @builtins.property
        def id(self) -> str:
            """``CfnDistribution.OriginGroupProperty.Id``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html#cfn-cloudfront-distribution-origingroup-id
            """
            return self._values.get("id")

        @builtins.property
        def members(
            self,
        ) -> typing.Union[
            "CfnDistribution.OriginGroupMembersProperty", _IResolvable_9ceae33e
        ]:
            """``CfnDistribution.OriginGroupProperty.Members``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html#cfn-cloudfront-distribution-origingroup-members
            """
            return self._values.get("members")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OriginGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.OriginGroupsProperty",
        jsii_struct_bases=[],
        name_mapping={"quantity": "quantity", "items": "items"},
    )
    class OriginGroupsProperty:
        def __init__(
            self,
            *,
            quantity: jsii.Number,
            items: typing.Optional[
                typing.Union[
                    _IResolvable_9ceae33e,
                    typing.List[
                        typing.Union[
                            "CfnDistribution.OriginGroupProperty", _IResolvable_9ceae33e
                        ]
                    ],
                ]
            ] = None,
        ) -> None:
            """
            :param quantity: ``CfnDistribution.OriginGroupsProperty.Quantity``.
            :param items: ``CfnDistribution.OriginGroupsProperty.Items``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html
            """
            self._values = {
                "quantity": quantity,
            }
            if items is not None:
                self._values["items"] = items

        @builtins.property
        def quantity(self) -> jsii.Number:
            """``CfnDistribution.OriginGroupsProperty.Quantity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html#cfn-cloudfront-distribution-origingroups-quantity
            """
            return self._values.get("quantity")

        @builtins.property
        def items(
            self,
        ) -> typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union[
                        "CfnDistribution.OriginGroupProperty", _IResolvable_9ceae33e
                    ]
                ],
            ]
        ]:
            """``CfnDistribution.OriginGroupsProperty.Items``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html#cfn-cloudfront-distribution-origingroups-items
            """
            return self._values.get("items")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OriginGroupsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.OriginProperty",
        jsii_struct_bases=[],
        name_mapping={
            "domain_name": "domainName",
            "id": "id",
            "connection_attempts": "connectionAttempts",
            "connection_timeout": "connectionTimeout",
            "custom_origin_config": "customOriginConfig",
            "origin_custom_headers": "originCustomHeaders",
            "origin_path": "originPath",
            "s3_origin_config": "s3OriginConfig",
        },
    )
    class OriginProperty:
        def __init__(
            self,
            *,
            domain_name: str,
            id: str,
            connection_attempts: typing.Optional[jsii.Number] = None,
            connection_timeout: typing.Optional[jsii.Number] = None,
            custom_origin_config: typing.Optional[
                typing.Union[
                    "CfnDistribution.CustomOriginConfigProperty", _IResolvable_9ceae33e
                ]
            ] = None,
            origin_custom_headers: typing.Optional[
                typing.Union[
                    _IResolvable_9ceae33e,
                    typing.List[
                        typing.Union[
                            "CfnDistribution.OriginCustomHeaderProperty",
                            _IResolvable_9ceae33e,
                        ]
                    ],
                ]
            ] = None,
            origin_path: typing.Optional[str] = None,
            s3_origin_config: typing.Optional[
                typing.Union[
                    "CfnDistribution.S3OriginConfigProperty", _IResolvable_9ceae33e
                ]
            ] = None,
        ) -> None:
            """
            :param domain_name: ``CfnDistribution.OriginProperty.DomainName``.
            :param id: ``CfnDistribution.OriginProperty.Id``.
            :param connection_attempts: ``CfnDistribution.OriginProperty.ConnectionAttempts``.
            :param connection_timeout: ``CfnDistribution.OriginProperty.ConnectionTimeout``.
            :param custom_origin_config: ``CfnDistribution.OriginProperty.CustomOriginConfig``.
            :param origin_custom_headers: ``CfnDistribution.OriginProperty.OriginCustomHeaders``.
            :param origin_path: ``CfnDistribution.OriginProperty.OriginPath``.
            :param s3_origin_config: ``CfnDistribution.OriginProperty.S3OriginConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html
            """
            self._values = {
                "domain_name": domain_name,
                "id": id,
            }
            if connection_attempts is not None:
                self._values["connection_attempts"] = connection_attempts
            if connection_timeout is not None:
                self._values["connection_timeout"] = connection_timeout
            if custom_origin_config is not None:
                self._values["custom_origin_config"] = custom_origin_config
            if origin_custom_headers is not None:
                self._values["origin_custom_headers"] = origin_custom_headers
            if origin_path is not None:
                self._values["origin_path"] = origin_path
            if s3_origin_config is not None:
                self._values["s3_origin_config"] = s3_origin_config

        @builtins.property
        def domain_name(self) -> str:
            """``CfnDistribution.OriginProperty.DomainName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-domainname
            """
            return self._values.get("domain_name")

        @builtins.property
        def id(self) -> str:
            """``CfnDistribution.OriginProperty.Id``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-id
            """
            return self._values.get("id")

        @builtins.property
        def connection_attempts(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.OriginProperty.ConnectionAttempts``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-connectionattempts
            """
            return self._values.get("connection_attempts")

        @builtins.property
        def connection_timeout(self) -> typing.Optional[jsii.Number]:
            """``CfnDistribution.OriginProperty.ConnectionTimeout``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-connectiontimeout
            """
            return self._values.get("connection_timeout")

        @builtins.property
        def custom_origin_config(
            self,
        ) -> typing.Optional[
            typing.Union[
                "CfnDistribution.CustomOriginConfigProperty", _IResolvable_9ceae33e
            ]
        ]:
            """``CfnDistribution.OriginProperty.CustomOriginConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-customoriginconfig
            """
            return self._values.get("custom_origin_config")

        @builtins.property
        def origin_custom_headers(
            self,
        ) -> typing.Optional[
            typing.Union[
                _IResolvable_9ceae33e,
                typing.List[
                    typing.Union[
                        "CfnDistribution.OriginCustomHeaderProperty",
                        _IResolvable_9ceae33e,
                    ]
                ],
            ]
        ]:
            """``CfnDistribution.OriginProperty.OriginCustomHeaders``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-origincustomheaders
            """
            return self._values.get("origin_custom_headers")

        @builtins.property
        def origin_path(self) -> typing.Optional[str]:
            """``CfnDistribution.OriginProperty.OriginPath``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-originpath
            """
            return self._values.get("origin_path")

        @builtins.property
        def s3_origin_config(
            self,
        ) -> typing.Optional[
            typing.Union[
                "CfnDistribution.S3OriginConfigProperty", _IResolvable_9ceae33e
            ]
        ]:
            """``CfnDistribution.OriginProperty.S3OriginConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-s3originconfig
            """
            return self._values.get("s3_origin_config")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OriginProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.RestrictionsProperty",
        jsii_struct_bases=[],
        name_mapping={"geo_restriction": "geoRestriction"},
    )
    class RestrictionsProperty:
        def __init__(
            self,
            *,
            geo_restriction: typing.Union[
                "CfnDistribution.GeoRestrictionProperty", _IResolvable_9ceae33e
            ],
        ) -> None:
            """
            :param geo_restriction: ``CfnDistribution.RestrictionsProperty.GeoRestriction``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-restrictions.html
            """
            self._values = {
                "geo_restriction": geo_restriction,
            }

        @builtins.property
        def geo_restriction(
            self,
        ) -> typing.Union[
            "CfnDistribution.GeoRestrictionProperty", _IResolvable_9ceae33e
        ]:
            """``CfnDistribution.RestrictionsProperty.GeoRestriction``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-restrictions.html#cfn-cloudfront-distribution-restrictions-georestriction
            """
            return self._values.get("geo_restriction")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RestrictionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.S3OriginConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"origin_access_identity": "originAccessIdentity"},
    )
    class S3OriginConfigProperty:
        def __init__(
            self, *, origin_access_identity: typing.Optional[str] = None
        ) -> None:
            """
            :param origin_access_identity: ``CfnDistribution.S3OriginConfigProperty.OriginAccessIdentity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-s3originconfig.html
            """
            self._values = {}
            if origin_access_identity is not None:
                self._values["origin_access_identity"] = origin_access_identity

        @builtins.property
        def origin_access_identity(self) -> typing.Optional[str]:
            """``CfnDistribution.S3OriginConfigProperty.OriginAccessIdentity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-s3originconfig.html#cfn-cloudfront-distribution-s3originconfig-originaccessidentity
            """
            return self._values.get("origin_access_identity")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OriginConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.StatusCodesProperty",
        jsii_struct_bases=[],
        name_mapping={"items": "items", "quantity": "quantity"},
    )
    class StatusCodesProperty:
        def __init__(
            self,
            *,
            items: typing.Union[_IResolvable_9ceae33e, typing.List[jsii.Number]],
            quantity: jsii.Number,
        ) -> None:
            """
            :param items: ``CfnDistribution.StatusCodesProperty.Items``.
            :param quantity: ``CfnDistribution.StatusCodesProperty.Quantity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html
            """
            self._values = {
                "items": items,
                "quantity": quantity,
            }

        @builtins.property
        def items(
            self,
        ) -> typing.Union[_IResolvable_9ceae33e, typing.List[jsii.Number]]:
            """``CfnDistribution.StatusCodesProperty.Items``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html#cfn-cloudfront-distribution-statuscodes-items
            """
            return self._values.get("items")

        @builtins.property
        def quantity(self) -> jsii.Number:
            """``CfnDistribution.StatusCodesProperty.Quantity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html#cfn-cloudfront-distribution-statuscodes-quantity
            """
            return self._values.get("quantity")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatusCodesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnDistribution.ViewerCertificateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "acm_certificate_arn": "acmCertificateArn",
            "cloud_front_default_certificate": "cloudFrontDefaultCertificate",
            "iam_certificate_id": "iamCertificateId",
            "minimum_protocol_version": "minimumProtocolVersion",
            "ssl_support_method": "sslSupportMethod",
        },
    )
    class ViewerCertificateProperty:
        def __init__(
            self,
            *,
            acm_certificate_arn: typing.Optional[str] = None,
            cloud_front_default_certificate: typing.Optional[
                typing.Union[bool, _IResolvable_9ceae33e]
            ] = None,
            iam_certificate_id: typing.Optional[str] = None,
            minimum_protocol_version: typing.Optional[str] = None,
            ssl_support_method: typing.Optional[str] = None,
        ) -> None:
            """
            :param acm_certificate_arn: ``CfnDistribution.ViewerCertificateProperty.AcmCertificateArn``.
            :param cloud_front_default_certificate: ``CfnDistribution.ViewerCertificateProperty.CloudFrontDefaultCertificate``.
            :param iam_certificate_id: ``CfnDistribution.ViewerCertificateProperty.IamCertificateId``.
            :param minimum_protocol_version: ``CfnDistribution.ViewerCertificateProperty.MinimumProtocolVersion``.
            :param ssl_support_method: ``CfnDistribution.ViewerCertificateProperty.SslSupportMethod``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html
            """
            self._values = {}
            if acm_certificate_arn is not None:
                self._values["acm_certificate_arn"] = acm_certificate_arn
            if cloud_front_default_certificate is not None:
                self._values[
                    "cloud_front_default_certificate"
                ] = cloud_front_default_certificate
            if iam_certificate_id is not None:
                self._values["iam_certificate_id"] = iam_certificate_id
            if minimum_protocol_version is not None:
                self._values["minimum_protocol_version"] = minimum_protocol_version
            if ssl_support_method is not None:
                self._values["ssl_support_method"] = ssl_support_method

        @builtins.property
        def acm_certificate_arn(self) -> typing.Optional[str]:
            """``CfnDistribution.ViewerCertificateProperty.AcmCertificateArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-acmcertificatearn
            """
            return self._values.get("acm_certificate_arn")

        @builtins.property
        def cloud_front_default_certificate(
            self,
        ) -> typing.Optional[typing.Union[bool, _IResolvable_9ceae33e]]:
            """``CfnDistribution.ViewerCertificateProperty.CloudFrontDefaultCertificate``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-cloudfrontdefaultcertificate
            """
            return self._values.get("cloud_front_default_certificate")

        @builtins.property
        def iam_certificate_id(self) -> typing.Optional[str]:
            """``CfnDistribution.ViewerCertificateProperty.IamCertificateId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-iamcertificateid
            """
            return self._values.get("iam_certificate_id")

        @builtins.property
        def minimum_protocol_version(self) -> typing.Optional[str]:
            """``CfnDistribution.ViewerCertificateProperty.MinimumProtocolVersion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-minimumprotocolversion
            """
            return self._values.get("minimum_protocol_version")

        @builtins.property
        def ssl_support_method(self) -> typing.Optional[str]:
            """``CfnDistribution.ViewerCertificateProperty.SslSupportMethod``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-sslsupportmethod
            """
            return self._values.get("ssl_support_method")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ViewerCertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.CfnDistributionProps",
    jsii_struct_bases=[],
    name_mapping={"distribution_config": "distributionConfig", "tags": "tags"},
)
class CfnDistributionProps:
    def __init__(
        self,
        *,
        distribution_config: typing.Union[
            "CfnDistribution.DistributionConfigProperty", _IResolvable_9ceae33e
        ],
        tags: typing.Optional[typing.List[_CfnTag_b4661f1a]] = None,
    ) -> None:
        """Properties for defining a ``AWS::CloudFront::Distribution``.

        :param distribution_config: ``AWS::CloudFront::Distribution.DistributionConfig``.
        :param tags: ``AWS::CloudFront::Distribution.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html
        """
        self._values = {
            "distribution_config": distribution_config,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def distribution_config(
        self,
    ) -> typing.Union[
        "CfnDistribution.DistributionConfigProperty", _IResolvable_9ceae33e
    ]:
        """``AWS::CloudFront::Distribution.DistributionConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html#cfn-cloudfront-distribution-distributionconfig
        """
        return self._values.get("distribution_config")

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_b4661f1a]]:
        """``AWS::CloudFront::Distribution.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html#cfn-cloudfront-distribution-tags
        """
        return self._values.get("tags")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_051e6ed8)
class CfnStreamingDistribution(
    _CfnResource_7760e8e4,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_cloudfront.CfnStreamingDistribution",
):
    """A CloudFormation ``AWS::CloudFront::StreamingDistribution``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html
    cloudformationResource:
    :cloudformationResource:: AWS::CloudFront::StreamingDistribution
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        streaming_distribution_config: typing.Union[
            "StreamingDistributionConfigProperty", _IResolvable_9ceae33e
        ],
        tags: typing.List[_CfnTag_b4661f1a],
    ) -> None:
        """Create a new ``AWS::CloudFront::StreamingDistribution``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param streaming_distribution_config: ``AWS::CloudFront::StreamingDistribution.StreamingDistributionConfig``.
        :param tags: ``AWS::CloudFront::StreamingDistribution.Tags``.
        """
        props = CfnStreamingDistributionProps(
            streaming_distribution_config=streaming_distribution_config, tags=tags
        )

        jsii.create(CfnStreamingDistribution, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: _ICfnFinder_3b168f30,
    ) -> "CfnStreamingDistribution":
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
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DomainName
        """
        return jsii.get(self, "attrDomainName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_2508893f:
        """``AWS::CloudFront::StreamingDistribution.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html#cfn-cloudfront-streamingdistribution-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="streamingDistributionConfig")
    def streaming_distribution_config(
        self,
    ) -> typing.Union["StreamingDistributionConfigProperty", _IResolvable_9ceae33e]:
        """``AWS::CloudFront::StreamingDistribution.StreamingDistributionConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig
        """
        return jsii.get(self, "streamingDistributionConfig")

    @streaming_distribution_config.setter
    def streaming_distribution_config(
        self,
        value: typing.Union[
            "StreamingDistributionConfigProperty", _IResolvable_9ceae33e
        ],
    ) -> None:
        jsii.set(self, "streamingDistributionConfig", value)

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnStreamingDistribution.LoggingProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "enabled": "enabled", "prefix": "prefix"},
    )
    class LoggingProperty:
        def __init__(
            self,
            *,
            bucket: str,
            enabled: typing.Union[bool, _IResolvable_9ceae33e],
            prefix: str,
        ) -> None:
            """
            :param bucket: ``CfnStreamingDistribution.LoggingProperty.Bucket``.
            :param enabled: ``CfnStreamingDistribution.LoggingProperty.Enabled``.
            :param prefix: ``CfnStreamingDistribution.LoggingProperty.Prefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html
            """
            self._values = {
                "bucket": bucket,
                "enabled": enabled,
                "prefix": prefix,
            }

        @builtins.property
        def bucket(self) -> str:
            """``CfnStreamingDistribution.LoggingProperty.Bucket``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html#cfn-cloudfront-streamingdistribution-logging-bucket
            """
            return self._values.get("bucket")

        @builtins.property
        def enabled(self) -> typing.Union[bool, _IResolvable_9ceae33e]:
            """``CfnStreamingDistribution.LoggingProperty.Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html#cfn-cloudfront-streamingdistribution-logging-enabled
            """
            return self._values.get("enabled")

        @builtins.property
        def prefix(self) -> str:
            """``CfnStreamingDistribution.LoggingProperty.Prefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html#cfn-cloudfront-streamingdistribution-logging-prefix
            """
            return self._values.get("prefix")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnStreamingDistribution.S3OriginProperty",
        jsii_struct_bases=[],
        name_mapping={
            "domain_name": "domainName",
            "origin_access_identity": "originAccessIdentity",
        },
    )
    class S3OriginProperty:
        def __init__(self, *, domain_name: str, origin_access_identity: str) -> None:
            """
            :param domain_name: ``CfnStreamingDistribution.S3OriginProperty.DomainName``.
            :param origin_access_identity: ``CfnStreamingDistribution.S3OriginProperty.OriginAccessIdentity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html
            """
            self._values = {
                "domain_name": domain_name,
                "origin_access_identity": origin_access_identity,
            }

        @builtins.property
        def domain_name(self) -> str:
            """``CfnStreamingDistribution.S3OriginProperty.DomainName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html#cfn-cloudfront-streamingdistribution-s3origin-domainname
            """
            return self._values.get("domain_name")

        @builtins.property
        def origin_access_identity(self) -> str:
            """``CfnStreamingDistribution.S3OriginProperty.OriginAccessIdentity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html#cfn-cloudfront-streamingdistribution-s3origin-originaccessidentity
            """
            return self._values.get("origin_access_identity")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OriginProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnStreamingDistribution.StreamingDistributionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comment": "comment",
            "enabled": "enabled",
            "s3_origin": "s3Origin",
            "trusted_signers": "trustedSigners",
            "aliases": "aliases",
            "logging": "logging",
            "price_class": "priceClass",
        },
    )
    class StreamingDistributionConfigProperty:
        def __init__(
            self,
            *,
            comment: str,
            enabled: typing.Union[bool, _IResolvable_9ceae33e],
            s3_origin: typing.Union[
                "CfnStreamingDistribution.S3OriginProperty", _IResolvable_9ceae33e
            ],
            trusted_signers: typing.Union[
                "CfnStreamingDistribution.TrustedSignersProperty", _IResolvable_9ceae33e
            ],
            aliases: typing.Optional[typing.List[str]] = None,
            logging: typing.Optional[
                typing.Union[
                    "CfnStreamingDistribution.LoggingProperty", _IResolvable_9ceae33e
                ]
            ] = None,
            price_class: typing.Optional[str] = None,
        ) -> None:
            """
            :param comment: ``CfnStreamingDistribution.StreamingDistributionConfigProperty.Comment``.
            :param enabled: ``CfnStreamingDistribution.StreamingDistributionConfigProperty.Enabled``.
            :param s3_origin: ``CfnStreamingDistribution.StreamingDistributionConfigProperty.S3Origin``.
            :param trusted_signers: ``CfnStreamingDistribution.StreamingDistributionConfigProperty.TrustedSigners``.
            :param aliases: ``CfnStreamingDistribution.StreamingDistributionConfigProperty.Aliases``.
            :param logging: ``CfnStreamingDistribution.StreamingDistributionConfigProperty.Logging``.
            :param price_class: ``CfnStreamingDistribution.StreamingDistributionConfigProperty.PriceClass``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html
            """
            self._values = {
                "comment": comment,
                "enabled": enabled,
                "s3_origin": s3_origin,
                "trusted_signers": trusted_signers,
            }
            if aliases is not None:
                self._values["aliases"] = aliases
            if logging is not None:
                self._values["logging"] = logging
            if price_class is not None:
                self._values["price_class"] = price_class

        @builtins.property
        def comment(self) -> str:
            """``CfnStreamingDistribution.StreamingDistributionConfigProperty.Comment``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-comment
            """
            return self._values.get("comment")

        @builtins.property
        def enabled(self) -> typing.Union[bool, _IResolvable_9ceae33e]:
            """``CfnStreamingDistribution.StreamingDistributionConfigProperty.Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-enabled
            """
            return self._values.get("enabled")

        @builtins.property
        def s3_origin(
            self,
        ) -> typing.Union[
            "CfnStreamingDistribution.S3OriginProperty", _IResolvable_9ceae33e
        ]:
            """``CfnStreamingDistribution.StreamingDistributionConfigProperty.S3Origin``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-s3origin
            """
            return self._values.get("s3_origin")

        @builtins.property
        def trusted_signers(
            self,
        ) -> typing.Union[
            "CfnStreamingDistribution.TrustedSignersProperty", _IResolvable_9ceae33e
        ]:
            """``CfnStreamingDistribution.StreamingDistributionConfigProperty.TrustedSigners``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-trustedsigners
            """
            return self._values.get("trusted_signers")

        @builtins.property
        def aliases(self) -> typing.Optional[typing.List[str]]:
            """``CfnStreamingDistribution.StreamingDistributionConfigProperty.Aliases``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-aliases
            """
            return self._values.get("aliases")

        @builtins.property
        def logging(
            self,
        ) -> typing.Optional[
            typing.Union[
                "CfnStreamingDistribution.LoggingProperty", _IResolvable_9ceae33e
            ]
        ]:
            """``CfnStreamingDistribution.StreamingDistributionConfigProperty.Logging``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-logging
            """
            return self._values.get("logging")

        @builtins.property
        def price_class(self) -> typing.Optional[str]:
            """``CfnStreamingDistribution.StreamingDistributionConfigProperty.PriceClass``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-priceclass
            """
            return self._values.get("price_class")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamingDistributionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk-experiment.aws_cloudfront.CfnStreamingDistribution.TrustedSignersProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "aws_account_numbers": "awsAccountNumbers"},
    )
    class TrustedSignersProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[bool, _IResolvable_9ceae33e],
            aws_account_numbers: typing.Optional[typing.List[str]] = None,
        ) -> None:
            """
            :param enabled: ``CfnStreamingDistribution.TrustedSignersProperty.Enabled``.
            :param aws_account_numbers: ``CfnStreamingDistribution.TrustedSignersProperty.AwsAccountNumbers``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html
            """
            self._values = {
                "enabled": enabled,
            }
            if aws_account_numbers is not None:
                self._values["aws_account_numbers"] = aws_account_numbers

        @builtins.property
        def enabled(self) -> typing.Union[bool, _IResolvable_9ceae33e]:
            """``CfnStreamingDistribution.TrustedSignersProperty.Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html#cfn-cloudfront-streamingdistribution-trustedsigners-enabled
            """
            return self._values.get("enabled")

        @builtins.property
        def aws_account_numbers(self) -> typing.Optional[typing.List[str]]:
            """``CfnStreamingDistribution.TrustedSignersProperty.AwsAccountNumbers``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html#cfn-cloudfront-streamingdistribution-trustedsigners-awsaccountnumbers
            """
            return self._values.get("aws_account_numbers")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrustedSignersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.CfnStreamingDistributionProps",
    jsii_struct_bases=[],
    name_mapping={
        "streaming_distribution_config": "streamingDistributionConfig",
        "tags": "tags",
    },
)
class CfnStreamingDistributionProps:
    def __init__(
        self,
        *,
        streaming_distribution_config: typing.Union[
            "CfnStreamingDistribution.StreamingDistributionConfigProperty",
            _IResolvable_9ceae33e,
        ],
        tags: typing.List[_CfnTag_b4661f1a],
    ) -> None:
        """Properties for defining a ``AWS::CloudFront::StreamingDistribution``.

        :param streaming_distribution_config: ``AWS::CloudFront::StreamingDistribution.StreamingDistributionConfig``.
        :param tags: ``AWS::CloudFront::StreamingDistribution.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html
        """
        self._values = {
            "streaming_distribution_config": streaming_distribution_config,
            "tags": tags,
        }

    @builtins.property
    def streaming_distribution_config(
        self,
    ) -> typing.Union[
        "CfnStreamingDistribution.StreamingDistributionConfigProperty",
        _IResolvable_9ceae33e,
    ]:
        """``AWS::CloudFront::StreamingDistribution.StreamingDistributionConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig
        """
        return self._values.get("streaming_distribution_config")

    @builtins.property
    def tags(self) -> typing.List[_CfnTag_b4661f1a]:
        """``AWS::CloudFront::StreamingDistribution.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html#cfn-cloudfront-streamingdistribution-tags
        """
        return self._values.get("tags")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStreamingDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk-experiment.aws_cloudfront.CloudFrontAllowedCachedMethods")
class CloudFrontAllowedCachedMethods(enum.Enum):
    """Enums for the methods CloudFront can cache.

    stability
    :stability: experimental
    """

    GET_HEAD = "GET_HEAD"
    """
    stability
    :stability: experimental
    """
    GET_HEAD_OPTIONS = "GET_HEAD_OPTIONS"
    """
    stability
    :stability: experimental
    """


@jsii.enum(jsii_type="monocdk-experiment.aws_cloudfront.CloudFrontAllowedMethods")
class CloudFrontAllowedMethods(enum.Enum):
    """An enum for the supported methods to a CloudFront distribution.

    stability
    :stability: experimental
    """

    GET_HEAD = "GET_HEAD"
    """
    stability
    :stability: experimental
    """
    GET_HEAD_OPTIONS = "GET_HEAD_OPTIONS"
    """
    stability
    :stability: experimental
    """
    ALL = "ALL"
    """
    stability
    :stability: experimental
    """


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.CloudFrontWebDistributionProps",
    jsii_struct_bases=[],
    name_mapping={
        "origin_configs": "originConfigs",
        "alias_configuration": "aliasConfiguration",
        "comment": "comment",
        "default_root_object": "defaultRootObject",
        "enable_ip_v6": "enableIpV6",
        "error_configurations": "errorConfigurations",
        "geo_restriction": "geoRestriction",
        "http_version": "httpVersion",
        "logging_config": "loggingConfig",
        "price_class": "priceClass",
        "viewer_certificate": "viewerCertificate",
        "viewer_protocol_policy": "viewerProtocolPolicy",
        "web_acl_id": "webACLId",
    },
)
class CloudFrontWebDistributionProps:
    def __init__(
        self,
        *,
        origin_configs: typing.List["SourceConfiguration"],
        alias_configuration: typing.Optional["AliasConfiguration"] = None,
        comment: typing.Optional[str] = None,
        default_root_object: typing.Optional[str] = None,
        enable_ip_v6: typing.Optional[bool] = None,
        error_configurations: typing.Optional[
            typing.List["CfnDistribution.CustomErrorResponseProperty"]
        ] = None,
        geo_restriction: typing.Optional["GeoRestriction"] = None,
        http_version: typing.Optional["HttpVersion"] = None,
        logging_config: typing.Optional["LoggingConfiguration"] = None,
        price_class: typing.Optional["PriceClass"] = None,
        viewer_certificate: typing.Optional["ViewerCertificate"] = None,
        viewer_protocol_policy: typing.Optional["ViewerProtocolPolicy"] = None,
        web_acl_id: typing.Optional[str] = None,
    ) -> None:
        """
        :param origin_configs: The origin configurations for this distribution. Behaviors are a part of the origin.
        :param alias_configuration: AliasConfiguration is used to configured CloudFront to respond to requests on custom domain names. Default: - None.
        :param comment: A comment for this distribution in the CloudFront console. Default: - No comment is added to distribution.
        :param default_root_object: The default object to serve. Default: - "index.html" is served.
        :param enable_ip_v6: If your distribution should have IPv6 enabled. Default: true
        :param error_configurations: How CloudFront should handle requests that are not successful (eg PageNotFound). By default, CloudFront does not replace HTTP status codes in the 4xx and 5xx range with custom error messages. CloudFront does not cache HTTP status codes. Default: - No custom error configuration.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: No geo restriction
        :param http_version: The max supported HTTP Versions. Default: HttpVersion.HTTP2
        :param logging_config: Optional - if we should enable logging. You can pass an empty object ({}) to have us auto create a bucket for logging. Omission of this property indicates no logging is to be enabled. Default: - no logging is enabled by default.
        :param price_class: The price class for the distribution (this impacts how many locations CloudFront uses for your distribution, and billing). Default: PriceClass.PRICE_CLASS_100 the cheapest option for CloudFront is picked by default.
        :param viewer_certificate: Specifies whether you want viewers to use HTTP or HTTPS to request your objects, whether you're using an alternate domain name with HTTPS, and if so, if you're using AWS Certificate Manager (ACM) or a third-party certificate authority. Default: ViewerCertificate.fromCloudFrontDefaultCertificate()
        :param viewer_protocol_policy: The default viewer policy for incoming clients. Default: RedirectToHTTPs
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. Default: - No AWS Web Application Firewall web access control list (web ACL).

        stability
        :stability: experimental
        """
        if isinstance(alias_configuration, dict):
            alias_configuration = AliasConfiguration(**alias_configuration)
        if isinstance(logging_config, dict):
            logging_config = LoggingConfiguration(**logging_config)
        self._values = {
            "origin_configs": origin_configs,
        }
        if alias_configuration is not None:
            self._values["alias_configuration"] = alias_configuration
        if comment is not None:
            self._values["comment"] = comment
        if default_root_object is not None:
            self._values["default_root_object"] = default_root_object
        if enable_ip_v6 is not None:
            self._values["enable_ip_v6"] = enable_ip_v6
        if error_configurations is not None:
            self._values["error_configurations"] = error_configurations
        if geo_restriction is not None:
            self._values["geo_restriction"] = geo_restriction
        if http_version is not None:
            self._values["http_version"] = http_version
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if price_class is not None:
            self._values["price_class"] = price_class
        if viewer_certificate is not None:
            self._values["viewer_certificate"] = viewer_certificate
        if viewer_protocol_policy is not None:
            self._values["viewer_protocol_policy"] = viewer_protocol_policy
        if web_acl_id is not None:
            self._values["web_acl_id"] = web_acl_id

    @builtins.property
    def origin_configs(self) -> typing.List["SourceConfiguration"]:
        """The origin configurations for this distribution.

        Behaviors are a part of the origin.

        stability
        :stability: experimental
        """
        return self._values.get("origin_configs")

    @builtins.property
    def alias_configuration(self) -> typing.Optional["AliasConfiguration"]:
        """AliasConfiguration is used to configured CloudFront to respond to requests on custom domain names.

        default
        :default: - None.

        deprecated
        :deprecated: see {@link CloudFrontWebDistributionProps#viewerCertificate} with {@link ViewerCertificate#acmCertificate}

        stability
        :stability: deprecated
        """
        return self._values.get("alias_configuration")

    @builtins.property
    def comment(self) -> typing.Optional[str]:
        """A comment for this distribution in the CloudFront console.

        default
        :default: - No comment is added to distribution.

        stability
        :stability: experimental
        """
        return self._values.get("comment")

    @builtins.property
    def default_root_object(self) -> typing.Optional[str]:
        """The default object to serve.

        default
        :default: - "index.html" is served.

        stability
        :stability: experimental
        """
        return self._values.get("default_root_object")

    @builtins.property
    def enable_ip_v6(self) -> typing.Optional[bool]:
        """If your distribution should have IPv6 enabled.

        default
        :default: true

        stability
        :stability: experimental
        """
        return self._values.get("enable_ip_v6")

    @builtins.property
    def error_configurations(
        self,
    ) -> typing.Optional[typing.List["CfnDistribution.CustomErrorResponseProperty"]]:
        """How CloudFront should handle requests that are not successful (eg PageNotFound).

        By default, CloudFront does not replace HTTP status codes in the 4xx and 5xx range
        with custom error messages. CloudFront does not cache HTTP status codes.

        default
        :default: - No custom error configuration.

        stability
        :stability: experimental
        """
        return self._values.get("error_configurations")

    @builtins.property
    def geo_restriction(self) -> typing.Optional["GeoRestriction"]:
        """Controls the countries in which your content is distributed.

        default
        :default: No geo restriction

        stability
        :stability: experimental
        """
        return self._values.get("geo_restriction")

    @builtins.property
    def http_version(self) -> typing.Optional["HttpVersion"]:
        """The max supported HTTP Versions.

        default
        :default: HttpVersion.HTTP2

        stability
        :stability: experimental
        """
        return self._values.get("http_version")

    @builtins.property
    def logging_config(self) -> typing.Optional["LoggingConfiguration"]:
        """Optional - if we should enable logging.

        You can pass an empty object ({}) to have us auto create a bucket for logging.
        Omission of this property indicates no logging is to be enabled.

        default
        :default: - no logging is enabled by default.

        stability
        :stability: experimental
        """
        return self._values.get("logging_config")

    @builtins.property
    def price_class(self) -> typing.Optional["PriceClass"]:
        """The price class for the distribution (this impacts how many locations CloudFront uses for your distribution, and billing).

        default
        :default: PriceClass.PRICE_CLASS_100 the cheapest option for CloudFront is picked by default.

        stability
        :stability: experimental
        """
        return self._values.get("price_class")

    @builtins.property
    def viewer_certificate(self) -> typing.Optional["ViewerCertificate"]:
        """Specifies whether you want viewers to use HTTP or HTTPS to request your objects, whether you're using an alternate domain name with HTTPS, and if so, if you're using AWS Certificate Manager (ACM) or a third-party certificate authority.

        default
        :default: ViewerCertificate.fromCloudFrontDefaultCertificate()

        see
        :see: https://aws.amazon.com/premiumsupport/knowledge-center/custom-ssl-certificate-cloudfront/
        stability
        :stability: experimental
        """
        return self._values.get("viewer_certificate")

    @builtins.property
    def viewer_protocol_policy(self) -> typing.Optional["ViewerProtocolPolicy"]:
        """The default viewer policy for incoming clients.

        default
        :default: RedirectToHTTPs

        stability
        :stability: experimental
        """
        return self._values.get("viewer_protocol_policy")

    @builtins.property
    def web_acl_id(self) -> typing.Optional[str]:
        """Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution.

        default
        :default: - No AWS Web Application Firewall web access control list (web ACL).

        see
        :see: https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html
        stability
        :stability: experimental
        """
        return self._values.get("web_acl_id")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFrontWebDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.CustomOriginConfig",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "allowed_origin_ssl_versions": "allowedOriginSSLVersions",
        "http_port": "httpPort",
        "https_port": "httpsPort",
        "origin_headers": "originHeaders",
        "origin_keepalive_timeout": "originKeepaliveTimeout",
        "origin_path": "originPath",
        "origin_protocol_policy": "originProtocolPolicy",
        "origin_read_timeout": "originReadTimeout",
    },
)
class CustomOriginConfig:
    def __init__(
        self,
        *,
        domain_name: str,
        allowed_origin_ssl_versions: typing.Optional[
            typing.List["OriginSslPolicy"]
        ] = None,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        origin_headers: typing.Optional[typing.Mapping[str, str]] = None,
        origin_keepalive_timeout: typing.Optional[_Duration_5170c158] = None,
        origin_path: typing.Optional[str] = None,
        origin_protocol_policy: typing.Optional["OriginProtocolPolicy"] = None,
        origin_read_timeout: typing.Optional[_Duration_5170c158] = None,
    ) -> None:
        """A custom origin configuration.

        :param domain_name: The domain name of the custom origin. Should not include the path - that should be in the parent SourceConfiguration
        :param allowed_origin_ssl_versions: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLSv1_2
        :param http_port: The origin HTTP port. Default: 80
        :param https_port: The origin HTTPS port. Default: 443
        :param origin_headers: Any additional headers to pass to the origin. Default: - No additional headers are passed.
        :param origin_keepalive_timeout: The keep alive timeout when making calls in seconds. Default: Duration.seconds(5)
        :param origin_path: The relative path to the origin root to use for sources. Default: /
        :param origin_protocol_policy: The protocol (http or https) policy to use when interacting with the origin. Default: OriginProtocolPolicy.HttpsOnly
        :param origin_read_timeout: The read timeout when calling the origin in seconds. Default: Duration.seconds(30)

        stability
        :stability: experimental
        """
        self._values = {
            "domain_name": domain_name,
        }
        if allowed_origin_ssl_versions is not None:
            self._values["allowed_origin_ssl_versions"] = allowed_origin_ssl_versions
        if http_port is not None:
            self._values["http_port"] = http_port
        if https_port is not None:
            self._values["https_port"] = https_port
        if origin_headers is not None:
            self._values["origin_headers"] = origin_headers
        if origin_keepalive_timeout is not None:
            self._values["origin_keepalive_timeout"] = origin_keepalive_timeout
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if origin_protocol_policy is not None:
            self._values["origin_protocol_policy"] = origin_protocol_policy
        if origin_read_timeout is not None:
            self._values["origin_read_timeout"] = origin_read_timeout

    @builtins.property
    def domain_name(self) -> str:
        """The domain name of the custom origin.

        Should not include the path - that should be in the parent SourceConfiguration

        stability
        :stability: experimental
        """
        return self._values.get("domain_name")

    @builtins.property
    def allowed_origin_ssl_versions(
        self,
    ) -> typing.Optional[typing.List["OriginSslPolicy"]]:
        """The SSL versions to use when interacting with the origin.

        default
        :default: OriginSslPolicy.TLSv1_2

        stability
        :stability: experimental
        """
        return self._values.get("allowed_origin_ssl_versions")

    @builtins.property
    def http_port(self) -> typing.Optional[jsii.Number]:
        """The origin HTTP port.

        default
        :default: 80

        stability
        :stability: experimental
        """
        return self._values.get("http_port")

    @builtins.property
    def https_port(self) -> typing.Optional[jsii.Number]:
        """The origin HTTPS port.

        default
        :default: 443

        stability
        :stability: experimental
        """
        return self._values.get("https_port")

    @builtins.property
    def origin_headers(self) -> typing.Optional[typing.Mapping[str, str]]:
        """Any additional headers to pass to the origin.

        default
        :default: - No additional headers are passed.

        stability
        :stability: experimental
        """
        return self._values.get("origin_headers")

    @builtins.property
    def origin_keepalive_timeout(self) -> typing.Optional[_Duration_5170c158]:
        """The keep alive timeout when making calls in seconds.

        default
        :default: Duration.seconds(5)

        stability
        :stability: experimental
        """
        return self._values.get("origin_keepalive_timeout")

    @builtins.property
    def origin_path(self) -> typing.Optional[str]:
        """The relative path to the origin root to use for sources.

        default
        :default: /

        stability
        :stability: experimental
        """
        return self._values.get("origin_path")

    @builtins.property
    def origin_protocol_policy(self) -> typing.Optional["OriginProtocolPolicy"]:
        """The protocol (http or https) policy to use when interacting with the origin.

        default
        :default: OriginProtocolPolicy.HttpsOnly

        stability
        :stability: experimental
        """
        return self._values.get("origin_protocol_policy")

    @builtins.property
    def origin_read_timeout(self) -> typing.Optional[_Duration_5170c158]:
        """The read timeout when calling the origin in seconds.

        default
        :default: Duration.seconds(30)

        stability
        :stability: experimental
        """
        return self._values.get("origin_read_timeout")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomOriginConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.DistributionAttributes",
    jsii_struct_bases=[],
    name_mapping={"distribution_id": "distributionId", "domain_name": "domainName"},
)
class DistributionAttributes:
    def __init__(self, *, distribution_id: str, domain_name: str) -> None:
        """Attributes used to import a Distribution.

        :param distribution_id: The distribution ID for this distribution.
        :param domain_name: The generated domain name of the Distribution, such as d111111abcdef8.cloudfront.net.

        stability
        :stability: experimental
        """
        self._values = {
            "distribution_id": distribution_id,
            "domain_name": domain_name,
        }

    @builtins.property
    def distribution_id(self) -> str:
        """The distribution ID for this distribution.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get("distribution_id")

    @builtins.property
    def domain_name(self) -> str:
        """The generated domain name of the Distribution, such as d111111abcdef8.cloudfront.net.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get("domain_name")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributionAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.DistributionProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_behavior": "defaultBehavior",
        "additional_behaviors": "additionalBehaviors",
        "certificate": "certificate",
        "error_responses": "errorResponses",
        "price_class": "priceClass",
    },
)
class DistributionProps:
    def __init__(
        self,
        *,
        default_behavior: "BehaviorOptions",
        additional_behaviors: typing.Optional[
            typing.Mapping[str, "BehaviorOptions"]
        ] = None,
        certificate: typing.Optional[_ICertificate_8f3d4c96] = None,
        error_responses: typing.Optional[typing.List["ErrorResponse"]] = None,
        price_class: typing.Optional["PriceClass"] = None,
    ) -> None:
        """Properties for a Distribution.

        :param default_behavior: The default behavior for the distribution.
        :param additional_behaviors: Additional behaviors for the distribution, mapped by the pathPattern that specifies which requests to apply the behavior to. Default: - no additional behaviors are added.
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param error_responses: How CloudFront should handle requests that are not successful (e.g., PageNotFound). Default: - No custom error responses.
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_ALL

        stability
        :stability: experimental
        """
        if isinstance(default_behavior, dict):
            default_behavior = BehaviorOptions(**default_behavior)
        self._values = {
            "default_behavior": default_behavior,
        }
        if additional_behaviors is not None:
            self._values["additional_behaviors"] = additional_behaviors
        if certificate is not None:
            self._values["certificate"] = certificate
        if error_responses is not None:
            self._values["error_responses"] = error_responses
        if price_class is not None:
            self._values["price_class"] = price_class

    @builtins.property
    def default_behavior(self) -> "BehaviorOptions":
        """The default behavior for the distribution.

        stability
        :stability: experimental
        """
        return self._values.get("default_behavior")

    @builtins.property
    def additional_behaviors(
        self,
    ) -> typing.Optional[typing.Mapping[str, "BehaviorOptions"]]:
        """Additional behaviors for the distribution, mapped by the pathPattern that specifies which requests to apply the behavior to.

        default
        :default: - no additional behaviors are added.

        stability
        :stability: experimental
        """
        return self._values.get("additional_behaviors")

    @builtins.property
    def certificate(self) -> typing.Optional[_ICertificate_8f3d4c96]:
        """A certificate to associate with the distribution.

        The certificate must be located in N. Virginia (us-east-1).

        default
        :default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.

        stability
        :stability: experimental
        """
        return self._values.get("certificate")

    @builtins.property
    def error_responses(self) -> typing.Optional[typing.List["ErrorResponse"]]:
        """How CloudFront should handle requests that are not successful (e.g., PageNotFound).

        default
        :default: - No custom error responses.

        stability
        :stability: experimental
        """
        return self._values.get("error_responses")

    @builtins.property
    def price_class(self) -> typing.Optional["PriceClass"]:
        """The price class that corresponds with the maximum price that you want to pay for CloudFront service.

        If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations.
        If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location
        that has the lowest latency among the edge locations in your price class.

        default
        :default: PriceClass.PRICE_CLASS_ALL

        stability
        :stability: experimental
        """
        return self._values.get("price_class")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.EdgeLambda",
    jsii_struct_bases=[],
    name_mapping={"event_type": "eventType", "function_version": "functionVersion"},
)
class EdgeLambda:
    def __init__(
        self, *, event_type: "LambdaEdgeEventType", function_version: _IVersion_1dc10564
    ) -> None:
        """Represents a Lambda function version and event type when using Lambda@Edge.

        The type of the {@link AddBehaviorOptions.edgeLambdas} property.

        :param event_type: The type of event in response to which should the function be invoked.
        :param function_version: The version of the Lambda function that will be invoked. **Note**: it's not possible to use the '$LATEST' function version for Lambda@Edge!

        stability
        :stability: experimental
        """
        self._values = {
            "event_type": event_type,
            "function_version": function_version,
        }

    @builtins.property
    def event_type(self) -> "LambdaEdgeEventType":
        """The type of event in response to which should the function be invoked.

        stability
        :stability: experimental
        """
        return self._values.get("event_type")

    @builtins.property
    def function_version(self) -> _IVersion_1dc10564:
        """The version of the Lambda function that will be invoked.

        **Note**: it's not possible to use the '$LATEST' function version for Lambda@Edge!

        stability
        :stability: experimental
        """
        return self._values.get("function_version")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EdgeLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.ErrorResponse",
    jsii_struct_bases=[],
    name_mapping={
        "http_status": "httpStatus",
        "response_http_status": "responseHttpStatus",
        "response_page_path": "responsePagePath",
        "ttl": "ttl",
    },
)
class ErrorResponse:
    def __init__(
        self,
        *,
        http_status: jsii.Number,
        response_http_status: typing.Optional[jsii.Number] = None,
        response_page_path: typing.Optional[str] = None,
        ttl: typing.Optional[_Duration_5170c158] = None,
    ) -> None:
        """Options for configuring custom error responses.

        :param http_status: The HTTP status code for which you want to specify a custom error page and/or a caching duration.
        :param response_http_status: The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. If you specify a value for ``responseHttpStatus``, you must also specify a value for ``responsePagePath``. Default: - not set, the error code will be returned as the response code.
        :param response_page_path: The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the ``httpStatus``, for example, /4xx-errors/403-forbidden.html. Default: - the default CloudFront response is shown.
        :param ttl: The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode. Default: - the default caching TTL behavior applies

        stability
        :stability: experimental
        """
        self._values = {
            "http_status": http_status,
        }
        if response_http_status is not None:
            self._values["response_http_status"] = response_http_status
        if response_page_path is not None:
            self._values["response_page_path"] = response_page_path
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def http_status(self) -> jsii.Number:
        """The HTTP status code for which you want to specify a custom error page and/or a caching duration.

        stability
        :stability: experimental
        """
        return self._values.get("http_status")

    @builtins.property
    def response_http_status(self) -> typing.Optional[jsii.Number]:
        """The HTTP status code that you want CloudFront to return to the viewer along with the custom error page.

        If you specify a value for ``responseHttpStatus``, you must also specify a value for ``responsePagePath``.

        default
        :default: - not set, the error code will be returned as the response code.

        stability
        :stability: experimental
        """
        return self._values.get("response_http_status")

    @builtins.property
    def response_page_path(self) -> typing.Optional[str]:
        """The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the ``httpStatus``, for example, /4xx-errors/403-forbidden.html.

        default
        :default: - the default CloudFront response is shown.

        stability
        :stability: experimental
        """
        return self._values.get("response_page_path")

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_5170c158]:
        """The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode.

        default
        :default: - the default caching TTL behavior applies

        stability
        :stability: experimental
        """
        return self._values.get("ttl")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ErrorResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk-experiment.aws_cloudfront.FailoverStatusCode")
class FailoverStatusCode(enum.Enum):
    """HTTP status code to failover to second origin.

    stability
    :stability: experimental
    """

    FORBIDDEN = "FORBIDDEN"
    """Forbidden (403).

    stability
    :stability: experimental
    """
    NOT_FOUND = "NOT_FOUND"
    """Not found (404).

    stability
    :stability: experimental
    """
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    """Internal Server Error (500).

    stability
    :stability: experimental
    """
    BAD_GATEWAY = "BAD_GATEWAY"
    """Bad Gateway (502).

    stability
    :stability: experimental
    """
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    """Service Unavailable (503).

    stability
    :stability: experimental
    """
    GATEWAY_TIMEOUT = "GATEWAY_TIMEOUT"
    """Gateway Timeout (504).

    stability
    :stability: experimental
    """


class GeoRestriction(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_cloudfront.GeoRestriction",
):
    """Controls the countries in which your content is distributed.

    stability
    :stability: experimental
    """

    @jsii.member(jsii_name="blacklist")
    @builtins.classmethod
    def blacklist(cls, *locations: str) -> "GeoRestriction":
        """Blacklist specific countries which you don't want CloudFront to distribute your content.

        :param locations: Two-letter, uppercase country code for a country that you want to blacklist. Include one element for each country. See ISO 3166-1-alpha-2 code on the *International Organization for Standardization* website

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "blacklist", [*locations])

    @jsii.member(jsii_name="whitelist")
    @builtins.classmethod
    def whitelist(cls, *locations: str) -> "GeoRestriction":
        """Whitelist specific countries which you want CloudFront to distribute your content.

        :param locations: Two-letter, uppercase country code for a country that you want to whitelist. Include one element for each country. See ISO 3166-1-alpha-2 code on the *International Organization for Standardization* website

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "whitelist", [*locations])

    @builtins.property
    @jsii.member(jsii_name="locations")
    def locations(self) -> typing.List[str]:
        """Two-letter, uppercase country code for a country that you want to whitelist/blacklist.

        Include one element for each country.
        See ISO 3166-1-alpha-2 code on the *International Organization for Standardization* website

        stability
        :stability: experimental
        """
        return jsii.get(self, "locations")

    @builtins.property
    @jsii.member(jsii_name="restrictionType")
    def restriction_type(self) -> str:
        """Specifies the restriction type to impose (whitelist or blacklist).

        stability
        :stability: experimental
        """
        return jsii.get(self, "restrictionType")


@jsii.enum(jsii_type="monocdk-experiment.aws_cloudfront.HttpVersion")
class HttpVersion(enum.Enum):
    """
    stability
    :stability: experimental
    """

    HTTP1_1 = "HTTP1_1"
    """
    stability
    :stability: experimental
    """
    HTTP2 = "HTTP2"
    """
    stability
    :stability: experimental
    """


@jsii.interface(jsii_type="monocdk-experiment.aws_cloudfront.IDistribution")
class IDistribution(_IResource_72f7ee7e, jsii.compat.Protocol):
    """Interface for CloudFront distributions.

    stability
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IDistributionProxy

    @builtins.property
    @jsii.member(jsii_name="distributionDomainName")
    def distribution_domain_name(self) -> str:
        """The domain name of the Distribution, such as d111111abcdef8.cloudfront.net.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        ...

    @builtins.property
    @jsii.member(jsii_name="distributionId")
    def distribution_id(self) -> str:
        """The distribution ID for this distribution.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        ...

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> str:
        """The domain name of the Distribution, such as d111111abcdef8.cloudfront.net.

        deprecated
        :deprecated: - Use ``distributionDomainName`` instead.

        stability
        :stability: deprecated
        attribute:
        :attribute:: true
        """
        ...


class _IDistributionProxy(jsii.proxy_for(_IResource_72f7ee7e)):
    """Interface for CloudFront distributions.

    stability
    :stability: experimental
    """

    __jsii_type__ = "monocdk-experiment.aws_cloudfront.IDistribution"

    @builtins.property
    @jsii.member(jsii_name="distributionDomainName")
    def distribution_domain_name(self) -> str:
        """The domain name of the Distribution, such as d111111abcdef8.cloudfront.net.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "distributionDomainName")

    @builtins.property
    @jsii.member(jsii_name="distributionId")
    def distribution_id(self) -> str:
        """The distribution ID for this distribution.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "distributionId")

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> str:
        """The domain name of the Distribution, such as d111111abcdef8.cloudfront.net.

        deprecated
        :deprecated: - Use ``distributionDomainName`` instead.

        stability
        :stability: deprecated
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "domainName")


@jsii.interface(jsii_type="monocdk-experiment.aws_cloudfront.IOrigin")
class IOrigin(jsii.compat.Protocol):
    """Represents the concept of a CloudFront Origin.

    You provide one or more origins when creating a Distribution.

    stability
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IOriginProxy

    @jsii.member(jsii_name="bind")
    def bind(self, scope: _Construct_f50a3f53, *, origin_id: str) -> "OriginBindConfig":
        """The method called when a given Origin is added (for the first time) to a Distribution.

        :param scope: -
        :param origin_id: The identifier of this Origin, as assigned by the Distribution this Origin has been used added to.

        stability
        :stability: experimental
        """
        ...


class _IOriginProxy:
    """Represents the concept of a CloudFront Origin.

    You provide one or more origins when creating a Distribution.

    stability
    :stability: experimental
    """

    __jsii_type__ = "monocdk-experiment.aws_cloudfront.IOrigin"

    @jsii.member(jsii_name="bind")
    def bind(self, scope: _Construct_f50a3f53, *, origin_id: str) -> "OriginBindConfig":
        """The method called when a given Origin is added (for the first time) to a Distribution.

        :param scope: -
        :param origin_id: The identifier of this Origin, as assigned by the Distribution this Origin has been used added to.

        stability
        :stability: experimental
        """
        options = OriginBindOptions(origin_id=origin_id)

        return jsii.invoke(self, "bind", [scope, options])


@jsii.interface(jsii_type="monocdk-experiment.aws_cloudfront.IOriginAccessIdentity")
class IOriginAccessIdentity(
    _IResource_72f7ee7e, _IGrantable_0fcfc53a, jsii.compat.Protocol
):
    """Interface for CloudFront OriginAccessIdentity.

    stability
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IOriginAccessIdentityProxy

    @builtins.property
    @jsii.member(jsii_name="originAccessIdentityName")
    def origin_access_identity_name(self) -> str:
        """The Origin Access Identity Name.

        stability
        :stability: experimental
        """
        ...


class _IOriginAccessIdentityProxy(
    jsii.proxy_for(_IResource_72f7ee7e), jsii.proxy_for(_IGrantable_0fcfc53a)
):
    """Interface for CloudFront OriginAccessIdentity.

    stability
    :stability: experimental
    """

    __jsii_type__ = "monocdk-experiment.aws_cloudfront.IOriginAccessIdentity"

    @builtins.property
    @jsii.member(jsii_name="originAccessIdentityName")
    def origin_access_identity_name(self) -> str:
        """The Origin Access Identity Name.

        stability
        :stability: experimental
        """
        return jsii.get(self, "originAccessIdentityName")


@jsii.enum(jsii_type="monocdk-experiment.aws_cloudfront.LambdaEdgeEventType")
class LambdaEdgeEventType(enum.Enum):
    """The type of events that a Lambda@Edge function can be invoked in response to.

    stability
    :stability: experimental
    """

    ORIGIN_REQUEST = "ORIGIN_REQUEST"
    """The origin-request specifies the request to the origin location (e.g. S3).

    stability
    :stability: experimental
    """
    ORIGIN_RESPONSE = "ORIGIN_RESPONSE"
    """The origin-response specifies the response from the origin location (e.g. S3).

    stability
    :stability: experimental
    """
    VIEWER_REQUEST = "VIEWER_REQUEST"
    """The viewer-request specifies the incoming request.

    stability
    :stability: experimental
    """
    VIEWER_RESPONSE = "VIEWER_RESPONSE"
    """The viewer-response specifies the outgoing reponse.

    stability
    :stability: experimental
    """


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.LambdaFunctionAssociation",
    jsii_struct_bases=[],
    name_mapping={"event_type": "eventType", "lambda_function": "lambdaFunction"},
)
class LambdaFunctionAssociation:
    def __init__(
        self, *, event_type: "LambdaEdgeEventType", lambda_function: _IVersion_1dc10564
    ) -> None:
        """
        :param event_type: The lambda event type defines at which event the lambda is called during the request lifecycle.
        :param lambda_function: A version of the lambda to associate.

        stability
        :stability: experimental
        """
        self._values = {
            "event_type": event_type,
            "lambda_function": lambda_function,
        }

    @builtins.property
    def event_type(self) -> "LambdaEdgeEventType":
        """The lambda event type defines at which event the lambda is called during the request lifecycle.

        stability
        :stability: experimental
        """
        return self._values.get("event_type")

    @builtins.property
    def lambda_function(self) -> _IVersion_1dc10564:
        """A version of the lambda to associate.

        stability
        :stability: experimental
        """
        return self._values.get("lambda_function")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.LoggingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "include_cookies": "includeCookies",
        "prefix": "prefix",
    },
)
class LoggingConfiguration:
    def __init__(
        self,
        *,
        bucket: typing.Optional[_IBucket_25bad983] = None,
        include_cookies: typing.Optional[bool] = None,
        prefix: typing.Optional[str] = None,
    ) -> None:
        """Logging configuration for incoming requests.

        :param bucket: Bucket to log requests to. Default: - A logging bucket is automatically created.
        :param include_cookies: Whether to include the cookies in the logs. Default: false
        :param prefix: Where in the bucket to store logs. Default: - No prefix.

        stability
        :stability: experimental
        """
        self._values = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if include_cookies is not None:
            self._values["include_cookies"] = include_cookies
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket(self) -> typing.Optional[_IBucket_25bad983]:
        """Bucket to log requests to.

        default
        :default: - A logging bucket is automatically created.

        stability
        :stability: experimental
        """
        return self._values.get("bucket")

    @builtins.property
    def include_cookies(self) -> typing.Optional[bool]:
        """Whether to include the cookies in the logs.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get("include_cookies")

    @builtins.property
    def prefix(self) -> typing.Optional[str]:
        """Where in the bucket to store logs.

        default
        :default: - No prefix.

        stability
        :stability: experimental
        """
        return self._values.get("prefix")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IOriginAccessIdentity)
class OriginAccessIdentity(
    _Resource_884d0774,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_cloudfront.OriginAccessIdentity",
):
    """An origin access identity is a special CloudFront user that you can associate with Amazon S3 origins, so that you can secure all or just some of your Amazon S3 content.

    stability
    :stability: experimental
    resource:
    :resource:: AWS::CloudFront::CloudFrontOriginAccessIdentity
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        comment: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param comment: Any comments you want to include about the origin access identity. Default: "Allows CloudFront to reach the bucket"

        stability
        :stability: experimental
        """
        props = OriginAccessIdentityProps(comment=comment)

        jsii.create(OriginAccessIdentity, self, [scope, id, props])

    @jsii.member(jsii_name="fromOriginAccessIdentityName")
    @builtins.classmethod
    def from_origin_access_identity_name(
        cls, scope: _Construct_f50a3f53, id: str, origin_access_identity_name: str
    ) -> "IOriginAccessIdentity":
        """Creates a OriginAccessIdentity by providing the OriginAccessIdentityName.

        :param scope: -
        :param id: -
        :param origin_access_identity_name: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(
            cls,
            "fromOriginAccessIdentityName",
            [scope, id, origin_access_identity_name],
        )

    @jsii.member(jsii_name="arn")
    def _arn(self) -> str:
        """The ARN to include in S3 bucket policy to allow CloudFront access.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "arn", [])

    @builtins.property
    @jsii.member(jsii_name="cloudFrontOriginAccessIdentityS3CanonicalUserId")
    def cloud_front_origin_access_identity_s3_canonical_user_id(self) -> str:
        """The Amazon S3 canonical user ID for the origin access identity, used when giving the origin access identity read permission to an object in Amazon S3.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "cloudFrontOriginAccessIdentityS3CanonicalUserId")

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_97126874:
        """Derived principal value for bucket access.

        stability
        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @builtins.property
    @jsii.member(jsii_name="originAccessIdentityName")
    def origin_access_identity_name(self) -> str:
        """The Origin Access Identity Name (physical id).

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "originAccessIdentityName")


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.OriginAccessIdentityProps",
    jsii_struct_bases=[],
    name_mapping={"comment": "comment"},
)
class OriginAccessIdentityProps:
    def __init__(self, *, comment: typing.Optional[str] = None) -> None:
        """Properties of CloudFront OriginAccessIdentity.

        :param comment: Any comments you want to include about the origin access identity. Default: "Allows CloudFront to reach the bucket"

        stability
        :stability: experimental
        """
        self._values = {}
        if comment is not None:
            self._values["comment"] = comment

    @builtins.property
    def comment(self) -> typing.Optional[str]:
        """Any comments you want to include about the origin access identity.

        default
        :default: "Allows CloudFront to reach the bucket"

        stability
        :stability: experimental
        """
        return self._values.get("comment")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginAccessIdentityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IOrigin)
class OriginBase(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk-experiment.aws_cloudfront.OriginBase",
):
    """Represents a distribution origin, that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files.

    stability
    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _OriginBaseProxy

    def __init__(
        self,
        domain_name: str,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_5170c158] = None,
        custom_headers: typing.Optional[typing.Mapping[str, str]] = None,
        origin_path: typing.Optional[str] = None,
    ) -> None:
        """
        :param domain_name: -
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'

        stability
        :stability: experimental
        """
        props = OriginProps(
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_path=origin_path,
        )

        jsii.create(OriginBase, self, [domain_name, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self, _scope: _Construct_f50a3f53, *, origin_id: str
    ) -> "OriginBindConfig":
        """Binds the origin to the associated Distribution.

        Can be used to grant permissions, create dependent resources, etc.

        :param _scope: -
        :param origin_id: The identifier of this Origin, as assigned by the Distribution this Origin has been used added to.

        stability
        :stability: experimental
        """
        options = OriginBindOptions(origin_id=origin_id)

        return jsii.invoke(self, "bind", [_scope, options])

    @jsii.member(jsii_name="renderCustomOriginConfig")
    def _render_custom_origin_config(
        self,
    ) -> typing.Optional["CfnDistribution.CustomOriginConfigProperty"]:
        """
        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderCustomOriginConfig", [])

    @jsii.member(jsii_name="renderS3OriginConfig")
    def _render_s3_origin_config(
        self,
    ) -> typing.Optional["CfnDistribution.S3OriginConfigProperty"]:
        """
        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderS3OriginConfig", [])


class _OriginBaseProxy(OriginBase):
    pass


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.OriginBindConfig",
    jsii_struct_bases=[],
    name_mapping={
        "failover_config": "failoverConfig",
        "origin_property": "originProperty",
    },
)
class OriginBindConfig:
    def __init__(
        self,
        *,
        failover_config: typing.Optional["OriginFailoverConfig"] = None,
        origin_property: typing.Optional["CfnDistribution.OriginProperty"] = None,
    ) -> None:
        """The struct returned from {@link IOrigin.bind}.

        :param failover_config: The failover configuration for this Origin. Default: - nothing is returned
        :param origin_property: The CloudFormation OriginProperty configuration for this Origin. Default: - nothing is returned

        stability
        :stability: experimental
        """
        if isinstance(failover_config, dict):
            failover_config = OriginFailoverConfig(**failover_config)
        if isinstance(origin_property, dict):
            origin_property = CfnDistribution.OriginProperty(**origin_property)
        self._values = {}
        if failover_config is not None:
            self._values["failover_config"] = failover_config
        if origin_property is not None:
            self._values["origin_property"] = origin_property

    @builtins.property
    def failover_config(self) -> typing.Optional["OriginFailoverConfig"]:
        """The failover configuration for this Origin.

        default
        :default: - nothing is returned

        stability
        :stability: experimental
        """
        return self._values.get("failover_config")

    @builtins.property
    def origin_property(self) -> typing.Optional["CfnDistribution.OriginProperty"]:
        """The CloudFormation OriginProperty configuration for this Origin.

        default
        :default: - nothing is returned

        stability
        :stability: experimental
        """
        return self._values.get("origin_property")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginBindConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.OriginBindOptions",
    jsii_struct_bases=[],
    name_mapping={"origin_id": "originId"},
)
class OriginBindOptions:
    def __init__(self, *, origin_id: str) -> None:
        """Options passed to Origin.bind().

        :param origin_id: The identifier of this Origin, as assigned by the Distribution this Origin has been used added to.

        stability
        :stability: experimental
        """
        self._values = {
            "origin_id": origin_id,
        }

    @builtins.property
    def origin_id(self) -> str:
        """The identifier of this Origin, as assigned by the Distribution this Origin has been used added to.

        stability
        :stability: experimental
        """
        return self._values.get("origin_id")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.OriginFailoverConfig",
    jsii_struct_bases=[],
    name_mapping={"failover_origin": "failoverOrigin", "status_codes": "statusCodes"},
)
class OriginFailoverConfig:
    def __init__(
        self,
        *,
        failover_origin: "IOrigin",
        status_codes: typing.Optional[typing.List[jsii.Number]] = None,
    ) -> None:
        """The failover configuration used for Origin Groups, returned in {@link OriginBindConfig.failoverConfig}.

        :param failover_origin: The origin to use as the fallback origin.
        :param status_codes: The HTTP status codes of the response that trigger querying the failover Origin. Default: - 500, 502, 503 and 504

        stability
        :stability: experimental
        """
        self._values = {
            "failover_origin": failover_origin,
        }
        if status_codes is not None:
            self._values["status_codes"] = status_codes

    @builtins.property
    def failover_origin(self) -> "IOrigin":
        """The origin to use as the fallback origin.

        stability
        :stability: experimental
        """
        return self._values.get("failover_origin")

    @builtins.property
    def status_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        """The HTTP status codes of the response that trigger querying the failover Origin.

        default
        :default: - 500, 502, 503 and 504

        stability
        :stability: experimental
        """
        return self._values.get("status_codes")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginFailoverConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.OriginProps",
    jsii_struct_bases=[],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_path": "originPath",
    },
)
class OriginProps:
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_5170c158] = None,
        custom_headers: typing.Optional[typing.Mapping[str, str]] = None,
        origin_path: typing.Optional[str] = None,
    ) -> None:
        """Properties to define an Origin.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'

        stability
        :stability: experimental
        """
        self._values = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_path is not None:
            self._values["origin_path"] = origin_path

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        """The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        default
        :default: 3

        stability
        :stability: experimental
        """
        return self._values.get("connection_attempts")

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_5170c158]:
        """The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        default
        :default: Duration.seconds(10)

        stability
        :stability: experimental
        """
        return self._values.get("connection_timeout")

    @builtins.property
    def custom_headers(self) -> typing.Optional[typing.Mapping[str, str]]:
        """A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        default
        :default: {}

        stability
        :stability: experimental
        """
        return self._values.get("custom_headers")

    @builtins.property
    def origin_path(self) -> typing.Optional[str]:
        """An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        default
        :default: '/'

        stability
        :stability: experimental
        """
        return self._values.get("origin_path")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk-experiment.aws_cloudfront.OriginProtocolPolicy")
class OriginProtocolPolicy(enum.Enum):
    """Defines what protocols CloudFront will use to connect to an origin.

    stability
    :stability: experimental
    """

    HTTP_ONLY = "HTTP_ONLY"
    """Connect on HTTP only.

    stability
    :stability: experimental
    """
    MATCH_VIEWER = "MATCH_VIEWER"
    """Connect with the same protocol as the viewer.

    stability
    :stability: experimental
    """
    HTTPS_ONLY = "HTTPS_ONLY"
    """Connect on HTTPS only.

    stability
    :stability: experimental
    """


@jsii.enum(jsii_type="monocdk-experiment.aws_cloudfront.OriginSslPolicy")
class OriginSslPolicy(enum.Enum):
    """
    stability
    :stability: experimental
    """

    SSL_V3 = "SSL_V3"
    """
    stability
    :stability: experimental
    """
    TLS_V1 = "TLS_V1"
    """
    stability
    :stability: experimental
    """
    TLS_V1_1 = "TLS_V1_1"
    """
    stability
    :stability: experimental
    """
    TLS_V1_2 = "TLS_V1_2"
    """
    stability
    :stability: experimental
    """


@jsii.enum(jsii_type="monocdk-experiment.aws_cloudfront.PriceClass")
class PriceClass(enum.Enum):
    """The price class determines how many edge locations CloudFront will use for your distribution.

    See https://aws.amazon.com/cloudfront/pricing/ for full list of supported regions.

    stability
    :stability: experimental
    """

    PRICE_CLASS_100 = "PRICE_CLASS_100"
    """USA, Canada, Europe, & Israel.

    stability
    :stability: experimental
    """
    PRICE_CLASS_200 = "PRICE_CLASS_200"
    """PRICE_CLASS_100 + South Africa, Kenya, Middle East, Japan, Singapore, South Korea, Taiwan, Hong Kong, & Philippines.

    stability
    :stability: experimental
    """
    PRICE_CLASS_ALL = "PRICE_CLASS_ALL"
    """All locations.

    stability
    :stability: experimental
    """


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.S3OriginConfig",
    jsii_struct_bases=[],
    name_mapping={
        "s3_bucket_source": "s3BucketSource",
        "origin_access_identity": "originAccessIdentity",
        "origin_headers": "originHeaders",
        "origin_path": "originPath",
    },
)
class S3OriginConfig:
    def __init__(
        self,
        *,
        s3_bucket_source: _IBucket_25bad983,
        origin_access_identity: typing.Optional["IOriginAccessIdentity"] = None,
        origin_headers: typing.Optional[typing.Mapping[str, str]] = None,
        origin_path: typing.Optional[str] = None,
    ) -> None:
        """S3 origin configuration for CloudFront.

        :param s3_bucket_source: The source bucket to serve content from.
        :param origin_access_identity: The optional Origin Access Identity of the origin identity cloudfront will use when calling your s3 bucket. Default: No Origin Access Identity which requires the S3 bucket to be public accessible
        :param origin_headers: Any additional headers to pass to the origin. Default: - No additional headers are passed.
        :param origin_path: The relative path to the origin root to use for sources. Default: /

        stability
        :stability: experimental
        """
        self._values = {
            "s3_bucket_source": s3_bucket_source,
        }
        if origin_access_identity is not None:
            self._values["origin_access_identity"] = origin_access_identity
        if origin_headers is not None:
            self._values["origin_headers"] = origin_headers
        if origin_path is not None:
            self._values["origin_path"] = origin_path

    @builtins.property
    def s3_bucket_source(self) -> _IBucket_25bad983:
        """The source bucket to serve content from.

        stability
        :stability: experimental
        """
        return self._values.get("s3_bucket_source")

    @builtins.property
    def origin_access_identity(self) -> typing.Optional["IOriginAccessIdentity"]:
        """The optional Origin Access Identity of the origin identity cloudfront will use when calling your s3 bucket.

        default
        :default: No Origin Access Identity which requires the S3 bucket to be public accessible

        stability
        :stability: experimental
        """
        return self._values.get("origin_access_identity")

    @builtins.property
    def origin_headers(self) -> typing.Optional[typing.Mapping[str, str]]:
        """Any additional headers to pass to the origin.

        default
        :default: - No additional headers are passed.

        stability
        :stability: experimental
        """
        return self._values.get("origin_headers")

    @builtins.property
    def origin_path(self) -> typing.Optional[str]:
        """The relative path to the origin root to use for sources.

        default
        :default: /

        stability
        :stability: experimental
        """
        return self._values.get("origin_path")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3OriginConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk-experiment.aws_cloudfront.SSLMethod")
class SSLMethod(enum.Enum):
    """The SSL method CloudFront will use for your distribution.

    Server Name Indication (SNI) - is an extension to the TLS computer networking protocol by which a client indicates
    which hostname it is attempting to connect to at the start of the handshaking process. This allows a server to present
    multiple certificates on the same IP address and TCP port number and hence allows multiple secure (HTTPS) websites
    (or any other service over TLS) to be served by the same IP address without requiring all those sites to use the same certificate.

    CloudFront can use SNI to host multiple distributions on the same IP - which a large majority of clients will support.

    If your clients cannot support SNI however - CloudFront can use dedicated IPs for your distribution - but there is a prorated monthly charge for
    using this feature. By default, we use SNI - but you can optionally enable dedicated IPs (VIP).

    See the CloudFront SSL for more details about pricing : https://aws.amazon.com/cloudfront/custom-ssl-domains/

    stability
    :stability: experimental
    """

    SNI = "SNI"
    """
    stability
    :stability: experimental
    """
    VIP = "VIP"
    """
    stability
    :stability: experimental
    """


@jsii.enum(jsii_type="monocdk-experiment.aws_cloudfront.SecurityPolicyProtocol")
class SecurityPolicyProtocol(enum.Enum):
    """The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections.

    CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify.

    stability
    :stability: experimental
    """

    SSL_V3 = "SSL_V3"
    """
    stability
    :stability: experimental
    """
    TLS_V1 = "TLS_V1"
    """
    stability
    :stability: experimental
    """
    TLS_V1_2016 = "TLS_V1_2016"
    """
    stability
    :stability: experimental
    """
    TLS_V1_1_2016 = "TLS_V1_1_2016"
    """
    stability
    :stability: experimental
    """
    TLS_V1_2_2018 = "TLS_V1_2_2018"
    """
    stability
    :stability: experimental
    """


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.SourceConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "behaviors": "behaviors",
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_origin_source": "customOriginSource",
        "failover_criteria_status_codes": "failoverCriteriaStatusCodes",
        "failover_custom_origin_source": "failoverCustomOriginSource",
        "failover_s3_origin_source": "failoverS3OriginSource",
        "origin_headers": "originHeaders",
        "origin_path": "originPath",
        "s3_origin_source": "s3OriginSource",
    },
)
class SourceConfiguration:
    def __init__(
        self,
        *,
        behaviors: typing.List["Behavior"],
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_5170c158] = None,
        custom_origin_source: typing.Optional["CustomOriginConfig"] = None,
        failover_criteria_status_codes: typing.Optional[
            typing.List["FailoverStatusCode"]
        ] = None,
        failover_custom_origin_source: typing.Optional["CustomOriginConfig"] = None,
        failover_s3_origin_source: typing.Optional["S3OriginConfig"] = None,
        origin_headers: typing.Optional[typing.Mapping[str, str]] = None,
        origin_path: typing.Optional[str] = None,
        s3_origin_source: typing.Optional["S3OriginConfig"] = None,
    ) -> None:
        """A source configuration is a wrapper for CloudFront origins and behaviors.

        An origin is what CloudFront will "be in front of" - that is, CloudFront will pull it's assets from an origin.

        If you're using s3 as a source - pass the ``s3Origin`` property, otherwise, pass the ``customOriginSource`` property.

        One or the other must be passed, and it is invalid to pass both in the same SourceConfiguration.

        :param behaviors: The behaviors associated with this source. At least one (default) behavior must be included.
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin. You can specify 1, 2, or 3 as the number of attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. You can specify a number of seconds between 1 and 10 (inclusive). Default: cdk.Duration.seconds(10)
        :param custom_origin_source: A custom origin source - for all non-s3 sources.
        :param failover_criteria_status_codes: HTTP status code to failover to second origin. Default: [500, 502, 503, 504]
        :param failover_custom_origin_source: A custom origin source for failover in case the s3OriginSource returns invalid status code. Default: - no failover configuration
        :param failover_s3_origin_source: An s3 origin source for failover in case the s3OriginSource returns invalid status code. Default: - no failover configuration
        :param origin_headers: Any additional headers to pass to the origin. Default: - No additional headers are passed.
        :param origin_path: The relative path to the origin root to use for sources. Default: /
        :param s3_origin_source: An s3 origin source - if you're using s3 for your assets.

        stability
        :stability: experimental
        """
        if isinstance(custom_origin_source, dict):
            custom_origin_source = CustomOriginConfig(**custom_origin_source)
        if isinstance(failover_custom_origin_source, dict):
            failover_custom_origin_source = CustomOriginConfig(
                **failover_custom_origin_source
            )
        if isinstance(failover_s3_origin_source, dict):
            failover_s3_origin_source = S3OriginConfig(**failover_s3_origin_source)
        if isinstance(s3_origin_source, dict):
            s3_origin_source = S3OriginConfig(**s3_origin_source)
        self._values = {
            "behaviors": behaviors,
        }
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_origin_source is not None:
            self._values["custom_origin_source"] = custom_origin_source
        if failover_criteria_status_codes is not None:
            self._values[
                "failover_criteria_status_codes"
            ] = failover_criteria_status_codes
        if failover_custom_origin_source is not None:
            self._values[
                "failover_custom_origin_source"
            ] = failover_custom_origin_source
        if failover_s3_origin_source is not None:
            self._values["failover_s3_origin_source"] = failover_s3_origin_source
        if origin_headers is not None:
            self._values["origin_headers"] = origin_headers
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if s3_origin_source is not None:
            self._values["s3_origin_source"] = s3_origin_source

    @builtins.property
    def behaviors(self) -> typing.List["Behavior"]:
        """The behaviors associated with this source.

        At least one (default) behavior must be included.

        stability
        :stability: experimental
        """
        return self._values.get("behaviors")

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        """The number of times that CloudFront attempts to connect to the origin.

        You can specify 1, 2, or 3 as the number of attempts.

        default
        :default: 3

        stability
        :stability: experimental
        """
        return self._values.get("connection_attempts")

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_5170c158]:
        """The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        You can specify a number of seconds between 1 and 10 (inclusive).

        default
        :default: cdk.Duration.seconds(10)

        stability
        :stability: experimental
        """
        return self._values.get("connection_timeout")

    @builtins.property
    def custom_origin_source(self) -> typing.Optional["CustomOriginConfig"]:
        """A custom origin source - for all non-s3 sources.

        stability
        :stability: experimental
        """
        return self._values.get("custom_origin_source")

    @builtins.property
    def failover_criteria_status_codes(
        self,
    ) -> typing.Optional[typing.List["FailoverStatusCode"]]:
        """HTTP status code to failover to second origin.

        default
        :default: [500, 502, 503, 504]

        stability
        :stability: experimental
        """
        return self._values.get("failover_criteria_status_codes")

    @builtins.property
    def failover_custom_origin_source(self) -> typing.Optional["CustomOriginConfig"]:
        """A custom origin source for failover in case the s3OriginSource returns invalid status code.

        default
        :default: - no failover configuration

        stability
        :stability: experimental
        """
        return self._values.get("failover_custom_origin_source")

    @builtins.property
    def failover_s3_origin_source(self) -> typing.Optional["S3OriginConfig"]:
        """An s3 origin source for failover in case the s3OriginSource returns invalid status code.

        default
        :default: - no failover configuration

        stability
        :stability: experimental
        """
        return self._values.get("failover_s3_origin_source")

    @builtins.property
    def origin_headers(self) -> typing.Optional[typing.Mapping[str, str]]:
        """Any additional headers to pass to the origin.

        default
        :default: - No additional headers are passed.

        deprecated
        :deprecated: Use originHeaders on s3OriginSource or customOriginSource

        stability
        :stability: deprecated
        """
        return self._values.get("origin_headers")

    @builtins.property
    def origin_path(self) -> typing.Optional[str]:
        """The relative path to the origin root to use for sources.

        default
        :default: /

        deprecated
        :deprecated: Use originPath on s3OriginSource or customOriginSource

        stability
        :stability: deprecated
        """
        return self._values.get("origin_path")

    @builtins.property
    def s3_origin_source(self) -> typing.Optional["S3OriginConfig"]:
        """An s3 origin source - if you're using s3 for your assets.

        stability
        :stability: experimental
        """
        return self._values.get("s3_origin_source")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourceConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ViewerCertificate(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_cloudfront.ViewerCertificate",
):
    """Viewer certificate configuration class.

    stability
    :stability: experimental
    """

    @jsii.member(jsii_name="fromAcmCertificate")
    @builtins.classmethod
    def from_acm_certificate(
        cls,
        certificate: _ICertificate_8f3d4c96,
        *,
        aliases: typing.Optional[typing.List[str]] = None,
        security_policy: typing.Optional["SecurityPolicyProtocol"] = None,
        ssl_method: typing.Optional["SSLMethod"] = None,
    ) -> "ViewerCertificate":
        """Generate an AWS Certificate Manager (ACM) viewer certificate configuration.

        :param certificate: AWS Certificate Manager (ACM) certificate. Your certificate must be located in the us-east-1 (US East (N. Virginia)) region to be accessed by CloudFront
        :param aliases: Domain names on the certificate (both main domain name and Subject Alternative names).
        :param security_policy: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: - SSLv3 if sslMethod VIP, TLSv1 if sslMethod SNI
        :param ssl_method: How CloudFront should serve HTTPS requests. See the notes on SSLMethod if you wish to use other SSL termination types. Default: SSLMethod.SNI

        stability
        :stability: experimental
        """
        options = ViewerCertificateOptions(
            aliases=aliases, security_policy=security_policy, ssl_method=ssl_method
        )

        return jsii.sinvoke(cls, "fromAcmCertificate", [certificate, options])

    @jsii.member(jsii_name="fromCloudFrontDefaultCertificate")
    @builtins.classmethod
    def from_cloud_front_default_certificate(cls, *aliases: str) -> "ViewerCertificate":
        """Generate a viewer certifcate configuration using the CloudFront default certificate (e.g. d111111abcdef8.cloudfront.net) and a {@link SecurityPolicyProtocol.TLS_V1} security policy.

        :param aliases: Alternative CNAME aliases You also must create a CNAME record with your DNS service to route queries.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromCloudFrontDefaultCertificate", [*aliases])

    @jsii.member(jsii_name="fromIamCertificate")
    @builtins.classmethod
    def from_iam_certificate(
        cls,
        iam_certificate_id: str,
        *,
        aliases: typing.Optional[typing.List[str]] = None,
        security_policy: typing.Optional["SecurityPolicyProtocol"] = None,
        ssl_method: typing.Optional["SSLMethod"] = None,
    ) -> "ViewerCertificate":
        """Generate an IAM viewer certificate configuration.

        :param iam_certificate_id: Identifier of the IAM certificate.
        :param aliases: Domain names on the certificate (both main domain name and Subject Alternative names).
        :param security_policy: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: - SSLv3 if sslMethod VIP, TLSv1 if sslMethod SNI
        :param ssl_method: How CloudFront should serve HTTPS requests. See the notes on SSLMethod if you wish to use other SSL termination types. Default: SSLMethod.SNI

        stability
        :stability: experimental
        """
        options = ViewerCertificateOptions(
            aliases=aliases, security_policy=security_policy, ssl_method=ssl_method
        )

        return jsii.sinvoke(cls, "fromIamCertificate", [iam_certificate_id, options])

    @builtins.property
    @jsii.member(jsii_name="aliases")
    def aliases(self) -> typing.List[str]:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "aliases")

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDistribution.ViewerCertificateProperty":
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "props")


@jsii.data_type(
    jsii_type="monocdk-experiment.aws_cloudfront.ViewerCertificateOptions",
    jsii_struct_bases=[],
    name_mapping={
        "aliases": "aliases",
        "security_policy": "securityPolicy",
        "ssl_method": "sslMethod",
    },
)
class ViewerCertificateOptions:
    def __init__(
        self,
        *,
        aliases: typing.Optional[typing.List[str]] = None,
        security_policy: typing.Optional["SecurityPolicyProtocol"] = None,
        ssl_method: typing.Optional["SSLMethod"] = None,
    ) -> None:
        """
        :param aliases: Domain names on the certificate (both main domain name and Subject Alternative names).
        :param security_policy: The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. CloudFront serves your objects only to browsers or devices that support at least the SSL version that you specify. Default: - SSLv3 if sslMethod VIP, TLSv1 if sslMethod SNI
        :param ssl_method: How CloudFront should serve HTTPS requests. See the notes on SSLMethod if you wish to use other SSL termination types. Default: SSLMethod.SNI

        stability
        :stability: experimental
        """
        self._values = {}
        if aliases is not None:
            self._values["aliases"] = aliases
        if security_policy is not None:
            self._values["security_policy"] = security_policy
        if ssl_method is not None:
            self._values["ssl_method"] = ssl_method

    @builtins.property
    def aliases(self) -> typing.Optional[typing.List[str]]:
        """Domain names on the certificate (both main domain name and Subject Alternative names).

        stability
        :stability: experimental
        """
        return self._values.get("aliases")

    @builtins.property
    def security_policy(self) -> typing.Optional["SecurityPolicyProtocol"]:
        """The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections.

        CloudFront serves your objects only to browsers or devices that support at
        least the SSL version that you specify.

        default
        :default: - SSLv3 if sslMethod VIP, TLSv1 if sslMethod SNI

        stability
        :stability: experimental
        """
        return self._values.get("security_policy")

    @builtins.property
    def ssl_method(self) -> typing.Optional["SSLMethod"]:
        """How CloudFront should serve HTTPS requests.

        See the notes on SSLMethod if you wish to use other SSL termination types.

        default
        :default: SSLMethod.SNI

        see
        :see: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ViewerCertificate.html
        stability
        :stability: experimental
        """
        return self._values.get("ssl_method")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ViewerCertificateOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk-experiment.aws_cloudfront.ViewerProtocolPolicy")
class ViewerProtocolPolicy(enum.Enum):
    """How HTTPs should be handled with your distribution.

    stability
    :stability: experimental
    """

    HTTPS_ONLY = "HTTPS_ONLY"
    """HTTPS only.

    stability
    :stability: experimental
    """
    REDIRECT_TO_HTTPS = "REDIRECT_TO_HTTPS"
    """Will redirect HTTP requests to HTTPS.

    stability
    :stability: experimental
    """
    ALLOW_ALL = "ALLOW_ALL"
    """Both HTTP and HTTPS supported.

    stability
    :stability: experimental
    """


@jsii.implements(IDistribution)
class CloudFrontWebDistribution(
    _Resource_884d0774,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_cloudfront.CloudFrontWebDistribution",
):
    """Amazon CloudFront is a global content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to your viewers with low latency and high transfer speeds.

    CloudFront fronts user provided content and caches it at edge locations across the world.

    Here's how you can use this construct::

       # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
       from aws_cdk.aws_cloudfront import CloudFrontWebDistribution

       source_bucket = Bucket(self, "Bucket")

       distribution = CloudFrontWebDistribution(self, "MyDistribution",
           origin_configs=[SourceConfiguration(
               s3_origin_source=S3OriginConfig(
                   s3_bucket_source=source_bucket
               ),
               behaviors=[Behavior(is_default_behavior=True)]
           )
           ]
       )

    This will create a CloudFront distribution that uses your S3Bucket as it's origin.

    You can customize the distribution using additional properties from the CloudFrontWebDistributionProps interface.

    stability
    :stability: experimental
    resource:
    :resource:: AWS::CloudFront::Distribution
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        origin_configs: typing.List["SourceConfiguration"],
        alias_configuration: typing.Optional["AliasConfiguration"] = None,
        comment: typing.Optional[str] = None,
        default_root_object: typing.Optional[str] = None,
        enable_ip_v6: typing.Optional[bool] = None,
        error_configurations: typing.Optional[
            typing.List["CfnDistribution.CustomErrorResponseProperty"]
        ] = None,
        geo_restriction: typing.Optional["GeoRestriction"] = None,
        http_version: typing.Optional["HttpVersion"] = None,
        logging_config: typing.Optional["LoggingConfiguration"] = None,
        price_class: typing.Optional["PriceClass"] = None,
        viewer_certificate: typing.Optional["ViewerCertificate"] = None,
        viewer_protocol_policy: typing.Optional["ViewerProtocolPolicy"] = None,
        web_acl_id: typing.Optional[str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param origin_configs: The origin configurations for this distribution. Behaviors are a part of the origin.
        :param alias_configuration: AliasConfiguration is used to configured CloudFront to respond to requests on custom domain names. Default: - None.
        :param comment: A comment for this distribution in the CloudFront console. Default: - No comment is added to distribution.
        :param default_root_object: The default object to serve. Default: - "index.html" is served.
        :param enable_ip_v6: If your distribution should have IPv6 enabled. Default: true
        :param error_configurations: How CloudFront should handle requests that are not successful (eg PageNotFound). By default, CloudFront does not replace HTTP status codes in the 4xx and 5xx range with custom error messages. CloudFront does not cache HTTP status codes. Default: - No custom error configuration.
        :param geo_restriction: Controls the countries in which your content is distributed. Default: No geo restriction
        :param http_version: The max supported HTTP Versions. Default: HttpVersion.HTTP2
        :param logging_config: Optional - if we should enable logging. You can pass an empty object ({}) to have us auto create a bucket for logging. Omission of this property indicates no logging is to be enabled. Default: - no logging is enabled by default.
        :param price_class: The price class for the distribution (this impacts how many locations CloudFront uses for your distribution, and billing). Default: PriceClass.PRICE_CLASS_100 the cheapest option for CloudFront is picked by default.
        :param viewer_certificate: Specifies whether you want viewers to use HTTP or HTTPS to request your objects, whether you're using an alternate domain name with HTTPS, and if so, if you're using AWS Certificate Manager (ACM) or a third-party certificate authority. Default: ViewerCertificate.fromCloudFrontDefaultCertificate()
        :param viewer_protocol_policy: The default viewer policy for incoming clients. Default: RedirectToHTTPs
        :param web_acl_id: Unique identifier that specifies the AWS WAF web ACL to associate with this CloudFront distribution. Default: - No AWS Web Application Firewall web access control list (web ACL).

        stability
        :stability: experimental
        """
        props = CloudFrontWebDistributionProps(
            origin_configs=origin_configs,
            alias_configuration=alias_configuration,
            comment=comment,
            default_root_object=default_root_object,
            enable_ip_v6=enable_ip_v6,
            error_configurations=error_configurations,
            geo_restriction=geo_restriction,
            http_version=http_version,
            logging_config=logging_config,
            price_class=price_class,
            viewer_certificate=viewer_certificate,
            viewer_protocol_policy=viewer_protocol_policy,
            web_acl_id=web_acl_id,
        )

        jsii.create(CloudFrontWebDistribution, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="distributionDomainName")
    def distribution_domain_name(self) -> str:
        """The domain name created by CloudFront for this distribution.

        If you are using aliases for your distribution, this is the domainName your DNS records should point to.
        (In Route53, you could create an ALIAS record to this value, for example.)

        stability
        :stability: experimental
        """
        return jsii.get(self, "distributionDomainName")

    @builtins.property
    @jsii.member(jsii_name="distributionId")
    def distribution_id(self) -> str:
        """The distribution ID for this distribution.

        stability
        :stability: experimental
        """
        return jsii.get(self, "distributionId")

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> str:
        """The domain name created by CloudFront for this distribution.

        If you are using aliases for your distribution, this is the domainName your DNS records should point to.
        (In Route53, you could create an ALIAS record to this value, for example.)

        deprecated
        :deprecated: - Use ``distributionDomainName`` instead.

        stability
        :stability: deprecated
        """
        return jsii.get(self, "domainName")

    @builtins.property
    @jsii.member(jsii_name="loggingBucket")
    def logging_bucket(self) -> typing.Optional[_IBucket_25bad983]:
        """The logging bucket for this CloudFront distribution.

        If logging is not enabled for this distribution - this property will be undefined.

        stability
        :stability: experimental
        """
        return jsii.get(self, "loggingBucket")


@jsii.implements(IDistribution)
class Distribution(
    _Resource_884d0774,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk-experiment.aws_cloudfront.Distribution",
):
    """A CloudFront distribution with associated origin(s) and caching behavior(s).

    stability
    :stability: experimental
    """

    def __init__(
        self,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        default_behavior: "BehaviorOptions",
        additional_behaviors: typing.Optional[
            typing.Mapping[str, "BehaviorOptions"]
        ] = None,
        certificate: typing.Optional[_ICertificate_8f3d4c96] = None,
        error_responses: typing.Optional[typing.List["ErrorResponse"]] = None,
        price_class: typing.Optional["PriceClass"] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param default_behavior: The default behavior for the distribution.
        :param additional_behaviors: Additional behaviors for the distribution, mapped by the pathPattern that specifies which requests to apply the behavior to. Default: - no additional behaviors are added.
        :param certificate: A certificate to associate with the distribution. The certificate must be located in N. Virginia (us-east-1). Default: - the CloudFront wildcard certificate (*.cloudfront.net) will be used.
        :param error_responses: How CloudFront should handle requests that are not successful (e.g., PageNotFound). Default: - No custom error responses.
        :param price_class: The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations. If you specify a price class other than PriceClass_All, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Default: PriceClass.PRICE_CLASS_ALL

        stability
        :stability: experimental
        """
        props = DistributionProps(
            default_behavior=default_behavior,
            additional_behaviors=additional_behaviors,
            certificate=certificate,
            error_responses=error_responses,
            price_class=price_class,
        )

        jsii.create(Distribution, self, [scope, id, props])

    @jsii.member(jsii_name="fromDistributionAttributes")
    @builtins.classmethod
    def from_distribution_attributes(
        cls,
        scope: _Construct_f50a3f53,
        id: str,
        *,
        distribution_id: str,
        domain_name: str,
    ) -> "IDistribution":
        """Creates a Distribution construct that represents an external (imported) distribution.

        :param scope: -
        :param id: -
        :param distribution_id: The distribution ID for this distribution.
        :param domain_name: The generated domain name of the Distribution, such as d111111abcdef8.cloudfront.net.

        stability
        :stability: experimental
        """
        attrs = DistributionAttributes(
            distribution_id=distribution_id, domain_name=domain_name
        )

        return jsii.sinvoke(cls, "fromDistributionAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="addBehavior")
    def add_behavior(
        self,
        path_pattern: str,
        origin: "IOrigin",
        *,
        allowed_methods: typing.Optional["AllowedMethods"] = None,
        cached_methods: typing.Optional["CachedMethods"] = None,
        compress: typing.Optional[bool] = None,
        edge_lambdas: typing.Optional[typing.List["EdgeLambda"]] = None,
        forward_query_string: typing.Optional[bool] = None,
        forward_query_string_cache_keys: typing.Optional[typing.List[str]] = None,
        smooth_streaming: typing.Optional[bool] = None,
        viewer_protocol_policy: typing.Optional["ViewerProtocolPolicy"] = None,
    ) -> None:
        """Adds a new behavior to this distribution for the given pathPattern.

        :param path_pattern: the path pattern (e.g., 'images/*') that specifies which requests to apply the behavior to.
        :param origin: the origin to use for this behavior.
        :param allowed_methods: HTTP methods to allow for this behavior. Default: AllowedMethods.ALLOW_GET_HEAD
        :param cached_methods: HTTP methods to cache for this behavior. Default: CachedMethods.CACHE_GET_HEAD
        :param compress: Whether you want CloudFront to automatically compress certain files for this cache behavior. See https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-cloudfront-file-types for file types CloudFront will compress. Default: false
        :param edge_lambdas: The Lambda@Edge functions to invoke before serving the contents. Default: - no Lambda functions will be invoked
        :param forward_query_string: Whether CloudFront will forward query strings to the origin. If this is set to true, CloudFront will forward all query parameters to the origin, and cache based on all parameters. See ``forwardQueryStringCacheKeys`` for a way to limit the query parameters CloudFront caches on. Default: false
        :param forward_query_string_cache_keys: A set of query string parameter names to use for caching if ``forwardQueryString`` is set to true. Default: []
        :param smooth_streaming: Set this to true to indicate you want to distribute media files in the Microsoft Smooth Streaming format using this behavior. Default: false
        :param viewer_protocol_policy: The protocol that viewers can use to access the files controlled by this behavior. Default: ViewerProtocolPolicy.ALLOW_ALL

        stability
        :stability: experimental
        """
        behavior_options = AddBehaviorOptions(
            allowed_methods=allowed_methods,
            cached_methods=cached_methods,
            compress=compress,
            edge_lambdas=edge_lambdas,
            forward_query_string=forward_query_string,
            forward_query_string_cache_keys=forward_query_string_cache_keys,
            smooth_streaming=smooth_streaming,
            viewer_protocol_policy=viewer_protocol_policy,
        )

        return jsii.invoke(
            self, "addBehavior", [path_pattern, origin, behavior_options]
        )

    @builtins.property
    @jsii.member(jsii_name="distributionDomainName")
    def distribution_domain_name(self) -> str:
        """The domain name of the Distribution, such as d111111abcdef8.cloudfront.net.

        stability
        :stability: experimental
        """
        return jsii.get(self, "distributionDomainName")

    @builtins.property
    @jsii.member(jsii_name="distributionId")
    def distribution_id(self) -> str:
        """The distribution ID for this distribution.

        stability
        :stability: experimental
        """
        return jsii.get(self, "distributionId")

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> str:
        """The domain name of the Distribution, such as d111111abcdef8.cloudfront.net.

        stability
        :stability: experimental
        """
        return jsii.get(self, "domainName")


__all__ = [
    "AddBehaviorOptions",
    "AliasConfiguration",
    "AllowedMethods",
    "Behavior",
    "BehaviorOptions",
    "CachedMethods",
    "CfnCloudFrontOriginAccessIdentity",
    "CfnCloudFrontOriginAccessIdentityProps",
    "CfnDistribution",
    "CfnDistributionProps",
    "CfnStreamingDistribution",
    "CfnStreamingDistributionProps",
    "CloudFrontAllowedCachedMethods",
    "CloudFrontAllowedMethods",
    "CloudFrontWebDistribution",
    "CloudFrontWebDistributionProps",
    "CustomOriginConfig",
    "Distribution",
    "DistributionAttributes",
    "DistributionProps",
    "EdgeLambda",
    "ErrorResponse",
    "FailoverStatusCode",
    "GeoRestriction",
    "HttpVersion",
    "IDistribution",
    "IOrigin",
    "IOriginAccessIdentity",
    "LambdaEdgeEventType",
    "LambdaFunctionAssociation",
    "LoggingConfiguration",
    "OriginAccessIdentity",
    "OriginAccessIdentityProps",
    "OriginBase",
    "OriginBindConfig",
    "OriginBindOptions",
    "OriginFailoverConfig",
    "OriginProps",
    "OriginProtocolPolicy",
    "OriginSslPolicy",
    "PriceClass",
    "S3OriginConfig",
    "SSLMethod",
    "SecurityPolicyProtocol",
    "SourceConfiguration",
    "ViewerCertificate",
    "ViewerCertificateOptions",
    "ViewerProtocolPolicy",
]

publication.publish()
