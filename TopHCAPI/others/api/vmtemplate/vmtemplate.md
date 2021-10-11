[back to api overview](../api_overview.md#label_api)
### 虚拟机模板相关接口
## /v1/vmtemplate/list
虚拟机模板列表
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
http://192.168.201.213:8080/v1/vmtemplate/list?tenant=76373db8-e98d-4ad5-a373-9e9e4cd6048e&page_num=0&page_size=10&filter_name=&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
```


#### 正常返回示例
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
        "namespace": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
        "name": "api-test1-template-1107184806",
        "uuid": "862233bc-c660-434b-aec0-586889d306e1",
        "virtual_machine_uuid": "",
        "cpu_max_count": 2,
        "cpu_nr_count": "2",
        "mem_max_number": 274877906944,
        "mem_nr_number": 4294967296,
        "os": "Ubuntu x64",
        "tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
        "tenant_name": "gg_tenant01"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/vmtemplate/inspect
虚拟机模板详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
compute_image_uuid|string|是|-|过滤名称

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/vmtemplate/inspect?compute_image_uuid=862233bc-c660-434b-aec0-586889d306e1&tenant=76373db8-e98d-4ad5-a373-9e9e4cd6048e&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
```


#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "tenant": "",
    "tenant_name": "",
    "uuid": "862233bc-c660-434b-aec0-586889d306e1",
    "name": "api-test1-template-1107184806",
    "type": "GUS",
    "create_time": 1573123690,
    "modify_time": 1573123690,
    "state": "shutoff",
    "ga_state": "disconnected",
    "action": "noaction",
    "os": "Ubuntu x64",
    "owner": "",
    "owner_name": "",
    "create_type": "",
    "namespace": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
    "machine_uuid": "",
    "owner_is_ldap": false,
    "labels": null,
    "interface_ips": [],
    "attr": null,
    "parent_uuid": "",
    "migrate_dest": "",
    "baseline": "Westmere",
    "import_machine": "",
    "exceed_cluster_baseline": false,
    "cpu_current": "2",
    "cpu_max_count": 2,
    "cpu_nr_count": 0,
    "cpu_sockets": 1,
    "cpu_socket_cores": 2,
    "mem_size": 4294967296,
    "mem_max": 274877906944,
    "compute_name": "",
    "ha_mode": "on",
    "os_loader_path": "BIOS",
    "video_model_type": "vga",
    "panic_model": "",
    "startup_setting": {
      "hosts": null,
      "labels": null
    },
    "vnc_enable": false,
    "mem_sec_enabled": false,
    "vnc_port": 0,
    "vnc_password": "",
    "spice_port": 0,
    "spice_password": "FakePasswd",
    "panic": "on",
    "interfaces": [
      {
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
        "port_group": "2dae0240-6710-4841-aa0b-502c8ca54e13",
        "port_group_name": "default",
        "vlan_tag_ids": null,
        "is_old": false
      }
    ],
    "cdrom": {
      "attached": false,
      "name": ""
    },
    "floppy": {
      "attached": false,
      "name": ""
    },
    "disks": [
      {
        "disk_target_device": "sda",
        "disk_vsd_source": {
          "volume_uuid": "4b50424b-77cd-4da6-9871-6b0f02ff09b3",
          "volume_name": "api-test1-volume1",
          "disk_capacity": 2147483648,
          "pool_uuid": "b200ea6d-cd4e-4204-96c9-08eb525d3d55",
          "pool_name": "sss",
          "replica": "2",
          "drive_type": "HDD",
          "redundancy": 1
        },
        "disk_cache_mode": "none",
        "backing_store": {
          "index": 0,
          "format": null,
          "source": null,
          "backing_store": null
        }
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
    "usbs": [],
    "kvm_clock_enable": true,
    "virt_nested_enable": false,
    "memory_huge_pages_enable": false,
    "memory_qos": {
      "hard_limit": 0,
      "soft_limit": 0,
      "swap_hard_limit": 0,
      "min_guarantee": 0
    },
    "cpu_reserve_enable": false,
    "memory_reserve_enable": false,
    "expand_config": {
      "cpu_auto_expand_enable": false,
      "memory_auto_expand_enable": false,
      "max_expand_cpu": 0,
      "max_expand_mem": 0,
      "expand_cpu": 0,
      "expand_mem": 0
    },
    "data_localization_mode_on": "off"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/vmtemplate/create
虚拟机模板创建
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
http://192.168.201.147:9990/v1/vmtemplate/create
```
Body:
```
{
	"tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
	"compute_uuid": "862233bc-c660-434b-aec0-586889d306e1",
	"compute_image_name": "api-test1-template-1107184806",
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
  "data": {
    "name": "",
    "uuid": "",
    "tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/vmtemplate/delete
虚拟机模板删除
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
http://192.168.201.147:9990/v1/vmtemplate/delete
```
Body:
```
{
	"tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
	"compute_image_uuid": "862233bc-c660-434b-aec0-586889d306e1",
	"compute_image_name": "api-test1-template-1107184806",
	"is_delete_volumes": true,
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


