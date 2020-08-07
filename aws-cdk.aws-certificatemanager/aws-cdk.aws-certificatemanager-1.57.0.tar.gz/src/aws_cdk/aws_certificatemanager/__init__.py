"""
## AWS Certificate Manager Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This package provides Constructs for provisioning and referencing
certificates which can be used in CloudFront and ELB.

The following requests a certificate for a given domain:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
cert = certmgr.Certificate(self, "Certificate",
    domain_name="example.com"
)
```

After requesting a certificate, you will need to prove that you own the
domain in question before the certificate will be granted. The CloudFormation
deployment will wait until this verification process has been completed.

Because of this wait time, when using manual validation methods, it's better
to provision your certificates either in a separate stack from your main
service, or provision them manually and import them into your CDK application.

### Email validation

Email-validated certificates (the default) are validated by receiving an
email on one of a number of predefined domains and following the instructions
in the email.

See [Validate with Email](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html)
in the AWS Certificate Manager User Guide.

### DNS validation

If Amazon Route 53 is your DNS provider for the requested domain, the DNS record can be
created automatically:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
Certificate(self, "Certificate",
    domain_name="hello.example.com",
    validation=CertificateValidation.from_dns(my_hosted_zone)
)
```

Otherwise DNS records must be added manually and the stack will not complete
creating until the records are added.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
Certificate(self, "Certificate",
    domain_name="hello.example.com",
    validation=CertificateValidation.from_dns()
)
```

See also [Validate with DNS](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html)
in the AWS Certificate Manager User Guide.

When working with multiple domains, use the `CertificateValidation.fromDnsMultiZone()`:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
example_com = route53.HostedZone(self, "ExampleCom",
    zone_name="example.com"
)

example_net = route53.HostedZone(self, "ExampelNet",
    zone_name="example.net"
)

cert = acm.Certificate(self, "Certificate",
    domain_name="test.example.com",
    subject_alternative_names=["cool.example.com", "test.example.net"],
    validation=acm.CertificateValidation.from_dns_multi_zone({
        "text.example.com": example_com,
        "cool.example.com": example_com,
        "test.example.net": example_net
    })
)
```

Use the `DnsValidatedCertificate` construct for cross-region certificate creation:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
DnsValidatedCertificate(self, "CrossRegionCertificate",
    domain_name="hello.example.com",
    hosted_zone=my_hosted_zone,
    region="us-east-1"
)
```

This is useful when deploying a stack in a region other than `us-east-1` with a
certificate for a CloudFront distribution.

If cross-region is not needed, the recommended solution is to use the
`Certificate` construct which uses a native CloudFormation implementation.

### Importing

If you want to import an existing certificate, you can do so from its ARN:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
arn = "arn:aws:..."
certificate = Certificate.from_certificate_arn(self, "Certificate", arn)
```

### Sharing between Stacks

To share the certificate between stacks in the same CDK application, simply
pass the `Certificate` object between the stacks.
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from ._jsii import *

import aws_cdk.aws_iam
import aws_cdk.aws_route53
import aws_cdk.core


@jsii.data_type(
    jsii_type="@aws-cdk/aws-certificatemanager.CertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "subject_alternative_names": "subjectAlternativeNames",
        "validation": "validation",
        "validation_domains": "validationDomains",
        "validation_method": "validationMethod",
    },
)
class CertificateProps:
    def __init__(
        self,
        *,
        domain_name: str,
        subject_alternative_names: typing.Optional[typing.List[str]] = None,
        validation: typing.Optional["CertificateValidation"] = None,
        validation_domains: typing.Optional[typing.Mapping[str, str]] = None,
        validation_method: typing.Optional["ValidationMethod"] = None,
    ) -> None:
        """Properties for your certificate.

        :param domain_name: Fully-qualified domain name to request a certificate for. May contain wildcards, such as ``*.domain.com``.
        :param subject_alternative_names: Alternative domain names on your certificate. Use this to register alternative domain names that represent the same site. Default: - No additional FQDNs will be included as alternative domain names.
        :param validation: How to validate this certifcate. Default: CertificateValidation.fromEmail()
        :param validation_domains: What validation domain to use for every requested domain. Has to be a superdomain of the requested domain. Default: - Apex domain is used for every domain that's not overridden.
        :param validation_method: Validation method used to assert domain ownership. Default: ValidationMethod.EMAIL
        """
        self._values = {
            "domain_name": domain_name,
        }
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names
        if validation is not None:
            self._values["validation"] = validation
        if validation_domains is not None:
            self._values["validation_domains"] = validation_domains
        if validation_method is not None:
            self._values["validation_method"] = validation_method

    @builtins.property
    def domain_name(self) -> str:
        """Fully-qualified domain name to request a certificate for.

        May contain wildcards, such as ``*.domain.com``.
        """
        return self._values.get("domain_name")

    @builtins.property
    def subject_alternative_names(self) -> typing.Optional[typing.List[str]]:
        """Alternative domain names on your certificate.

        Use this to register alternative domain names that represent the same site.

        default
        :default: - No additional FQDNs will be included as alternative domain names.
        """
        return self._values.get("subject_alternative_names")

    @builtins.property
    def validation(self) -> typing.Optional["CertificateValidation"]:
        """How to validate this certifcate.

        default
        :default: CertificateValidation.fromEmail()
        """
        return self._values.get("validation")

    @builtins.property
    def validation_domains(self) -> typing.Optional[typing.Mapping[str, str]]:
        """What validation domain to use for every requested domain.

        Has to be a superdomain of the requested domain.

        default
        :default: - Apex domain is used for every domain that's not overridden.

        deprecated
        :deprecated: use ``validation`` instead.

        stability
        :stability: deprecated
        """
        return self._values.get("validation_domains")

    @builtins.property
    def validation_method(self) -> typing.Optional["ValidationMethod"]:
        """Validation method used to assert domain ownership.

        default
        :default: ValidationMethod.EMAIL

        deprecated
        :deprecated: use ``validation`` instead.

        stability
        :stability: deprecated
        """
        return self._values.get("validation_method")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CertificateValidation(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-certificatemanager.CertificateValidation",
):
    """How to validate a certificate."""

    @jsii.member(jsii_name="fromDns")
    @builtins.classmethod
    def from_dns(
        cls, hosted_zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None
    ) -> "CertificateValidation":
        """Validate the certifcate with DNS.

        IMPORTANT: If ``hostedZone`` is not specified, DNS records must be added
        manually and the stack will not complete creating until the records are
        added.

        :param hosted_zone: the hosted zone where DNS records must be created.
        """
        return jsii.sinvoke(cls, "fromDns", [hosted_zone])

    @jsii.member(jsii_name="fromDnsMultiZone")
    @builtins.classmethod
    def from_dns_multi_zone(
        cls, hosted_zones: typing.Mapping[str, aws_cdk.aws_route53.IHostedZone]
    ) -> "CertificateValidation":
        """Validate the certifcate with automatically created DNS records in multiple Amazon Route 53 hosted zones.

        :param hosted_zones: a map of hosted zones where DNS records must be created for the domains in the certificate.
        """
        return jsii.sinvoke(cls, "fromDnsMultiZone", [hosted_zones])

    @jsii.member(jsii_name="fromEmail")
    @builtins.classmethod
    def from_email(
        cls, validation_domains: typing.Optional[typing.Mapping[str, str]] = None
    ) -> "CertificateValidation":
        """Validate the certifcate with Email.

        IMPORTANT: if you are creating a certificate as part of your stack, the stack
        will not complete creating until you read and follow the instructions in the
        email that you will receive.

        ACM will send validation emails to the following addresses:

        admin@domain.com
        administrator@domain.com
        hostmaster@domain.com
        postmaster@domain.com
        webmaster@domain.com

        For every domain that you register.

        :param validation_domains: a map of validation domains to use for domains in the certificate.
        """
        return jsii.sinvoke(cls, "fromEmail", [validation_domains])

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> "ValidationMethod":
        """The validation method."""
        return jsii.get(self, "method")

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CertificationValidationProps":
        """Certification validation properties."""
        return jsii.get(self, "props")


@jsii.data_type(
    jsii_type="@aws-cdk/aws-certificatemanager.CertificationValidationProps",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone": "hostedZone",
        "hosted_zones": "hostedZones",
        "method": "method",
        "validation_domains": "validationDomains",
    },
)
class CertificationValidationProps:
    def __init__(
        self,
        *,
        hosted_zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
        hosted_zones: typing.Optional[
            typing.Mapping[str, aws_cdk.aws_route53.IHostedZone]
        ] = None,
        method: typing.Optional["ValidationMethod"] = None,
        validation_domains: typing.Optional[typing.Mapping[str, str]] = None,
    ) -> None:
        """Properties for certificate validation.

        :param hosted_zone: Hosted zone to use for DNS validation. Default: - use email validation
        :param hosted_zones: A map of hosted zones to use for DNS validation. Default: - use ``hostedZone``
        :param method: Validation method. Default: ValidationMethod.EMAIL
        :param validation_domains: Validation domains to use for email validation. Default: - Apex domain
        """
        self._values = {}
        if hosted_zone is not None:
            self._values["hosted_zone"] = hosted_zone
        if hosted_zones is not None:
            self._values["hosted_zones"] = hosted_zones
        if method is not None:
            self._values["method"] = method
        if validation_domains is not None:
            self._values["validation_domains"] = validation_domains

    @builtins.property
    def hosted_zone(self) -> typing.Optional[aws_cdk.aws_route53.IHostedZone]:
        """Hosted zone to use for DNS validation.

        default
        :default: - use email validation
        """
        return self._values.get("hosted_zone")

    @builtins.property
    def hosted_zones(
        self,
    ) -> typing.Optional[typing.Mapping[str, aws_cdk.aws_route53.IHostedZone]]:
        """A map of hosted zones to use for DNS validation.

        default
        :default: - use ``hostedZone``
        """
        return self._values.get("hosted_zones")

    @builtins.property
    def method(self) -> typing.Optional["ValidationMethod"]:
        """Validation method.

        default
        :default: ValidationMethod.EMAIL
        """
        return self._values.get("method")

    @builtins.property
    def validation_domains(self) -> typing.Optional[typing.Mapping[str, str]]:
        """Validation domains to use for email validation.

        default
        :default: - Apex domain
        """
        return self._values.get("validation_domains")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificationValidationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCertificate(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-certificatemanager.CfnCertificate",
):
    """A CloudFormation ``AWS::CertificateManager::Certificate``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html
    cloudformationResource:
    :cloudformationResource:: AWS::CertificateManager::Certificate
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        domain_name: str,
        certificate_authority_arn: typing.Optional[str] = None,
        certificate_transparency_logging_preference: typing.Optional[str] = None,
        domain_validation_options: typing.Optional[
            typing.Union[
                aws_cdk.core.IResolvable,
                typing.List[
                    typing.Union[
                        "DomainValidationOptionProperty", aws_cdk.core.IResolvable
                    ]
                ],
            ]
        ] = None,
        subject_alternative_names: typing.Optional[typing.List[str]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
        validation_method: typing.Optional[str] = None,
    ) -> None:
        """Create a new ``AWS::CertificateManager::Certificate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_name: ``AWS::CertificateManager::Certificate.DomainName``.
        :param certificate_authority_arn: ``AWS::CertificateManager::Certificate.CertificateAuthorityArn``.
        :param certificate_transparency_logging_preference: ``AWS::CertificateManager::Certificate.CertificateTransparencyLoggingPreference``.
        :param domain_validation_options: ``AWS::CertificateManager::Certificate.DomainValidationOptions``.
        :param subject_alternative_names: ``AWS::CertificateManager::Certificate.SubjectAlternativeNames``.
        :param tags: ``AWS::CertificateManager::Certificate.Tags``.
        :param validation_method: ``AWS::CertificateManager::Certificate.ValidationMethod``.
        """
        props = CfnCertificateProps(
            domain_name=domain_name,
            certificate_authority_arn=certificate_authority_arn,
            certificate_transparency_logging_preference=certificate_transparency_logging_preference,
            domain_validation_options=domain_validation_options,
            subject_alternative_names=subject_alternative_names,
            tags=tags,
            validation_method=validation_method,
        )

        jsii.create(CfnCertificate, self, [scope, id, props])

    @jsii.member(jsii_name="fromCloudFormation")
    @builtins.classmethod
    def from_cloud_formation(
        cls,
        scope: aws_cdk.core.Construct,
        id: str,
        resource_attributes: typing.Any,
        *,
        finder: aws_cdk.core.ICfnFinder,
    ) -> "CfnCertificate":
        """A factory method that creates a new instance of this class from an object containing the CloudFormation properties of this resource.

        Used in the @aws-cdk/cloudformation-include module.

        :param scope: -
        :param id: -
        :param resource_attributes: -
        :param finder: The finder interface used to resolve references across the template.

        stability
        :stability: experimental
        """
        options = aws_cdk.core.FromCloudFormationOptions(finder=finder)

        return jsii.sinvoke(
            cls, "fromCloudFormation", [scope, id, resource_attributes, options]
        )

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::CertificateManager::Certificate.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> str:
        """``AWS::CertificateManager::Certificate.DomainName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-domainname
        """
        return jsii.get(self, "domainName")

    @domain_name.setter
    def domain_name(self, value: str) -> None:
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> typing.Optional[str]:
        """``AWS::CertificateManager::Certificate.CertificateAuthorityArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-certificateauthorityarn
        """
        return jsii.get(self, "certificateAuthorityArn")

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "certificateAuthorityArn", value)

    @builtins.property
    @jsii.member(jsii_name="certificateTransparencyLoggingPreference")
    def certificate_transparency_logging_preference(self) -> typing.Optional[str]:
        """``AWS::CertificateManager::Certificate.CertificateTransparencyLoggingPreference``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-certificatetransparencyloggingpreference
        """
        return jsii.get(self, "certificateTransparencyLoggingPreference")

    @certificate_transparency_logging_preference.setter
    def certificate_transparency_logging_preference(
        self, value: typing.Optional[str]
    ) -> None:
        jsii.set(self, "certificateTransparencyLoggingPreference", value)

    @builtins.property
    @jsii.member(jsii_name="domainValidationOptions")
    def domain_validation_options(
        self,
    ) -> typing.Optional[
        typing.Union[
            aws_cdk.core.IResolvable,
            typing.List[
                typing.Union["DomainValidationOptionProperty", aws_cdk.core.IResolvable]
            ],
        ]
    ]:
        """``AWS::CertificateManager::Certificate.DomainValidationOptions``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-domainvalidationoptions
        """
        return jsii.get(self, "domainValidationOptions")

    @domain_validation_options.setter
    def domain_validation_options(
        self,
        value: typing.Optional[
            typing.Union[
                aws_cdk.core.IResolvable,
                typing.List[
                    typing.Union[
                        "DomainValidationOptionProperty", aws_cdk.core.IResolvable
                    ]
                ],
            ]
        ],
    ) -> None:
        jsii.set(self, "domainValidationOptions", value)

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNames")
    def subject_alternative_names(self) -> typing.Optional[typing.List[str]]:
        """``AWS::CertificateManager::Certificate.SubjectAlternativeNames``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-subjectalternativenames
        """
        return jsii.get(self, "subjectAlternativeNames")

    @subject_alternative_names.setter
    def subject_alternative_names(
        self, value: typing.Optional[typing.List[str]]
    ) -> None:
        jsii.set(self, "subjectAlternativeNames", value)

    @builtins.property
    @jsii.member(jsii_name="validationMethod")
    def validation_method(self) -> typing.Optional[str]:
        """``AWS::CertificateManager::Certificate.ValidationMethod``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-validationmethod
        """
        return jsii.get(self, "validationMethod")

    @validation_method.setter
    def validation_method(self, value: typing.Optional[str]) -> None:
        jsii.set(self, "validationMethod", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-certificatemanager.CfnCertificate.DomainValidationOptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "domain_name": "domainName",
            "hosted_zone_id": "hostedZoneId",
            "validation_domain": "validationDomain",
        },
    )
    class DomainValidationOptionProperty:
        def __init__(
            self,
            *,
            domain_name: str,
            hosted_zone_id: typing.Optional[str] = None,
            validation_domain: typing.Optional[str] = None,
        ) -> None:
            """
            :param domain_name: ``CfnCertificate.DomainValidationOptionProperty.DomainName``.
            :param hosted_zone_id: ``CfnCertificate.DomainValidationOptionProperty.HostedZoneId``.
            :param validation_domain: ``CfnCertificate.DomainValidationOptionProperty.ValidationDomain``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html
            """
            self._values = {
                "domain_name": domain_name,
            }
            if hosted_zone_id is not None:
                self._values["hosted_zone_id"] = hosted_zone_id
            if validation_domain is not None:
                self._values["validation_domain"] = validation_domain

        @builtins.property
        def domain_name(self) -> str:
            """``CfnCertificate.DomainValidationOptionProperty.DomainName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoptions-domainname
            """
            return self._values.get("domain_name")

        @builtins.property
        def hosted_zone_id(self) -> typing.Optional[str]:
            """``CfnCertificate.DomainValidationOptionProperty.HostedZoneId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoption-hostedzoneid
            """
            return self._values.get("hosted_zone_id")

        @builtins.property
        def validation_domain(self) -> typing.Optional[str]:
            """``CfnCertificate.DomainValidationOptionProperty.ValidationDomain``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoption-validationdomain
            """
            return self._values.get("validation_domain")

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DomainValidationOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-certificatemanager.CfnCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "certificate_authority_arn": "certificateAuthorityArn",
        "certificate_transparency_logging_preference": "certificateTransparencyLoggingPreference",
        "domain_validation_options": "domainValidationOptions",
        "subject_alternative_names": "subjectAlternativeNames",
        "tags": "tags",
        "validation_method": "validationMethod",
    },
)
class CfnCertificateProps:
    def __init__(
        self,
        *,
        domain_name: str,
        certificate_authority_arn: typing.Optional[str] = None,
        certificate_transparency_logging_preference: typing.Optional[str] = None,
        domain_validation_options: typing.Optional[
            typing.Union[
                aws_cdk.core.IResolvable,
                typing.List[
                    typing.Union[
                        "CfnCertificate.DomainValidationOptionProperty",
                        aws_cdk.core.IResolvable,
                    ]
                ],
            ]
        ] = None,
        subject_alternative_names: typing.Optional[typing.List[str]] = None,
        tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]] = None,
        validation_method: typing.Optional[str] = None,
    ) -> None:
        """Properties for defining a ``AWS::CertificateManager::Certificate``.

        :param domain_name: ``AWS::CertificateManager::Certificate.DomainName``.
        :param certificate_authority_arn: ``AWS::CertificateManager::Certificate.CertificateAuthorityArn``.
        :param certificate_transparency_logging_preference: ``AWS::CertificateManager::Certificate.CertificateTransparencyLoggingPreference``.
        :param domain_validation_options: ``AWS::CertificateManager::Certificate.DomainValidationOptions``.
        :param subject_alternative_names: ``AWS::CertificateManager::Certificate.SubjectAlternativeNames``.
        :param tags: ``AWS::CertificateManager::Certificate.Tags``.
        :param validation_method: ``AWS::CertificateManager::Certificate.ValidationMethod``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html
        """
        self._values = {
            "domain_name": domain_name,
        }
        if certificate_authority_arn is not None:
            self._values["certificate_authority_arn"] = certificate_authority_arn
        if certificate_transparency_logging_preference is not None:
            self._values[
                "certificate_transparency_logging_preference"
            ] = certificate_transparency_logging_preference
        if domain_validation_options is not None:
            self._values["domain_validation_options"] = domain_validation_options
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names
        if tags is not None:
            self._values["tags"] = tags
        if validation_method is not None:
            self._values["validation_method"] = validation_method

    @builtins.property
    def domain_name(self) -> str:
        """``AWS::CertificateManager::Certificate.DomainName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-domainname
        """
        return self._values.get("domain_name")

    @builtins.property
    def certificate_authority_arn(self) -> typing.Optional[str]:
        """``AWS::CertificateManager::Certificate.CertificateAuthorityArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-certificateauthorityarn
        """
        return self._values.get("certificate_authority_arn")

    @builtins.property
    def certificate_transparency_logging_preference(self) -> typing.Optional[str]:
        """``AWS::CertificateManager::Certificate.CertificateTransparencyLoggingPreference``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-certificatetransparencyloggingpreference
        """
        return self._values.get("certificate_transparency_logging_preference")

    @builtins.property
    def domain_validation_options(
        self,
    ) -> typing.Optional[
        typing.Union[
            aws_cdk.core.IResolvable,
            typing.List[
                typing.Union[
                    "CfnCertificate.DomainValidationOptionProperty",
                    aws_cdk.core.IResolvable,
                ]
            ],
        ]
    ]:
        """``AWS::CertificateManager::Certificate.DomainValidationOptions``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-domainvalidationoptions
        """
        return self._values.get("domain_validation_options")

    @builtins.property
    def subject_alternative_names(self) -> typing.Optional[typing.List[str]]:
        """``AWS::CertificateManager::Certificate.SubjectAlternativeNames``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-subjectalternativenames
        """
        return self._values.get("subject_alternative_names")

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::CertificateManager::Certificate.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-tags
        """
        return self._values.get("tags")

    @builtins.property
    def validation_method(self) -> typing.Optional[str]:
        """``AWS::CertificateManager::Certificate.ValidationMethod``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-validationmethod
        """
        return self._values.get("validation_method")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-certificatemanager.DnsValidatedCertificateProps",
    jsii_struct_bases=[CertificateProps],
    name_mapping={
        "domain_name": "domainName",
        "subject_alternative_names": "subjectAlternativeNames",
        "validation": "validation",
        "validation_domains": "validationDomains",
        "validation_method": "validationMethod",
        "hosted_zone": "hostedZone",
        "custom_resource_role": "customResourceRole",
        "region": "region",
        "route53_endpoint": "route53Endpoint",
    },
)
class DnsValidatedCertificateProps(CertificateProps):
    def __init__(
        self,
        *,
        domain_name: str,
        subject_alternative_names: typing.Optional[typing.List[str]] = None,
        validation: typing.Optional["CertificateValidation"] = None,
        validation_domains: typing.Optional[typing.Mapping[str, str]] = None,
        validation_method: typing.Optional["ValidationMethod"] = None,
        hosted_zone: aws_cdk.aws_route53.IHostedZone,
        custom_resource_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        region: typing.Optional[str] = None,
        route53_endpoint: typing.Optional[str] = None,
    ) -> None:
        """Properties to create a DNS validated certificate managed by AWS Certificate Manager.

        :param domain_name: Fully-qualified domain name to request a certificate for. May contain wildcards, such as ``*.domain.com``.
        :param subject_alternative_names: Alternative domain names on your certificate. Use this to register alternative domain names that represent the same site. Default: - No additional FQDNs will be included as alternative domain names.
        :param validation: How to validate this certifcate. Default: CertificateValidation.fromEmail()
        :param validation_domains: What validation domain to use for every requested domain. Has to be a superdomain of the requested domain. Default: - Apex domain is used for every domain that's not overridden.
        :param validation_method: Validation method used to assert domain ownership. Default: ValidationMethod.EMAIL
        :param hosted_zone: Route 53 Hosted Zone used to perform DNS validation of the request. The zone must be authoritative for the domain name specified in the Certificate Request.
        :param custom_resource_role: Role to use for the custom resource that creates the validated certificate. Default: - A new role will be created
        :param region: AWS region that will host the certificate. This is needed especially for certificates used for CloudFront distributions, which require the region to be us-east-1. Default: the region the stack is deployed in.
        :param route53_endpoint: An endpoint of Route53 service, which is not necessary as AWS SDK could figure out the right endpoints for most regions, but for some regions such as those in aws-cn partition, the default endpoint is not working now, hence the right endpoint need to be specified through this prop. Route53 is not been offically launched in China, it is only available for AWS internal accounts now. To make DnsValidatedCertificate work for internal accounts now, a special endpoint needs to be provided. Default: - The AWS SDK will determine the Route53 endpoint to use based on region

        stability
        :stability: experimental
        """
        self._values = {
            "domain_name": domain_name,
            "hosted_zone": hosted_zone,
        }
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names
        if validation is not None:
            self._values["validation"] = validation
        if validation_domains is not None:
            self._values["validation_domains"] = validation_domains
        if validation_method is not None:
            self._values["validation_method"] = validation_method
        if custom_resource_role is not None:
            self._values["custom_resource_role"] = custom_resource_role
        if region is not None:
            self._values["region"] = region
        if route53_endpoint is not None:
            self._values["route53_endpoint"] = route53_endpoint

    @builtins.property
    def domain_name(self) -> str:
        """Fully-qualified domain name to request a certificate for.

        May contain wildcards, such as ``*.domain.com``.
        """
        return self._values.get("domain_name")

    @builtins.property
    def subject_alternative_names(self) -> typing.Optional[typing.List[str]]:
        """Alternative domain names on your certificate.

        Use this to register alternative domain names that represent the same site.

        default
        :default: - No additional FQDNs will be included as alternative domain names.
        """
        return self._values.get("subject_alternative_names")

    @builtins.property
    def validation(self) -> typing.Optional["CertificateValidation"]:
        """How to validate this certifcate.

        default
        :default: CertificateValidation.fromEmail()
        """
        return self._values.get("validation")

    @builtins.property
    def validation_domains(self) -> typing.Optional[typing.Mapping[str, str]]:
        """What validation domain to use for every requested domain.

        Has to be a superdomain of the requested domain.

        default
        :default: - Apex domain is used for every domain that's not overridden.

        deprecated
        :deprecated: use ``validation`` instead.

        stability
        :stability: deprecated
        """
        return self._values.get("validation_domains")

    @builtins.property
    def validation_method(self) -> typing.Optional["ValidationMethod"]:
        """Validation method used to assert domain ownership.

        default
        :default: ValidationMethod.EMAIL

        deprecated
        :deprecated: use ``validation`` instead.

        stability
        :stability: deprecated
        """
        return self._values.get("validation_method")

    @builtins.property
    def hosted_zone(self) -> aws_cdk.aws_route53.IHostedZone:
        """Route 53 Hosted Zone used to perform DNS validation of the request.

        The zone
        must be authoritative for the domain name specified in the Certificate Request.

        stability
        :stability: experimental
        """
        return self._values.get("hosted_zone")

    @builtins.property
    def custom_resource_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        """Role to use for the custom resource that creates the validated certificate.

        default
        :default: - A new role will be created

        stability
        :stability: experimental
        """
        return self._values.get("custom_resource_role")

    @builtins.property
    def region(self) -> typing.Optional[str]:
        """AWS region that will host the certificate.

        This is needed especially
        for certificates used for CloudFront distributions, which require the region
        to be us-east-1.

        default
        :default: the region the stack is deployed in.

        stability
        :stability: experimental
        """
        return self._values.get("region")

    @builtins.property
    def route53_endpoint(self) -> typing.Optional[str]:
        """An endpoint of Route53 service, which is not necessary as AWS SDK could figure out the right endpoints for most regions, but for some regions such as those in aws-cn partition, the default endpoint is not working now, hence the right endpoint need to be specified through this prop.

        Route53 is not been offically launched in China, it is only available for AWS
        internal accounts now. To make DnsValidatedCertificate work for internal accounts
        now, a special endpoint needs to be provided.

        default
        :default: - The AWS SDK will determine the Route53 endpoint to use based on region

        stability
        :stability: experimental
        """
        return self._values.get("route53_endpoint")

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsValidatedCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-certificatemanager.ICertificate")
class ICertificate(aws_cdk.core.IResource, jsii.compat.Protocol):
    """Represents a certificate in AWS Certificate Manager."""

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _ICertificateProxy

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> str:
        """The certificate's ARN.

        attribute:
        :attribute:: true
        """
        ...


class _ICertificateProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """Represents a certificate in AWS Certificate Manager."""

    __jsii_type__ = "@aws-cdk/aws-certificatemanager.ICertificate"

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> str:
        """The certificate's ARN.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "certificateArn")


@jsii.enum(jsii_type="@aws-cdk/aws-certificatemanager.ValidationMethod")
class ValidationMethod(enum.Enum):
    """Method used to assert ownership of the domain."""

    EMAIL = "EMAIL"
    """Send email to a number of email addresses associated with the domain.

    see
    :see: https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html
    """
    DNS = "DNS"
    """Validate ownership by adding appropriate DNS records.

    see
    :see: https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html
    """


@jsii.implements(ICertificate)
class Certificate(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-certificatemanager.Certificate",
):
    """A certificate managed by AWS Certificate Manager."""

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        domain_name: str,
        subject_alternative_names: typing.Optional[typing.List[str]] = None,
        validation: typing.Optional["CertificateValidation"] = None,
        validation_domains: typing.Optional[typing.Mapping[str, str]] = None,
        validation_method: typing.Optional["ValidationMethod"] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param domain_name: Fully-qualified domain name to request a certificate for. May contain wildcards, such as ``*.domain.com``.
        :param subject_alternative_names: Alternative domain names on your certificate. Use this to register alternative domain names that represent the same site. Default: - No additional FQDNs will be included as alternative domain names.
        :param validation: How to validate this certifcate. Default: CertificateValidation.fromEmail()
        :param validation_domains: What validation domain to use for every requested domain. Has to be a superdomain of the requested domain. Default: - Apex domain is used for every domain that's not overridden.
        :param validation_method: Validation method used to assert domain ownership. Default: ValidationMethod.EMAIL
        """
        props = CertificateProps(
            domain_name=domain_name,
            subject_alternative_names=subject_alternative_names,
            validation=validation,
            validation_domains=validation_domains,
            validation_method=validation_method,
        )

        jsii.create(Certificate, self, [scope, id, props])

    @jsii.member(jsii_name="fromCertificateArn")
    @builtins.classmethod
    def from_certificate_arn(
        cls, scope: aws_cdk.core.Construct, id: str, certificate_arn: str
    ) -> "ICertificate":
        """Import a certificate.

        :param scope: -
        :param id: -
        :param certificate_arn: -
        """
        return jsii.sinvoke(cls, "fromCertificateArn", [scope, id, certificate_arn])

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> str:
        """The certificate's ARN."""
        return jsii.get(self, "certificateArn")


@jsii.implements(ICertificate)
class DnsValidatedCertificate(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-certificatemanager.DnsValidatedCertificate",
):
    """A certificate managed by AWS Certificate Manager.

    Will be automatically
    validated using DNS validation against the specified Route 53 hosted zone.

    stability
    :stability: experimental
    resource:
    :resource:: AWS::CertificateManager::Certificate
    """

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: str,
        *,
        hosted_zone: aws_cdk.aws_route53.IHostedZone,
        custom_resource_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        region: typing.Optional[str] = None,
        route53_endpoint: typing.Optional[str] = None,
        domain_name: str,
        subject_alternative_names: typing.Optional[typing.List[str]] = None,
        validation: typing.Optional["CertificateValidation"] = None,
        validation_domains: typing.Optional[typing.Mapping[str, str]] = None,
        validation_method: typing.Optional["ValidationMethod"] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param hosted_zone: Route 53 Hosted Zone used to perform DNS validation of the request. The zone must be authoritative for the domain name specified in the Certificate Request.
        :param custom_resource_role: Role to use for the custom resource that creates the validated certificate. Default: - A new role will be created
        :param region: AWS region that will host the certificate. This is needed especially for certificates used for CloudFront distributions, which require the region to be us-east-1. Default: the region the stack is deployed in.
        :param route53_endpoint: An endpoint of Route53 service, which is not necessary as AWS SDK could figure out the right endpoints for most regions, but for some regions such as those in aws-cn partition, the default endpoint is not working now, hence the right endpoint need to be specified through this prop. Route53 is not been offically launched in China, it is only available for AWS internal accounts now. To make DnsValidatedCertificate work for internal accounts now, a special endpoint needs to be provided. Default: - The AWS SDK will determine the Route53 endpoint to use based on region
        :param domain_name: Fully-qualified domain name to request a certificate for. May contain wildcards, such as ``*.domain.com``.
        :param subject_alternative_names: Alternative domain names on your certificate. Use this to register alternative domain names that represent the same site. Default: - No additional FQDNs will be included as alternative domain names.
        :param validation: How to validate this certifcate. Default: CertificateValidation.fromEmail()
        :param validation_domains: What validation domain to use for every requested domain. Has to be a superdomain of the requested domain. Default: - Apex domain is used for every domain that's not overridden.
        :param validation_method: Validation method used to assert domain ownership. Default: ValidationMethod.EMAIL

        stability
        :stability: experimental
        """
        props = DnsValidatedCertificateProps(
            hosted_zone=hosted_zone,
            custom_resource_role=custom_resource_role,
            region=region,
            route53_endpoint=route53_endpoint,
            domain_name=domain_name,
            subject_alternative_names=subject_alternative_names,
            validation=validation,
            validation_domains=validation_domains,
            validation_method=validation_method,
        )

        jsii.create(DnsValidatedCertificate, self, [scope, id, props])

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[str]:
        """Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "validate", [])

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> str:
        """The certificate's ARN.

        stability
        :stability: experimental
        """
        return jsii.get(self, "certificateArn")


__all__ = [
    "Certificate",
    "CertificateProps",
    "CertificateValidation",
    "CertificationValidationProps",
    "CfnCertificate",
    "CfnCertificateProps",
    "DnsValidatedCertificate",
    "DnsValidatedCertificateProps",
    "ICertificate",
    "ValidationMethod",
]

publication.publish()
