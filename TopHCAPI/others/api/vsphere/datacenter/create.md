[back to api overview](../api_overview.md#api)

## /v1/vsphere/datacenter/create
数据中心的创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid|string| 是|- | vsphere集群uuid
 folder_reference|string| 是|- |文件夹的唯一标识
 datacenter_name|string|是|-|数据中心名称

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/vsphere/datacenter/create
```
Body:
```
{
	"vsphere_uuid": "{{ vsphere_uuid  }}",
	"datacenter_name": "datacenter_032801",
	"folder_reference": "Folder:group-d1"
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