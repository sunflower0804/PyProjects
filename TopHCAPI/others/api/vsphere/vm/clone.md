[back to api overview](../api_overview.md#api)

## /v1/vsphere/vm/clone
虚拟机克隆为虚拟机或模板
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid|string| 是|-  | vsphere uuid
 vm_reference|string|是|-|虚拟机的唯一标识
 folder_reference|string|是|-|文件夹的唯一标识
 name|string|是|-|虚拟机或模板的名称
 clone_spec|clone_spec object|是|-|虚拟机或模板的名称

#### clone_spec object
名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
power_on|bool|否|false|克隆后的虚拟机是否启动，模板忽略
template|bool|否|false|是否克隆为模板

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/vsphere/vm/clone
```
Body:
```
{
	"vsphere_uuid":"{{ vsphere_uuid  }}",
	"vm_reference":"VirtualMachine:vm-23",
	"folder_reference":"Folder:group-v3",
	"name":"debian_clone1",
	"clone_spec":{
		"power_on":true,
		"template":false
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
  "data": ""
}
```

#### 异常返回示例

### 状态码