## /v1/network/vm/net/info
#### 功能：获取虚拟机网络详情
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/vm/net/info
```
Body:
```	
{
	"cluster_uuid": "66b2edab-14aa-11e9-b0b9-5256ff003400",
	"tenant": "55b2edab-14aa-11e9-b0b9-5256ff003400",
	"mac": "52:56:09:30:56:49"
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
	"data": {
		"switch":null,
		"vm_network": {
			"uuid": "78289f34-b67a-48a4-807b-4a27d1fcf19d",
			"interface": "test",
			"mac": "52:56:b0:06:3f:b1",
			"attached": false,
			"sw_uuid": "56f79d98-ed71-4ab3-ad3c-6eaf90a41578"
		}
	}
}

```

#### 异常返回示例

### 状态码




## /v1/network/security/vm/count/inspect
#### 功能：获取各安全服务的虚拟机数量
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid

### 返回参数
名称|参数类型|描述 
---|---|---
vdfw_num|int|分布式防火墙数量
vgate_num|int|下一代防火墙数量
dlp_num|int|数据防泄漏数量
ssan_um|int|运维安全审计系统数量
svpn_num|int|SSL VPN数量
lcas_num|int|日志收集与分析系统数量


### 示例
#### 请求示例
```
http://192.168.201.57:9990/v1/network/security/vm/count/inspect?tenant_uuid=1c64fac3-1324-11e9-b910-5254fffffffd
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "vdfw_num": 1,
    "vgate_num": 2,
    "dlp_num": 3,
    "ssan_um": 4,
    "svpn_num": 4,
    "lcas_num": 3
  }
}
```

#### 异常返回示例
### 状态码





## /v1/network/security_host/list 
#### 功能：获取安全主机列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://10.30.12.173:9990/v1/role/inspect?cluster_uuid=78289f34-b67a-48a4-807b-4a27d1fcf19d
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
				"host_uuid": "78289f34-b67a-48a4-807b-4a27d1fcf19d",
				"host_name": "test",
				"host_ip": "192.168.30.1",
				"is_init": false,
				"taedaemond":false
			}
		]
	}
}
```

#### 异常返回示例

### 状态码



## /v1/network/security_host/init 
#### 功能：安全主机初始化
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/security_host/init 
```
Body:
```	
{
	"cluster_uuid":"78289f34-b67a-48a4-807b-4a27d1fcf19d",
	"host_uuid":"f96b808a-397a-43e4-83cf-7034fa067bf9",
	"host_name":"test",
	"host_ip":"192.168.30.1"
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
	"data": {
		"cluster_uuid": "78289f34-b67a-48a4-807b-4a27d1fcf19d",
		"host_uuid": "f96b808a-397a-43e4-83cf-7034fa067bf9"
	}
}
```

#### 异常返回示例

### 状态码


## /v1/network/taedaemond/enable 
#### 功能：开启taedaemond
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/taedaemond/enable
```
Body:
```	
{
	"cluster_uuid": "78289f34-b67a-48a4-807b-4a27d1fcf19d",
	"host_uuid": "f96b808a-397a-43e4-83cf-7034fa067bf9",
	"vgate_uuid": "7b4c8a5c-0933-4ffe-8c1b-617a7449227b",
	"host_ip": "192.168.30.1"
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
	"data": {
		"cluster_uuid": "78289f34-b67a-48a4-807b-4a27d1fcf19d",
		"host_uuid": "f96b808a-397a-43e4-83cf-7034fa067bf9"
	}
}
```

#### 异常返回示例

### 状态码


## /v1/network/security_vm/create
#### 功能：创建安全虚拟机
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/
```
Body:
```	
{
	"cluster_uuid": "78289f34-b67a-48a4-807b-4a27d1fcf19d",
	"tenant_uuid": "f96b808a-397a-43e4-83cf-7034fa067bf9",
	"host_uuid": "f96b808a-397a-43e4-83cf-7034fa067bf9",
	"pool_uuid": "888b808a-397a-43e4-83cf-7034fa067bf9",
	"image_size": 1568243,
	"security_vm_type": 3,
	"security_vm_ip": "192.168.201.9"
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
	"data": {
		"cluster_uuid": "78289f34-b67a-48a4-807b-4a27d1fcf19d",
		"tenant_uuid": "f96b808a-397a-43e4-83cf-7034fa067bf9",
		"host_uuid": "f96b808a-397a-43e4-83cf-7034fa067bf9",
		"pool_uuid": "888b808a-397a-43e4-83cf-7034fa067bf9",
		"image_size": 1568243,
		"security_vm_type": 3,
		"security_vm_ip": "192.168.201.9",
		"create_time":1573123402,
		"update_time":1573123402
	}
}
```

#### 异常返回示例

### 状态码




## /v1/network/security_vm/state/update
#### 功能：修改安全虚拟机
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/security_vm/state/update
```
Body:
```	
{
	"cluster_uuid": "78289f34-b67a-48a4-807b-4a27d1fcf19d",
	"tenant_uuid": "27289f34-b67a-48a4-807b-4a27d1fcf19d",
	"security_vm_ip": "192.168.201.1",
	"security_vm_type": 2,
	"is_enable": true
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
	"data": {
		"tenant_uuid": "27289f34-b67a-48a4-807b-4a27d1fcf19d",
		"security_vm_ip": "192.168.201.1",
		"security_vm_type": 2,
		"is_enable": true
	}
}
```

#### 异常返回示例

### 状态码

## /v1/network/security_vm/delete
#### 功能：删除安全虚拟机
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/security_vm/delete
```
Body:
```	
{
	"cluster_uuid": "78289f34-b67a-48a4-807b-4a27d1fcf19d",
	"tenant_uuid": "27289f34-b67a-48a4-807b-4a27d1fcf19d",
	"host_uuid": "66289f34-b67a-48a4-807b-4a27d1fcf19d",
	"security_vm_ip": "192.168.201.1",
	"security_vm_type": 2,
	"security_vm_uuid": "88889f34-b67a-48a4-807b-4a27d1fcf19d"
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
	"data": {
		"tenant_uuid": "27289f34-b67a-48a4-807b-4a27d1fcf19d",
		"host_uuid": "66289f34-b67a-48a4-807b-4a27d1fcf19d",
		"security_vm_ip": "192.168.201.1",
		"security_vm_type": 2,
	}
}
```

#### 异常返回示例

### 状态码



## /v1/network/float_vm/list 
#### 功能：获取游离的虚拟机列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://10.30.12.173:9990/v1/network/float_vm/list%20?cluster_uuid=f96b808a-397a-43e4-83cf-7034fa067bf9&tenant_uuid=27289f34-b67a-48a4-807b-4a27d1fcf19d
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
				"vm_uuid": "78289f34-b67a-48a4-807b-4a27d1fcf19d",
				"vm_name": "test",
				"vm_type": "security",
				"create_time": 159524256,
				"update_time": 159524256,
				"vm_state": 0,
				"parent_uuid": "56f79d98-ed71-4ab3-ad3c-6eaf90a41578"
			}
		]
	}
}
```

#### 异常返回示例

### 状态码


## /v1/network/security_vm/inspect
#### 功能：获取安全虚拟机详情
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://10.30.12.173:9990/v1/network/security_vm/inspect?cluster_uuid=f96b808a-397a-43e4-83cf-7034fa067bf9&tenant_uuid=27289f34-b67a-48a4-807b-4a27d1fcf19d&security_vm_type=2&security_vm_ip=192.168.201.29
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
		"vm_uuid": "78289f34-b67a-48a4-807b-4a27d1fcf19d",
		"vm_name": "test",
		"vm_type": "security",
		"create_time": 159524256,
		"update_time": 159524256,
		"vm_state": 0,
		"parent_uuid": "56f79d98-ed71-4ab3-ad3c-6eaf90a41578"
	}
}
```

#### 异常返回示例

### 状态码


## /v1/network/security_vm/list
#### 功能：获取安全虚拟机列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/security_vm/list
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码



## /v1/network/cloud/image/repository/inspect 
#### 功能：获取system下云镜像仓库
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/cloud/image/repository/inspect 
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码



## /v1/network/available_vlan/update
#### 功能：修改vlan
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/available_vlan/update
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码



## /v1/network/available_vlan/list
#### 功能：获取vlan列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/available_vlan/list
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/reserved_vlan/list
#### 功能：获取预留vlan列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/reserved_vlan/list
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/license_server/inspect
#### 功能：获取许可证服务器
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/license_server/inspect
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码










































