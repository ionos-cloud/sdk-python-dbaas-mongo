# coding: utf-8

# flake8: noqa
"""
    IONOS DBaaS MongoDB REST API

    With IONOS Cloud Database as a Service, you have the ability to quickly set up and manage a MongoDB database. You can also delete clusters, manage backups and users via the API.   MongoDB is an open source, cross-platform, document-oriented database program. Classified as a NoSQL database program, it uses JSON-like documents with optional schemas.  The MongoDB API allows you to create additional database clusters or modify existing ones. Both tools, the Data Center Designer (DCD) and the API use the same concepts consistently and are well suited for smooth and intuitive use.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from ionoscloud_dbaas_mongo.models.api_version import APIVersion
from ionoscloud_dbaas_mongo.models.cluster_list import ClusterList
from ionoscloud_dbaas_mongo.models.cluster_list_all_of import ClusterListAllOf
from ionoscloud_dbaas_mongo.models.cluster_logs import ClusterLogs
from ionoscloud_dbaas_mongo.models.cluster_logs_instances import ClusterLogsInstances
from ionoscloud_dbaas_mongo.models.cluster_logs_messages import ClusterLogsMessages
from ionoscloud_dbaas_mongo.models.cluster_properties import ClusterProperties
from ionoscloud_dbaas_mongo.models.cluster_response import ClusterResponse
from ionoscloud_dbaas_mongo.models.connection import Connection
from ionoscloud_dbaas_mongo.models.create_cluster_properties import CreateClusterProperties
from ionoscloud_dbaas_mongo.models.create_cluster_request import CreateClusterRequest
from ionoscloud_dbaas_mongo.models.create_restore_request import CreateRestoreRequest
from ionoscloud_dbaas_mongo.models.day_of_the_week import DayOfTheWeek
from ionoscloud_dbaas_mongo.models.error_message import ErrorMessage
from ionoscloud_dbaas_mongo.models.error_response import ErrorResponse
from ionoscloud_dbaas_mongo.models.health import Health
from ionoscloud_dbaas_mongo.models.maintenance_window import MaintenanceWindow
from ionoscloud_dbaas_mongo.models.metadata import Metadata
from ionoscloud_dbaas_mongo.models.pagination import Pagination
from ionoscloud_dbaas_mongo.models.pagination_links import PaginationLinks
from ionoscloud_dbaas_mongo.models.patch_cluster_properties import PatchClusterProperties
from ionoscloud_dbaas_mongo.models.patch_cluster_request import PatchClusterRequest
from ionoscloud_dbaas_mongo.models.patch_user_properties import PatchUserProperties
from ionoscloud_dbaas_mongo.models.patch_user_request import PatchUserRequest
from ionoscloud_dbaas_mongo.models.resource_type import ResourceType
from ionoscloud_dbaas_mongo.models.snapshot_list import SnapshotList
from ionoscloud_dbaas_mongo.models.snapshot_list_all_of import SnapshotListAllOf
from ionoscloud_dbaas_mongo.models.snapshot_properties import SnapshotProperties
from ionoscloud_dbaas_mongo.models.snapshot_response import SnapshotResponse
from ionoscloud_dbaas_mongo.models.state import State
from ionoscloud_dbaas_mongo.models.template_list import TemplateList
from ionoscloud_dbaas_mongo.models.template_list_all_of import TemplateListAllOf
from ionoscloud_dbaas_mongo.models.template_response import TemplateResponse
from ionoscloud_dbaas_mongo.models.user import User
from ionoscloud_dbaas_mongo.models.user_metadata import UserMetadata
from ionoscloud_dbaas_mongo.models.user_properties import UserProperties
from ionoscloud_dbaas_mongo.models.user_roles import UserRoles
from ionoscloud_dbaas_mongo.models.users_list import UsersList
