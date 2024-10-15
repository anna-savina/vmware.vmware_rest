#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated using the ansible.content_builder.
# See: https://github.com/ansible-community/ansible.content_builder


DOCUMENTATION = r"""
module: appliance_infraprofile_configs
short_description: Exports the desired profile specification.
description: Exports the desired profile specification.
options:
    description:
        description:
        - Custom description provided by the user.
        - If unset description will be empty.
        type: str
    encryption_key:
        description:
        - Encryption Key to encrypt/decrypt profiles.
        - If unset encryption will not be used for the profile.
        type: str
    profiles:
        description:
        - Profiles to be exported/imported.
        - If unset or empty, all profiles will be returned.
        - When clients pass a value of this structure as a parameter, the field must
            contain the id of resources returned by M(vmware.vmware_rest.appliance_infraprofile_configs).
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
    state:
        choices:
        - export
        description: []
        required: true
        type: str
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
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 2.0.0
requirements:
- vSphere 7.0.3 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.3
"""

EXAMPLES = r"""
- name: Export the ApplianceManagement profile
  vmware.vmware_rest.appliance_infraprofile_configs:
    state: export
    profiles:
    - ApplianceManagement
  register: result
"""
RETURN = r"""
# content generated by the update_return_section callback# task: Export the ApplianceManagement profile
value:
  description: Export the ApplianceManagement profile
  returned: On success
  sample: '{"action":"RESTART_SERVICE","productName":"VMware vCenter Server","creationTime":"2022-11-23T20:11:00+0000","version":"7.0.3.00800","profiles":{"ApplianceManagement":{"action":"RESTART_SERVICE","actionOn":{"VC_SERVICES":["applmgmt"],"SYSTEMD":["sendmail","rsyslog"]},"description":"Appliance
    Mangment Service","version":"7.0","config":{"/etc/applmgmt/appliance/appliance.conf":{"Is
    shell Enabled":true,"Shell Expiration Time":9,"TimeSync Mode (Host/NTP)":"NTP"},"/etc/ntp.conf":{"Time
    servers":"time.nist.gov"},"/etc/shadow":{"root":{"maximumDays":"90","warningDays":"7"},"bin":{"maximumDays":"90","warningDays":"7"},"daemon":{"maximumDays":"90","warningDays":"7"},"messagebus":{"maximumDays":"90","warningDays":"7"},"systemd-bus-proxy":{"maximumDays":"90","warningDays":"7"},"systemd-journal-gateway":{"maximumDays":"90","warningDays":"7"},"systemd-journal-remote":{"maximumDays":"90","warningDays":"7"},"systemd-journal-upload":{"maximumDays":"90","warningDays":"7"},"systemd-network":{"maximumDays":"90","warningDays":"7"},"systemd-resolve":{"maximumDays":"90","warningDays":"7"},"systemd-timesync":{"maximumDays":"90","warningDays":"7"},"nobody":{"maximumDays":"90","warningDays":"7"},"rpc":{"maximumDays":"90","warningDays":"7"},"sshd":{"maximumDays":"90","warningDays":"7"},"ntp":{"maximumDays":"90","warningDays":"7"},"smmsp":{"maximumDays":"90","warningDays":"7"},"apache":{"maximumDays":"90","warningDays":"7"},"tftp":{"maximumDays":"","warningDays":""},"named":{"maximumDays":"","warningDays":""},"vmdird":{"maximumDays":"90","warningDays":"7"},"sso-user":{"maximumDays":"90","warningDays":"7"},"dnsmasq":{"maximumDays":"","warningDays":""},"observability":{"maximumDays":"","warningDays":""},"vdtc":{"maximumDays":"","warningDays":""},"vmafdd-user":{"maximumDays":"90","warningDays":"7"},"vmcad-user":{"maximumDays":"90","warningDays":"7"},"pod":{"maximumDays":"","warningDays":""},"vmonapi":{"maximumDays":"","warningDays":""},"envoy":{"maximumDays":"","warningDays":""},"vpostgres":{"maximumDays":"","warningDays":"7"},"lookupsvc":{"maximumDays":"","warningDays":""},"cis-license":{"maximumDays":"","warningDays":""},"pschealth":{"maximumDays":"","warningDays":""},"netdumper":{"maximumDays":"","warningDays":""},"vapiEndpoint":{"maximumDays":"90","warningDays":"7"},"vpxd-svcs":{"maximumDays":"","warningDays":""},"certauth":{"maximumDays":"90","warningDays":"7"},"certmgr":{"maximumDays":"90","warningDays":"7"},"infraprofile":{"maximumDays":"","warningDays":""},"topologysvc":{"maximumDays":"90","warningDays":"7"},"trustmanagement":{"maximumDays":"","warningDays":""},"vpxd":{"maximumDays":"","warningDays":""},"analytics":{"maximumDays":"","warningDays":""},"eam":{"maximumDays":"90","warningDays":"7"},"sps":{"maximumDays":"","warningDays":""},"deploy":{"maximumDays":"","warningDays":""},"updatemgr":{"maximumDays":"","warningDays":""},"vlcm":{"maximumDays":"90","warningDays":"7"},"vmcam":{"maximumDays":"90","warningDays":"7"},"vsan-health":{"maximumDays":"90","warningDays":"7"},"vsm":{"maximumDays":"90","warningDays":"7"},"vsphere-ui":{"maximumDays":"90","warningDays":"7"},"vtsdbuser":{"maximumDays":"","warningDays":""},"vstatsuser":{"maximumDays":"","warningDays":""},"wcp":{"maximumDays":"","warningDays":"7"},"content-library":{"maximumDays":"90","warningDays":"7"},"imagebuilder":{"maximumDays":"90","warningDays":"7"},"perfcharts":{"maximumDays":"90","warningDays":"7"},"vpgmonusr":{"maximumDays":"","warningDays":"7"},"vtsdbmonusr":{"maximumDays":"","warningDays":"7"},"zuul":{"maximumDays":"90","warningDays":"7"},"Send
    Waring before this No of Days.":null,"Password validity (days)":null},"/etc/sysconfig/clock":{"Time
    zone":"\"Etc/UTC\"","UTC":"1"},"/usr/bin/systemctl/sshd.service":{"Enable SSH":"true"},"/etc/mail/sendmail.cf":{"SMTP
    Port":null,"Mail server":null},"/etc/vmware-syslog/syslog.conf":{"Port [2]":null,"Port
    [1]":null,"Port [0]":null,"Protocol [2]":null,"Remote Syslog Host [1]":null,"Protocol
    [1]":null,"Remote Syslog Host [0]":null,"Protocol [0]":null,"Remote Syslog Host
    [2]":null},"/etc/pam.d/system-auth":{"Deny Login after these many Unsuccessful
    Attempts.":null,"Unlock root after (seconds)":null,"On Error Login will be.":null,"Include
    Root user for SSH lockout.":null,"Unlock user after (seconds)":null}},"name":"ApplianceManagement"}}}'
  type: str
"""


# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "export": {
        "query": {},
        "body": {
            "description": "description",
            "encryption_key": "encryption_key",
            "profiles": "profiles",
        },
        "path": {},
    }
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
    exists,
    gen_args,
    get_subdevice_type,
    open_session,
    prepare_payload,
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

    argument_spec["description"] = {"type": "str"}
    argument_spec["encryption_key"] = {"no_log": True, "type": "str"}
    argument_spec["profiles"] = {"type": "list", "elements": "str"}
    argument_spec["state"] = {"required": True, "type": "str", "choices": ["export"]}

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


# template: default_module.j2
def build_url(params):
    return ("https://{vcenter_hostname}" "/api/appliance/infraprofile/configs").format(
        **params
    )


async def entry_point(module, session):

    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]

    func = globals()["_" + operation]

    return await func(module.params, session)


async def _export(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["export"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["export"])
    subdevice_type = get_subdevice_type(
        "/api/appliance/infraprofile/configs?action=export"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/appliance/infraprofile/configs?action=export"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "export")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(current_loop)
        current_loop.run_until_complete(main())
    finally:
        current_loop.close()
