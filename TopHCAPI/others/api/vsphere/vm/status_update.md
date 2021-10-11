[back to api overview](../api_overview.md#api)

## /v1/vsphere/vm/status/update
虚拟机状态设置，包括打开电源，关闭电源，重启，关机，重置电源，挂起
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid|string| 是|-  | vsphere uuid
 vm_reference|string|是|-|虚拟机的唯一标识
 type|string|是|-|虚拟机操作类型，power_off，power_on，reboot_guest，shutdown_guest，reset，suspend可选


### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/vsphere/vm/status/update
```
Body:
```
{
	"vsphere_uuid": "{{ vsphere_uuid  }}",
	"vm_reference": "VirtualMachine:vm-23",
	"type": "resetss"
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