[back to api overview](../api_overview.md#label_api)
### 外置存储存储池(外置池)相关接口
## /v1/pool/share/list
共享存储(第三方)池列表
### 请求类型
POST

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
http://192.168.201.212:8080/v1/pool/share/list
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "page_num": 1,
  "page_size": 10,
  "filter_name": "",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "infos": [
      {
        "tenant": "",
        "tenant_name": "",
        "pool": {
          "UUID": "12897ef6-9d3e-4f1f-80f3-b3bc30c4d202",
          "Name": "1111",
          "Type": 4,
          "NamespaceUUID": "",
          "ZoneUUID": "3e2f589c-d5d7-4807-9c03-238fe967cdbd",
          "ZoneName": "default",
          "MachineUUID": "f04d95d6-c4f2-45c9-a1ef-164482af658a",
          "IP": "10.30.15.242",
          "Port": "",
          "Source": "wwn-0x5000c500ad9285bb",
          "Username": "",
          "Password": "",
          "Ctime": 1611199933,
          "Mtime": 0,
          "VolumeTotalCount": 4,
          "AvailHosts": null,
          "Volumes": null,
          "Capacity": 3998833524736,
          "ShareNsUUIDs": null,
          "Used": 33338699776,
          "Attr": {
            "overAllocationThreshold": "1.0"
          },
          "ShareNsNames": null,
          "Status": "healthy",
          "AllocatedCapacity": 10737418240,
          "LimitHost": false
        },
        "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
        "cluster_name": "cluster_name_243",
        "cluster_mode": ""
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
        "cluster_name": "cluster_name_243",
        "cluster_mode": "",
        "namespace_uuid": "83b1add8-2b9d-4f0c-8f3b-e0c3a2001006",
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 11
      }
    ],
    "TotalCount": 11
  }
}
```

#### 异常返回示例

### 状态码



## /v1/pool/share/get
存储池详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
pool_uuid|string|是|-|池uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/pool/share/get
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "pool_uuid": "0eca2be3-056f-4634-a25b-5cf717e067fb",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "pool": {
      "UUID": "0eca2be3-056f-4634-a25b-5cf717e067fb",
      "Name": "disks",
      "Type": 4,
      "NamespaceUUID": "",
      "ZoneUUID": "3e2f589c-d5d7-4807-9c03-238fe967cdbd",
      "ZoneName": "default",
      "MachineUUID": "f04d95d6-c4f2-45c9-a1ef-164482af658a",
      "IP": "10.30.15.242",
      "Port": "",
      "Source": "wwn-0x5000c500a7ebca1b",
      "Username": "",
      "Password": "",
      "Ctime": 1615451195,
      "Mtime": 0,
      "VolumeTotalCount": 5,
      "AvailHosts": [
        "f04d95d6-c4f2-45c9-a1ef-164482af658a"
      ],
      "Volumes": null,
      "Capacity": 3998833524736,
      "ShareNsUUIDs": null,
      "Used": 27915882496,
      "Attr": {
        "overAllocationThreshold": "1.0"
      },
      "ShareNsNames": null,
      "Status": "healthy",
      "AllocatedCapacity": 13958643712,
      "LimitHost": true
    },
    "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
    "tenant_name": "",
    "PoolTypes": null
  }
}
```

#### 异常返回示例

### 状态码


## /v1/pool/share/create
共享存储池(第三方存储)创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
pool_name|string|是|-|共享池名称
pool_type|int32|是|-|共享池类型
zone_uuid|string|是|-|资源池uuid
ip|string|是|-|源主机IP
port|string|否|-|源主机端口
source|string|否|-|目录路径
username|string|否|-|用户名
password|string|否|-|密码
limit_host|bool|否|-|是否限制主机
avail_host|[]string|否|-|池的可用挂载主机
avail_tenant|[]string|否|-|池的可用租户，为空代表所有租户都可用
attr|map[string][string]|是|-|存储池属性

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/pool/share/create
```
Body:
```
{
  "pool_name": "test--",
  "pool_type": 2,
  "zone_uuid": "3e2f589c-d5d7-4807-9c03-238fe967cdbd",
  "ip": "10.30.10.115",
  "port": "",
  "source": "/exports/b3405f60-fbb2-499d-82ac-d0edaadbf208/data",
  "username": "",
  "password": "",
  "limit_host": true,
  "avail_host": [
    "f04d95d6-c4f2-45c9-a1ef-164482af658a"
  ],
  "avail_tenant": [],
  "attr": {
    "overAllocationThreshold": "1.0"
  },
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "pool": {
      "UUID": "1c2a4db1-7591-481c-8108-5a15c40d4af1",
      "Name": "test--",
      "Type": 2,
      "NamespaceUUID": "",
      "ZoneUUID": "3e2f589c-d5d7-4807-9c03-238fe967cdbd",
      "ZoneName": "default",
      "MachineUUID": "f04d95d6-c4f2-45c9-a1ef-164482af658a",
      "IP": "10.30.10.115",
      "Port": "",
      "Source": "/exports/b3405f60-fbb2-499d-82ac-d0edaadbf208/data",
      "Username": "",
      "Password": "",
      "Ctime": 1615806832,
      "Mtime": 0,
      "VolumeTotalCount": 0,
      "AvailHosts": [
        "f04d95d6-c4f2-45c9-a1ef-164482af658a"
      ],
      "Volumes": null,
      "Capacity": 21464350720,
      "ShareNsUUIDs": null,
      "Used": 0,
      "Attr": {
        "overAllocationThreshold": "1.0"
      },
      "ShareNsNames": null,
      "Status": "healthy",
      "AllocatedCapacity": 0,
      "LimitHost": true
    },
    "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": "",
    "PoolTypes": null
  }
}
```

#### 异常返回示例

### 状态码


## /v1/pool/share/delete 
存储池删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
pool_uuid|string|是|-|共享池uuid
pool_name|string|是|-|共享池名称
cluster_uuid|string|是|-|集群uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/pool/share/delete 
```
Body:
```
{
	"tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
	"pool_uuid": "d9cff0da-4725-4e0e-82b3-466cc5105531",
	"pool_name": "nfs_test",
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
    "pool": {}
  }
}
```

#### 异常返回示例

### 状态码


## /v1/pool/share/set
存储池更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
pool_uuid|string|是|-|共享池uuid
pool_name|string|是|-|共享池名称
cluster_uuid|string|是|-|集群uuid
attr|map[string][string]|是|-|存储池属性(分配比例阈值)

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/pool/share/set
```
Body:
```
{
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
  "pool_uuid": "0eca2be3-056f-4634-a25b-5cf717e067fb",
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "pool_name": "disks",
  "attr": {
    "overAllocationThreshold": "1.0"
  }
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
    "pool": null,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": "",
    "PoolTypes": null
  }
}
```

#### 异常返回示例

### 状态码


## /v1/pool/share/status/check
存储池状态更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
pool_uuid|string|是|-|共享池uuid
cluster_uuid|string|是|-|集群uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/pool/share/status/check
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
  "pool_uuid": "12897ef6-9d3e-4f1f-80f3-b3bc30c4d202"
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
    "pool": null,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": "",
    "PoolTypes": null
  }
}
```

#### 异常返回示例

### 状态码


## /v1/pool/share/pool_type/support
获取支持创建的存储池类型
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.15.243:8080/v1/pool/share/pool_type/support?cluster_uuid=a97eb422-f42b-4b85-8556-725f152661f0
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
    "pool": null,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": "",
    "PoolTypes": [
      "iscsi",
      "nfs",
      "samba",
      "disk",
      "fc",
      "rbd"
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/pool/share/fc_device/list
获取可以被添加为FC共享池的设备列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
zone_uuid|string|是|-|资源池uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/pool/share/fc_device/list
```
Body:
```
{
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
  "zone_uuid": "3e2f589c-d5d7-4807-9c03-238fe967cdbd"
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
    "list": {
      "scsi-0TopHC_TopHC_vHDD_drive-scsi0-0-0-0": [
        {
          "host_uuid": "f9029fa9-4ce7-4ff2-bae5-2b88b7f3305a",
          "host_name": "10.30.10.107",
          "disk_path": "/dev/sda"
        }
      ]
    }
  }
}
```

#### 异常返回示例

### 状态码
