[back to api overview](../api_overview.md#api)

## /v1/vsphere/vcluster/dashboard
vsphere集群概览
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid|string|是|-|vsphere集群uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.25:9990/v1/vsphere/vcluster/dashboard?vsphere_uuid=757a9afa-5a01-11e9-b9ab-5256fffab0f3
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
    "alarm": null,
    "cpu": [
      {
        "value": 79,
        "name": "cpuUsed"
      },
      {
        "value": 17521,
        "name": "cpuFree"
      }
    ],
    "datastore": [
      {
        "value": 40347107328,
        "name": "diskFree"
      },
      {
        "value": 58974011392,
        "name": "diskUsed"
      }
    ],
    "hosts": [
      {
        "value": 1,
        "name": "connected"
      }
    ],
    "memory": [
      {
        "value": 1246756864,
        "name": "memUsed"
      },
      {
        "value": 7342571520,
        "name": "memFree"
      }
    ],
    "templates": null,
    "vms": [
      {
        "value": 6,
        "name": "poweredOff"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码