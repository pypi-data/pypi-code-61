import logging

import boto3

from . import credentials as cred


logger = logging.getLogger(__name__)


def get_client():
    return cred.get_client("logs")


def put_metric_filter(log_group_name, filter_name, filter_pattern,
                      metric_namespace, metric_name, metric_value,
                      default_value):
    client = get_client()
    response = client.put_metric_filter(
        logGroupName=log_group_name,
        filterName=filter_name,
        filterPattern=filter_pattern,
        metricTransformation={
            "metricNamespace": metric_namespace,
            "metricName": metric_name,
            "metricValue": metric_value,
            "defaultValue": default_value
        }
    )
    return response
