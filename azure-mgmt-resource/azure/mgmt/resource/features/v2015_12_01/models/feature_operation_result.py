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


class FeatureOperationResult(Model):
    """FeatureOperationResult.

    :param name: The name of the operation.
    :type name: str
    :param operations: The array of feature operations.
    :type operations:
     list[~azure.mgmt.resource.features.v2015_12_01.models.OperationDisplay]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'operations': {'key': 'operations', 'type': '[OperationDisplay]'},
    }

    def __init__(self, **kwargs):
        super(FeatureOperationResult, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.operations = kwargs.get('operations', None)
