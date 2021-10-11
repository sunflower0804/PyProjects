[back to api overview](../api_overview.md#label_api)

### 集群操作日志相关接口
## /v1/audit/log/list
集群日志列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-|集群uuid
 manipulator|string| 否|-| 操作者
 object_uuid|string|否|-|对象uuid
 object_type|string|否|-|对象类型
 operate_method|string|否|-|操作方法
 start_time|int64|否|0|开始时间，时间戳
 end_time|int64|否|0|结束时间，时间戳
 page_num|int32|否|0|显示页码
 page_size|int32|否|0|每页显示多少数据
 filter_name|int32|否|0|过滤名称


### 返回参数

名称|参数类型|描述
---|---|---
Infos|object array|列表
total_count|int32|总数量

#### Infos对象
名称|参数类型|描述
---|---|---
UUID|string|日志uuid
Manipulator|string|
ObjectType|string|对象类型
ObjectUUID|string|对象uuid
ObjectName|string|对象名称
OperateMethod|string|操作方法(动作)
Ctime|int64|创建时间
Message|string|描述
Result|string|结果


### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/audit/log/list?number=20&page=0&ObjectType=&FilterName=&OperateMethod=&start=1572236626&end=1572841426&cluster_uuid=b088822c-1176-4c79-9df7-5fad80c7fd1d
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
		"TotalCount": 91,
		"Infos": [
			{
				"UUID": "2e12255b-c0ae-4173-96d0-98c27f5aa4e3",
				"Manipulator": "",
				"ObjectType": "存储卷",
				"ObjectUUID": "billing_15版本测试-pool1-volume-1101162532-0938",
				"ObjectName": "存储卷(billing_15版本测试-pool1-volume-1101162532-0938)",
				"OperateMethod": "初始化VSD",
				"Ctime": 1572601909,
				"Message": "挂载共享卷(10.30.12.55-billing_15版本测试-pool1-volume-1101162532-0938)失败",
				"Result": "失败,错误: 卷(volume-1101162532-0938)挂载路径错误",
				"startTime": 0,
				"endTime": 0
			}
		]
	}
}
```

#### 异常返回示例

### 状态码
