[back to api overview](../api_overview.md#api)

# policy
* [/v1/policy/list](policy.md#/v1/policy/list)
* [/v1/policy/inspect](policy.md#/v1/policy/inspect)
* [/v1/policy/create](policy.md#/v1/policy/create)
* [/v1/policy/delete](policy.md#/v1/policy/delete)
* [/v1/policy/update](policy.md#/v1/policy/update)
* [/v1/policy/user/attach](policy.md#/v1/policy/user/attach)
* [/v1/policy/user/detach](policy.md#/v1/policy/user/detach)
* [/v1/policy/user_group/attach](policy.md#/v1/policy/user_group/attach)
* [/v1/policy/user_group/detach](policy.md#/v1/policy/user_group/detach)



## /v1/role/list
#### 功能：策略列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid  
 filter_complex|string| 否|""  | 统一过滤参数，当有多个需要过滤的参数时，用空格隔开
 page_num|int| 否|0  | 第几页
 page_size|int| 否|0  | 每一页的数量
 

### 返回参数

名称|参数类型|描述 
---|---|---
todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/role/list
```
Body:
```	
{	
 	"tenant_uuid":"1f652550-3f22-4b6b-986e-fbbfdd4c0a5a",
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
		"total_count": 1,
		"list": [
			{
				"uuid": "993c5f1f-80db-43b8-bd1f-878fe7473042",
				"tenant_uuid": "d40511b3-0f61-4f00-bd7b-417a6628b67c",
				"role_name": "ccc",
				"create_time": 1565836843,
				"description": "ccc",
				"is_bind": false
			}
		]
	}
}
```

#### 异常返回示例

### 状态码

## /v1/role/inspect
#### 功能：角色详情
### 请求类型 get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
tenant_uuid|string|是|""|租户uuid
role_uuid|string|是|""|角色uuid


### 返回参数

名称|参数类型|描述 
---|---|---
todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/role/inspect
```
Body:
```	
{
    "tenant_uuid":"d40511b3-0f61-4f00-bd7b-417a6628b67c",
    "role_uuid":"993c5f1f-80db-43b8-bd1f-878fe7473042"
}
```
#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {
    "role_uuid": "system",
    "role_name": "超级管理员",
    "tenant_uuid": "system",
    "create_time": 1570780508,
    "description": "超级管理员",
    "permission_info": [
      {
        "model": "ntp",
        "permission_list": [
          {
            "id": 3501,
            "model": "ntp",
            "description": "NTP service add/remove",
            "description_cn": "ntp服务添加/删除/设置时区/强制同步时间",
            "is_enable": true
          },
      }
      …………
    ]
  }
}  
```

#### 异常返回示例

### 状态码

## /v1/role/create
#### 功能：创建角色
### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""| 租户uuid
 role_name|string|是|""|角色名称
 description|string|否|""|角色描述信息

### 返回参数

名称|参数类型|描述 
---|---|---
todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/role/create
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "role_name": "thci_develop"
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


## /v1/role/delete
创建策略, 仅对系统租户有效。
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""| 租户uuid
 role_uuid|string|是|""|角色uuid
 role_name|string|否|""|角色名称

### 返回参数

名称|参数类型|描述 
---|---|---
无

### 示例

#### 请求示例
```
http://localhost:9990/v1/role/delete
```
Body:
```
{
	"tenant_uuid": "982a3998-21de-4353-94c9-481ddcd33920",
	"role_uuid": "001246d8-a59e-47af-a210-da5b5bea5ebf"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {}
}
```

#### 异常返回示例

### 状态码

## /v1/role/update
策略更新权限, 仅对系统租户有效。
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""| 租户uuid
 role_uuid|string|是|""|角色uuid
 role_name|string|否|""|角色名称
 description|string|否|""|描述信息
 perm_list|string|否|-|权限列表。一组int值，每个int值代表一个权限

##### permission_enable
 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 name|string| 是|-| 权限名
 enabled|bool|是|-|启动还是关闭

### 返回参数

名称|参数类型|描述 
---|---|---
无

### 示例

#### 请求示例
```
http://192.168.201.212:9990/v1/role/update
```
Body:
```
{
	"tenant_uuid": "982a3998-21de-4353-94c9-481ddcd33920",
	"role_uuid": "4176d129-2e8f-4f42-bcc5-5c3aab449d15",
	"role_name": "fadsf",
	"description": "fadf",
	"perm_list": [
		2211
	],
	"cluster_uuid": "3bf461e0-b92c-4df1-9aa6-4bf71ad2db7d"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {}
}
```

#### 异常返回示例

### 状态码

## /v1/role/user/bind
#### 功能：将角色和用户绑定
### 请求类型 post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""| 租户uuid
 role_uuid|string|是|""|角色uuid
 user_uuid|string|是|""|用户uuid

### 返回参数

名称|参数类型|描述 
---|---|---
无
### 示例

#### 请求示例
```
http://192.168.201.212:9990/v1/role/user/bind
```
Body:
```
{
	"tenant_uuid":"8a31aa18-1258-11e9-b844-5256ff003400",
	"role_uuid":"0b202212-6948-4448-b9c5-1b8b0a9bed7c",
	"user_uuid":"4786e280-a840-11e9-807e-5256ffeaa85c"
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


## /v1/role/user/unbind
#### 功能：策略取消关联用户
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""| 租户uuid
 role_uuid|string|是|""|角色uuid
 user_uuid|string|是|""|用户uuid

### 返回参数

名称|参数类型|描述 
---|---|---
无

### 示例

#### 请求示例
```
http://192.168.201.212:9990/v1/role/user/unbind
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "role_uuid": "8a31aa18-1258-11e9-b844-5256ff003400",
    "user_uuid": "9d45582e-1564-11e9-ad7d-525400f12f00"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {}
}
```

#### 异常返回示例

### 状态码




