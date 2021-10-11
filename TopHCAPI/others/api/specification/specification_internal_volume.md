[back to api overview](../api_overview.md#label_api)
### 融合存储卷(内置卷)规格相关接口
## /v1/specification/internalvolume/list
内置卷规格列表
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
http://192.168.201.212:8080/v1/specification/internalvolume/list?tenant=76373db8-e98d-4ad5-a373-9e9e4cd6048e&page_num=0&page_size=10&filter_name=&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
        "name": "volumeSpec-1107145400",
        "uuid": "cf780dcc-c442-4918-88fe-56af52bdc627",
        "create_time": 1573109650,
        "resource_version": 0,
        "kind": "Specification",
        "tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
        "creator": "69347874-085a-4b91-ab47-559bce0a2bac",
        "creator_name": "zhl",
        "creator_tenant": "system",
        "desc": "",
        "type": "ivolume",
        "internalvolume_spec": {
          "cluster_uuid": "",
          "tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
          "hosts": null,
          "auto_mount_host_count": 0,
          "pool_name": "sss",
          "volume_name": "volume-1107145400",
          "pool_uuid": "b200ea6d-cd4e-4204-96c9-08eb525d3d55",
          "capacity": 2147483648,
          "attribute": {
            "ComponentSetShift": "1",
            "ComponentShift": "30",
            "DataType": "replica",
            "DevType": "block",
            "DriveType": "HDD",
            "Encrypto": "off",
            "ReadBytesLimit": "0",
            "ReadIOPSLimit": "",
            "Safety": "first",
            "ScheduleOption": "intelligent",
            "StripeShift": "17",
            "ThinProvision": "on",
            "VmCache": "none",
            "WriteBytesLimit": "0",
            "WriteIOPSLimit": "",
            "ZoneName": "default",
            "Zone": "64864753-88a2-4020-8627-bf055964b4d8",
            "replica": "2"
          },
          "address": "",
          "accounts": null,
          "snap_capacity": 6442450944,
          "create_option": null
        },
        "tenant_name": "gg_tenant01"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/specification/internalvolume/inspect
内置卷规格详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
uuid|string|是|-|内置卷规格uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/specification/internalvolume/inspect?uuid=cf780dcc-c442-4918-88fe-56af52bdc627&tenant=76373db8-e98d-4ad5-a373-9e9e4cd6048e&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "name": "iscsiALL-1",
    "uuid": "d66c5c5e-b07c-4008-b339-b926afcdc149",
    "create_time": 1586489246,
    "resource_version": 0,
    "kind": "Specification",
    "tenant": "d6342cd6-bd3f-474e-b221-682bd4b07c3e",
    "cluster_uuid": "42e3b0db-5dce-4893-9421-7ae6fe8ac0ee",
    "creator": "edf841fd-e497-4f3e-803a-d96282ed2165",
    "creator_name": "高伟-",
    "creator_tenant": "system",
    "desc": "iscsiALL",
    "type": "ivolume",
    "internalvolume_spec": {
      "volume_name": "iscsiALL-1",
      "pool_uuid": "5548150a-e136-445c-96a4-9430783a6852",
      "capacity": 21474836480,
      "attribute": {
        "ComponentSetShift": "2",
        "ComponentShift": "30",
        "DataType": "replica",
        "DevType": "target",
        "DriveType": "HDD",
        "Encrypto": "off",
        "ReadBytesLimit": "157286400",
        "ReadIOPSLimit": "100",
        "Safety": "second",
        "ScheduleOption": "intelligent",
        "StripeShift": "17",
        "TargetACL": "ALL",
        "ThinProvision": "off",
        "VmCache": "none",
        "WriteBytesLimit": "157286400",
        "WriteIOPSLimit": "100",
        "Zone": "64864753-88a2-4020-8627-bf055964b4d8",
        "ZoneName": "default",
        "replica": "2"
      },
      "address": "",
      "accounts": null,
      "snap_capacity": 64424509440,
      "create_option": null,
      "cluster_uuid": "",
      "tenant": "d6342cd6-bd3f-474e-b221-682bd4b07c3e",
      "hosts": null,
      "auto_mount_host_count": 0,
      "pool_name": "B-1-5测试"
    },
    "tenant_name": "B-1-5测试组",
    "is_share": true
  }
}
```

#### 异常返回示例

### 状态码



## /v1/specification/internalvolume/add
内置卷规格添加
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
http://192.168.201.147:9990/v1/specification/internalvolume/add
```
Body:
```
{
  "tenant": "d1b0742d-7a6a-4409-9076-0bf8aac63087",
  "name": "volumeSpec-0415153823",
  "desc": "规格描述1",
  "share": false,
  "spec": {
    "tenant": "d1b0742d-7a6a-4409-9076-0bf8aac63087",
    "pool_uuid": "e7b322b9-d03d-4952-bd86-74e2f9827e48",
    "pool_name": "xzh",
    "volume_name": "volume-0415153823",
    "capacity": 1073741824,
    "snap_capacity": 3221225472,
    "attribute": {
      "DevType": "block",
      "DataType": "replica",
      "Safety": "first",
      "Encrypto": "off",
      "DriveType": "HDD",
      "ThinProvision": "on",
      "ReadIOPSLimit": "",
      "WriteIOPSLimit": "",
      "ReadBytesLimit": "0",
      "WriteBytesLimit": "0",
      "VmCache": "none",
      "ScheduleOption": "intelligent",
      "Zone": "64864753-88a2-4020-8627-bf055964b4d8",
      "ZoneName": "default",
      "replica": "2",
      "ComponentSetShift": "0",
      "ComponentShift": "30",
      "StripeShift": "17"
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



## /v1/specification/internalvolume/delete
内置卷规格删除
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
http://192.168.201.147:9990/v1/specification/internalvolume/delete
```
Body:
```
{
	"tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
	"uuid": "cf780dcc-c442-4918-88fe-56af52bdc627",
	"specification_name": "volumeSpec-1107145400",
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