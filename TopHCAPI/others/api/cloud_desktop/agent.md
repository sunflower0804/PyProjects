[back to api overview](../api_overview.md)

### 终端相关接口
## /v1/vdc_agent/list
终端列表
### 请求类型
GET
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 tenant|string|否|-| 租户uuid
 online|bool|否|false|过滤终端状态
 filter_object_group|string|否|-|过滤终端分组
 filter_ip|string|否|-|过滤终端IP
 page_num|int|否|0|显示页码
 page_size|int|否|0|每页显示多少数据
 ####返回示例
 ```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "list": [
      {
        "uuid": "TDT-5256ff0ad293",
        "description": "xxx",
        "group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
        "group_name": "default",
        "register_time": 1629099223,
        "is_connecting": false,
        "ip": "",
        "os_version": "windows",
        "agent_version": "3.3.0.0",
        "bind_vm_uuid": {},
        "last_connection_time": 1630031787,
        "last_disconnection_time": 1630032300,
        "strategy_bind": [
          3
        ],
        "recent_login_user": {
          "uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "name": "csw",
          "email": "dfa@qq.com",
          "event_windows_popup_push": {
            "push_level": 4,
            "push_enabled": true
          },
          "event_email_push": {
            "push_level": 4,
            "push_enabled": true
          },
          "event_shortmessage_push": {
            "push_level": 0,
            "push_enabled": false
          },
          "phone": "",
          "description": "",
          "create_time": 1628845108,
          "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "role": "administrator",
          "group": "",
          "policys": [
            "d590db81-e83c-4c5b-af59-abb30e0900b6"
          ],
          "default_cluster": "",
          "is_ldap": false,
          "last_password_modify_time": 1628845108,
          "s3_volumes": null,
          "tenant_name": "csw",
          "group_name": "",
          "doublefactor_authentication_type": ""
        },
        "vm_selected": null,
        "agent_resource": null
      },
      {
        "uuid": "TDT-241c04140b06",
        "description": "xxx",
        "group": "6701258a-73ec-48a5-95b2-df7b58ff7d62",
        "group_name": "default",
        "register_time": 1629169163,
        "is_connecting": false,
        "ip": "",
        "os_version": "linux",
        "agent_version": "3.3.0.0",
        "bind_vm_uuid": {},
        "last_connection_time": 1629711652,
        "last_disconnection_time": 1629714159,
        "strategy_bind": [
          3
        ],
        "recent_login_user": {
          "uuid": "0604fe35-3167-4d46-80b5-3b3c8f1218db",
          "name": "jy3",
          "email": "asdas@qq.com",
          "event_windows_popup_push": {
            "push_level": 1,
            "push_enabled": true
          },
          "event_email_push": {
            "push_level": 1,
            "push_enabled": false
          },
          "event_shortmessage_push": {
            "push_level": 1,
            "push_enabled": false
          },
          "phone": "",
          "description": "",
          "create_time": 1629710737,
          "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "role": "normalUser",
          "group": "",
          "policys": [
            "f48e56c3-0d48-43e1-bc94-f0acf5005e4b"
          ],
          "default_cluster": "39058114-31a1-452f-9ce7-54c002ca7f53",
          "is_ldap": false,
          "last_password_modify_time": 1629710737,
          "s3_volumes": null,
          "tenant_name": "csw",
          "group_name": "",
          "doublefactor_authentication_type": ""
        },
        "vm_selected": null,
        "agent_resource": null
      },
      {
        "uuid": "TDT-241c04140b8e",
        "description": "xxx",
        "group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
        "group_name": "default",
        "register_time": 1629195245,
        "is_connecting": false,
        "ip": "",
        "os_version": "windows",
        "agent_version": "3.3.0.0",
        "bind_vm_uuid": {},
        "last_connection_time": 1629974905,
        "last_disconnection_time": 1629974906,
        "strategy_bind": [
          3
        ],
        "recent_login_user": {
          "uuid": "2ec14edb-d2c1-44a6-a1ae-7aa2af37be2a",
          "name": "jy6",
          "email": "asdas@qq.com",
          "event_windows_popup_push": {
            "push_level": 1,
            "push_enabled": true
          },
          "event_email_push": {
            "push_level": 1,
            "push_enabled": false
          },
          "event_shortmessage_push": {
            "push_level": 1,
            "push_enabled": false
          },
          "phone": "",
          "description": "",
          "create_time": 1629710737,
          "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "role": "normalUser",
          "group": "",
          "policys": [
            "f48e56c3-0d48-43e1-bc94-f0acf5005e4b"
          ],
          "default_cluster": "39058114-31a1-452f-9ce7-54c002ca7f53",
          "is_ldap": false,
          "last_password_modify_time": 1629710737,
          "s3_volumes": null,
          "tenant_name": "csw",
          "group_name": "",
          "doublefactor_authentication_type": ""
        },
        "vm_selected": null,
        "agent_resource": null
      },
      {
        "uuid": "TDT-241c04141687",
        "description": "xxx",
        "group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
        "group_name": "default",
        "register_time": 1629196474,
        "is_connecting": false,
        "ip": "",
        "os_version": "linux",
        "agent_version": "3.3.0.0",
        "bind_vm_uuid": {},
        "last_connection_time": 1629939123,
        "last_disconnection_time": 1629939146,
        "strategy_bind": null,
        "recent_login_user": {
          "uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "name": "csw",
          "email": "dfa@qq.com",
          "event_windows_popup_push": {
            "push_level": 4,
            "push_enabled": true
          },
          "event_email_push": {
            "push_level": 4,
            "push_enabled": true
          },
          "event_shortmessage_push": {
            "push_level": 0,
            "push_enabled": false
          },
          "phone": "",
          "description": "",
          "create_time": 1628845108,
          "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "role": "administrator",
          "group": "",
          "policys": [
            "d590db81-e83c-4c5b-af59-abb30e0900b6"
          ],
          "default_cluster": "",
          "is_ldap": false,
          "last_password_modify_time": 1628845108,
          "s3_volumes": null,
          "tenant_name": "csw",
          "group_name": "",
          "doublefactor_authentication_type": ""
        },
        "vm_selected": null,
        "agent_resource": null
      },
      {
        "uuid": "TDT-241c041418a3",
        "description": "xxx",
        "group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
        "group_name": "default",
        "register_time": 1629438846,
        "is_connecting": false,
        "ip": "",
        "os_version": "linux",
        "agent_version": "3.3.0.0",
        "bind_vm_uuid": {},
        "last_connection_time": 1630027286,
        "last_disconnection_time": 1630027325,
        "strategy_bind": null,
        "recent_login_user": {
          "uuid": "7118a14a-c6b4-43a5-b389-e246fd7725b2",
          "name": "jy2",
          "email": "asdas@qq.com",
          "event_windows_popup_push": {
            "push_level": 1,
            "push_enabled": true
          },
          "event_email_push": {
            "push_level": 1,
            "push_enabled": false
          },
          "event_shortmessage_push": {
            "push_level": 1,
            "push_enabled": false
          },
          "phone": "",
          "description": "",
          "create_time": 1629710737,
          "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "role": "normalUser",
          "group": "",
          "policys": [
            "f48e56c3-0d48-43e1-bc94-f0acf5005e4b"
          ],
          "default_cluster": "39058114-31a1-452f-9ce7-54c002ca7f53",
          "is_ldap": false,
          "last_password_modify_time": 1629710737,
          "s3_volumes": null,
          "tenant_name": "csw",
          "group_name": "",
          "doublefactor_authentication_type": ""
        },
        "vm_selected": null,
        "agent_resource": null
      },
      {
        "uuid": "TDT-241c0414188f",
        "description": "xxx",
        "group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
        "group_name": "default",
        "register_time": 1629443672,
        "is_connecting": false,
        "ip": "",
        "os_version": "linux",
        "agent_version": "3.3.0.0",
        "bind_vm_uuid": {},
        "last_connection_time": 1630031221,
        "last_disconnection_time": 1630031252,
        "strategy_bind": null,
        "recent_login_user": {
          "uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "name": "csw",
          "email": "dfa@qq.com",
          "event_windows_popup_push": {
            "push_level": 4,
            "push_enabled": true
          },
          "event_email_push": {
            "push_level": 4,
            "push_enabled": true
          },
          "event_shortmessage_push": {
            "push_level": 0,
            "push_enabled": false
          },
          "phone": "",
          "description": "",
          "create_time": 1628845108,
          "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "role": "administrator",
          "group": "",
          "policys": [
            "d590db81-e83c-4c5b-af59-abb30e0900b6"
          ],
          "default_cluster": "",
          "is_ldap": false,
          "last_password_modify_time": 1628845108,
          "s3_volumes": null,
          "tenant_name": "csw",
          "group_name": "",
          "doublefactor_authentication_type": ""
        },
        "vm_selected": null,
        "agent_resource": null
      },
      {
        "uuid": "TDT-241c04111f0a",
        "description": "xxx",
        "group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
        "group_name": "default",
        "register_time": 1629447847,
        "is_connecting": false,
        "ip": "",
        "os_version": "linux",
        "agent_version": "3.3.0.0",
        "bind_vm_uuid": {},
        "last_connection_time": 1629715033,
        "last_disconnection_time": 1629715044,
        "strategy_bind": null,
        "recent_login_user": {
          "uuid": "ff4839c6-e1d7-4b1d-b8da-be719ed3663f",
          "name": "xzh1",
          "email": "",
          "event_windows_popup_push": {
            "push_level": 4,
            "push_enabled": false
          },
          "event_email_push": {
            "push_level": 4,
            "push_enabled": false
          },
          "event_shortmessage_push": {
            "push_level": 0,
            "push_enabled": false
          },
          "phone": "",
          "description": "",
          "create_time": 1628701330,
          "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "role": "normalUser",
          "group": "",
          "policys": [
            "f48e56c3-0d48-43e1-bc94-f0acf5005e4b"
          ],
          "default_cluster": "",
          "is_ldap": true,
          "last_password_modify_time": 0,
          "s3_volumes": null,
          "tenant_name": "csw",
          "group_name": "",
          "doublefactor_authentication_type": ""
        },
        "vm_selected": null,
        "agent_resource": null
      },
      {
        "uuid": "TDT-10e7c62e3fed",
        "description": "xxx",
        "group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
        "group_name": "default",
        "register_time": 1629687143,
        "is_connecting": false,
        "ip": "",
        "os_version": "windows",
        "agent_version": "3.3.0.0",
        "bind_vm_uuid": {},
        "last_connection_time": 1629959540,
        "last_disconnection_time": 1629959581,
        "strategy_bind": null,
        "recent_login_user": {
          "uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "name": "csw",
          "email": "dfa@qq.com",
          "event_windows_popup_push": {
            "push_level": 4,
            "push_enabled": true
          },
          "event_email_push": {
            "push_level": 4,
            "push_enabled": true
          },
          "event_shortmessage_push": {
            "push_level": 0,
            "push_enabled": false
          },
          "phone": "",
          "description": "",
          "create_time": 1628845108,
          "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "role": "administrator",
          "group": "",
          "policys": [
            "d590db81-e83c-4c5b-af59-abb30e0900b6"
          ],
          "default_cluster": "",
          "is_ldap": false,
          "last_password_modify_time": 1628845108,
          "s3_volumes": null,
          "tenant_name": "csw",
          "group_name": "",
          "doublefactor_authentication_type": ""
        },
        "vm_selected": null,
        "agent_resource": null
      },
      {
        "uuid": "TDT-5256ffe4d7d0",
        "description": "xxx",
        "group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
        "group_name": "default",
        "register_time": 1629768073,
        "is_connecting": false,
        "ip": "",
        "os_version": "windows",
        "agent_version": "3.2.1",
        "bind_vm_uuid": {},
        "last_connection_time": 1629769022,
        "last_disconnection_time": 1629768119,
        "strategy_bind": null,
        "recent_login_user": {
          "uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "name": "csw",
          "email": "dfa@qq.com",
          "event_windows_popup_push": {
            "push_level": 4,
            "push_enabled": true
          },
          "event_email_push": {
            "push_level": 4,
            "push_enabled": true
          },
          "event_shortmessage_push": {
            "push_level": 0,
            "push_enabled": false
          },
          "phone": "",
          "description": "",
          "create_time": 1628845108,
          "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "role": "administrator",
          "group": "",
          "policys": [
            "d590db81-e83c-4c5b-af59-abb30e0900b6"
          ],
          "default_cluster": "",
          "is_ldap": false,
          "last_password_modify_time": 1628845108,
          "s3_volumes": null,
          "tenant_name": "csw",
          "group_name": "",
          "doublefactor_authentication_type": ""
        },
        "vm_selected": null,
        "agent_resource": null
      },
      {
        "uuid": "TDT-241c041418ea",
        "description": "xxx",
        "group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
        "group_name": "default",
        "register_time": 1629938928,
        "is_connecting": false,
        "ip": "",
        "os_version": "linux",
        "agent_version": "3.2.2",
        "bind_vm_uuid": {},
        "last_connection_time": 1630025582,
        "last_disconnection_time": 1630025617,
        "strategy_bind": null,
        "recent_login_user": {
          "uuid": "84e1477b-0a83-4de0-a071-5702f1b931fe",
          "name": "lqf",
          "email": "123@qq.com",
          "event_windows_popup_push": {
            "push_level": 1,
            "push_enabled": true
          },
          "event_email_push": {
            "push_level": 1,
            "push_enabled": false
          },
          "event_shortmessage_push": {
            "push_level": 1,
            "push_enabled": false
          },
          "phone": "",
          "description": "",
          "create_time": 1629277310,
          "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
          "role": "administrator",
          "group": "",
          "policys": [
            "d590db81-e83c-4c5b-af59-abb30e0900b6"
          ],
          "default_cluster": "39058114-31a1-452f-9ce7-54c002ca7f53",
          "is_ldap": false,
          "last_password_modify_time": 1629277310,
          "s3_volumes": null,
          "tenant_name": "csw",
          "group_name": "",
          "doublefactor_authentication_type": ""
        },
        "vm_selected": null,
        "agent_resource": null
      }
    ],
    "total_count": 11
  }
}
```
 
 

## /v1/vdc_agent/list/each_cluster
单一集群终端列表
### 请求类型
GET
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 tenant|string|否|-| 租户uuid
 online|bool|否|false|过滤终端状态
 filter_object_group|string|否|-|过滤终端分组
 page_num|int|否|0|显示页码
 page_size|int|否|0|每页显示多少数据


## /v1/vdc_agent/control
终端操作
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 tenant|string|否|-| 租户uuid
 Agents|[]string|是|nil|所操作的终端ID
 control_type|int|否|0|代表操作的动作
 message_param|VDCAgentMessageControlData|否|nil|消息参数
 machine_control_param|VDCAgentMachineControlData|否|nil|设置参数
[back to filed page](field.md)

## /v1/vdc_agent/power_on
终端开机
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 tenant|string|否|-| 租户uuid
 Agents|[]string|是|nil|所操作的终端ID
 control_type|int|否|0|代表操作的动作
 message_param|VDCAgentMessageControlData|否|nil|消息参数
 machine_control_param|VDCAgentMachineControlData|否|nil|设置参数
[back to filed page](field.md)


## /v1/vdc_agent/update
终端设置
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 uuid|string|是|-|终端uuid
 description|string|否|-|终端描述
 object_group|string|否|-|终端分组
 bind_vm_uuid|map|否|-|终端绑定云桌面


## /v1/vdc_agent/delete
终端删除
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 uuid|string|是|-|终端uuid


## /v1/vdc_agent/overview
终端概览
### 请求类型
GET
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 tenant|string|是|-|租户uuid
 ####返回示例
 ```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "Info": {
      "CloudDesktop": {
        "CloudDesktop": {
          "Running": 7,
          "ShutOff": 13,
          "OtherState": 0,
          "Exclusive": 13,
          "Shared": 7
        },
        "CloudDesktopPool": {
          "Used": 1,
          "UnUsed": 12,
          "Exclusive": 9,
          "Shared": 4
        },
        "CloudTemplate": {
          "Used": 13,
          "UnUsed": 10
        }
      },
      "VDCAgent": {
        "Agents": {
          "FatClient": {
            "Total": 1,
            "Online": 0,
            "Offline": 1
          },
          "ThinClient": {
            "Total": 21,
            "Online": 1,
            "Offline": 20
          }
        },
        "VDCStrategies": {
          "IpStrategy": 0,
          "TimeStrategy": 0,
          "Bound": 0,
          "Unbound": 0
        },
        "PersonalizedStrategies": {
          "Total": 4,
          "Used": 2,
          "Unused": 2
        }
      },
      "ComputeManagementInfo": {
        "HostNum": 2,
        "CPU": 60,
        "CPUUsageRate": 5.51939680881364,
        "MemoryUsageRate": 27.06981458639198,
        "Memory": 147036270592,
        "HealthyNode": 2,
        "UnHealthyNode": 0
      },
      "StorageManagementInfo": {
        "InternalVolume": {
          "Total": 196,
          "Healthy": 196,
          "Disabled": 0,
          "Degraded": 0,
          "Verify": 0
        },
        "ExternalStorage": {
          "Total": 10,
          "Iscsi": 0,
          "NFS": 4,
          "smb": 4,
          "scsi": 1,
          "fc": 0,
          "fs": 0,
          "gcluster": 0,
          "RBD": 1
        }
      },
      "NetworkManagementInfo": {
        "L2Network": 4,
        "PortGroup": 6,
        "VPCEquipment": 25,
        "VPCNetwork": true
      }
    }
  }
}
```


## /v1/vdc_agent/DHCP/get
终端DHCP获取设置信息
### 请求类型
GET
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_uuid|string|是|-|主机uuid
host_name|string|是|-|主机名称

## /v1/vdc_agent/DHCP/enable
开启终端DHCP
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_uuid|string|是|-|主机uuid
listen_ip|string|是|-|监听ip
start_ip|string|是|-|起始ip
end_ip|string|是|-|结束ip
iface|string|是|-|网卡接口名称
lease_time|string|是|-|租期
lease_max|string|是|-|最大租期
gateway|string|是|-|网关
Netmask|string|是|-|子网掩码
dns|[]string|是|-|DNS

## /v1/vdc_agent/DHCP/alter
修改终端DHCP设置
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_uuid|string|是|-|主机uuid
listen_ip|string|是|-|监听ip
start_ip|string|是|-|起始ip
end_ip|string|是|-|结束ip
iface|string|是|-|网卡接口名称
lease_time|string|是|-|租期
lease_max|string|是|-|最大租期
gateway|string|是|-|网关
Netmask|string|是|-|子网掩码
dns|[]string|是|-|DNS

## /v1/vdc_agent/DHCP/disable
关闭终端DHCP
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_uuid|string|是|-|主机uuid
iface|string|是|-|网卡接口名称

## /v1/vdc_agent/PXE/activate
激活无盘终端
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 tenant|string|是|-|租户uuid
 uuid|string|是|-| uuid
 id|string|是|-| id
activate|bool|是|false|是否激活

            

## /v1/vdc_agent/PXE/add
添加无盘终端
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 tenant|string|是|-|租户uuid
 uuid|string|是|-| uuid
 id|string|是|-| id
 name|string|是|-| 无盘终端名称
 desc|string|否|-| 无盘终端描述
 owner|string|否|-| 所属用户
 mac_address|string|是|-|MAC地址
 ip|string|是|-|ip
 gate_way|string|是|-|网关
 os|string|是|-|系统信息
 vm_template|string|是|-|模板UUID
 zone|string|是|-|所属资源池UUID
activate|bool|是|false|是否激活
is_link|bool|是|false|是否链接克隆
filter_name|string|否|-|过滤名称
pxe_uuid|string|是|-|pxe服务器uuid
     
            

  ## /v1/vdc_agent/PXE/delete
  删除无盘终端
  ### 请求类型
  POST
  ### 请求参数
   名称 | 参数类型 | 是否必填 | 默认值 | 描述
  --- |---|---|--- |---
   cluster_uuid|string|是|-| 集群uuid
   tenant|string|是|-|租户uuid
   uuid|string|是|-| uuid
   id|string|是|-| id
       

  ## /v1/vdc_agent/PXE/get
  获取无盘终端
  ### 请求类型
  POST
  ### 请求参数
   名称 | 参数类型 | 是否必填 | 默认值 | 描述
  --- |---|---|--- |---
   cluster_uuid|string|是|-| 集群uuid
   tenant|string|是|-|租户uuid
   uuid|string|是|-| uuid
   id|string|是|-| id
 
 ## /v1/vdc_agent/PXE/edit
 编辑无盘终端
 ### 请求类型
 POST
 ### 请求参数
  名称 | 参数类型 | 是否必填 | 默认值 | 描述
 --- |---|---|--- |---
  cluster_uuid|string|是|-| 集群uuid
  tenant|string|是|-|租户uuid
  uuid|string|是|-| uuid
  id|string|是|-| id
  name|string|是|-| 无盘终端名称
  desc|string|否|-| 无盘终端描述
  owner|string|否|-| 所属用户
  mac_address|string|是|-|MAC地址
  ip|string|是|-|ip
  gate_way|string|是|-|网关
  os|string|是|-|系统信息
  vm_template|string|是|-|模板UUID
  zone|string|是|-|所属资源池UUID
 activate|bool|是|false|是否激活
 is_link|bool|是|false|是否链接克隆
 filter_name|string|否|-|过滤名称
 pxe_uuid|string|是|-|pxe服务器uuid

## /v1/vdc_agent/PXE/list
无盘终端列表
### 请求类型
POST
### 请求参数
名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-| 集群uuid
tenant|string|是|-|租户uuid
###返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "TotalCount": 2,
    "List": [
      {
        "UUID": "5a137b16-7d20-4b66-b5ec-d9a3b4ccd502",
        "ID": "",
        "Name": "vpc",
        "Desc": "vpc启动无盘",
        "NsUUID": "4a7f3010-ccef-48fd-99cb-edc7cc768d14",
        "Owner": "",
        "MACAddress": "52:56:ff:13:60:d4",
        "Ip": "10.30.15.62",
        "OS": "Windows 10 x64",
        "VolumeInfo": {
          "UUID": "7d30af1d-eb95-4f65-aa29-113ecca188ea",
          "Name": "vpc-vpc-win10-volume1-0",
          "Ctime": 1629698733,
          "Mtime": 1630039981,
          "NamespaceUUID": "4a7f3010-ccef-48fd-99cb-edc7cc768d14",
          "PoolUUID": "d072280e-c4d7-4d72-899a-295378572905",
          "status": 1,
          "capacity": 53687091200,
          "snapCap": 161061273600,
          "replicas": 1,
          "rw": null,
          "ro": null,
          "attr": {
            "5ffa226d-5251-4440-981c-be68aea825c4_VSD_PORT": "42701",
            "ChecksumData": "off",
            "ChecksumHeader": "off",
            "Client": "vpc",
            "ComponentSetShift": "0",
            "ComponentShift": "30",
            "DataType": "replica",
            "DelMode": "default",
            "DevType": "target",
            "DriveType": "HDD",
            "PRIOREPID": "0",
            "Repair": "off",
            "Safety": "first",
            "ScheduleOption": "intelligent",
            "StripeShift": "20",
            "TargetID": "1",
            "ThinProvision": "on",
            "ToMkfs": "true",
            "VReplicaStrategy": "prioRep",
            "VolumeName": "vpc-vpc-win10-volume1-0",
            "VsdVendor": "LIBTARGET",
            "Zone": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
            "ZoneName": "default",
            "replica": "1"
          },
          "sliceSize": 1073741824,
          "accessPath": {
            "5ffa226d-5251-4440-981c-be68aea825c4": "10.30.47.161:21204 iqn.2018-11.topsec.com.cn:7d30af1d-eb95-4f65-aa29-113ecca188eaid191680820"
          },
          "accounts": null,
          "quota": 0,
          "expand": false,
          "invalidAccessPath": null,
          "sharePoint": null,
          "userPerms": null,
          "userGroupPerms": null,
          "eventState": 0,
          "deleteTime": 0,
          "Label": null,
          "vsdState": null,
          "snapLength": 0,
          "snapLengthUpdateTime": 0,
          "StartPortMapping": false,
          "VDCPortMappingAddr": "",
          "cdp_usd_info": null,
          "Parent": "",
          "ParentSnapshot": "",
          "Children": null,
          "RestoreEtag": null,
          "CdpBpHistory": null,
          "BackupState": 0
        },
        "VmTemplate": "e8d7e40f-bd15-4760-ac30-db2f19f01a48",
        "AgentStatus": 2,
        "HostUuid": "d331295f-b997-4c5f-8c99-5601b60b525d",
        "GateWay": "10.30.15.1",
        "IsLink": false,
        "PxeUUID": "30a77730-197e-45a2-9412-f7f476595138",
        "CTime": 1629698748,
        "MTime": 1629698825,
        "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
        "cluster_name": "cluster_name_162",
        "tenant": "003a9df8-7cc8-45a5-b417-6b0673a5d8c8",
        "tenant_name": "xuu-tenant"
      },
      {
        "UUID": "7c418c89-6621-43cd-a460-08e505c04f4f",
        "ID": "",
        "Name": "无盘客户机-1",
        "Desc": "无盘客户机描述的0816",
        "NsUUID": "b44de1f7-c7bf-40cb-9d6e-9893422aa0a0",
        "Owner": "",
        "MACAddress": "52:56:ff:9e:45:fc",
        "Ip": "10.30.15.61",
        "OS": "Windows 7 x64",
        "VolumeInfo": {
          "UUID": "dd882b32-7587-4566-a77b-a65064308717",
          "Name": "无盘客户机-1-win7-0813-clone-0813165956-volume-1",
          "Ctime": 1629105504,
          "Mtime": 1630039980,
          "NamespaceUUID": "b44de1f7-c7bf-40cb-9d6e-9893422aa0a0",
          "PoolUUID": "60ef11e0-d273-4a50-b0f2-a223b0f327a0",
          "status": 1,
          "capacity": 85899345920,
          "snapCap": 257698037760,
          "replicas": 1,
          "rw": null,
          "ro": null,
          "attr": {
            "5ffa226d-5251-4440-981c-be68aea825c4_VSD_PORT": "42643",
            "ChecksumData": "off",
            "ChecksumHeader": "off",
            "Client": "无盘客户机-1",
            "ComponentSetShift": "0",
            "ComponentShift": "30",
            "DataType": "replica",
            "DelMode": "default",
            "DevType": "target",
            "DriveType": "HDD",
            "PRIOREPID": "0",
            "Repair": "off",
            "Safety": "first",
            "ScheduleOption": "intelligent",
            "StripeShift": "20",
            "TargetID": "1",
            "ThinProvision": "on",
            "ToMkfs": "true",
            "VReplicaStrategy": "prioRep",
            "VolumeName": "无盘客户机-1-win7-0813-clone-0813165956-volume-1",
            "VsdVendor": "LIBTARGET",
            "Zone": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
            "ZoneName": "default",
            "replica": "1"
          },
          "sliceSize": 1073741824,
          "accessPath": {
            "5ffa226d-5251-4440-981c-be68aea825c4": "10.30.47.161:20397 iqn.2018-11.topsec.com.cn:dd882b32-7587-4566-a77b-a65064308717id21253050"
          },
          "accounts": null,
          "quota": 0,
          "expand": false,
          "invalidAccessPath": null,
          "sharePoint": null,
          "userPerms": null,
          "userGroupPerms": null,
          "eventState": 0,
          "deleteTime": 0,
          "Label": null,
          "vsdState": null,
          "snapLength": 0,
          "snapLengthUpdateTime": 0,
          "StartPortMapping": false,
          "VDCPortMappingAddr": "",
          "cdp_usd_info": null,
          "Parent": "",
          "ParentSnapshot": "",
          "Children": null,
          "RestoreEtag": null,
          "CdpBpHistory": null,
          "BackupState": 0
        },
        "VmTemplate": "32d7cfa8-effc-4aa6-9eb4-71b60444627e",
        "AgentStatus": 2,
        "HostUuid": "d331295f-b997-4c5f-8c99-5601b60b525d",
        "GateWay": "10.30.15.1",
        "IsLink": false,
        "PxeUUID": "30a77730-197e-45a2-9412-f7f476595138",
        "CTime": 1629105504,
        "MTime": 1629105600,
        "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
        "cluster_name": "cluster_name_162",
        "tenant": "9a6463da-e194-43c1-898b-4918efe4c745",
        "tenant_name": "fish"
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
        "cluster_name": "cluster_name_162",
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 2
      }
    ]
  }
}
```
                                               