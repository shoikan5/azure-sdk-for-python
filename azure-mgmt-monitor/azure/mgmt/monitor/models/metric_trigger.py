# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MetricTrigger(Model):
    """The trigger that results in a scaling action.

    :param metric_name: the name of the metric that defines what the rule
     monitors.
    :type metric_name: str
    :param metric_resource_uri: the resource identifier of the resource the
     rule monitors.
    :type metric_resource_uri: str
    :param time_grain: the granularity of metrics the rule monitors. Must be
     one of the predefined values returned from metric definitions for the
     metric. Must be between 12 hours and 1 minute.
    :type time_grain: timedelta
    :param statistic: the metric statistic type. How the metrics from multiple
     instances are combined. Possible values include: 'Average', 'Min', 'Max',
     'Sum'
    :type statistic: str or ~azure.mgmt.monitor.models.MetricStatisticType
    :param time_window: the range of time in which instance data is collected.
     This value must be greater than the delay in metric collection, which can
     vary from resource-to-resource. Must be between 12 hours and 5 minutes.
    :type time_window: timedelta
    :param time_aggregation: time aggregation type. How the data that is
     collected should be combined over time. The default value is Average.
     Possible values include: 'Average', 'Minimum', 'Maximum', 'Total', 'Count'
    :type time_aggregation: str or
     ~azure.mgmt.monitor.models.TimeAggregationType
    :param operator: the operator that is used to compare the metric data and
     the threshold. Possible values include: 'Equals', 'NotEquals',
     'GreaterThan', 'GreaterThanOrEqual', 'LessThan', 'LessThanOrEqual'
    :type operator: str or ~azure.mgmt.monitor.models.ComparisonOperationType
    :param threshold: the threshold of the metric that triggers the scale
     action.
    :type threshold: float
    """

    _validation = {
        'metric_name': {'required': True},
        'metric_resource_uri': {'required': True},
        'time_grain': {'required': True},
        'statistic': {'required': True},
        'time_window': {'required': True},
        'time_aggregation': {'required': True},
        'operator': {'required': True},
        'threshold': {'required': True},
    }

    _attribute_map = {
        'metric_name': {'key': 'metricName', 'type': 'str'},
        'metric_resource_uri': {'key': 'metricResourceUri', 'type': 'str'},
        'time_grain': {'key': 'timeGrain', 'type': 'duration'},
        'statistic': {'key': 'statistic', 'type': 'MetricStatisticType'},
        'time_window': {'key': 'timeWindow', 'type': 'duration'},
        'time_aggregation': {'key': 'timeAggregation', 'type': 'TimeAggregationType'},
        'operator': {'key': 'operator', 'type': 'ComparisonOperationType'},
        'threshold': {'key': 'threshold', 'type': 'float'},
    }

    def __init__(self, metric_name, metric_resource_uri, time_grain, statistic, time_window, time_aggregation, operator, threshold):
        super(MetricTrigger, self).__init__()
        self.metric_name = metric_name
        self.metric_resource_uri = metric_resource_uri
        self.time_grain = time_grain
        self.statistic = statistic
        self.time_window = time_window
        self.time_aggregation = time_aggregation
        self.operator = operator
        self.threshold = threshold
