[back to api overview](../api_overview.md#label_api)

### 集群事件相关接口
## /v1/audit/event/list
集群事件列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-|集群uuid
 ObjectUUID|string|否|-|对象uuid
 ObjectName|string|否|-|对象名称
 ObjectType|string|否|-|对象类型
 EventType|string|否|-|事件类型
 start|int64|否|0|开始时间，时间戳
 end|int64|否|0|结束时间，时间戳
 page|int32|否|0|显示页码
 number|int32|否|0|每页显示多少数据
 FilterName|string|否|-|过滤名称
 FilterMessage|string|否|-|过滤描述


### 返回参数

名称|参数类型|描述
---|---|---
Infos|object array|列表
total_count|int32|总数量

#### Infos对象
名称|参数类型|描述
---|---|---
UUID|string|事件uuid
ObjectType|string|对象类型
ObjectUUID|string|对象uuid
ObjectName|string|对象名称
EventType|string|事件类型
EventMessage|string|描述
Ctime|int64|创建时间

### 示例

#### 请求示例
```
http://10.30.12.52:8080/v1/audit/event/list?page=0&number=10&start=1572233850&end=1572838650&ObjectType=&EventType=&FilterName=&FilterMessage=&cluster_uuid=667822c9-fec0-43ca-94dc-68ed45becce3
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
		"TotalCount": 8131,
		"Infos": [
			{
				"UUID": "0307364e-5db9-4dc1-bffb-b0df810c42ce",
				"ObjectType": "主机",
				"ObjectUUID": "10.30.12.68",
				"ObjectName": "10.30.12.68",
				"EventType": "主机宕机",
				"EventMessage": "主机宕机",
				"Ctime": 1572743318,
				"StartTime": 0,
				"EndTime": 0
			}
		]
	}
}
```

#### 异常返回示例

### 状态码
