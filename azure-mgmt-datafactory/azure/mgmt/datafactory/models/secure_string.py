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

from .secret_base import SecretBase


class SecureString(SecretBase):
    """Azure Data Factory secure string definition. The string value will be
    masked with asterisks '*' during Get or List API calls.

    :param type: Constant filled by server.
    :type type: str
    :param value: Value of secure string.
    :type value: str
    """

    _validation = {
        'type': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, value):
        super(SecureString, self).__init__()
        self.value = value
        self.type = 'SecureString'
