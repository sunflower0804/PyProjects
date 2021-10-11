[back to api overview](../api_overview.md#api)

## /v1/vsphere/datacenter/list
数据中心的列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid|string| 是|- | vsphere集群uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.87:9990/v1/vsphere/datacenter/list?vsphere_uuid=27bce68f-5c26-11e9-b651-5256fffab0f3
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
    "total_count": 4,
    "list": [
      {
        "datacenter_name": "Datacenter",
        "datecenter_reference": "Datacenter:datacenter-2"
      },
      {
        "datacenter_name": "datacenter_032101",
        "datecenter_reference": "Datacenter:datacenter-265"
      },
      {
        "datacenter_name": "datacenter_032801",
        "datecenter_reference": "Datacenter:datacenter-341"
      },
      {
        "datacenter_name": "Datacenter 3",
        "datecenter_reference": "Datacenter:datacenter-194"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码