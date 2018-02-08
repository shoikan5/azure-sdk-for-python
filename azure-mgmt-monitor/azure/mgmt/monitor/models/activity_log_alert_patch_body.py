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


class ActivityLogAlertPatchBody(Model):
    """An activity log alert object for the body of patch operations.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param enabled: Indicates whether this activity log alert is enabled. If
     an activity log alert is not enabled, then none of its actions will be
     activated. Default value: True .
    :type enabled: bool
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
    }

    def __init__(self, tags=None, enabled=True):
        super(ActivityLogAlertPatchBody, self).__init__()
        self.tags = tags
        self.enabled = enabled
