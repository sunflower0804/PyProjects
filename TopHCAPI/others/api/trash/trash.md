[back to api overview](../api_overview.md#label_api)
### 回收站相关接口
## /v1/trash/list
回收站列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
filter_object_name|string|否|-|过滤名称
filter_object_type|int32|否|-|过滤类型（1：存储卷；2：云服务器；4：VPC出口；5：逻辑VPC路由器；6：逻辑VPC交换机；7：虚拟IP；8:安全组；9：地址集；10：云容器）
page_num|int|否|0|第几页
page_size|int|否|0|每页数据条数
start|int64|否|0|开始时间
end|int64|否|0|结束时间

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.10.24:8080/v1/trash/list?cluster_uuid=3afdbbfc-e45a-430e-abba-842074a8b035&tenant=&filter_object_type=2&filter_object_name=&start=0&end=0&page_num=0&page_size=20
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
        "name": "122",
        "delete_time": 1570860627785718752,
        "uuid": "626154f7-cec1-4fa1-9862-3700bd789b9e",
        "type": 2,
        "namespace_uuid": "",
        "namespace": "61de6fef-17d2-471b-8bd1-ca1516dcb83c",
        "namespace_name": "xushengan",
        "tenant": "61de6fef-17d2-471b-8bd1-ca1516dcb83c",
        "tenant_name": "xushengan"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/trash/restore
回收站对象恢复
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/trash/restore
```
Body:
```
{
	"cluster_uuid": "3afdbbfc-e45a-430e-abba-842074a8b035",
	"tenant": "",
	"objects": [
		{
			"uuid": "626154f7-cec1-4fa1-9862-3700bd789b9e",
			"type": 2,
			"namespace_uuid": "61de6fef-17d2-471b-8bd1-ca1516dcb83c"
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
  "data": {}
}
```

#### 异常返回示例

### 状态码



## /v1/trash/delete
回收站对象删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/trash/delete
```
Body:
```
{
	"cluster_uuid": "3afdbbfc-e45a-430e-abba-842074a8b035",
	"tenant": "",
	"objects": [
		{
			"uuid": "ed429a4c-3d8e-46b9-9c99-4ca7dd17f29f",
			"type": 5,
			"namespace_uuid": "a15e717b-f2a4-462b-ade6-3ec3c1c2da8b"
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
  "data": {}
}
```

#### 异常返回示例

### 状态码

