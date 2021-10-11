[back to api overview](../api_overview.md#api)

## /v1/vsphere/vcluster/delete
vsphere集群删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid|string| 是|- |vsphere集群uuid

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/vsphere/vcluster/delete
```
Body:
```
{
	"vsphere_uuid":"ad9259b7-5b54-11e9-88de-5256fffab0f3"
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
  "data": ""
}
```

#### 异常返回示例

### 状态码