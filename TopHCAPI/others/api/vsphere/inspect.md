[back to api overview](../api_overview.md#api)

## /v1/vsphere/vcluster/inspect
vsphere集群详情
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
http://192.168.201.25:9990/v1/vsphere/vcluster/inspect?vsphere_uuid=757a9afa-5a01-11e9-b9ab-5256fffab0f3
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
    "name": "vcluster_040101",
    "host": "192.168.201.218",
    "uuid": "b3929c61-5489-11e9-8a2e-5256fffab0f3",
    "comment": "",
    "user": "administrator@vsphere.local",
    "createDate": 1554128601,
    "password": "Topsec12$$",
    "state": "init completed",
    "reason": ""
  }
}
```

#### 异常返回示例

### 状态码