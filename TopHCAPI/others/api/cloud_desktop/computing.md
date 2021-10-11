[back to api overview](../api_overview.md)

###云桌面相关接口


## /v1/compute/desktop/pool/exclusive/create
###桌面池创建
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
zone_uuid|string|是|-|资源池uuid
zone_name|string|是|-|资源池名称
vm_template_uuid|string|是|-|云桌面模板uuid
vm_template_name|string|是|-|云桌面模板名称
vm_number|int|是|-|想要创建的云桌面数量
vm_name|string|是|-|云桌面名称前缀
type|string|是|-|云桌面类型
release_type|int|是|-|还原类型
private_disk|PrivateDiskInfo|否|-|个人磁盘
networks|Interface|否|-|个人网卡
group_path_name|string|是|-|云桌面分组名称
group_path | string|是|-|云桌面分组uuid
exclusive_desktop_name| string|是|-|云桌面池名称
clone_model| string|是|-|云桌面池克隆类型
associated_user_group|UserGroupData|否|-|关联用户组
associated_user | UserData | 否|-|关联用户
ad_server_config | ADDomainServerConfig| 否| - | ad域设置
page_num|int|否|0|第几页
page_size|int|否|0|每页数量


## /v1/compute/desktop/pool/exclusive/list
###桌面池列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
filter_name|string|否|-|过滤名称
group_path|string|否|-|过滤分组
page_num|int|否|0|第几页
page_size|int|否|0|每页数量
####返回示例
```
{
     "scode": 0,
     "desc": "",
     "message": "success",
     "message_cn": "成功",
     "stack": null,
     "data": {
       "total_count": 1,
       "list": [
         {
           "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
           "cluster_name": "cluster_name_162",
           "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
           "tenant_name": "csw",
           "namespace_uuid": "56ecb474-4415-40f5-8367-50e71acc0ac7",
           "create_time": 1629789387,
           "modify_time": 1629789387,
           "exclusive_desktop_uuid": "16b7fa66-e247-4bdb-b30c-83940898555e",
           "exclusive_desktop_name": "csw-win10",
           "zone_uuid": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
           "zone_name": "default",
           "group_path": "e3483db5-c2b2-47c5-b545-096bf9735b56",
           "group_path_name": "default",
           "type": "internal",
           "release_type": 2,
           "clone_model": "link",
           "action": 0,
           "vm_template_uuid": "25e65813-9240-4f6e-920a-83f783e5302b",
           "vm_template_Name": "csw-cgt",
           "vm_template_os": "Windows 10 x64",
           "vm_template_os_type": "windows",
           "private_disk": [],
           "networks": null,
           "vm_uuids": null,
           "associated_user": [
             {
               "user_name": "jy2",
               "user_uuid": "7118a14a-c6b4-43a5-b389-e246fd7725b2",
               "tenant_name": "csw",
               "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
             },
             {
               "user_name": "jy8",
               "user_uuid": "c6861a09-0e01-40df-b6c5-bd674aeea46e",
               "tenant_name": "csw",
               "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
             },
             {
               "user_name": "jy1",
               "user_uuid": "47da81e9-1e83-4ca0-bf11-c9649a10c827",
               "tenant_name": "csw",
               "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
             },
             {
               "user_name": "jy3",
               "user_uuid": "0604fe35-3167-4d46-80b5-3b3c8f1218db",
               "tenant_name": "csw",
               "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
             },
             {
               "user_name": "jy7",
               "user_uuid": "e03be416-16ac-4258-a175-02416dd1d213",
               "tenant_name": "csw",
               "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
             },
             {
               "user_name": "jy4",
               "user_uuid": "8b3abee4-a77a-49d0-8a2d-2b2acf5633bc",
               "tenant_name": "csw",
               "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
             },
             {
               "user_name": "jy5",
               "user_uuid": "c29b6b87-e6ed-4fe0-9da1-a41b2dc25d71",
               "tenant_name": "csw",
               "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
             },
             {
               "user_name": "jy10",
               "user_uuid": "7b561ef5-41f2-4d92-aab2-5276f3354eb5",
               "tenant_name": "csw",
               "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
             },
             {
               "user_name": "jy6",
               "user_uuid": "2ec14edb-d2c1-44a6-a1ae-7aa2af37be2a",
               "tenant_name": "csw",
               "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
             },
             {
               "user_name": "jy9",
               "user_uuid": "cb954d85-4a59-4842-8848-3c2323a161ba",
               "tenant_name": "csw",
               "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
             }
           ],
           "associated_user_group": [],
           "user_auto_assign_vm": false,
           "shutdown_restore_set": {
             "unassign_vm": null,
             "reset_vm": null,
             "restore_disk_index": null,
             "enabled": null
           },
           "ad_server_config": {
             "enable": false,
             "start_ip": "",
             "end_ip": "",
             "net_mask": "",
             "gate_way": "",
             "time_zone": "Asia/Shanghai",
             "ad_server_dns": "",
             "ad_server_name": "",
             "ad_server_administrator": "",
             "ad_server_administrator_password": ""
           },
           "resolution": "1920x1080",
           "image_compression": "glz",
           "video_compression": "h264",
           "shared_clipboard": true,
           "shared_directory": true,
           "usb_redirection": true,
           "smart_card_redirection": true,
           "drag_drop_files": true,
           "ban_input": true,
           "start_full_screen": true,
           "vm_name": "",
           "vm_names": null,
           "vm_number": 0,
           "cloud_init_data": null,
           "is_can_delete": false,
           "vm_total": 3,
           "user_used_total": 3,
           "total_count": 0,
           "vm_list": [
             {
               "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
               "cluster_name": "cluster_name_162",
               "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
               "tenant_name": "csw",
               "owner_is_ldap": false,
               "owner": "47da81e9-1e83-4ca0-bf11-c9649a10c827",
               "owner_name": "jy1",
               "uuid": "c31d1299-4eb4-4559-8b39-9d4ddcf8dcb2",
               "name": "视频重定向-0",
               "type": "GDT",
               "create_time": 1629789399,
               "modify_time": 1630046374,
               "deleted_time": 0,
               "state": "running",
               "ga_state": "disconnected",
               "action": "noaction",
               "os": "Windows 10 x64",
               "first_shown_ip": "",
               "vdc_agent": "",
               "vdc_agent_list": null,
               "vdc_pool_uuid": "16b7fa66-e247-4bdb-b30c-83940898555e",
               "vdc_pool_name": "csw-win10",
               "create_type": "",
               "namespace": "56ecb474-4415-40f5-8367-50e71acc0ac7",
               "machine_uuid": "5ffa226d-5251-4440-981c-be68aea825c4",
               "labels": null,
               "interface_ips": [],
               "attr": null,
               "object_group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
               "object_group_name": "default",
               "plan": "",
               "plan_name": "",
               "plan_master_cluster_uuid": "",
               "plan_master_cluster_name": "",
               "plan_slave_cluster_uuid": "",
               "plan_slave_cluster_name": "",
               "running_cluster": "",
               "zone": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
               "zone_name": "default",
               "strategy": "",
               "strategy_name": "",
               "recover_to_related_zones": 2,
               "master_zone_take_over": 2,
               "spice_port_mapping": true,
               "console_server_listen_port": 9800,
               "task_tag": 1,
               "clone_error_reason": "",
               "clone_error_reason_cn": "",
               "clone_error_scode": 0,
               "clone_error_stak": null,
               "clone_error_desc": ""
             },
             {
               "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
               "cluster_name": "cluster_name_162",
               "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
               "tenant_name": "csw",
               "owner_is_ldap": false,
               "owner": "7118a14a-c6b4-43a5-b389-e246fd7725b2",
               "owner_name": "jy2",
               "uuid": "3397643d-a0df-40f5-b62f-4f36cf116f4f",
               "name": "视频重定向-1",
               "type": "GDT",
               "create_time": 1629789417,
               "modify_time": 1630046374,
               "deleted_time": 0,
               "state": "running",
               "ga_state": "connected",
               "action": "noaction",
               "os": "Windows 10 x64",
               "first_shown_ip": "10.30.14.56",
               "vdc_agent": "",
               "vdc_agent_list": null,
               "vdc_pool_uuid": "16b7fa66-e247-4bdb-b30c-83940898555e",
               "vdc_pool_name": "csw-win10",
               "create_type": "",
               "namespace": "56ecb474-4415-40f5-8367-50e71acc0ac7",
               "machine_uuid": "5ffa226d-5251-4440-981c-be68aea825c4",
               "labels": null,
               "interface_ips": [
                 {
                   "addr_type": "ipv4",
                   "ip": "10.30.14.56",
                   "address": "10.30.14.56",
                   "family": "ipv4",
                   "prefix": 24,
                   "peer": "",
                   "name": "以太网"
                 }
               ],
               "attr": null,
               "object_group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
               "object_group_name": "default",
               "plan": "",
               "plan_name": "",
               "plan_master_cluster_uuid": "",
               "plan_master_cluster_name": "",
               "plan_slave_cluster_uuid": "",
               "plan_slave_cluster_name": "",
               "running_cluster": "",
               "zone": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
               "zone_name": "default",
               "strategy": "",
               "strategy_name": "",
               "recover_to_related_zones": 2,
               "master_zone_take_over": 2,
               "spice_port_mapping": true,
               "console_server_listen_port": 9800,
               "task_tag": 1,
               "clone_error_reason": "",
               "clone_error_reason_cn": "",
               "clone_error_scode": 0,
               "clone_error_stak": null,
               "clone_error_desc": ""
             },
             {
               "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
               "cluster_name": "cluster_name_162",
               "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
               "tenant_name": "csw",
               "owner_is_ldap": false,
               "owner": "0604fe35-3167-4d46-80b5-3b3c8f1218db",
               "owner_name": "jy3",
               "uuid": "66840f9d-d2d3-4781-8778-e83aa51b4c54",
               "name": "视频重定向-2",
               "type": "GDT",
               "create_time": 1629789437,
               "modify_time": 1630046374,
               "deleted_time": 0,
               "state": "running",
               "ga_state": "disconnected",
               "action": "noaction",
               "os": "Windows 10 x64",
               "first_shown_ip": "",
               "vdc_agent": "",
               "vdc_agent_list": null,
               "vdc_pool_uuid": "16b7fa66-e247-4bdb-b30c-83940898555e",
               "vdc_pool_name": "csw-win10",
               "create_type": "",
               "namespace": "56ecb474-4415-40f5-8367-50e71acc0ac7",
               "machine_uuid": "5ffa226d-5251-4440-981c-be68aea825c4",
               "labels": null,
               "interface_ips": [],
               "attr": null,
               "object_group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
               "object_group_name": "default",
               "plan": "",
               "plan_name": "",
               "plan_master_cluster_uuid": "",
               "plan_master_cluster_name": "",
               "plan_slave_cluster_uuid": "",
               "plan_slave_cluster_name": "",
               "running_cluster": "",
               "zone": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
               "zone_name": "default",
               "strategy": "",
               "strategy_name": "",
               "recover_to_related_zones": 2,
               "master_zone_take_over": 2,
               "spice_port_mapping": true,
               "console_server_listen_port": 9800,
               "task_tag": 1,
               "clone_error_reason": "",
               "clone_error_reason_cn": "",
               "clone_error_scode": 0,
               "clone_error_stak": null,
               "clone_error_desc": ""
             }
           ],
           "personalized_strategy": {
             "name": "",
             "uuid": "",
             "description": "",
             "associated_user": null,
             "associated_desktop_pool": null,
             "create_time": 0,
             "modify_time": 0,
             "style_template": 0,
             "show_vm_ip_address": null,
             "show_vm_mac_address": null,
             "show_vdi_account": null,
             "show_vm_time": null,
             "enable_screen_watermark": null,
             "watermark_move_time": null,
             "underline_type": "",
             "watermark_content": "",
             "show_style": "",
             "content_color": "",
             "border_color": "",
             "background_color": "",
             "font_size": null,
             "font_thickness": null,
             "border_width": null,
             "transparency": null,
             "border_transparency": null,
             "lean": "",
             "watermark_coordinate_x": null,
             "watermark_coordinate_y": null,
             "allow_pc_clipboard": null,
             "pc_clipboard_mode": "",
             "allow_usb_memory": null,
             "usb_memory_mode": "",
             "allow_usb_printer": null,
             "usb_smart_card": null,
             "allow_usb_redirect": null,
             "drag_drop_files": null,
             "hide_navigation_bar": null,
             "shutdown_integration": null,
             "show_cloud_desktop": null,
             "show_cloud_server": null,
             "show_cloud_storage": null,
             "enable_auto_open_vm": null,
             "auto_login_time": null
           }
         }
       ],
       "each_range_list_state": [
         {
           "result": {
             "scode": 0,
             "desc": "",
             "message": "success",
             "message_cn": "成功",
             "stack": null,
             "data": ""
           },
           "total_count": 1
         },
         {
           "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
           "cluster_name": "cluster_name_162",
           "namespace_uuid": "56ecb474-4415-40f5-8367-50e71acc0ac7",
           "result": {
             "scode": 0,
             "desc": "",
             "message": "success",
             "message_cn": "成功",
             "stack": null,
             "data": ""
           },
           "total_count": 1
         }
       ]
     }
   }
```


## /v1/compute/desktop/pool/associated_user/List
###桌面池关联用户
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
exclusive_desktop_uuid|string|是|-|桌面池uuid
exclusive_desktop_name|string|是|-|桌面池名称
####返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "user_list": {
      "0604fe35-3167-4d46-80b5-3b3c8f1218db": "d590db81-e83c-4c5b-af59-abb30e0900b6",
      "2ec14edb-d2c1-44a6-a1ae-7aa2af37be2a": "d590db81-e83c-4c5b-af59-abb30e0900b6",
      "47da81e9-1e83-4ca0-bf11-c9649a10c827": "d590db81-e83c-4c5b-af59-abb30e0900b6",
      "7118a14a-c6b4-43a5-b389-e246fd7725b2": "d590db81-e83c-4c5b-af59-abb30e0900b6",
      "7b561ef5-41f2-4d92-aab2-5276f3354eb5": "d590db81-e83c-4c5b-af59-abb30e0900b6",
      "8b3abee4-a77a-49d0-8a2d-2b2acf5633bc": "d590db81-e83c-4c5b-af59-abb30e0900b6",
      "c29b6b87-e6ed-4fe0-9da1-a41b2dc25d71": "d590db81-e83c-4c5b-af59-abb30e0900b6",
      "c6861a09-0e01-40df-b6c5-bd674aeea46e": "d590db81-e83c-4c5b-af59-abb30e0900b6",
      "cb954d85-4a59-4842-8848-3c2323a161ba": "d590db81-e83c-4c5b-af59-abb30e0900b6",
      "e03be416-16ac-4258-a175-02416dd1d213": "d590db81-e83c-4c5b-af59-abb30e0900b6"
    }
  }
}
```


## /v1/compute/desktop/pool/exclusive/inspect
###桌面池详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
exclusive_desktop_uuid|string|是|-|桌面池uuid
####返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
    "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
    "namespace_uuid": "56ecb474-4415-40f5-8367-50e71acc0ac7",
    "create_time": 1629789387,
    "modify_time": 1629789387,
    "exclusive_desktop_uuid": "16b7fa66-e247-4bdb-b30c-83940898555e",
    "exclusive_desktop_name": "csw-win10",
    "zone_uuid": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
    "zone_name": "default",
    "group_path": "e3483db5-c2b2-47c5-b545-096bf9735b56",
    "group_path_name": "default",
    "type": "internal",
    "release_type": 2,
    "clone_model": "link",
    "action": 0,
    "vm_template_uuid": "25e65813-9240-4f6e-920a-83f783e5302b",
    "vm_template_Name": "csw-cgt",
    "vm_template_os": "Windows 10 x64",
    "vm_template_os_type": "windows",
    "private_disk": [],
    "networks": null,
    "vm_uuids": null,
    "associated_user": [
      {
        "user_name": "jy2",
        "user_uuid": "7118a14a-c6b4-43a5-b389-e246fd7725b2",
        "tenant_name": "csw",
        "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
      },
      {
        "user_name": "jy8",
        "user_uuid": "c6861a09-0e01-40df-b6c5-bd674aeea46e",
        "tenant_name": "csw",
        "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
      },
      {
        "user_name": "jy1",
        "user_uuid": "47da81e9-1e83-4ca0-bf11-c9649a10c827",
        "tenant_name": "csw",
        "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
      },
      {
        "user_name": "jy3",
        "user_uuid": "0604fe35-3167-4d46-80b5-3b3c8f1218db",
        "tenant_name": "csw",
        "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
      },
      {
        "user_name": "jy7",
        "user_uuid": "e03be416-16ac-4258-a175-02416dd1d213",
        "tenant_name": "csw",
        "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
      },
      {
        "user_name": "jy4",
        "user_uuid": "8b3abee4-a77a-49d0-8a2d-2b2acf5633bc",
        "tenant_name": "csw",
        "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
      },
      {
        "user_name": "jy5",
        "user_uuid": "c29b6b87-e6ed-4fe0-9da1-a41b2dc25d71",
        "tenant_name": "csw",
        "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
      },
      {
        "user_name": "jy10",
        "user_uuid": "7b561ef5-41f2-4d92-aab2-5276f3354eb5",
        "tenant_name": "csw",
        "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
      },
      {
        "user_name": "jy6",
        "user_uuid": "2ec14edb-d2c1-44a6-a1ae-7aa2af37be2a",
        "tenant_name": "csw",
        "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
      },
      {
        "user_name": "jy9",
        "user_uuid": "cb954d85-4a59-4842-8848-3c2323a161ba",
        "tenant_name": "csw",
        "tenant_uuid": "d590db81-e83c-4c5b-af59-abb30e0900b6"
      }
    ],
    "associated_user_group": [],
    "user_auto_assign_vm": false,
    "shutdown_restore_set": {
      "unassign_vm": null,
      "reset_vm": null,
      "restore_disk_index": null,
      "enabled": null
    },
    "ad_server_config": {
      "enable": false,
      "start_ip": "",
      "end_ip": "",
      "net_mask": "",
      "gate_way": "",
      "time_zone": "Asia/Shanghai",
      "ad_server_dns": "",
      "ad_server_name": "",
      "ad_server_administrator": "",
      "ad_server_administrator_password": ""
    },
    "resolution": "1920x1080",
    "image_compression": "glz",
    "video_compression": "h264",
    "shared_clipboard": true,
    "shared_directory": true,
    "usb_redirection": true,
    "smart_card_redirection": true,
    "drag_drop_files": true,
    "ban_input": true,
    "start_full_screen": true,
    "vm_name": "",
    "vm_names": null,
    "vm_number": 0,
    "cloud_init_data": null,
    "is_can_delete": false,
    "vm_total": 3,
    "user_used_total": 3,
    "total_count": 3,
    "vm_list": [
      {
        "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
        "cluster_name": "cluster_name_162",
        "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
        "tenant_name": "csw",
        "owner_is_ldap": false,
        "owner": "47da81e9-1e83-4ca0-bf11-c9649a10c827",
        "owner_name": "jy1",
        "uuid": "c31d1299-4eb4-4559-8b39-9d4ddcf8dcb2",
        "name": "视频重定向-0",
        "type": "GDT",
        "create_time": 1629789399,
        "modify_time": 1630046493,
        "deleted_time": 0,
        "state": "running",
        "ga_state": "disconnected",
        "action": "noaction",
        "os": "Windows 10 x64",
        "first_shown_ip": "",
        "vdc_agent": "",
        "vdc_agent_list": null,
        "vdc_pool_uuid": "16b7fa66-e247-4bdb-b30c-83940898555e",
        "vdc_pool_name": "csw-win10",
        "create_type": "",
        "namespace": "56ecb474-4415-40f5-8367-50e71acc0ac7",
        "machine_uuid": "5ffa226d-5251-4440-981c-be68aea825c4",
        "labels": null,
        "interface_ips": [],
        "attr": null,
        "object_group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
        "object_group_name": "default",
        "plan": "",
        "plan_name": "",
        "plan_master_cluster_uuid": "",
        "plan_master_cluster_name": "",
        "plan_slave_cluster_uuid": "",
        "plan_slave_cluster_name": "",
        "running_cluster": "",
        "zone": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
        "zone_name": "default",
        "strategy": "",
        "strategy_name": "",
        "recover_to_related_zones": 2,
        "master_zone_take_over": 2,
        "spice_port_mapping": true,
        "console_server_listen_port": 9800,
        "task_tag": 1,
        "clone_error_reason": "",
        "clone_error_reason_cn": "",
        "clone_error_scode": 0,
        "clone_error_stak": null,
        "clone_error_desc": ""
      },
      {
        "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
        "cluster_name": "cluster_name_162",
        "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
        "tenant_name": "csw",
        "owner_is_ldap": false,
        "owner": "7118a14a-c6b4-43a5-b389-e246fd7725b2",
        "owner_name": "jy2",
        "uuid": "3397643d-a0df-40f5-b62f-4f36cf116f4f",
        "name": "视频重定向-1",
        "type": "GDT",
        "create_time": 1629789417,
        "modify_time": 1630046493,
        "deleted_time": 0,
        "state": "running",
        "ga_state": "connected",
        "action": "noaction",
        "os": "Windows 10 x64",
        "first_shown_ip": "10.30.14.56",
        "vdc_agent": "",
        "vdc_agent_list": null,
        "vdc_pool_uuid": "16b7fa66-e247-4bdb-b30c-83940898555e",
        "vdc_pool_name": "csw-win10",
        "create_type": "",
        "namespace": "56ecb474-4415-40f5-8367-50e71acc0ac7",
        "machine_uuid": "5ffa226d-5251-4440-981c-be68aea825c4",
        "labels": null,
        "interface_ips": [
          {
            "addr_type": "ipv4",
            "ip": "10.30.14.56",
            "address": "10.30.14.56",
            "family": "ipv4",
            "prefix": 24,
            "peer": "",
            "name": "以太网"
          }
        ],
        "attr": null,
        "object_group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
        "object_group_name": "default",
        "plan": "",
        "plan_name": "",
        "plan_master_cluster_uuid": "",
        "plan_master_cluster_name": "",
        "plan_slave_cluster_uuid": "",
        "plan_slave_cluster_name": "",
        "running_cluster": "",
        "zone": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
        "zone_name": "default",
        "strategy": "",
        "strategy_name": "",
        "recover_to_related_zones": 2,
        "master_zone_take_over": 2,
        "spice_port_mapping": true,
        "console_server_listen_port": 9800,
        "task_tag": 1,
        "clone_error_reason": "",
        "clone_error_reason_cn": "",
        "clone_error_scode": 0,
        "clone_error_stak": null,
        "clone_error_desc": ""
      },
      {
        "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
        "cluster_name": "cluster_name_162",
        "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
        "tenant_name": "csw",
        "owner_is_ldap": false,
        "owner": "0604fe35-3167-4d46-80b5-3b3c8f1218db",
        "owner_name": "jy3",
        "uuid": "66840f9d-d2d3-4781-8778-e83aa51b4c54",
        "name": "视频重定向-2",
        "type": "GDT",
        "create_time": 1629789437,
        "modify_time": 1630046493,
        "deleted_time": 0,
        "state": "running",
        "ga_state": "disconnected",
        "action": "noaction",
        "os": "Windows 10 x64",
        "first_shown_ip": "",
        "vdc_agent": "",
        "vdc_agent_list": null,
        "vdc_pool_uuid": "16b7fa66-e247-4bdb-b30c-83940898555e",
        "vdc_pool_name": "csw-win10",
        "create_type": "",
        "namespace": "56ecb474-4415-40f5-8367-50e71acc0ac7",
        "machine_uuid": "5ffa226d-5251-4440-981c-be68aea825c4",
        "labels": null,
        "interface_ips": [],
        "attr": null,
        "object_group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
        "object_group_name": "default",
        "plan": "",
        "plan_name": "",
        "plan_master_cluster_uuid": "",
        "plan_master_cluster_name": "",
        "plan_slave_cluster_uuid": "",
        "plan_slave_cluster_name": "",
        "running_cluster": "",
        "zone": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
        "zone_name": "default",
        "strategy": "",
        "strategy_name": "",
        "recover_to_related_zones": 2,
        "master_zone_take_over": 2,
        "spice_port_mapping": true,
        "console_server_listen_port": 9800,
        "task_tag": 1,
        "clone_error_reason": "",
        "clone_error_reason_cn": "",
        "clone_error_scode": 0,
        "clone_error_stak": null,
        "clone_error_desc": ""
      }
    ],
    "personalized_strategy": {
      "name": "",
      "uuid": "",
      "description": "",
      "associated_user": null,
      "associated_desktop_pool": null,
      "create_time": 0,
      "modify_time": 0,
      "style_template": 0,
      "show_vm_ip_address": null,
      "show_vm_mac_address": null,
      "show_vdi_account": null,
      "show_vm_time": null,
      "enable_screen_watermark": null,
      "watermark_move_time": null,
      "underline_type": "",
      "watermark_content": "",
      "show_style": "",
      "content_color": "",
      "border_color": "",
      "background_color": "",
      "font_size": null,
      "font_thickness": null,
      "border_width": null,
      "transparency": null,
      "border_transparency": null,
      "lean": "",
      "watermark_coordinate_x": null,
      "watermark_coordinate_y": null,
      "allow_pc_clipboard": null,
      "pc_clipboard_mode": "",
      "allow_usb_memory": null,
      "usb_memory_mode": "",
      "allow_usb_printer": null,
      "usb_smart_card": null,
      "allow_usb_redirect": null,
      "drag_drop_files": null,
      "hide_navigation_bar": null,
      "shutdown_integration": null,
      "show_cloud_desktop": null,
      "show_cloud_server": null,
      "show_cloud_storage": null,
      "enable_auto_open_vm": null,
      "auto_login_time": null
    }
  }
}
```


## /v1/compute/desktop/pool/exclusive/vm_uesr_info/inspect
###桌面池分配信息
### 请求类型
GET

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
exclusive_desktop_uuid|string|是|-|桌面池uuid
filter_user_name|string|否|-|过滤用户名称
filter_user_uuid|string|否|-|过滤用户名称uuid
filter_compute_name|string|否|-|过滤云桌面名称
####返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "total_count": 3,
    "user_vm_info": [
      {
        "user_name": "jy1",
        "user_uuid": "47da81e9-1e83-4ca0-bf11-c9649a10c827",
        "vm_name_list": [
          {
            "vm_name": "视频重定向-0",
            "vm_uuid": "c31d1299-4eb4-4559-8b39-9d4ddcf8dcb2"
          }
        ]
      },
      {
        "user_name": "jy2",
        "user_uuid": "7118a14a-c6b4-43a5-b389-e246fd7725b2",
        "vm_name_list": [
          {
            "vm_name": "视频重定向-1",
            "vm_uuid": "3397643d-a0df-40f5-b62f-4f36cf116f4f"
          }
        ]
      },
      {
        "user_name": "jy3",
        "user_uuid": "0604fe35-3167-4d46-80b5-3b3c8f1218db",
        "vm_name_list": [
          {
            "vm_name": "视频重定向-2",
            "vm_uuid": "66840f9d-d2d3-4781-8778-e83aa51b4c54"
          }
        ]
      }
    ]
  }
}
```





## /v1/compute/desktop/pool/exclusive/delete
###桌面池删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
exclusive_desktop_uuid|string|是|-|桌面池uuid



## /v1/compute/desktop/pool/exclusive/modify
###桌面池修改
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
zone_uuid|string|是|-|资源池uuid
zone_name|string|是|-|资源池名称
vm_template_uuid|string|是|-|云桌面模板uuid
vm_template_name|string|是|-|云桌面模板名称
vm_number|int|是|-|想要创建的云桌面数量
vm_name|string|是|-|云桌面名称前缀
type|string|是|-|云桌面类型
release_type|int|是|-|还原类型
private_disk|PrivateDiskInfo|否|-|个人磁盘
networks|Interface|否|-|个人网卡
group_path_name|string|是|-|云桌面分组名称
group_path | string|是|-|云桌面分组uuid
exclusive_desktop_name| string|是|-|云桌面池名称
clone_model| string|是|-|云桌面池克隆类型
associated_user_group|UserGroupData|否|-|关联用户组
associated_user | UserData | 否|-|关联用户
ad_server_config | ADDomainServerConfig| 否| - | ad域设置
page_num|int|否|0|第几页
page_size|int|否|0|每页数量



## /v1/compute/desktop/pool/exclusive/add/vm
###桌面池添加云桌面
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
vm_number|int|是|-|想要创建的云桌面数量
vm_name|string|是|-|云桌面名称前缀
exclusive_desktop_uuid| string|是|-|云桌面池uuid
exclusive_desktop_name| string|是|-|云桌面池名称



## /v1/compute/desktop/pool/exclusive/delete/vm
###桌面池批量删除云桌面
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
exclusive_desktop_uuid| string|是|-|云桌面池uuid
exclusive_desktop_name| string|是|-|云桌面池名称
is_delete_volumes|bool|否|false|是否同步删除卷
real_delete|bool|否|false|是否彻底删除
vms|ComputeIdentifier|是|-|要删除的云桌面信息



## /v1/compute/desktop/pool/exclusive/vm/restore
###桌面池云桌面恢复
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
exclusive_desktop_uuid| string|是|-|云桌面池uuid
exclusive_desktop_name| string|是|-|云桌面池名称
vms|ComputeIdentifier|是|-|要删除的云桌面信息
restore_disk_index|[]int32|是|-|删除磁盘的索引
unassign_vm|bool|否|false|云桌面取消分配
reset_vm|bool|否|false|云桌面重置
desktop_pool_all_vm|bool|否|false|是否对全部云桌面生效



## /v1/compute/desktop/pool/exclusive/vm/cancel_assign/user
###桌面池云桌面终端取消分配
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
agent_client_id|string|是|-|终端uuid



## /v1/compute/desktop/pool/exclusive/disk/update
###桌面池云桌面修改磁盘
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
compute_uuid|string|是|-|云桌面uuid
compute_name|string|是|-|云桌面名称
old_disk|Disk|是|-|要修改的磁盘
new_disk|Disk|是|-|替换的磁盘
exclusive_desktop_uuid| string|是|-|云桌面池uuid



###云桌面模板相关接口

## /v1/compute/desktop/pool/vm/template/create
###桌面池云桌面创建模板
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
component_cache|bool|是|false|是否开启内存快照
compute_image_name|string|是|-|模板名称
compute_uuid|string|是|-|云桌面uuid

## /v1/compute/desktop/pool/vm/template/delete
###桌面池云桌面删除模板
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
compute_image_uuid|string|是|-|模板uuid
compute_image_name|string|是|-|模板名称
is_delete_volumes|bool|是|false|是否同步删除存储卷

## /v1/compute/desktop/pool/vm/template/modify
###桌面池云桌面更新模板
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
component_cache|bool|是|false|是否开启内存快照
compute_image_name|string|是|-|模板名称
compute_uuid|string|是|-|云桌面uuid

## /v1/compute/desktop/pool/vm/template/list
###桌面池云桌面更新模板
### 请求类型
GET
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
filter_name|string|否|-|过滤名称
filter_zone_uuid|string|否|-|过滤资源池
page_num|int|否|0|第几页
page_size|int|否|0|每页数量
####返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "total_count": 2,
    "list": [
      {
        "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
        "tenant_name": "csw",
        "namespace": "",
        "name": "ppp",
        "uuid": "8141830b-d87c-4a9b-9a4e-75e684fdc7de",
        "virtual_machine_uuid": "",
        "cpu_max_count": 4,
        "cpu_nr_count": "2",
        "mem_max_number": 274877906944,
        "mem_nr_number": 4294967296,
        "creat_time": 0,
        "os": "Windows 10 x64",
        "zone": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
        "zone_name": "",
        "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
        "cluster_name": "cluster_name_162",
        "vm_template_type": "",
        "component_cache": false,
        "create_time": 1629881866,
        "modify_time": 1629881866,
        "template_update_last_finish_time": 0,
        "template_update_last_result": 0,
        "is_can_delete": true,
        "desktop_pool_uuid": "",
        "desktop_pool_name": ""
      },
      {
        "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
        "tenant_name": "csw",
        "namespace": "",
        "name": "csw-cgt",
        "uuid": "25e65813-9240-4f6e-920a-83f783e5302b",
        "virtual_machine_uuid": "",
        "cpu_max_count": 4,
        "cpu_nr_count": "2",
        "mem_max_number": 274877906944,
        "mem_nr_number": 4294967296,
        "creat_time": 0,
        "os": "Windows 10 x64",
        "zone": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
        "zone_name": "",
        "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
        "cluster_name": "cluster_name_162",
        "vm_template_type": "",
        "component_cache": true,
        "create_time": 1629789338,
        "modify_time": 1629789338,
        "template_update_last_finish_time": 0,
        "template_update_last_result": 0,
        "is_can_delete": false,
        "desktop_pool_uuid": "16b7fa66-e247-4bdb-b30c-83940898555e",
        "desktop_pool_name": "csw-win10"
      }
    ],
    "each_range_list_state": [
      {
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 1
      },
      {
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 1
      },
      {
        "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
        "cluster_name": "cluster_name_162",
        "namespace_uuid": "56ecb474-4415-40f5-8367-50e71acc0ac7",
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

## /v1/compute/desktop/pool/vm/template/inspect
###桌面池云桌面更新模板
### 请求类型
GET
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
compute_image_uuid|string|是|-|模板uuid
####返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
    "tenant_name": "csw",
    "owner_is_ldap": false,
    "owner": "",
    "owner_name": "",
    "uuid": "8141830b-d87c-4a9b-9a4e-75e684fdc7de",
    "name": "ppp",
    "type": "GDT",
    "deleted_time": 0,
    "state": "shutoff",
    "ga_state": "disconnected",
    "action": "noaction",
    "os": "Windows 10 x64",
    "first_shown_ip": "",
    "vdc_agent": "",
    "vdc_agent_list": null,
    "vdc_pool_uuid": "",
    "vdc_pool_name": "",
    "create_type": "",
    "namespace": "56ecb474-4415-40f5-8367-50e71acc0ac7",
    "machine_uuid": "",
    "labels": null,
    "interface_ips": [],
    "attr": null,
    "object_group": "",
    "object_group_name": "",
    "plan": "",
    "plan_name": "",
    "plan_master_cluster_uuid": "",
    "plan_master_cluster_name": "",
    "plan_slave_cluster_uuid": "",
    "plan_slave_cluster_name": "",
    "running_cluster": "",
    "zone": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
    "zone_name": "default",
    "strategy": "",
    "strategy_name": "",
    "spice_port_mapping": false,
    "console_server_listen_port": 0,
    "task_tag": 0,
    "mem_size": 4294967296,
    "mem_max": 274877906944,
    "memory_huge_pages_enable": false,
    "memory_qos": {
      "hard_limit": 0,
      "soft_limit": 0,
      "swap_hard_limit": 0,
      "min_guarantee": 0
    },
    "compute_name": "",
    "ha_mode": "on",
    "os_loader_path": "BIOS",
    "video": [
      {
        "model_type": "qxl",
        "heads": 1,
        "ram_size": 0,
        "vga_mem": 0
      }
    ],
    "startup_setting": {
      "hosts": null,
      "labels": null
    },
    "vnc_enable": false,
    "mem_sec_enabled": false,
    "ha_config": {
      "priority": 0
    },
    "parent_uuid": "25e65813-9240-4f6e-920a-83f783e5302b",
    "migrate_dest": "",
    "baseline": "Skylake-Server-IBRS",
    "device_name": "",
    "import_machine": "",
    "exceed_cluster_baseline": false,
    "cpu_current": "2",
    "cpu_max_count": 4,
    "cpu_nr_count": 0,
    "cpu_sockets": 1,
    "cpu_socket_cores": 4,
    "vnc_port": 0,
    "vnc_password": "",
    "streaming_mode": "filter",
    "compression_mode": "glz",
    "spice_port": 5927,
    "spice_password": "9f6c9983cb72938f8b5c950e10a40884",
    "panic": "on",
    "interfaces": [
      {
        "interface_model_type": "virtio",
        "interface_type": "compute",
        "mac_address": "0",
        "target_dev": "",
        "port_group": "a3324ded-1cce-403a-a668-46210a8cada8",
        "port_group_name": "VOI测试VLAN14",
        "vlan_tag_ids": [
          14
        ],
        "driver": null,
        "vhost_queue": 0,
        "name": ""
      }
    ],
    "cdrom": {},
    "floppy": {},
    "disks": [
      {
        "disk_target_device": "sda",
        "disk_target_bus": "sata",
        "disk_vsd_source": {
          "volume_uuid": "c18ad35f-874d-4d66-92ad-bf35a5570d99",
          "volume_name": "csw-win10-cgt-clone-0824151520-volume-1",
          "disk_capacity": 42949672960,
          "pool_uuid": "0c9f4554-7bc1-4c76-8304-dbe6da79a49e",
          "pool_name": "csw-VDI",
          "replica": "1",
          "drive_type": "HDD",
          "redundancy": 1,
          "attribute": null,
          "vsd_vendor": "LIBTARGET"
        },
        "disk_cache_mode": "none",
        "backing_store": {
          "index": 0,
          "format": null,
          "source": null,
          "backing_store": null
        },
        "disk_is_system": false
      }
    ],
    "device_order": [
      "sda",
      "hdd",
      "fda"
    ],
    "disk_type": [
      {
        "type": 3,
        "value": "sda"
      },
      {
        "type": 1,
        "value": "hdd"
      },
      {
        "type": 2,
        "value": "fda"
      }
    ],
    "usbs": [
      {
        "bus": 2,
        "port": "4",
        "product_id": "",
        "product_name": "控制台USB重定向接口",
        "vendor_id": "",
        "vendor_name": "",
        "source_type": "spice_vmc"
      }
    ],
    "is_external_disk": false,
    "has_passthrough_disk": false,
    "kvm_clock_enable": true,
    "virt_nested_enable": false,
    "cpu_reserve_enable": false,
    "cpu_reserve_numa": false,
    "memory_reserve_enable": false,
    "expand_config": {
      "cpu_auto_expand_enable": false,
      "memory_auto_expand_enable": false,
      "max_expand_cpu": 0,
      "max_expand_mem": 0,
      "expand_cpu": 0,
      "expand_mem": 0
    },
    "data_localization_mode_on": "off",
    "pci_devices": null,
    "mdev_devices": null,
    "tpm_devices": null,
    "recover_to_related_zones": 2,
    "master_zone_take_over": 2,
    "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
    "cluster_name": "cluster_name_162",
    "vm_template_type": "",
    "component_cache": false,
    "create_time": 0,
    "modify_time": 0,
    "template_update_last_finish_time": 0,
    "template_update_last_result": 0,
    "template_sync_status": 0,
    "vm_inspect": {
      "tenant": "d590db81-e83c-4c5b-af59-abb30e0900b6",
      "tenant_name": "csw",
      "owner_is_ldap": false,
      "owner": "",
      "owner_name": "",
      "uuid": "cbb3dfc2-3299-46bf-8e00-dc59317d7890",
      "name": "hidden_vm_ppp",
      "type": "GDT",
      "create_time": 1629881865,
      "modify_time": 1629881876,
      "deleted_time": 0,
      "state": "shutoff",
      "ga_state": "disconnected",
      "action": "noaction",
      "os": "Windows 10 x64",
      "first_shown_ip": "",
      "vdc_agent": "",
      "vdc_agent_list": null,
      "vdc_pool_uuid": "",
      "vdc_pool_name": "",
      "create_type": "",
      "namespace": "56ecb474-4415-40f5-8367-50e71acc0ac7",
      "machine_uuid": "",
      "labels": null,
      "interface_ips": [
        {
          "addr_type": "",
          "ip": "",
          "address": "",
          "family": "",
          "prefix": 0,
          "peer": "",
          "name": ""
        }
      ],
      "attr": null,
      "object_group": "e3483db5-c2b2-47c5-b545-096bf9735b56",
      "object_group_name": "default",
      "plan": "",
      "plan_name": "",
      "plan_master_cluster_uuid": "",
      "plan_master_cluster_name": "",
      "plan_slave_cluster_uuid": "",
      "plan_slave_cluster_name": "",
      "running_cluster": "",
      "zone": "63c7e502-9f7a-44fc-b77b-3c1930c39442",
      "zone_name": "default",
      "strategy": "",
      "strategy_name": "",
      "spice_port_mapping": false,
      "console_server_listen_port": 0,
      "task_tag": 1,
      "mem_size": 4294967296,
      "mem_max": 274877906944,
      "memory_huge_pages_enable": false,
      "memory_qos": {
        "hard_limit": 0,
        "soft_limit": 0,
        "swap_hard_limit": 0,
        "min_guarantee": 0
      },
      "compute_name": "",
      "ha_mode": "on",
      "os_loader_path": "BIOS",
      "video": [
        {
          "model_type": "qxl",
          "heads": 1,
          "ram_size": 131072,
          "vga_mem": 32768
        }
      ],
      "startup_setting": {
        "hosts": null,
        "labels": null
      },
      "vnc_enable": false,
      "mem_sec_enabled": false,
      "ha_config": {
        "priority": 0
      },
      "parent_uuid": "8141830b-d87c-4a9b-9a4e-75e684fdc7de",
      "migrate_dest": "",
      "baseline": "Skylake-Server-IBRS",
      "device_name": "",
      "import_machine": "",
      "exceed_cluster_baseline": false,
      "cpu_current": "2",
      "cpu_max_count": 4,
      "cpu_nr_count": 0,
      "cpu_sockets": 1,
      "cpu_socket_cores": 4,
      "vnc_port": 0,
      "vnc_password": "",
      "streaming_mode": "filter",
      "compression_mode": "glz",
      "spice_port": 0,
      "spice_password": "6564b156430e51b0168d37ae56822d93",
      "panic": "on",
      "interfaces": [
        {
          "interface_id": "fa6d9ff7-b561-4a69-a829-ae5145201a58",
          "interface_model_type": "virtio",
          "interface_type": "compute",
          "mac_address": "52:56:ff:b1:da:1e",
          "ips": [
            {
              "addr_type": "",
              "ip": "",
              "address": "",
              "family": "",
              "prefix": 0,
              "peer": "",
              "name": ""
            }
          ],
          "target_dev": "",
          "port_group": "a3324ded-1cce-403a-a668-46210a8cada8",
          "port_group_name": "VOI测试VLAN14",
          "vlan_tag_ids": [
            14
          ],
          "driver": null,
          "vhost_queue": 0,
          "name": ""
        }
      ],
      "cdrom": {},
      "floppy": {},
      "disks": [
        {
          "disk_target_device": "sda",
          "disk_target_bus": "sata",
          "disk_vsd_source": {
            "volume_uuid": "da01bdbd-fc80-4e32-a109-ba627246eb4a",
            "volume_name": "hidden_vm_ppp-volume-1",
            "disk_capacity": 42949672960,
            "pool_uuid": "0c9f4554-7bc1-4c76-8304-dbe6da79a49e",
            "pool_name": "csw-VDI",
            "replica": "1",
            "drive_type": "HDD",
            "redundancy": 0,
            "attribute": null,
            "vsd_vendor": "LIBTARGET"
          },
          "backing_store": {
            "index": 0,
            "format": null,
            "source": null,
            "backing_store": null
          },
          "disk_is_system": false
        }
      ],
      "device_order": [
        "sda",
        "hdd",
        "fda"
      ],
      "disk_type": [
        {
          "type": 3,
          "value": "sda"
        },
        {
          "type": 1,
          "value": "hdd"
        },
        {
          "type": 2,
          "value": "fda"
        }
      ],
      "usbs": [
        {
          "bus": 2,
          "port": "4",
          "product_id": "",
          "product_name": "控制台USB重定向接口",
          "vendor_id": "",
          "vendor_name": "",
          "source_type": "spice_vmc"
        }
      ],
      "is_external_disk": false,
      "has_passthrough_disk": false,
      "kvm_clock_enable": true,
      "virt_nested_enable": false,
      "cpu_reserve_enable": false,
      "cpu_reserve_numa": false,
      "memory_reserve_enable": false,
      "expand_config": {
        "cpu_auto_expand_enable": false,
        "memory_auto_expand_enable": false,
        "max_expand_cpu": 0,
        "max_expand_mem": 0,
        "expand_cpu": 0,
        "expand_mem": 0
      },
      "data_localization_mode_on": "",
      "pci_devices": null,
      "mdev_devices": null,
      "tpm_devices": null,
      "recover_to_related_zones": 2,
      "master_zone_take_over": 2
    },
    "is_can_update": false
  }
}
```

## /v1/compute/desktop/pool/vm/template/sync
###桌面池云桌面更新模板
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
compute_image_uuid|string|是|-|模板uuid


## /v1/compute/desktop/pool/vm/template/sync/init
###桌面池云桌面更新模板
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
compute_image_uuid|string|是|-|模板uuid









##云桌面个性化设置相关接口

## /v1/compute/desktop/personalized_strategy/add
###桌面池云桌面添加个性化设置
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
allow_pc_clipboard|bool|否|false|允许剪贴板权限
allow_usb_memory|bool|否|false|允许usb权限
allow_usb_redirect|bool|否|false|允许usb重定向权限
associated_desktop_pool|[]string|否|-|关联桌面池
associated_user|[]string|否|-|关联用户
auto_login_time|int|否|-|自动登录次数
background_color|string|否|-|背景颜色
content_color|string|否|-|正文颜色
description|string|否|-|描述
drag_drop_files|bool|否|false|允许拖拽文件
enable_auto_open_vm|bool|否|false|自动登录云桌面
enable_screen_watermark|bool|否|false|是否启动屏幕水印
font_size|int|是|-|文字大小
font_thickness|int|否|-|文字粗细
hide_navigation_bar|bool|否|false|是否隐藏导航栏
lean|string|是|-|租字体倾斜（默认添normal）
name|string|是|-|名称
pc_clipboard_mode|string|是|-|剪贴板模式（默认添“1”）
show_cloud_desktop|bool|否|false|终端菜单是否显示云桌面
show_cloud_server|bool|否|false|终端菜单是否显示云桌面
show_cloud_storage|bool|否|false|终端菜单是否显示云桌面
show_style|string|是|-|显示模式（默认添normal）
show_vdi_account|bool|否|false|是否显示vdi账户
show_vm_ip_address|bool|否|false|是否显示云桌面ip
show_vm_mac_address|bool|否|false|是否显示云桌面mac
show_vm_time|bool|否|false|是否显示云桌面时间
underline_type|string|是|-|下划线类型（默认添none）
usb_memory_mode|string|是|-|usb模式（默认添“1”）
watermark_content|string|否|-|水印内容
watermark_coordinate_x|int|是|-|水印横坐标
watermark_coordinate_y|int|是|-|水印竖坐标
watermark_move_time|int|是|0|水印移动时间
####请求示例
```
https://10.30.47.162/v1/compute/desktop/personalized_strategy/add
```


## /v1/compute/desktop/personalized_strategy/modify
###桌面池云桌面修改个性化设
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
allow_pc_clipboard|bool|否|false|允许剪贴板权限
allow_usb_memory|bool|否|false|允许usb权限
allow_usb_redirect|bool|否|false|允许usb重定向权限
associated_desktop_pool|[]string|否|-|关联桌面池
associated_user|[]string|否|-|关联用户
auto_login_time|int|否|-|自动登录次数
background_color|string|否|-|背景颜色
content_color|string|否|-|正文颜色
description|string|否|-|描述
drag_drop_files|bool|否|false|允许拖拽文件
enable_auto_open_vm|bool|否|false|自动登录云桌面
enable_screen_watermark|bool|否|false|是否启动屏幕水印
font_size|int|是|-|文字大小
font_thickness|int|否|-|文字粗细
hide_navigation_bar|bool|否|false|是否隐藏导航栏
lean|string|是|-|租字体倾斜（默认添normal）
name|string|是|-|名称
pc_clipboard_mode|string|是|-|剪贴板模式（默认添“1”）
show_cloud_desktop|bool|否|false|终端菜单是否显示云桌面
show_cloud_server|bool|否|false|终端菜单是否显示云桌面
show_cloud_storage|bool|否|false|终端菜单是否显示云桌面
show_style|string|是|-|显示模式（默认添normal）
show_vdi_account|bool|否|false|是否显示vdi账户
show_vm_ip_address|bool|否|false|是否显示云桌面ip
show_vm_mac_address|bool|否|false|是否显示云桌面mac
show_vm_time|bool|否|false|是否显示云桌面时间
underline_type|string|是|-|下划线类型（默认添none）
usb_memory_mode|string|是|-|usb模式（默认添“1”）
watermark_content|string|否|-|水印内容
watermark_coordinate_x|int|是|-|水印横坐标
watermark_coordinate_y|int|是|-|水印竖坐标
watermark_move_time|int|是|0|水印移动时间
####请求示例
```
https://10.30.47.162/v1/compute/desktop/personalized_strategy/modify
```

## /v1/compute/desktop/personalized_strategy/delete
###桌面池云桌面删除个性化设
### 请求类型
POST
### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
uuid|string|是|-|uuid
####请求示例
```
https://10.30.47.162/v1/compute/desktop/personalized_strategy/delete
```


## /v1/compute/desktop/personalized_strategy/list
###桌面池云桌面个性化设置列表
### 请求类型
GET
### 请求参数(todo:fill parameters)
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
filter_name|string|否|-|过滤名称
PagingParam|PagingParam|否|-|分页
####请求示例
```
https://10.30.47.162/v1/compute/desktop/personalized_strategy/list?filter_name=&pagenum=0&pagesize=10&tenant=78e956c3-499f-45a2-969a-cae82b1067d1&cluster_uuid=39058114-31a1-452f-9ce7-54c002ca7f53
```
####返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "total_count": 2,
    "list": [
      {
        "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
        "tenant": "78e956c3-499f-45a2-969a-cae82b1067d1",
        "tenant_name": "cwxtenant",
        "name": "two",
        "uuid": "d307cd7e-f178-45e9-a317-42a734782009",
        "description": "firefox",
        "associated_user": [],
        "associated_desktop_pool": [],
        "create_time": 1629773780,
        "modify_time": 1629773780,
        "style_template": 0,
        "show_vm_ip_address": false,
        "show_vm_mac_address": false,
        "show_vdi_account": false,
        "show_vm_time": false,
        "enable_screen_watermark": true,
        "watermark_move_time": 0,
        "underline_type": "none",
        "watermark_content": "添加个性化策略",
        "show_style": "normal",
        "content_color": "black",
        "border_color": "",
        "background_color": "transparent",
        "font_size": 24,
        "font_thickness": 2,
        "border_width": null,
        "transparency": null,
        "border_transparency": null,
        "lean": "normal",
        "watermark_coordinate_x": 0.5,
        "watermark_coordinate_y": 0.5,
        "allow_pc_clipboard": true,
        "pc_clipboard_mode": "1",
        "allow_usb_memory": true,
        "usb_memory_mode": "1",
        "allow_usb_printer": null,
        "usb_smart_card": null,
        "allow_usb_redirect": true,
        "drag_drop_files": true,
        "hide_navigation_bar": false,
        "shutdown_integration": false,
        "show_cloud_desktop": true,
        "show_cloud_server": true,
        "show_cloud_storage": true,
        "enable_auto_open_vm": false,
        "auto_login_time": 10,
        "is_can_delete": true
      },
      {
        "cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
        "tenant": "78e956c3-499f-45a2-969a-cae82b1067d1",
        "tenant_name": "cwxtenant",
        "name": "one",
        "uuid": "ef422df5-d26a-4b6b-9e79-2c5105bc6c6a",
        "description": "添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个性化策略添加个",
        "associated_user": [],
        "associated_desktop_pool": [],
        "create_time": 1629773584,
        "modify_time": 1629773584,
        "style_template": 0,
        "show_vm_ip_address": false,
        "show_vm_mac_address": false,
        "show_vdi_account": false,
        "show_vm_time": false,
        "enable_screen_watermark": true,
        "watermark_move_time": 1,
        "underline_type": "none",
        "watermark_content": "添加个性化策略",
        "show_style": "normal",
        "content_color": "lightgrey",
        "border_color": "",
        "background_color": "transparent",
        "font_size": 24,
        "font_thickness": 2,
        "border_width": null,
        "transparency": null,
        "border_transparency": null,
        "lean": "normal",
        "watermark_coordinate_x": 1,
        "watermark_coordinate_y": 1,
        "allow_pc_clipboard": true,
        "pc_clipboard_mode": "1",
        "allow_usb_memory": true,
        "usb_memory_mode": "1",
        "allow_usb_printer": null,
        "usb_smart_card": null,
        "allow_usb_redirect": true,
        "drag_drop_files": true,
        "hide_navigation_bar": false,
        "shutdown_integration": false,
        "show_cloud_desktop": true,
        "show_cloud_server": true,
        "show_cloud_storage": true,
        "enable_auto_open_vm": false,
        "auto_login_time": 5,
        "is_can_delete": true
      }
    ],
    "each_range_list_state": [
      {
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 1
      },
      {
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 1
      }
    ]
  }
}
```


## /v1/compute/desktop/personalized_strategy/inspect/login_user
###桌面池云桌面个性化设置关联用户
### 请求类型
GET
### 请求参数(todo:fill parameters)
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid

## /v1/compute/desktop/personalized_strategy/unassociated/desktop_pool/list
###桌面池云桌面个性化设置未关联桌面池
### 请求类型
GET
### 请求参数(todo:fill parameters)
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid

## /v1/compute/desktop/personalized_strategy/unassociated/user/list
###桌面池云桌面个性化设置未关联用户
### 请求类型
GET
### 请求参数(todo:fill parameters)
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid










