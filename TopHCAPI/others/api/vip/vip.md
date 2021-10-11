[back to api overview](../api_overview.md#api)



## /v1/network/vip/add
#### 功能：添加虚拟ip
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
http://localhost:9990/v1/network/vip/add
```
Body:
```	
{
	"tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
	"list": [
		{
			"ip": "192.168.201.29/23",
			"gateway": "1.1.1.1"
		}
	],
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
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
  "data": {}
}
```

#### 异常返回示例

### 状态码




## /v1/vip/delete
#### 功能：删除虚拟ip
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 vip_uuid|string| 是|""  | 虚拟ip的uuid
 

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant|string| 租户uuid
 uuid|string| 虚拟ip的uuid

### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/vip/delete
```
Body:
```
{	
    "tenant": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
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
  "data": {}
}
```

#### 异常返回示例
### 状态码


## /v1/vip/list
#### 功能：获取虚拟ip列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 page_num|int| 否|0  | 第几页
 page_size|int| 否|0  | 每页的数量 
 filter_name|string| 否|-  | 要过滤的名字 
 

### 返回参数
名称|参数类型|描述 
---|---|---
total_count|int|总数量
list| array | 虚拟ip列表

#### list对象
名称|参数类型|描述 
---|---|---
ctime|int64|创建时间
mtime|int64|修改时间
uuid|string|uuid
name|string|虚拟ip名称
assigned_ip|string|分配的ip
gateway|string|网关
mask|string|掩码
en_status|bool|todo
introduction|string|todo
net_service|string|todo


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/vip/list?tenant_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400&page_num=1&page_size=10
```


#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
   "total_count":145,
   "list"[
    {
        "ns":"4a7e240b-14aa-11e9-b0b9-5"
        "ctime":3554545455
        "mtime":4555226552
        "uuid":"4a7e240b-14aa-11e9-b0b9-5"
        "name":"testname"
        "assigned_ip":"192.168.201.2"
        "gateway":"192.168.201.1"
        "mask":"255.255.255.0"
        "en_status":false
        "introduction":"aaaaa"
        "net_service":"aaaaa"
    }
   ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/unused/vip/list
#### 功能：获取未使用的虚拟ip列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 page_num|int| 否|0  | 第几页
 page_size|int| 否|0  | 每页的数量 
 

### 返回参数
名称|参数类型|描述 
---|---|---
total_count|int|总数量
list|Vip object| 虚拟ip列表

#### list对象
名称|参数类型|描述 
---|---|---
ns|string|名称空间
ctime|int64|创建时间
mtime|int64|修改时间
uuid|string|uuid
name|string|虚拟ip名称
assigned_ip|string|分配的ip
gateway|string|网关
mask|string|掩码
en_status|bool|todo
introduction|string|todo
net_service|string|todo


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/network/unused/vip/list?tenant_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400&page_num=1&page_size=10
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
   "total_count":145,
   "list"[
    {
        "ns":"4a7e240b-14aa-11e9-b0b9-5"
        "ctime":3554545455
        "mtime":4555226552
        "uuid":"4a7e240b-14aa-11e9-b0b9-5"
        "name":"testname"
        "assigned_ip":"192.168.201.2"
        "gateway":"192.168.201.1"
        "mask":"255.255.255.0"
        "en_status":false
        "introduction":"aaaaa"
        "net_service":"aaaaa"
    }
   ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/vip/applyed/list
#### 功能：获取已使用的虚拟ip列表
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
http://192.168.201.57:9990/v1/network/vip/applyed/list?tenant_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400&page_num=1&page_size=10
```
#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
   "total_count":145,
   "list"[
    {
        "ns":"4a7e240b-14aa-11e9-b0b9-5"
        "ctime":3554545455
        "mtime":4555226552
        "uuid":"4a7e240b-14aa-11e9-b0b9-5"
        "name":"testname"
        "assigned_ip":"192.168.201.2"
        "gateway":"192.168.201.1"
        "mask":"255.255.255.0"
        "en_status":false
        "introduction":"aaaaa"
        "net_service":"aaaaa"
    }
   ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/vip/assiged
#### 功能：分配虚拟ip
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
http://localhost:9990/v1/network/vip/assiged
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


## /v1/network/vip/applyed/unused/list
#### 功能：获取所有分配但并未使用的虚拟ip
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
http://localhost:9990/v1/network/
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




## /v1/network/vip/info
#### 功能：获取虚拟ip详情
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 vip_uuid|string| 是|""  | 虚拟ip的uuid

### 返回参数
名称|参数类型|描述 
---|---|---
ns|string|名称空间
ctime|int64|创建时间
mtime|int64|修改时间
uuid|string|uuid
name|string|虚拟ip名称
assigned_ip|string|分配的ip
gateway|string|网关
mask|string|掩码
en_status|bool|todo
introduction|string|todo
net_service|string|todo

### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/network/vip/info
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "vip_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
        "ctime":3554545455
        "mtime":4555226552
        "uuid":"4a7e240b-14aa-11e9-b0b9-5"
        "name":"testname"
        "assigned_ip":"192.168.201.2"
        "gateway":"192.168.201.1"
        "mask":"255.255.255.0"
        "en_status":false
        "introduction":"aaaaa"
        "net_service":"aaaaa"
  }
}
```

#### 异常返回示例
### 状态码





