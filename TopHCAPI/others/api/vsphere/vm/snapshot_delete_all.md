[back to api overview](../api_overview.md#api)

## /v1/vsphere/vm/snapshot/delete/all
删除虚拟机所有快照
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid|string| 是|-  | vsphere uuid
 vm_reference|string|是|-|虚拟机的唯一标识


### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/vsphere/vm/snapshot/delete/all
```
Body:
```
{
	"vsphere_uuid": "e0a133e7-4568-11e9-8ea8-5256ff006a00",
	"vm_reference": "VirtualMachine:vm-41",
	"name": "snapshot_031501"
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