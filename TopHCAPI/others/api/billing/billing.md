[back to api overview](../api_overview.md#label_api)
# billing

## /v1/billing/specfication/update
#### 功能：添加计费规格
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 effective_time|int| 否|当前时间的下一分钟的开始时间|生效时间。
 tenant_uuid|string| 是|""  | 租户uuid
 specification_type|string| 是| "" | 规格类型,支持的参数：CPU MEMORY DISK
 specification_name|string| 是| "" | 规格名称
 description|string| 否| "" | 规格的描述信息
 quantity_unit|string| 否|""  | 数量单位，支持的参数：M G T,当规格类型为CPU时，不填，其他情况必填
 time_unit|string| 是|""  | 时间单位，支持的参数：小时，天
 price|float| 是|0.0  | 价格
 

### 返回参数
名称|参数类型|描述 
---|---|---


### 示例

#### 请求示例
```
http://host:9990/v1/billing/specfication/update
```
Body:
```
{
	"effective_time":100000000,
	"tenant_uuid":"34e7299a-a180-42e6-a2d4-dac6dbd0206e",
	"specification_type":"CPU",
	"specification_name":"aaaaaaaaa",
	"quantity_unit":"G",
	"time_unit":"小时",
	"price":60
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




## /v1/billing/specification/list
#### 功能：获取计费规格列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 filter_complex|string| 否|""  | 统一过滤参数，当有多个需要过滤的参数时，用空格隔开
 page_num|int| 否|0  | 第几页
 tenant_size|int| 否|0  | 每一页的数量
 

### 返回参数
名称|参数类型|描述 
---|---|---
 total_count|int| 总数量
 list|[specification 列表](define.md#speficiation_resp)| 规格列表


### 示例

#### 请求示例
```
http://host:9990/v1/billing/specification/list?tenant_uuid=34e7299a-a180-42e6-a2d4-dac6dbd0206e
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
				"specification_uuid": "f5abcd07-a88f-4a9b-9b2e-a488ae32a31d",
				"specification_name": "aaaaaaaaa",
				"create_time": 1571389637,
				"desire_effective_time": 100000000,
				"permit_effective_time": 100000020,
				"last_billing_time": 100000020,
				"last_record_time": 100000020,
				"end_time": 9223372036854775807,
				"description": "",
				"status": "未生效",
				"operate_tenant_uuid": "system",
				"operator_tenant_name": "system",
				"operator_uuid": "f0ed27b3-37e9-4c28-85fc-77450a00ab23",
				"operator_name": "lts",
				"operator_role": "administrator",
				"tenant_uuid": "27618f52-aa26-4283-92e2-491317bd980e",
				"tenant_name": "",
				"specification_type": "CPU",
				"price": 60,
				"quantity_unit": "",
				"time_unit": "小时"
			}
		]
	}
}
```

#### 异常返回示例

### 状态码

## /v1/billing/specification/inspect
#### 功能：获取规格详情
#### 请求类型：  GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 specification_uuid|string| 是|"" | 规格uuid

### 返回参数
名称|参数类型|描述 
---|---|---
 specification|[specification 对象](define.md#speficiation_resp)| 规格列表


### 示例

#### 请求示例
```
http://host:9990/v1/billing/specification/inspect?tenant_uuid=004b5011-7ca8-46b8-ad7d-38d0c83d913a&specification_uuid=821d0567-04c3-4b02-8f39-b35c1e2b5135
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
		"specification_uuid": "821d0567-04c3-4b02-8f39-b35c1e2b5135",
		"specification_name": "cpu_specificaiton_test_name",
		"create_time": 1555669490,
		"desire_effective_time": 1555769100,
		"permit_effective_time": 1555769100,
		"status": "UNUSED",
		"operate_tenant_uuid": "system",
		"operator_tenant_name": "system",
		"operator_uuid": "668b45a3-627b-11e9-9626-52564832b7a0",
		"operator_name": "lts",
		"operator_role": "normalUser",
		"tenant_uuid": "004b5011-7ca8-46b8-ad7d-38d0c83d913a",
		"tenant_name": "ttt",
		"specification_type": "CPU",
		"price": 2,
		"quantity_unit": "",
		"time_unit": "天"
	}
}
```

#### 异常返回示例

### 状态码

## /v1/billing/month/udpate
#### 功能：修改账单状态
#### 请求类型：  post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid 
 year|int| 是|0 | 年份
 month|int| 是|0 | 月份
 status|string| 是|"" | 账单状态，可选择的参数： PAIED NOT_PAIED

### 返回参数
名称|参数类型|描述 
---|---|---
 year|int| 年份
 month|int| 月份

### 示例

#### 请求示例
```
http://host:9990/v1/billing/month/update
```
Body:
```
{
	"tenant_uuid":"1f652550-3f22-4b6b-986e-fbbfdd4c0a5a",
	"year":2018,
	"month":11,
	"status":"PAIED"
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




## /v1/billing/month/inspect
#### 功能：获取账单详情
#### 请求类型：  GET  

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid  
 year|int| 是|0  | 年份  
 month|int| 是|0  | 月份  
 

### 返回参数
名称|参数类型|描述 
---|---|---
 month|[month 对象](define.md#month_resp)| 月-账单


### 示例

#### 请求示例
```
http://host:9990/v1/billing/month/inspect?year=2019&month=04&tenant_uuid=502c5cb7-0762-4379-bc95-ff4f7c0cb7cf
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
		"total_count": 0,
		"uuid": "cb225bb7-7752-4b18-a0e0-1c7a1dd521fd",
		"name": "2019-04",
		"status": "未付款",
		"update_time": 0,
		"create_time": 1554048000,
		"tenant_uuid": "502c5cb7-0762-4379-bc95-ff4f7c0cb7cf",
		"month": {
			"year": 2019,
			"month": 4,
			"start_time": "2019-04-01T00:00:00+08:00",
			"end_time": "2019-04-30T23:59:59+08:00"
		},
		"operator_tenant_uuid": "",
		"operator_tenant_name": "",
		"operator_uuid": "",
		"operator_name": "",
		"operator_role": "",
		"total_fee": 0,
		"cpu_fee": 1065067.11,
		"memory_fee": 0,
		"disk_fee": 0,
		"cpu_detail_list": [
			{
				"record_uuid": "7f149630-e5e7-4c3f-8977-eb9e9d3fc72a",
				"tenant_uuid": "502c5cb7-0762-4379-bc95-ff4f7c0cb7cf",
				"start_time": 1554048000,
				"end_time": 1556443380,
				"type": "CPU",
				"t": "NOTE",
				"month": {
					"year": 2019,
					"month": 4,
					"start_time": "2019-04-01T00:00:00+08:00",
					"end_time": "2019-04-30T23:59:59+08:00"
				},
				"qos": 800,
				"quantity_unit": "",
				"time_unit": "小时",
				"price": 2,
				"fee": 1064613.7777777778
			},
			{
				"record_uuid": "6cb3aa7f-682e-4349-9604-a9d7910fd544",
				"tenant_uuid": "502c5cb7-0762-4379-bc95-ff4f7c0cb7cf",
				"start_time": 1556443380,
				"end_time": 1556444399,
				"type": "CPU",
				"t": "NOTE",
				"month": {
					"year": 2019,
					"month": 4,
					"start_time": "2019-04-01T00:00:00+08:00",
					"end_time": "2019-04-30T23:59:59+08:00"
				},
				"qos": 800,
				"quantity_unit": "",
				"time_unit": "小时",
				"price": 2,
				"fee": 453.3333333333333
			}
		],
		"memory_detail_list": [],
		"disk_detail_list": []
	}
}
```

#### 异常返回示例

### 状态码




## /v1/billing/month/list 
#### 功能：获取月账单列表
#### 请求类型：  GET  

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
 total_fee|float| 总费用
 cpu_fee|float| cpu总费用
 memory_fee|float| memory总费用
 disk_fee|float| disk总费用
 total_count|int| month总数量
 list|[month 列表](define.md#speficiation_resp)| month 列表


### 示例

#### 请求示例
```
http://host:9990/v1/billing/month/list?tenant_uuid=502c5cb7-0762-4379-bc95-ff4f7c0cb7cf
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
		"total_fee": 6863467.11,
		"cpu_fee": 6863467.11,
		"memory_fee": 0,
		"disk_fee": 0,
		"total_count": 1,
		"list": [
			{
				"uuid": "52295493-ea2f-447a-9692-85df21e2f487",
				"name": "2019-03",
				"status": "NOT_PAIED",
				"update_time": 0,
				"create_time": 1551369600,
				"tenant_uuid": "502c5cb7-0762-4379-bc95-ff4f7c0cb7cf",
				"month": {
					"year": 2019,
					"month": 3,
					"start_time": "2019-03-01T00:00:00+08:00",
					"end_time": "2019-03-31T23:59:59+08:00"
				},
				"operator_tenant_uuid": "",
				"operator_tenant_name": "",
				"operator_uuid": "",
				"operator_name": "",
				"operator_role": "",
				"total_fee": 0,
				"cpu_fee": 1190400,
				"memory_fee": 0,
				"disk_fee": 0,
				"cpu_detail_list": [
					{
						"record_uuid": "546133ea-61d9-4bc1-a2df-6aabcb4e5fda",
						"tenant_uuid": "502c5cb7-0762-4379-bc95-ff4f7c0cb7cf",
						"start_time": 1551369600,
						"end_time": 1554047999,
						"type": "CPU",
						"t": "NOTE",
						"month": {
							"year": 2019,
							"month": 3,
							"start_time": "2019-03-01T00:00:00+08:00",
							"end_time": "2019-03-31T23:59:59+08:00"
						},
						"qos": 800,
						"quantity_unit": "",
						"time_unit": "小时",
						"price": 2,
						"fee": 1190400
					}
				],
				"memory_detail_list": [],
				"disk_detail_list": []
			}
		]
	}
}
```

#### 异常返回示例

### 状态码



## /v1/billing/tenant/info/url
#### 功能：导出租户消费信息url
#### 请求类型：  GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 year|int| 是| -  | 年份
 month|int| 是|- | 月份
 cluster_uuid|string| 是|-  | 集群uuid

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://host:9990/v1/billing/tenant/info/url?tenant_uuid=82300f99-a7e9-45bb-83cb-ca8b946b083e&year=2021&month=8&protol=http&cluster_uuid=232671ca-d1e7-44ea-9278-a7c2d5920fa7
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
    "download_url": "http://10.30.12.37:34728/2021-08-zhangqi--2021-08-26-13-41-55.csv",
    "file_name": "2021-08-zhangqi--2021-08-26-13-41-55.csv"
  }
}
```

#### 异常返回示例

### 状态码



