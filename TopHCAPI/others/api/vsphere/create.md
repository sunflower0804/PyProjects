[back to api overview](../api_overview.md#api)

## /v1/vsphere/vcluster/create
vsphere集群添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 name|string| 是|-  | vsphere集群名称
 host|string|是|-|主机ip
 user|string|是|-|用户名
 password|string|是|-|密码

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/vsphere/vcluster/create
```
Body:
```
{
	"name": "vcluster_040801",
	"host": "192.168.201.218",
	"user": "administrator@vsphere.local",
	"password": "Topsec12$"
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