[back to api overview](../api_overview.md#api)


## /v1/tencent/image/create
#### 功能：创建镜像
#### 请求类型：  post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 list|string 列表| 是| - | 工单的uuid列表
 
### 返回参数
名称|参数类型|描述 
---|---|---
ticket_uuid|string| 工单uuid
ticket_name|string| 工单name




### 示例

#### 请求示例
```
http://localhost:9990/v1/ticket/confirm
```
Body:
```
{	
	"list":[
		"ad0bcf7e-ab75-4873-b0a2-6caa294b083f"
	]
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
		"success": 1,
		"fail": 0,
		"results": [
			{
				"scode": 0,
				"desc": "",
				"message": "success",
				"message_cn": "成功",
				"stack": null,
				"data": {
					"ticket_uuid": "ad0bcf7e-ab75-4873-b0a2-6caa294b083f",
					"ticket_name": "反馈"
				}
			}
		]
	}
}
```

#### 异常返回示例

### 状态码


## /v1/ticket/save
#### 功能：保存或者修改工单
#### 请求类型：  post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
ticketInfo | ticketInfo 对象|是|-| 需要保存的工单的参数


### 返回参数
名称|参数类型|描述 
---|---|---
ticket_uuid|string| 工单uuid
ticket_name|string| 工单name


### 示例

#### 请求示例
```
http://localhost:9990/v1/ticket/save
```
Body:
```
{
	"ticket_name":"反馈",
	"type":"FEEDBACK",
    "reason":"原因：规格申请虚拟机",
	"process_uuid":"ba452aa0-b1c5-41d5-97ce-be07ebe0a749"
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
		"ticket_uuid": "fdf54510-55e2-44e9-ae85-fdd638af7732",
		"ticket_name": "反馈"
	}
}
```

#### 异常返回示例

### 状态码


## /v1/ticket/submit
#### 功能：提交
#### 请求类型： post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
ticketinfo |[ticketinfo 对象](./define.md#ticketInfo)|是|-|工单信息

### 返回参数
名称|参数类型|描述 
---|---|---
ticket_uuid|string| 工单uuid
ticket_name|string| 工单name

### 示例

#### 请求示例
```
http://localhost:9990/v1/ticket/submit
```
Body:
```
{
	"ticket_name":"测试",
	"type":"FEEDBACK",
    "reason":"原因：规格申请虚拟机",
	"process_uuid":"ba452aa0-b1c5-41d5-97ce-be07ebe0a749"
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
		"ticket_uuid": "ab29aed2-449f-446a-95e6-1407caf16837",
		"ticket_name": "测试"
	}
}
```

#### 异常返回示例

### 状态码


## /v1/ticket/list
#### 功能：获取规格列表
#### 请求类型：  GET 

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
http://localhost:9990/v1/ticket/list
```
Body:
```
{	
    "tenant_uuid":""
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
				"ticket_uuid": "7e512229-3450-41b9-9766-238e2d405bb5",
				"ticket_name": "fdsf",
				"ticket_type": "问题反馈",
				"ticket_state": "待审批",
				"ticket_is_over": false,
				"is_confirm": "未确认",
				"ticket_create_time": 1570532439,
				"applyer_name": "lts",
				"applyer_uuid": "a11671e6-17e5-4170-92c5-5d1634ece435",
				"applyer_role": "租户",
				"applyer_tenant_uuid": "a11671e6-17e5-4170-92c5-5d1634ece435",
				"applyer_tenant_name": "lts",
				"reason": "fdsf",
				"user_name": "超级管理员",
				"user_uuid": "system",
				"user_tenant_uuid": "system",
				"detail_uuid": "c258949e-d4c4-44b8-94f6-c5287e12d266",
				"process_uuid": "system",
				"process_name": "默认审批流程",
				"processers": [
					{
						"processer_tenant_uuid": "system",
						"processer_tenant_name": "system",
						"owner_uuid": "system",
						"owner_name": "超级管理员",
						"processer_uuid": "",
						"processer_name": "",
						"processer_role": "",
						"processer_action": "",
						"processer_approval_time": 0,
						"reason": ""
					}
				]
			}
		]
	}
}
```

#### 异常返回示例

### 状态码


## /v1/ticket/inspect
#### 功能：获取工单详情
#### 请求类型：  GET

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
http://localhost:9990/v1/ticket/inspect
```
Body:
```
{	
    "ticket_uuid"
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
		"ticket_uuid": "67beed65-bcd0-4b31-bb27-c3c1e3e96077",
		"ticket_name": "rongrongrongrongrongrongqi",
		"ticket_type": "未确认",
		"ticket_state": "已通过",
		"ticket_is_over": true,
		"is_confirm": "",
		"ticket_create_time": 1569226722,
		"applyer_name": "gate",
		"applyer_uuid": "271b0384-066a-4af0-aa55-b57a4f916bb4",
		"applyer_role": "租户",
		"applyer_tenant_uuid": "271b0384-066a-4af0-aa55-b57a4f916bb4",
		"applyer_tenant_name": "gate",
		"reason": "测试",
		"user_name": "gate",
		"user_uuid": "271b0384-066a-4af0-aa55-b57a4f916bb4",
		"user_tenant_uuid": "271b0384-066a-4af0-aa55-b57a4f916bb4",
		"detail_uuid": "8e4579de-f90f-4c0c-9a68-b8415a8f282c",
		"process_uuid": "system",
		"process_name": "默认审批流程",
		"processers": [
			{
				"processer_tenant_uuid": "system",
				"processer_tenant_name": "system",
				"owner_uuid": "system",
				"owner_name": "超级管理员",
				"processer_uuid": "admin-1234567890987654321",
				"processer_name": "admin",
				"processer_role": "",
				"processer_action": "通过",
				"processer_approval_time": 1569227162,
				"reason": ""
			}
		],
		"storage": {
			"volume_specification": {
				"specification_uuid": "",
				"specification_name": "",
				"volume_name": "",
				"volume_uuid": "",
				"specification_info": null
			},
			"tenant_quota": {
				"cpu_count": 0,
				"memory_size": 0,
				"disk_size": 0,
				"switch_count": 0,
				"router_count": 0,
				"gateway_count": 0
			},
			"volume_expantion": {
				"volume_uuid": "",
				"capacity": 0
			}
		}
	}
}
```

#### 异常返回示例

### 状态码


## /v1/ticket/saved/submit
#### 功能：提交保存的工单
#### 请求类型：  post

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
http://localhost:9990/v1/ticket/saved/submit
```
Body:
```
{	
    list:[
        "8e4579de-f90f-4c0c-9a68-b8415a8f282c"
    ]
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
		"success": 1,
		"fail": 0,
		"results": [
			{
				"scode": 0,
				"desc": "",
				"message": "success",
				"message_cn": "成功",
				"stack": null,
				"data": {
					"ticket_uuid": "a1e8f15f-15c4-4e1c-bb69-9fc1dfa045c9",
					"ticket_name": "反馈"
				}
			}
		]
	}
}
```

#### 异常返回示例

### 状态码




## /v1/ticket/overruled/submit
#### 功能：从新提交被驳回的
#### 请求类型：  post

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
http://localhost:9990/v1/ticket/overruled/submit
```
Body:
```
{
	"list":[
		"e08f29d7-1cbf-41cc-8e5e-37341c719800"	
	]
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
		"success": 1,
		"fail": 0,
		"results": [
			{
				"scode": 0,
				"desc": "",
				"message": "success",
				"message_cn": "成功",
				"stack": null,
				"data": {
					"ticket_uuid": "e08f29d7-1cbf-41cc-8e5e-37341c719800",
					"ticket_name": "测试"
				}
			}
		]
	}
}
```

#### 异常返回示例

### 状态码

## /v1/ticket/archive
#### 功能：工单归档
#### 请求类型：  post

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
http://localhost:9990/v1/ticket/archive
```
Body:
```
{
	"list":[
		"aa3eee15-bf13-45dd-bdb4-d71c59b8e4ab"	
	]
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
		"success": 1,
		"fail": 0,
		"results": [
			{
				"scode": 0,
				"desc": "",
				"message": "success",
				"message_cn": "成功",
				"stack": null,
				"data": {
					"ticket_uuid": "aa3eee15-bf13-45dd-bdb4-d71c59b8e4ab",
					"ticket_name": ""
				}
			}
		]
	}
}
```

#### 异常返回示例

### 状态码


## /v1/ticket/overrule
#### 功能： 驳回工单
#### 请求类型：  get

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
http://localhost:9990/v1/ticket/overrule
```
Body:
```
{
	"list":[
		"5a66d45c-202f-4a1d-a25a-39e5eef1137a"
	],
	"reason":"测试"
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
		"success": 1,
		"fail": 0,
		"results": [
			{
				"scode": 0,
				"desc": "",
				"message": "success",
				"message_cn": "成功",
				"stack": null,
				"data": {
					"ticket_uuid": "5a66d45c-202f-4a1d-a25a-39e5eef1137a",
					"ticket_name": "哒哒哒哒哒"
				}
			}
		]
	}
}
```

#### 异常返回示例

### 状态码

## /v1/ticket/pass
#### 功能：通过工单
#### 请求类型： post

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
http://localhost:9990/v1/ticket/pass
```
Body:
```	
{
	"list":[
		"3f7dfe70-6055-4d48-aa94-c871d3677fc0"	
	],
	"config":{
		"contianer":{
			"auto_container":{
					"host_uuid":"host_uuid_aaaaaaaaaaaaaa",
					"labels":[
						{
							"must":true,
							"selector":"bbbbb",
							"key":"ccccccccccc",
							"value":[
								"111111111111",
								"222222222222"
							]
						}
					]	
			}
		}
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
	"data": {
		"success": 1,
		"fail": 0,
		"results": [
			{
				"scode": 0,
				"desc": "",
				"message": "success",
				"message_cn": "成功",
				"stack": null,
				"data": {
					"ticket_uuid": "3f7dfe70-6055-4d48-aa94-c871d3677fc0",
					"ticket_name": "aaa"
				}
			}
		]
	}
}
```

#### 异常返回示例

### 状态码

## /v1/ticket/withdraw
#### 功能： 撤回工单
#### 请求类型： post

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
http://localhost:9990/v1/ticket/withdraw
```
Body:
```	
{
	"list":[
		"2b31737f-0f1e-4b87-82cf-4a1a8140eadc"	
	]
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
		"success": 1,
		"fail": 0,
		"results": [
			{
				"scode": 0,
				"desc": "",
				"message": "success",
				"message_cn": "成功",
				"stack": null,
				"data": {
					"ticket_uuid": "2b31737f-0f1e-4b87-82cf-4a1a8140eadc",
					"ticket_name": "测试"
				}
			}
		]
	}
}
```

#### 异常返回示例

### 状态码



## /v1/ticket/process/create
#### 功能： 创建流程
#### 请求类型： post

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
http://localhost:9990/v1/ticket/process/create
```
Body:
```	
{
	"tenant_uuid":"d40511b3-0f61-4f00-bd7b-417a6628b67c",
	"process_name":"111",
	"approval_list":[
		{
			"tenant_uuid":"d40511b3-0f61-4f00-bd7b-417a6628b67c",
			"role_uuid":"16802782-97f5-4b31-9c8c-3d80dd742189"
		},
		{
			"tenant_uuid":"d40511b3-0f61-4f00-bd7b-417a6628b67c",
			"role_uuid":"b9bf1df8-f21d-48ca-ac65-7696c2142d73"
		},
		{
			"tenant_uuid":"d40511b3-0f61-4f00-bd7b-417a6628b67c",
			"role_uuid":"993c5f1f-80db-43b8-bd1f-878fe7473042"
		}
	]
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
		"process_uuid": "ba452aa0-b1c5-41d5-97ce-be07ebe0a749",
		"process_name": "111"
	}
}
```

#### 异常返回示例

### 状态码


## /v1/ticket/process/delete
#### 功能： 流程删除
#### 请求类型： post

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
http://localhost:9990/v1/ticket/process/delete
```
Body:
```	
{
	"tenant_uuid":"b7550505-5050-4a18-879b-66d8167afcff",
	"tenant_uuid":"b7550505-5050-4a18-879b-66d8167afcff",
	"list":[
		{
			"process_uuid":"f4d4a842-230f-4228-a1b2-13772953434b"
		}
	]
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
		"success": 1,
		"fail": 0,
		"results": [
			{
				"scode": 0,
				"desc": "",
				"message": "success",
				"message_cn": "成功",
				"stack": null,
				"data": {
					"process_uuid": "f4d4a842-230f-4228-a1b2-13772953434b",
					"process_name": ""
				}
			}
		]
	}
}
```

#### 异常返回示例

### 状态码



## /v1/ticket/process/update
#### 功能： 流程修改
#### 请求类型： post

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
http://localhost:9990/v1/ticket/process/update
```
Body:
```	
{
	"tenant_uuid":"d40511b3-0f61-4f00-bd7b-417a6628b67c",
	"process_uuid":"ba452aa0-b1c5-41d5-97ce-be07ebe0a749",
	"process_name":"啊啊啊啊啊啊啊啊啊啊啊",
	"description":"评论-随便的一个评论",
	"approval_list":[
					{
						"tenant_uuid": "d40511b3-0f61-4f00-bd7b-417a6628b67c",
						"tenant_name": "lts",
						"role_uuid": "16802782-97f5-4b31-9c8c-3d80dd742189",
						"role_name": "aaa"
					},
					{
						"tenant_uuid": "d40511b3-0f61-4f00-bd7b-417a6628b67c",
						"tenant_name": "lts",
						"role_uuid": "b9bf1df8-f21d-48ca-ac65-7696c2142d73",
						"role_name": "bbb"
					},
					{
						"tenant_uuid": "d40511b3-0f61-4f00-bd7b-417a6628b67c",
						"tenant_name": "lts",
						"role_uuid": "993c5f1f-80db-43b8-bd1f-878fe7473042",
						"role_name": "ccc"
					}
	]
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
		"process_uuid": "",
		"process_name": ""
	}
}
```

#### 异常返回示例

### 状态码



## /v1/ticket/process/inspect
#### 功能： 获取流程详情
#### 请求类型： get

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
http://localhost:9990/v1/ticket/process/inspect
```
Body:
```	
{
    "tenant_uuid":"d40511b3-0f61-4f00-bd7b-417a6628b67c",
    "process_uuid":"ba452aa0-b1c5-41d5-97ce-be07ebe0a749"
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
		"process_uuid": "ba452aa0-b1c5-41d5-97ce-be07ebe0a749",
		"process_name": "啊啊啊啊啊啊啊啊啊啊啊",
		"tenant_uuid": "d40511b3-0f61-4f00-bd7b-417a6628b67c",
		"tenant_name": "lts",
		"description": "评论-随便的一个评论",
		"create_time": 1565941831,
		"creator_uuid": "admin-1234567890987654321",
		"creator_name": "admin",
		"creator_role": "超级管理员",
		"creator_tenant_uuid": "system",
		"creator_tenant_name": "system",
		"process_list": [
			{
				"tenant_uuid": "d40511b3-0f61-4f00-bd7b-417a6628b67c",
				"tenant_name": "lts",
				"role_uuid": "16802782-97f5-4b31-9c8c-3d80dd742189",
				"role_name": "aaa"
			},
			{
				"tenant_uuid": "d40511b3-0f61-4f00-bd7b-417a6628b67c",
				"tenant_name": "lts",
				"role_uuid": "b9bf1df8-f21d-48ca-ac65-7696c2142d73",
				"role_name": "bbb"
			},
			{
				"tenant_uuid": "d40511b3-0f61-4f00-bd7b-417a6628b67c",
				"tenant_name": "lts",
				"role_uuid": "993c5f1f-80db-43b8-bd1f-878fe7473042",
				"role_name": "ccc"
			}
		]
	}
}
```

#### 异常返回示例

### 状态码



## /v1/ticket/process/list
#### 功能： 获取流程列表
#### 请求类型： get

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

http://localhost:9990/v1/ticket/process/list

```
Body:
```	
{
    "tenant_uuid":"tenant_uuid"
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
				"process_uuid": "system",
				"process_name": "默认审批流程",
				"tenant_uuid": "system",
				"tenant_name": "system",
				"description": "默认审批流程",
				"create_time": 1569826447,
				"creator_uuid": "admin-1234567890987654321",
				"creator_name": "admin",
				"creator_role": "超级管理员",
				"creator_tenant_uuid": "system",
				"creator_tenant_name": "system",
				"is_in_using": true,
				"process_list": [
					{
						"tenant_uuid": "a11671e6-17e5-4170-92c5-5d1634ece435",
						"tenant_name": "lts",
						"role_uuid": "a11671e6-17e5-4170-92c5-5d1634ece435",
						"role_name": "租户管理员"
					},
					{
						"tenant_uuid": "system",
						"tenant_name": "system",
						"role_uuid": "system",
						"role_name": "超级管理员"
					}
				]
			}
		]
	}
}
```

#### 异常返回示例

### 状态码

## /v1/ticket/delete
#### 功能： 工单删除
#### 请求类型： post

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
http://localhost:9990/v1/ticket/delete
```
Body:
```	
{
	"list":[
		"ad0bcf7e-ab75-4873-b0a2-6caa294b083f"
	]
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
		"success": 1,
		"fail": 0,
		"results": [
			{
				"scode": 0,
				"desc": "",
				"message": "success",
				"message_cn": "成功",
				"stack": null,
				"data": {
					"ticket_uuid": "ad0bcf7e-ab75-4873-b0a2-6caa294b083f",
					"ticket_name": "反馈"
				}
			}
		]
	}
}
```

#### 异常返回示例

### 状态码
