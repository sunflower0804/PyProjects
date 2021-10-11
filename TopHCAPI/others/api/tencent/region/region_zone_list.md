[back to api overview](../api_overview.md#api)


## /v1/tencent/region/zone/list
#### 功能：用于查询可用区列表信息
#### 请求类型：  post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid|string| 是| - | 租户uuid
 ProjectId|int| 是| - | 项目id


### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|uint64| 可用区数量
List|Array of Region | 可用区列表信息   todo



### 示例

#### 请求示例
```
http://localhost:9990/v1/tencent/region/list
```
Body:
```
{
	"TenantUuid":"aaaaa",
	"ProjectId":1184854
}

```
#### 正常返回示例
```
{
	"message": "success",
	"message_cn": "成功",
	"scode": 0,
	"desc": "",
	"stack": null,
	"data": {
		"TotalCount": 20,
		"List": [
			{
				"Region": "ap-bangkok",
				"RegionName": "亚太地区(曼谷)",
				"RegionState": "AVAILABLE"
			}
		]

```

#### 异常返回示例

### 状态码