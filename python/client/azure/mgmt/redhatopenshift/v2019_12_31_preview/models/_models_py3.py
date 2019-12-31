# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class CloudError(Model):
    """CloudError represents a cloud error.

    :param error: An error response from the service.
    :type error:
     ~azure.mgmt.redhatopenshift.v2019_12_31_preview.models.CloudErrorBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CloudErrorBody'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(CloudError, self).__init__(**kwargs)
        self.error = error


class CloudErrorException(HttpOperationError):
    """Server responsed with exception of type: 'CloudError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CloudErrorException, self).__init__(deserialize, response, 'CloudError', *args)


class CloudErrorBody(Model):
    """CloudErrorBody represents the body of a cloud error.

    :param code: An identifier for the error. Codes are invariant and are
     intended to be consumed programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable
     for display in a user interface.
    :type message: str
    :param target: The target of the particular error. For example, the name
     of the property in error.
    :type target: str
    :param details: A list of additional details about the error.
    :type details:
     list[~azure.mgmt.redhatopenshift.v2019_12_31_preview.models.CloudErrorBody]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CloudErrorBody]'},
    }

    def __init__(self, *, code: str=None, message: str=None, target: str=None, details=None, **kwargs) -> None:
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class Display(Model):
    """Display represents the display details of an operation.

    :param provider: Friendly name of the resource provider.
    :type provider: str
    :param resource: Resource type on which the operation is performed.
    :type resource: str
    :param operation: Operation type: read, write, delete, listKeys/action,
     etc.
    :type operation: str
    :param description: Friendly name of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, provider: str=None, resource: str=None, operation: str=None, description: str=None, **kwargs) -> None:
        super(Display, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class MasterProfile(Model):
    """MasterProfile represents a master profile.

    :param vm_size: The size of the master VMs (immutable). Possible values
     include: 'Standard_D2s_v3', 'Standard_D4s_v3', 'Standard_D8s_v3'
    :type vm_size: str or
     ~azure.mgmt.redhatopenshift.v2019_12_31_preview.models.enum
    :param subnet_id: The Azure resource ID of the master subnet (immutable).
    :type subnet_id: str
    """

    _attribute_map = {
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'subnet_id': {'key': 'subnetId', 'type': 'str'},
    }

    def __init__(self, *, vm_size=None, subnet_id: str=None, **kwargs) -> None:
        super(MasterProfile, self).__init__(**kwargs)
        self.vm_size = vm_size
        self.subnet_id = subnet_id


class NetworkProfile(Model):
    """NetworkProfile represents a network profile.

    :param pod_cidr: The CIDR used for OpenShift/Kubernetes Pods (immutable).
    :type pod_cidr: str
    :param service_cidr: The CIDR used for OpenShift/Kubernetes Services
     (immutable).
    :type service_cidr: str
    """

    _attribute_map = {
        'pod_cidr': {'key': 'podCidr', 'type': 'str'},
        'service_cidr': {'key': 'serviceCidr', 'type': 'str'},
    }

    def __init__(self, *, pod_cidr: str=None, service_cidr: str=None, **kwargs) -> None:
        super(NetworkProfile, self).__init__(**kwargs)
        self.pod_cidr = pod_cidr
        self.service_cidr = service_cidr


class OpenShiftCluster(Model):
    """OpenShiftCluster represents an Azure Red Hat OpenShift cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID (immutable).
    :vartype id: str
    :ivar name: The resource name (immutable).
    :vartype name: str
    :ivar type: The resource type (immutable).
    :vartype type: str
    :param location: The resource location (immutable).
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param provisioning_state: The cluster provisioning state (immutable).
     Possible values include: 'Creating', 'Deleting', 'Failed', 'Succeeded',
     'Updating'
    :type provisioning_state: str or
     ~azure.mgmt.redhatopenshift.v2019_12_31_preview.models.enum
    :param service_principal_profile: The cluster service principal profile.
    :type service_principal_profile:
     ~azure.mgmt.redhatopenshift.v2019_12_31_preview.models.ServicePrincipalProfile
    :param network_profile: The cluster network profile.
    :type network_profile:
     ~azure.mgmt.redhatopenshift.v2019_12_31_preview.models.NetworkProfile
    :param master_profile: The cluster master profile.
    :type master_profile:
     ~azure.mgmt.redhatopenshift.v2019_12_31_preview.models.MasterProfile
    :param worker_profiles: The cluster worker profiles.
    :type worker_profiles:
     list[~azure.mgmt.redhatopenshift.v2019_12_31_preview.models.WorkerProfile]
    :param apiserver_url: The URL to access the cluster API server
     (immutable).
    :type apiserver_url: str
    :param console_url: The URL to access the cluster console (immutable).
    :type console_url: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'service_principal_profile': {'key': 'properties.servicePrincipalProfile', 'type': 'ServicePrincipalProfile'},
        'network_profile': {'key': 'properties.networkProfile', 'type': 'NetworkProfile'},
        'master_profile': {'key': 'properties.masterProfile', 'type': 'MasterProfile'},
        'worker_profiles': {'key': 'properties.workerProfiles', 'type': '[WorkerProfile]'},
        'apiserver_url': {'key': 'properties.apiserverUrl', 'type': 'str'},
        'console_url': {'key': 'properties.consoleUrl', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, tags=None, provisioning_state=None, service_principal_profile=None, network_profile=None, master_profile=None, worker_profiles=None, apiserver_url: str=None, console_url: str=None, **kwargs) -> None:
        super(OpenShiftCluster, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags
        self.provisioning_state = provisioning_state
        self.service_principal_profile = service_principal_profile
        self.network_profile = network_profile
        self.master_profile = master_profile
        self.worker_profiles = worker_profiles
        self.apiserver_url = apiserver_url
        self.console_url = console_url


class OpenShiftClusterCredentials(Model):
    """OpenShiftClusterCredentials represents an OpenShift cluster's credentials.

    :param kubeadmin_password: The password for the kubeadmin user
    :type kubeadmin_password: str
    """

    _attribute_map = {
        'kubeadmin_password': {'key': 'kubeadminPassword', 'type': 'str'},
    }

    def __init__(self, *, kubeadmin_password: str=None, **kwargs) -> None:
        super(OpenShiftClusterCredentials, self).__init__(**kwargs)
        self.kubeadmin_password = kubeadmin_password


class OpenShiftClusterList(Model):
    """OpenShiftClusterList represents a list of OpenShift clusters.

    :param value: The list of OpenShift clusters.
    :type value:
     list[~azure.mgmt.redhatopenshift.v2019_12_31_preview.models.OpenShiftCluster]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OpenShiftCluster]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(OpenShiftClusterList, self).__init__(**kwargs)
        self.value = value


class Operation(Model):
    """Operation represents an operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The object that describes the operation.
    :type display:
     ~azure.mgmt.redhatopenshift.v2019_12_31_preview.models.Display
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'Display'},
    }

    def __init__(self, *, name: str=None, display=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display


class OperationList(Model):
    """OperationList represents an operation list.

    :param value: List of operations supported by the resource provider.
    :type value:
     list[~azure.mgmt.redhatopenshift.v2019_12_31_preview.models.Operation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(OperationList, self).__init__(**kwargs)
        self.value = value


class ServicePrincipalProfile(Model):
    """ServicePrincipalProfile represents a service principal profile.

    :param client_id: The client ID used for the cluster (immutable).
    :type client_id: str
    :param client_secret: The client secret used for the cluster (immutable).
    :type client_secret: str
    """

    _attribute_map = {
        'client_id': {'key': 'clientId', 'type': 'str'},
        'client_secret': {'key': 'clientSecret', 'type': 'str'},
    }

    def __init__(self, *, client_id: str=None, client_secret: str=None, **kwargs) -> None:
        super(ServicePrincipalProfile, self).__init__(**kwargs)
        self.client_id = client_id
        self.client_secret = client_secret


class WorkerProfile(Model):
    """WorkerProfile represents a worker profile.

    :param name: The worker profile name.  Must be "worker" (immutable).
    :type name: str
    :param vm_size: The size of the worker VMs (immutable). Possible values
     include: 'Standard_D2s_v3', 'Standard_D4s_v3', 'Standard_D8s_v3'
    :type vm_size: str or
     ~azure.mgmt.redhatopenshift.v2019_12_31_preview.models.enum
    :param disk_size_gb: The disk size of the worker VMs.  Must be 128 or
     greater (immutable).
    :type disk_size_gb: int
    :param subnet_id: The Azure resource ID of the worker subnet (immutable).
    :type subnet_id: str
    :param count: The number of worker VMs.  Must be between 3 and 20.
    :type count: int
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'disk_size_gb': {'key': 'diskSizeGB', 'type': 'int'},
        'subnet_id': {'key': 'subnetId', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
    }

    def __init__(self, *, name: str=None, vm_size=None, disk_size_gb: int=None, subnet_id: str=None, count: int=None, **kwargs) -> None:
        super(WorkerProfile, self).__init__(**kwargs)
        self.name = name
        self.vm_size = vm_size
        self.disk_size_gb = disk_size_gb
        self.subnet_id = subnet_id
        self.count = count
