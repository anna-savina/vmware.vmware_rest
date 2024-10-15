#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated using the ansible.content_builder.
# See: https://github.com/ansible-community/ansible.content_builder


DOCUMENTATION = r"""
module: vcenter_vm_info
short_description: Returns information about a virtual machine.
description: Returns information about a virtual machine.
options:
    clusters:
        description:
        - Clusters that must contain the virtual machine for the virtual machine to
            match the filter.
        - If unset or empty, virtual machines in any cluster match the filter.
        - When clients pass a value of this structure as a parameter, the field must
            contain the id of resources returned by M(vmware.vmware_rest.vcenter_cluster_info).
        elements: str
        type: list
    datacenters:
        aliases:
        - filter_datacenters
        description:
        - Datacenters that must contain the virtual machine for the virtual machine
            to match the filter.
        - If unset or empty, virtual machines in any datacenter match the filter.
        - When clients pass a value of this structure as a parameter, the field must
            contain the id of resources returned by M(vmware.vmware_rest.vcenter_datacenter_info).
        elements: str
        type: list
    folders:
        aliases:
        - filter_folders
        description:
        - Folders that must contain the virtual machine for the virtual machine to
            match the filter.
        - If unset or empty, virtual machines in any folder match the filter.
        - When clients pass a value of this structure as a parameter, the field must
            contain the id of resources returned by M(vmware.vmware_rest.vcenter_folder_info).
        elements: str
        type: list
    hosts:
        description:
        - Hosts that must contain the virtual machine for the virtual machine to match
            the filter.
        - If unset or empty, virtual machines on any host match the filter.
        - When clients pass a value of this structure as a parameter, the field must
            contain the id of resources returned by M(vmware.vmware_rest.vcenter_host_info).
        elements: str
        type: list
    names:
        aliases:
        - filter_names
        description:
        - Names that virtual machines must have to match the filter (see I(name)).
        - If unset or empty, virtual machines with any name match the filter.
        elements: str
        type: list
    power_states:
        description:
        - Power states that a virtual machine must be in to match the filter (see
            I()
        - If unset or empty, virtual machines in any power state match the filter.
        elements: str
        type: list
    resource_pools:
        description:
        - Resource pools that must contain the virtual machine for the virtual machine
            to match the filter.
        - If unset or empty, virtual machines in any resource pool match the filter.
        - When clients pass a value of this structure as a parameter, the field must
            contain the id of resources returned by M(vmware.vmware_rest.vcenter_resourcepool_info).
        elements: str
        type: list
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    vcenter_hostname:
        description:
        - The hostname or IP address of the vSphere vCenter
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_HOST) will be used instead.
        required: true
        type: str
    vcenter_password:
        description:
        - The vSphere vCenter password
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_PASSWORD) will be used instead.
        required: true
        type: str
    vcenter_rest_log_file:
        description:
        - 'You can use this optional parameter to set the location of a log file. '
        - 'This file will be used to record the HTTP REST interaction. '
        - 'The file will be stored on the host that runs the module. '
        - 'If the value is not specified in the task, the value of '
        - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
        type: str
    vcenter_username:
        description:
        - The vSphere vCenter username
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_USER) will be used instead.
        required: true
        type: str
    vcenter_validate_certs:
        default: true
        description:
        - Allows connection when SSL certificates are not valid. Set to C(false) when
            certificates are not trusted.
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_VALIDATE_CERTS) will be used instead.
        type: bool
    vm:
        description:
        - Virtual machine identifier.
        - The parameter must be the id of a resource returned by M(vmware.vmware_rest.vcenter_vm_info).
            Required with I(state=['get'])
        type: str
    vms:
        description:
        - Identifiers of virtual machines that can match the filter.
        - If unset or empty, virtual machines with any identifier match the filter.
        - When clients pass a value of this structure as a parameter, the field must
            contain the id of resources returned by M(vmware.vmware_rest.vcenter_vm_info).
        elements: str
        type: list
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 0.1.0
requirements:
- vSphere 7.0.3 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.3
"""

EXAMPLES = r"""
- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster') }}"
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local') }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources') }}"
    name: test_vm1
    guest_OS: RHEL_7_64
    hardware_version: VMX_11
    memory:
      hot_add_enabled: true
      size_MiB: 1024
    disks:
    - type: SATA
      backing:
        type: VMDK_FILE
        vmdk_file: '[local] test_vm1/{{ disk_name }}.vmdk'
    - type: SATA
      new_vmdk:
        name: second_disk
        capacity: 32000000000
    cdroms:
    - type: SATA
      sata:
        bus: 0
        unit: 2
    nics:
    - backing:
        type: STANDARD_PORTGROUP
        network: "{{ lookup('vmware.vmware_rest.network_moid', '/my_dc/network/VM Network') }}"
  register: my_vm

- name: Wait until my VM is off
  vmware.vmware_rest.vcenter_vm_info:
    vm: '{{ my_vm.id }}'
  register: vm_info
  until:
  - vm_info is not failed
  - vm_info.value.power_state == "POWERED_OFF"
  retries: 60
  delay: 5

- register: _should_be_empty
  name: Search with an invalid filter
  vmware.vmware_rest.vcenter_vm_info:
    filter_names: test_vm1_does_not_exists

- name: Look up the VM called test_vm1 in the inventory
  register: search_result
  vmware.vmware_rest.vcenter_vm_info:
    filter_names:
    - test_vm1

- name: Collect information about a specific VM
  vmware.vmware_rest.vcenter_vm_info:
    vm: '{{ search_result.value[0].vm }}'
  register: test_vm1_info
"""
RETURN = r"""
# content generated by the update_return_section callback# task: Wait until my VM is off
id:
  description: moid of the resource
  returned: On success
  sample: vm-1049
  type: str
value:
  description: Wait until my VM is off
  returned: On success
  sample:
    boot:
      delay: 0
      enter_setup_mode: 0
      retry: 0
      retry_delay: 10000
      type: BIOS
    boot_devices: []
    cdroms:
      '16002':
        allow_guest_control: 0
        backing:
          auto_detect: 1
          device_access_type: EMULATION
          type: HOST_DEVICE
        label: CD/DVD drive 1
        sata:
          bus: 0
          unit: 2
        start_connected: 0
        state: NOT_CONNECTED
        type: SATA
    cpu:
      cores_per_socket: 1
      count: 1
      hot_add_enabled: 0
      hot_remove_enabled: 0
    disks:
      '16000':
        backing:
          type: VMDK_FILE
          vmdk_file: '[local] test_vm1/rhel-8.5.vmdk'
        capacity: 16106127360
        label: Hard disk 1
        sata:
          bus: 0
          unit: 0
        type: SATA
      '16001':
        backing:
          type: VMDK_FILE
          vmdk_file: '[local] test_vm1_1/second_disk.vmdk'
        capacity: 32000000000
        label: Hard disk 2
        sata:
          bus: 0
          unit: 1
        type: SATA
    floppies: {}
    guest_OS: RHEL_7_64
    hardware:
      upgrade_policy: NEVER
      upgrade_status: NONE
      version: VMX_11
    identity:
      bios_uuid: 4231943a-a1b5-9d24-1e05-d447e9ff0396
      instance_uuid: 5031e081-01a7-d61a-31f8-4bc54057ec60
      name: test_vm1
    instant_clone_frozen: 0
    memory:
      hot_add_enabled: 1
      size_MiB: 1024
    name: test_vm1
    nics:
      '4000':
        allow_guest_control: 0
        backing:
          network: network-1041
          network_name: VM Network
          type: STANDARD_PORTGROUP
        label: Network adapter 1
        mac_address: 00:50:56:b1:22:7d
        mac_type: ASSIGNED
        pci_slot_number: 160
        start_connected: 0
        state: NOT_CONNECTED
        type: VMXNET3
        upt_compatibility_enabled: 0
        wake_on_lan_enabled: 0
    nvme_adapters: {}
    parallel_ports: {}
    power_state: POWERED_OFF
    sata_adapters:
      '15000':
        bus: 0
        label: SATA controller 0
        pci_slot_number: 32
        type: AHCI
    scsi_adapters: {}
    serial_ports: {}
  type: dict
"""


# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "get": {"query": {}, "body": {}, "path": {"vm": "vm"}},
    "list": {
        "query": {
            "clusters": "clusters",
            "datacenters": "datacenters",
            "folders": "folders",
            "hosts": "hosts",
            "names": "names",
            "power_states": "power_states",
            "resource_pools": "resource_pools",
            "vms": "vms",
        },
        "body": {},
        "path": {},
    },
}  # pylint: disable=line-too-long

from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    open_session,
    session_timeout,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["clusters"] = {"type": "list", "elements": "str"}
    argument_spec["datacenters"] = {
        "aliases": ["filter_datacenters"],
        "type": "list",
        "elements": "str",
    }
    argument_spec["folders"] = {
        "aliases": ["filter_folders"],
        "type": "list",
        "elements": "str",
    }
    argument_spec["hosts"] = {"type": "list", "elements": "str"}
    argument_spec["names"] = {
        "aliases": ["filter_names"],
        "type": "list",
        "elements": "str",
    }
    argument_spec["power_states"] = {"type": "list", "elements": "str"}
    argument_spec["resource_pools"] = {"type": "list", "elements": "str"}
    argument_spec["vm"] = {"type": "str"}
    argument_spec["vms"] = {"type": "list", "elements": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: info_list_and_get_module.j2
def build_url(params):
    import yarl

    if params.get("vm"):
        _in_query_parameters = PAYLOAD_FORMAT["get"]["query"].keys()
        return yarl.URL(
            ("https://{vcenter_hostname}" "/api/vcenter/vm/").format(**params)
            + params["vm"]
            + gen_args(params, _in_query_parameters),
            encoded=True,
        )
    _in_query_parameters = PAYLOAD_FORMAT["list"]["query"].keys()
    return yarl.URL(
        ("https://{vcenter_hostname}" "/api/vcenter/vm").format(**params)
        + gen_args(params, _in_query_parameters),
        encoded=True,
    )


async def entry_point(module, session):
    url = build_url(module.params)
    async with session.get(url, **session_timeout(module.params)) as resp:
        _json = await resp.json()

        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}

        if module.params.get("vm"):
            _json["id"] = module.params.get("vm")
        elif module.params.get("label"):  # TODO extend the list of filter
            _json = await exists(module.params, session, str(url))
        elif (
            isinstance(_json["value"], list)
            and len(_json["value"]) > 0
            and isinstance(_json["value"][0], str)
        ):
            # this is a list of id, we fetch the details
            full_device_list = await build_full_device_list(session, str(url), _json)
            _json = {"value": [i["value"] for i in full_device_list]}

        return await update_changed_flag(_json, resp.status, "get")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(current_loop)
        current_loop.run_until_complete(main())
    finally:
        current_loop.close()
