[back to api overview](../api_overview.md#label_api)
### 虚拟机规格相关接口
## /v1/specification/unified_vm/list
虚拟机规格列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
filter_name|string|否|-|过滤名称
page_num|int|否|0|第几页
page_size|int|否|0|每页数据条数

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/specification/unified_vm/list?tenant=76373db8-e98d-4ad5-a373-9e9e4cd6048e&page_num=0&page_size=10&filter_name=&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
```


#### 正常返回示例
```
{
  "message": "success",
  "message_cn": "成功",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {
    "total_count": 1,
    "list": [
      {
        "name": "spe1",
        "uuid": "34164e68-a753-45ab-bdf1-350ef00296fa",
        "create_time": 1586936711,
        "resource_version": 0,
        "kind": "Specification",
        "tenant": "d1b0742d-7a6a-4409-9076-0bf8aac63087",
        "cluster_uuid": "42e3b0db-5dce-4893-9421-7ae6fe8ac0ee",
        "creator": "7fa86d51-dc81-48ce-89ba-bc70f0fdb86d",
        "creator_name": "zhanghai",
        "creator_tenant": "system",
        "desc": "规格描述1",
        "type": "unifiedvm",
        "unified_vm_spec": {
          "cpunr": 2,
          "max_cpu_nr": 2,
          "cpu_sockets": 1,
          "cpu_socket_cores": 2,
          "mem_size": 4294967296,
          "mem_max": 274877906944,
          "image_uuid": "",
          "type": "server",
          "os": "Ubuntu x64",
          "meta": {
            "compute_name": "spec_vm1",
            "ha_mode": "on",
            "os_loader_path": "BIOS",
            "video_model_type": "vga",
            "panic_model": "isa",
            "startup_setting": null,
            "vnc_enable": false,
            "mem_sec_enabled": false,
            "virt_nested_enable": false,
            "data_localization_mode_on": "off",
            "recover_to_related_zones": 2,
            "master_zone_take_over": 2
          },
          "cdrom": {
            "attached": false,
            "name": ""
          },
          "floppy": {
            "attached": false,
            "name": ""
          },
          "parent_uuid": "",
          "create_type": 0,
          "baseline": "Westmere",
          "object_group": "",
          "zone": "64864753-88a2-4020-8627-bf055964b4d8",
          "zone_name": "default",
          "interfaces": [
            {
              "interface_id": "",
              "interface_model_type": "virtio",
              "interface_type": "manage",
              "mac_address": "",
              "ips": null,
              "in_bount": {
                "average": 0,
                "peak": 0,
                "burst": 0
              },
              "out_bount": {
                "average": 0,
                "peak": 0,
                "burst": 0
              },
              "switch_uuid": "",
              "switch_name": "",
              "gateway_uuid": "",
              "gateway_name": "",
              "port_group": "bfc88395-06c1-475d-af50-7bc42ace6420",
              "port_group_name": "default",
              "vlan_tag_ids": [
                0
              ],
              "is_old": false,
              "bound_ip": "",
              "peer": ""
            }
          ],
          "disks": [
            {
              "disk_target_device": "",
              "disk_target_bus": "scsi",
              "disk_cache_mode": "none",
              "backing_store": {
                "index": 0,
                "format": null,
                "source": null,
                "backing_store": null
              },
              "disk_unified_vsd": {
                "volume_name": "spec_vm1-volume1",
                "pool_uuid": "e7b322b9-d03d-4952-bd86-74e2f9827e48",
                "capacity": 1073741824,
                "attribute": {
                  "DriveType": "HDD",
                  "replica": "2"
                },
                "address": "",
                "accounts": null,
                "snap_capacity": 3221225472,
                "create_option": null,
                "cluster_uuid": "",
                "tenant": "d1b0742d-7a6a-4409-9076-0bf8aac63087",
                "hosts": null,
                "auto_mount_host_count": 0,
                "pool_name": "xzh",
                "redundancy": 0
              },
              "is_old": false,
              "image_name": "",
              "redundancy": 1,
              "device": "",
              "file_path": "",
              "vsphere_vm_disk_key": 0
            }
          ]
        },
        "tenant_name": "xzh",
        "is_share": false
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/specification/unified_vm/inspect
虚拟机规格详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
uuid|string|是|-|虚拟机规格uuid


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/specification/unified_vm/inspect?uuid=baa19d2a-455f-45d8-859d-92c5fac4ae89&tenant=76373db8-e98d-4ad5-a373-9e9e4cd6048e&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
```


#### 正常返回示例
```
{
  "message": "success",
  "message_cn": "成功",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {
    "name": "spe1",
    "uuid": "34164e68-a753-45ab-bdf1-350ef00296fa",
    "create_time": 1586936711,
    "resource_version": 0,
    "kind": "Specification",
    "tenant": "d1b0742d-7a6a-4409-9076-0bf8aac63087",
    "cluster_uuid": "42e3b0db-5dce-4893-9421-7ae6fe8ac0ee",
    "creator": "7fa86d51-dc81-48ce-89ba-bc70f0fdb86d",
    "creator_name": "zhanghai",
    "creator_tenant": "system",
    "desc": "规格描述1",
    "type": "unifiedvm",
    "unified_vm_spec": {
      "cpunr": 2,
      "max_cpu_nr": 2,
      "cpu_sockets": 1,
      "cpu_socket_cores": 2,
      "mem_size": 4294967296,
      "mem_max": 274877906944,
      "image_uuid": "",
      "type": "server",
      "os": "Ubuntu x64",
      "meta": {
        "compute_name": "spec_vm1",
        "ha_mode": "on",
        "os_loader_path": "BIOS",
        "video_model_type": "vga",
        "panic_model": "isa",
        "startup_setting": null,
        "vnc_enable": false,
        "mem_sec_enabled": false,
        "virt_nested_enable": false,
        "data_localization_mode_on": "off",
        "recover_to_related_zones": 2,
        "master_zone_take_over": 2
      },
      "cdrom": {
        "attached": false,
        "name": ""
      },
      "floppy": {
        "attached": false,
        "name": ""
      },
      "parent_uuid": "",
      "create_type": 0,
      "baseline": "Westmere",
      "object_group": "",
      "zone": "64864753-88a2-4020-8627-bf055964b4d8",
      "zone_name": "default",
      "interfaces": [
        {
          "interface_id": "",
          "interface_model_type": "virtio",
          "interface_type": "manage",
          "mac_address": "",
          "ips": null,
          "in_bount": {
            "average": 0,
            "peak": 0,
            "burst": 0
          },
          "out_bount": {
            "average": 0,
            "peak": 0,
            "burst": 0
          },
          "switch_uuid": "",
          "switch_name": "",
          "gateway_uuid": "",
          "gateway_name": "",
          "port_group": "bfc88395-06c1-475d-af50-7bc42ace6420",
          "port_group_name": "default",
          "vlan_tag_ids": [
            0
          ],
          "is_old": false,
          "bound_ip": "",
          "peer": ""
        }
      ],
      "disks": [
        {
          "disk_target_device": "",
          "disk_target_bus": "scsi",
          "disk_cache_mode": "none",
          "backing_store": {
            "index": 0,
            "format": null,
            "source": null,
            "backing_store": null
          },
          "disk_unified_vsd": {
            "volume_name": "spec_vm1-volume1",
            "pool_uuid": "e7b322b9-d03d-4952-bd86-74e2f9827e48",
            "capacity": 1073741824,
            "attribute": {
              "DriveType": "HDD",
              "replica": "2"
            },
            "address": "",
            "accounts": null,
            "snap_capacity": 3221225472,
            "create_option": null,
            "cluster_uuid": "",
            "tenant": "d1b0742d-7a6a-4409-9076-0bf8aac63087",
            "hosts": null,
            "auto_mount_host_count": 0,
            "pool_name": "xzh",
            "redundancy": 0
          },
          "is_old": false,
          "image_name": "",
          "redundancy": 1,
          "device": "",
          "file_path": "",
          "vsphere_vm_disk_key": 0
        }
      ]
    },
    "tenant_name": "xzh",
    "is_share": false
  }
}
```

#### 异常返回示例

### 状态码


## /v1/specification/unified_vm/add
虚拟机规格添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/specification/unified_vm/add
```
Body:
```
{
  "name": "spe1",
  "share": false,
  "tenant": "d1b0742d-7a6a-4409-9076-0bf8aac63087",
  "desc": "规格描述1",
  "spec": {
    "tenant": "d1b0742d-7a6a-4409-9076-0bf8aac63087",
    "zone": "64864753-88a2-4020-8627-bf055964b4d8",
    "cpunr": 2,
    "cpu_sockets": 1,
    "cpu_socket_cores": 2,
    "baseline": "Westmere",
    "max_cpu_nr": 2,
    "mem_size": 4294967296,
    "mem_max": 274877906944,
    "image_uuid": "",
    "type": "server",
    "os": "Ubuntu x64",
    "meta": {
      "compute_name": "spec_vm1",
      "ha_mode": "on",
      "os_loader_path": "BIOS",
      "video_model_type": "vga",
      "panic_model": "isa",
      "vnc_enable": false,
      "mem_sec_enabled": false,
      "data_localization_mode_on": "off",
      "virt_nested_enable": false,
      "startup_setting": null,
      "recover_to_related_zones": 2,
      "master_zone_take_over": 2
    },
    "disks": [
      {
        "disk_target_bus": "scsi",
        "disk_cache_mode": "none",
        "disk_unified_vsd": {
          "tenant": "d1b0742d-7a6a-4409-9076-0bf8aac63087",
          "pool_uuid": "e7b322b9-d03d-4952-bd86-74e2f9827e48",
          "pool_name": "xzh",
          "volume_name": "spec_vm1-volume1",
          "capacity": 1073741824,
          "snap_capacity": 3221225472,
          "attribute": {
            "replica": "2",
            "DriveType": "HDD"
          }
        },
        "image_name": null,
        "redundancy": 1
      }
    ],
    "interfaces": [
      {
        "interface_model_type": "virtio",
        "interface_type": "manage",
        "port_group": "bfc88395-06c1-475d-af50-7bc42ace6420",
        "port_group_name": "default",
        "vlan_tag_ids": [
          0
        ],
        "in_bount": {
          "average": 0,
          "peak": 0,
          "burst": 0
        },
        "out_bount": {
          "average": 0,
          "peak": 0,
          "burst": 0
        },
        "switch_uuid": "",
        "switch_name": ""
      }
    ],
    "cdrom": {
      "name": ""
    },
    "floppy": {
      "name": ""
    }
  },
  "cluster_uuid": "42e3b0db-5dce-4893-9421-7ae6fe8ac0ee"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {}
}
```

#### 异常返回示例

### 状态码


## /v1/specification/unified_vm/delete
虚拟机规格删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/specification/unified_vm/delete
```
Body:
```
{
	"tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
	"uuid": "baa19d2a-455f-45d8-859d-92c5fac4ae89",
	"specification_name": "vm_specifi_1",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {}
}
```

#### 异常返回示例

### 状态码

